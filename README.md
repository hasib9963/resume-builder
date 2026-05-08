# Resume Builder

A Django-based web application for creating, managing, and analyzing professional resumes with PDF generation capabilities.

## Features

- **User Authentication**: Secure user registration and login system
- **Resume Creation**: Build professional resumes with comprehensive sections including:
  - Personal information (name, email, phone, address)
  - Profile image upload
  - Professional summary
  - Skills and expertise
  - Work experience
  - Education
  - Languages
  - References
  - Social links (LinkedIn, Portfolio)
- **PDF Generation**: Automatic PDF generation using WeasyPrint with professional styling
- **Resume Analysis**: AI-powered resume analysis using spaCy NLP to provide:
  - Resume scoring
  - Improvement suggestions
  - Action verb detection
  - Metrics and achievements analysis
- **Dashboard**: User-friendly dashboard to:
  - View all created resumes
  - Track download statistics
  - Monitor average resume scores
  - Edit and delete resumes
- **Responsive Design**: Clean, modern interface built with Django templates

## Tech Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (default)
- **PDF Generation**: WeasyPrint 66.0
- **NLP/Analysis**: spaCy 3.8.11 with en_core_web_sm model
- **Web Server**: Gunicorn 23.0.0
- **Image Processing**: Pillow 12.0.0
- **Frontend**: Django Templates with CSS styling

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd resume-builder
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

## Usage

### Creating a Resume

1. Register a new account or log in
2. Navigate to the "Build Resume" page
3. Fill in your personal information, summary, skills, experience, education, and other details
4. Upload a professional profile image (optional)
5. Click "Create Resume" to generate your resume
6. The system will automatically:
   - Analyze your resume content
   - Provide a quality score and suggestions
   - Generate a professional PDF

### Managing Resumes

- **View Dashboard**: See all your created resumes with statistics
- **Edit Resume**: Modify existing resumes and regenerate PDFs
- **Delete Resume**: Remove resumes you no longer need
- **Download PDF**: Download your resume as a professionally formatted PDF

### Resume Analysis

The application analyzes your resume and provides:
- **Quality Score** (0-100) based on:
  - Use of action verbs
  - Inclusion of quantifiable metrics
  - Completeness of profile
  - Presence of expertise and languages
- **Suggestions** for improvement in areas such as:
  - Adding more action verbs
  - Including measurable achievements
  - Expanding your summary
  - Adding a profile photo
  - Showcasing expertise and languages

## Project Structure

```
resume-builder/
├── accounts/                 # User authentication app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── forms.py             # Authentication forms
│   ├── models.py            # User models
│   ├── urls.py              # URL patterns
│   └── views.py             # View functions
├── resumes/                 # Resume management app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── forms.py             # Resume forms
│   ├── models.py            # Resume models
│   ├── urls.py              # URL patterns
│   └── views.py             # View functions
├── resume_builder/          # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── media/                   # User-uploaded files
│   ├── profile_images/      # Profile pictures
│   └── resumes/             # Generated PDFs
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── db.sqlite3              # SQLite database (default)
```

## Configuration

### Media Files

Media files are stored in the `media/` directory:
- Profile images: `media/profile_images/user_{id}/`
- Generated PDFs: `media/resumes/`

### Database

The default configuration uses SQLite. To use a different database (PostgreSQL, MySQL, etc.), modify the `DATABASES` setting in `resume_builder/settings.py`.

### Security

For production deployment:
- Set `DEBUG = False` in settings
- Change the `SECRET_KEY` to a secure value
- Configure `ALLOWED_HOSTS` with your domain
- Use environment variables for sensitive configuration
- Set up proper file permissions for media directories

## Deployment

### Using Gunicorn

1. Install Gunicorn (included in requirements.txt)
2. Run the application:
   ```bash
   gunicorn resume_builder.wsgi:application
   ```

### Production Considerations

- Use a production-grade web server (Nginx, Apache)
- Configure static files serving
- Set up a production database (PostgreSQL recommended)
- Configure HTTPS/SSL certificates
- Set up regular database backups
- Monitor application logs

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues, questions, or suggestions, please open an issue on the repository or contact the development team.

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- PDF generation powered by [WeasyPrint](https://weasyprint.org/)
- NLP analysis using [spaCy](https://spacy.io/)
- Styled with modern CSS and responsive design principles

---

**Note**: This application is intended for educational and personal use. For production deployments, ensure proper security measures and testing are implemented.