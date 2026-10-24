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