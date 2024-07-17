from django.db import models
class Tour(models.Model):
    name = models.CharField(max_length=100)
    place=models.ForeignKey('places',on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    departure = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class agencies(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    representative=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    Tours_available=models.ManyToManyField(Tour)
    def __str__(self):
        return self.name
class places(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name