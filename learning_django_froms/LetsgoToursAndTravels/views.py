from django.shortcuts import render
from .models import Tour,agencies,places
from .forms import TourForm
# Create your views here.
def index(request):
    Tours_avilable=Tour.objects.all()
    return render(request,'index.html',context={'tours_avilable':Tours_avilable})
def tour_form(request):
    if request.method=='POST':
        tf=TourForm(request.POST)
        print(tf.is_valid())
        if tf.is_valid():
            print("valid")
            tour=tf.cleaned_data['Tour']
            Name=tf.cleaned_data['Name']
            phone=tf.cleaned_data['phone']
            address=tf.cleaned_data['address']
            insurance=tf.cleaned_data['insurance']
            tour=Tour.objects.get(name=tour)
            agency=agencies.objects.get(Tours_available=tour.id)
            return render(request,'tour_form.html',context={'tour':tour,'Name':Name,'phone':phone,'address':address,'insurance':insurance,'Tour':tour,"Agency":agency,'data':True})
        else:
            return render(request,'tour_form.html',context={'message':"error processing data!"})
    else:
        tf=TourForm()
        return render (request,"tour_form.html",context={'form':tf})