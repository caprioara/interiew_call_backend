from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User

def register_account(request):
    template_name = 'account/register.html'

    register_form = RegistrationForm()
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            user = User.objects.create(username=username, email=email, is_staff=False, is_active=False)
            user.set_password(password)
            user.save()

            # display register data on another page
            return redirect('display_data')

    return render(request, template_name, {'register_form': register_form})