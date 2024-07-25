from django.contrib import admin
from .models import Tour, agencies,places,pictures,bookings
admin.site.register(Tour)
admin.site.register(agencies)
admin.site.register(places)
admin.site.register(pictures)
admin.site.register(bookings)

# Register your models here.
