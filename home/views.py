from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import patientInfo

# Create your views here.

def home_page(request):
    if request.method == "POST" :

        length = int(request.POST.get('patientSize'))
        weight = int(request.POST.get('patientWeight'))
        bmi = weight / (length * length / 10000)
        if bmi <= 25 : 
            info = "WEAK"
        else :
            info = "FAT"
        patientInfo.objects.create(userName="Ert",bodyBmi=bmi,bodyInfo=info)
   
        return redirect('menus')
    return render(request,'home/home.html',{})

def logout_view(request):
     logout(request)
     return render(request, 'login/login.html')

  

