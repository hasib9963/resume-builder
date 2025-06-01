import os
import spacy
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from django.conf import settings
from weasyprint import HTML
from .forms import ResumeForm
from .models import Resume, ResumeAnalysis
from django.contrib.auth.decorators import login_required

nlp = spacy.load("en_core_web_sm")

def home(request):
    return render(request, 'resumes/home.html')

@login_required
def build_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            if request.user.is_authenticated:
                resume.user = request.user
            resume.save()
            
            # Analyze resume
            analysis = analyze_resume(resume)
            ResumeAnalysis.objects.create(resume=resume, **analysis)
            
            # Generate PDF - pass the request object
            generate_pdf(request, resume)
            
            return redirect('download_resume', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'resumes/build.html', {'form': form})

def analyze_resume(resume):
    text = f"{resume.summary} {resume.skills} {resume.experience} {resume.education}"
    doc = nlp(text)
    
    # Simple analysis - count action verbs
    action_verbs = ['managed', 'led', 'developed', 'created', 'implemented', 'improved']
    verb_count = sum(1 for token in doc if token.text.lower() in action_verbs)
    
    # Check for metrics
    has_metrics = any(token.like_num for token in doc)
    
    # Generate suggestions
    suggestions = []
    if verb_count < 3:
        suggestions.append("Add more action verbs to strengthen your experience section.")
    if not has_metrics:
        suggestions.append("Include quantifiable achievements (e.g., 'increased sales by 20%').")
    if len(resume.summary.split()) < 30:
        suggestions.append("Consider expanding your summary to better highlight your qualifications.")
    
    return {
        'score': min(100, verb_count * 10 + (20 if has_metrics else 0)),
        'suggestions': "\n".join(suggestions)
    }

def generate_pdf(request, resume):
    html_string = render_to_string('resumes/resume_pdf.html', {'resume': resume})
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf_file = f"resumes/resume_{resume.id}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_file)
    
    # Create media/resumes directory if it doesn't exist
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    html.write_pdf(target=pdf_path)
    resume.pdf_file = pdf_file
    resume.save()

def download_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    if resume.pdf_file:
        return FileResponse(open(resume.pdf_file.path, 'rb'), content_type='application/pdf')
    return HttpResponse("Resume not found", status=404)


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user_resumes = Resume.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'resumes/dashboard.html', {'resumes': user_resumes})