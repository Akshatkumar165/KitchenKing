from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=200,primary_key=True)
    fisrt_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10 ,null=True)
    address=models.CharField(max_length=300 ,null=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    name=models.CharField(max_length=254,primary_key=True)
    price=models.FloatField()
    stock=models.IntegerField()
    delivery=models.FloatField(default=0)
    des_line1=models.CharField(max_length=500,default="",null=True,blank=True)
    des_line2=models.CharField(max_length=500,default="",null=True,blank=True)
    des_line3=models.CharField(max_length=500,default="",null=True,blank=True)
    des_line4=models.CharField(max_length=500,default="",null=True,blank=True)
    des_line5=models.CharField(max_length=500,default="",null=True,blank=True)
    img1=models.ImageField(null=True,blank=True)
    img2=models.ImageField(null=True,blank=True)
    img3=models.ImageField(null=True,blank=True)
    img4=models.ImageField(null=True,blank=True)
    img5=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    pass
    

