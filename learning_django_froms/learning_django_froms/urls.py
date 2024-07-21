"""
URL configuration for learning_django_froms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LetsgoToursAndTravels.views import index, tour_form, add_tour, add_agency, add_place, upload_picture,view_picture
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('form', tour_form.as_view(),name='tour_form'),
    path('add_place', add_place,name='add_place'),
    path('add_agency', add_agency,name='add_agency'),
    path('add_tour', add_tour.as_view(),name='add_tour'),
    path('upload_picture', upload_picture,name='upload_picture'),
    path('view_picture', view_picture,name='view_picture'),
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
