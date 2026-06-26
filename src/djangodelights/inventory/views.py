from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('login')





