from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('build/', views.build_resume, name='build_resume'),
    path('download/<int:resume_id>/', views.download_resume, name='download_resume'),
    path('dashboard/', views.dashboard, name='dashboard'),
]