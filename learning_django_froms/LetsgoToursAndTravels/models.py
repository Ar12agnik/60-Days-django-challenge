from django.db import models
class Tour(models.Model):
    name = models.CharField(max_length=100,verbose_name="Tour Name")
    place=models.ForeignKey('places',on_delete=models.CASCADE,verbose_name="Place")
    description = models.TextField(verbose_name = "Description")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name = "Price")
    duration = models.IntegerField(verbose_name = "Duration")
    departure = models.DateTimeField(verbose_name = "Departure")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "Created At")
    updated_at = models.DateTimeField(auto_now=True,verbose_name = "Updated At")
    def __str__(self):
        return self.name
class agencies(models.Model):
    name=models.CharField(max_length=100,verbose_name = "Agency Name")
    address=models.TextField(verbose_name = "Address")
    representative=models.CharField(max_length=100,verbose_name = "Representative")
    contact=models.CharField(max_length=100,verbose_name = "Contact")
    Tours_available=models.ManyToManyField(Tour,verbose_name = "Tours Available")
    def __str__(self):
        return self.name
class places(models.Model):
    name=models.CharField(max_length=100,verbose_name = "Place Name")
    description=models.TextField(verbose_name = "Description")
    def __str__(self):
        return self.name