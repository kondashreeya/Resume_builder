from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('form/', views.resume_form, name='form'),
    path('resume/<int:id>/', views.view_resume, name='view_resume'),
    path('edit/<int:id>/', views.resume_form, name='edit'),
    path('delete/<int:id>/', views.delete_resume, name='delete'),
    path('download/<int:id>/', views.download_resume, name='download'),
]