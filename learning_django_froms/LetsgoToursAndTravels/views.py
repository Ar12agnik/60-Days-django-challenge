from django.shortcuts import render
from .models import Tour,agencies,places,pictures
from .forms import TourForm,addTourForm,addAgenciesForm,addPlacesForm,pictures_upload_form
from django.views.generic import View
# Create your views here.
def index(request):
    Tours_avilable=Tour.objects.all()
    return render(request,'index.html',context={'tours_avilable':Tours_avilable})
# def tour_form(request):
#     if request.method=='POST':
#         tf=TourForm(request.POST)
#         print(tf.is_valid())
#         if tf.is_valid():
#             print("valid")
#             tour=tf.cleaned_data['Tour']
#             Name=tf.cleaned_data['Name']
#             phone=tf.cleaned_data['phone']
#             address=tf.cleaned_data['address']
#             insurance=tf.cleaned_data['insurance']
#             tour=Tour.objects.get(name=tour)
#             agency=agencies.objects.get(Tours_available=tour.id)
#             return render(request,'tour_form.html',context={'tour':tour,'Name':Name,'phone':phone,'address':address,'insurance':insurance,'Tour':tour,"Agency":agency,'data':True})
#         else:
#             return render(request,'tour_form.html',context={'message':"error processing data!"})
#     else:
#         tf=TourForm()
#         return render (request,"tour_form.html",context={'form':tf})
class tour_form(View):
    def get(self,request):
        tf=TourForm()
        return render (request,"tour_form.html",context={'form':tf})
    def post(self,request):
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
        
# def add_tour(request):
#     if request.method=='POST':
#         tf=addTourForm(request.POST)
#         if tf.is_valid():
#             tf.save()
#             return render(request,'add_tour.html',context={'message':"Tour added successfully!"})
#         else:
#             return render(request,'add_tour.html',context={'message':"error adding tour!"})
#     else:
#         tf=addTourForm()
#         return render(request,'add_tour.html',context={'form':tf})
class add_tour(View):
    def get(self,request):
        tf=addTourForm()
        return render(request,'add_tour.html',context={'form':tf})
    def post(self,request):
        tf=addTourForm(request.POST)
        if tf.is_valid():
            tf.save()
            return render(request,'add_tour.html',context={'message':"Tour added successfully!"})
        else:
            return render(request,'add_tour.html',context={'message':"error adding tour!"})

        
# def add_agency(request):    
#     if request.method=='POST':
#         tf=addAgenciesForm(request.POST)
#         if tf.is_valid():
#             tf.save()
#             return render(request,'add_agency.html',context={'message':"Agency added successfully!"})
#         else:
#             return render(request,'add_agency.html',context={'message':"error adding agency!"})
#     else:
#         tf=addAgenciesForm()
#         return render(request,'add_agency.html',context={'form':tf})
class add_agency(View):
    def get(self,request):
        tf=addAgenciesForm()
        return render(request,'add_agency.html',context={'form':tf})
    def post(self,request):
        tf=addAgenciesForm(request.POST)
        if tf.is_valid():
            tf.save()
            return render(request,'add_agency.html',context={'message':"Agency added successfully!"})
        else:
            return render(request,'add_agency.html',context={'message':"error adding agency!"})
# def add_place(request):
#     if request.method=='POST':
#         tf=addPlacesForm(request.POST)
#         if tf.is_valid():
#             tf.save()
#             return render(request,'add_place.html',context={'message':"Place added successfully!"})
#         else:
#             return render(request,'add_place.html',context={'message':"error adding place!"})
#     else:
#         tf=addPlacesForm()
#         return render(request,'add_place.html',context={'form':tf})
class add_place(View):
    def get(self,request):
        tf=addPlacesForm()
        return render(request,'add_place.html',context={'form':tf})
    def post(self,request):
        tf=addPlacesForm(request.POST)
        if tf.is_valid():
            tf.save()
            return render(request,'add_place.html',context={'message':"Place added successfully!"})
        else:
            return render(request,'add_place.html',context={'message':"error adding place!"})
# def upload_picture(request):
#     if request.method=="POST":
#         form=pictures_upload_form(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request,'upload_picture.html',context={'message':"Picture uploaded successfully!"})  
#         else:
#             return render(request,'upload_picture.html',context={'message':"error uploading picture!",'form':form})
#     else:
#         form=pictures_upload_form()
#         return render(request,'upload_picture.html',context={'form':form})
class upload_picture(View):
    def get(self,request):
        form=pictures_upload_form()
        return render(request,'upload_picture.html',context={'form':form})
    def post(self,request):
        form=pictures_upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'upload_picture.html',context={'message':"Picture uploaded successfully!"})  
        else:
            return render(request,'upload_picture.html',context={'message':"error uploading picture!",'form':form})
def view_picture(request):
    pics=pictures.objects.all()
    return render(request,'viewpicture.html',context={'pics':pics})