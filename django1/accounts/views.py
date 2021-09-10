from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView): # generic view default django
    form_class = UserCreationForm # form default
    success_url = reverse_lazy('login') # like a redirect, where the user will go after signup, use when u create a baseview
    template_name = 'registration/register.html'
