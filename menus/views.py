from django.shortcuts import render
from .models import foodInfo
from home.models import patientInfo
import random
# Create your views here.



def menu_view(request):
    morningPlan = []
    morningTime = "9:00"
    eveningPlan = []
    eveningTime = "18:00"
    mPlan = []
    ePlan = []
    a = 0
    b = 0
    foodInfos = foodInfo.objects.all()
    patientInfos = patientInfo.objects.get(id=23)
    if request.method == "POST" :
        foods = request.POST.getlist('foods')
        for f in foods : 
            if foodInfo.objects.get(id=f).foodCalorie > 110 :
               
                morningPlan.append(foodInfo.objects.get(id=f).foodName)
                
            else : 
                eveningPlan.append(foodInfo.objects.get(id=f).foodName)  
        while a < len(morningPlan) :
            mPlan.append(morningPlan[random.randint(0,len(morningPlan)-1)])
            a += 1
        while b < len(eveningPlan) :
            ePlan.append(eveningPlan[random.randint(0,len(eveningPlan)-1)])
            b += 1
        print(mPlan)
        print(ePlan)
    return render(request,'diet-plan/diet-plan.html',{'foodInfos':foodInfos,'patientInfos':patientInfos,
    'morningPlan':mPlan,'eveningPlan':ePlan,'morningTime':morningTime,'eveningTime':eveningTime})