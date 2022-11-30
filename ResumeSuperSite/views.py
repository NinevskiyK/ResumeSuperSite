from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings


def main_page(request):
    if not request.user.is_authenticated:
        return redirect('{}?next={}'.format(reverse('login'), reverse('resume_redirect_url')))
    else:
        return redirect('resume_redirect_url')
