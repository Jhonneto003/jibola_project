from django.db import models
from User_service.models import CustomUser
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
# User = get_user_model()
# default_user = User.objects.first()

class Category(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
    

class Store(models.Model):
    name_of_store= models.CharField(max_length= 200)
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code = models.IntegerField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_stores')
    

     
    def __str__(self) -> str:
        return f'{self.name_of_store}'

class Products(models.Model):
    name= models.CharField(max_length=100, blank=False)
    description= models.TextField(null=True, blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    store=models.ForeignKey(Store, on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner_products')


   
     
    def __str__(self) -> str:
        return f'{self.name}'

