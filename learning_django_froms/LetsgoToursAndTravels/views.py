from django.shortcuts import render
from .models import Tour,agencies,places,pictures
from .forms import TourForm,addTourForm,addAgenciesForm,addPlacesForm,pictures_upload_form
from django.views.generic import View
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    
    page=request.GET.get('page',1)
    prev=request.GET.get('prev',False)
    next=request.GET.get('next',False)
    Tours_avilable=Tour.objects.all()
    Tours_avilable=Paginator(Tours_avilable, 1)
    total_no_of_pages=Tours_avilable.num_pages
    if not prev and not next:
        if int(page)<1:
            page=1

        Tours_avilable=Tours_avilable.page(page)
    elif prev=='true':
        page=int(page)-1
        if page<1:
            page=1
        Tours_avilable=Tours_avilable.page(page)
    elif next=='true':
        page=int(page)+1
        if page>total_no_of_pages:
            page=total_no_of_pages
        Tours_avilable=Tours_avilable.page(page)
    
    return render(request,'index.html',context={'tours_avilable':Tours_avilable,"page":int(page)})
#** class based view
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
# class tour_form(View):
#     def get(self,request):
#         tf=TourForm()
#         return render (request,"tour_form.html",context={'form':tf})
#     def post(self,request):
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
class tour_form(View):
    form_class=TourForm
    inicial={"Name":"your name","phone":1234567890,"address":"Kerala","insurance":False}
    template_name='tour_form.html'
    def get(self,request):
        form=self.form_class(initial=self.inicial)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            tour=form.cleaned_data['Tour']
            Name=form.cleaned_data['Name']
            phone=form.cleaned_data['phone']
            address=form.cleaned_data['address']
            insurance=form.cleaned_data['insurance']
            tour=Tour.objects.get(name=tour)
            agency=agencies.objects.get(Tours_available=tour.id)
            return render(request,self.template_name,context={'tour':tour,'Name':Name,'phone':phone,'address':address,'insurance':insurance,'Tour':tour,"Agency":agency,'data':True})
        else:
            return render(request,self.template_name,context={'message':"error processing data!"})
    
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