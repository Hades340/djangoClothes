from functools import total_ordering
from django.db import models
import datetime
# Create your models here.
#python manage.py makemigrations 
#python manage.py migrate

class category_product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_type = models.CharField(max_length=400)
    category_owner = models.CharField(max_length=400, null=True, choices= [{"Men","Woman"}], default="Men")
    def __str__(self):
        return self.category_type

class product_detail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    size = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(category_product,on_delete=models.CASCADE)
    name = models.TextField()
    img = models.ImageField()
    decription = models.TextField()
    detail = models.TextField()
    price = models.FloatField()
    sale = models.BooleanField()
    product_detail_id = models.ManyToManyField(product_detail)
    def __str__(self):
        return self.name



class customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length= 300)
    address = models.TextField()
    phone = models.FloatField()
    def __str__(self):
        return self.username

class order(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_oder = models.DateField(auto_created=True,auto_now_add=True)
    id_Customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    total = models.FloatField()
    def __str__(self):
        return str(self.date_oder)
    
class order_detail(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    def __str__(self):
        return self.order_id
    
