from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})




