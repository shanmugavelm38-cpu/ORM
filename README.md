# Ex02 Django ORM Web Application
## Date: 24-10-2026
## REG NO: 26008603
## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
from django.db import models
from django.contrib import admin
class cardb(models.Model):
    carname = models.CharField(max_length=100)
    carid = models.IntegerField(primary_key=True)
    carmodel = models.CharField(max_length=100)
    carprice = models.IntegerField()
    carcolor = models.CharField(max_length=100)
    automatic = models.BooleanField(default=False)
    comments = models.TextField()
class carAdmin(admin.ModelAdmin):
    list_display = ('carname', 'carmodel', 'carprice', 'carcolor', 'automatic')



from django.contrib import admin
from .models import cardb, carAdmin
admin.site.register(cardb, carAdmin)
~~~


## OUTPUT
![alt text](<Screenshot 2026-10-24 154322.png>)

## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
