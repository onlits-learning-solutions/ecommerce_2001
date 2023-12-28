from django.db import models

# Create your models here.
class Seller (models.Model) :
    name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    gstin = models.CharField(max_length=15)
    pan = models.CharField(max_length=10, null=True)
