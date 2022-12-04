from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from resume.models import Resume
from django.shortcuts import render
import pdfkit
import uuid
from resume.forms import ResumeForm
from django.template.loader import render_to_string
from django.http import HttpResponse

@login_required
def redirect_to_user_page(request):
    return redirect('resume_list_url', user_login=request.user.username)


@login_required
def resume_list(request, user_login):
    if user_login != request.user.username:
        return redirect_to_user_page(request)
    resumes = Resume.objects.filter(user=request.user.id)
    return render(request, 'resume_list.html', locals())


@login_required
def resume_create(request, user_login):
    if user_login != request.user.username:
        return redirect_to_user_page(request)
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list_url', user_login=request.user.username)
        else:
            return render(request, 'create_resume.html', locals())
    form = ResumeForm()
    return render(request, 'create_resume.html', locals())



@login_required
def resume_download(request, user_login, resume_name):
    if user_login != request.user.username:
        return redirect_to_user_page(request)
    resume = Resume.objects.get(user=request.user.id, name=resume_name)
    pdf = pdfkit.from_string(render_to_string('resume.html', locals(), request), False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Resume!"'
    return response

@login_required
def resume_view(request, user_login, resume_name):
    if user_login != request.user.username:
        return redirect_to_user_page(request)
    resume = Resume.objects.get(user=request.user.id, name=resume_name)
    return render(request, 'resume.html', locals())
