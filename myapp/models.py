from django.db import models

# Create your models here.

class registration(models.Model):
  name = models.CharField(max_length=50)
  dob = models.DateField()
  gender = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  pin = models.IntegerField()
  mobile = models.IntegerField()
  email = models.EmailField()
  job_location = models.CharField(max_length=50)
  image = models.ImageField(upload_to ='image', blank=True)
  file = models.FileField(upload_to='file', blank=True)



