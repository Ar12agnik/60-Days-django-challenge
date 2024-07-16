from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the index.")
def view2(request):
    return HttpResponse("Hello, world. You're at view2.")
def view3(request):
    return HttpResponse("Hello, world. You're at view3.")