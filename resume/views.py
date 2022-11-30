from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from resume.models import Resume
from django.shortcuts import render
import pdfkit
import uuid
from resume.forms import ResumeForm
@login_required
def redirect_to_user_page(request):
    return redirect('resume_list_url', user_login=request.user.username)


@login_required
def resume_list(request, user_login):
    if user_login != request.user.username:
        redirect_to_user_page(request)
    resumes = Resume.objects.filter(user=request.user.id)
    return render(request, 'resume_list.html', locals())


@login_required
def resume_create(request, user_login):
    if user_login != request.user.username:
        redirect_to_user_page(request)
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list_url', user_login=request.user.username)
    form = ResumeForm()
    return render(request, 'create_resume.html', locals())



@login_required
def resume_download(request, user_login, resume_name):
    if user_login != request.user.username:
        redirect_to_user_page(request)
    resume = Resume.objects.get(user=request.user.id, name=resume_name)
    a = render(request, 'resume.html', locals())
    path = 'resume/resumes/{}.pdf'.format(uuid.uuid4())
    pdfkit.from_string(str(a.content), path)
    a['Content-Disposition'] = "attachment; filename=%s" % path
    return a

@login_required
def resume_view(request, user_login, resume_name):
    if user_login != request.user.username:
        redirect_to_user_page(request)
    resume = Resume.objects.get(user=request.user.id, name=resume_name)
    return render(request, 'resume.html', locals())
