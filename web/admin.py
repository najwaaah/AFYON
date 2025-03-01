from django.contrib import admin
from .models import Rating, Services, Contact, Products

# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ( 'name',)  

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ( 'name',) 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ()
