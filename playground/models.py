from django.db import models

# Create your models here.
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images/')
    generic_name = models.CharField(max_length=100)
    manufacture = models.CharField(max_length=66)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    batch_number = models.CharField(max_length=100)
    description = models.TextField()