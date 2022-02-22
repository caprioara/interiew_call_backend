from django.shortcuts import render
from django.contrib.auth.models import User

def display_data(request):
    template_name="account/display_data.html"

    users = User.objects.all()

    return render(request, template_name, {'users': users})