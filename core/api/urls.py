
from django.urls import path
from expense import views
urlpatterns = [
    path("view_transactions/", views.get_transactions),
]
