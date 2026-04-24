from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
# import pdfkit
from xhtml2pdf import pisa
from io import BytesIO


def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})



def resume_form(request, id=None):
    if id:
        obj = get_object_or_404(Resume, id=id)
    else:
        obj = None
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=obj)
    return render(request, 'form.html', {'form': form})



def download_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    template = get_template('view_resume.html')
    html = template.render({'resume': resume})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response



def delete_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    resume.delete()
    return redirect('resume_list')

def view_resume(request, id):
    resume = Resume.objects.get(id=id)

    context = {
        'resume': resume,
        'skills_list': resume.skills.splitlines(),
        'certifications_list': resume.certifications.splitlines(),
        'interpersonal_list': resume.interpersonal_skills.splitlines(),
    }
    return render(request, 'view_resume.html', context)

