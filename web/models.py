from django.db import models

# Create your models here.
class Rating(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/ratings')
    description = models.TextField(default='no')


    class Meta:
        verbose_name_plural = "rating"
        verbose_name = "Ratings"
    def __str__(self):
        return self.name 
    
class Services(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/services')
    


    class Meta:
        verbose_name_plural = "service"
        verbose_name = "Services"
    def __str__(self):
        return self.name 
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name   

class Products(models.Model):
    image = models.ImageField(upload_to='media/products')
    


    class Meta:
        verbose_name_plural = "product"
        verbose_name = "Products"     