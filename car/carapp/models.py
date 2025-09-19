from django.db import models
from django.contrib import admin

class Car(models.Model):
    name = models.CharField(max_length=255, help_text="Car Name")
    brand = models.CharField(max_length=100, help_text="Car Brand")
    release_date = models.DateField(help_text="Release Date")
    car_type = models.CharField(max_length=50, help_text="Car Type (e.g., SUV, Sedan)")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Car Price (e.g., 1500000.00)")
    horsepower = models.IntegerField(help_text="Horsepower (e.g., 250)")

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'release_date', 'car_type', 'price', 'horsepower')