from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request): 
     form = LoginForm(request.POST or None)
     if form.is_valid():
          username = form.cleaned_data.get('username')
          password = form.cleaned_data.get('password')
          user = authenticate(username = username, password=password)
          if user is None : 
               return render(request,'login/login.html')
          else : 
               login(request, user)
               return redirect('home')
     return render(request, 'login/login.html')





