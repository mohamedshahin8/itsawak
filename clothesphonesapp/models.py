import random
import os
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.


class Shop(models.Model):
    types           = (
        ('CLOTHES' , "CLOTHES"),
        ('PHONES'  , "PHONES")
    )

    shop_type       = models.CharField(max_length = 7 , choices = types , default = None)
    shop_owner      = models.ForeignKey(User, on_delete= models.CASCADE)
    shop_name       = models.CharField(max_length= 25)
    shop_phone      = models.CharField(max_length= 11)
    shop_location   = models.CharField(max_length= 220)
    num_of_share    = models.DecimalField(max_digits= 10 , decimal_places= 0, default= 0)
    shop_image   = models.CharField(max_length = 700 , default = None)
    class Meta:
        ordering = ['num_of_share']

    def __str__(self):
        return(self.shop_name)



class Product(models.Model):

    type                = models.CharField(max_length= 120 , help_text="T-shirt , Pantalon , Sheos , Phone , Laptop...etc")
    color               = models.CharField(max_length= 120, help_text="red , green , black , blue....")
    size                = models.CharField(max_length= 10 ,default= 'S' , help_text= "S,M,L,XL,XXL")
    price               = models.DecimalField(decimal_places = 2 , max_digits = 20, default= 0.00)
    describtion         = models.TextField(null = True , help_text = 'this is optional if type is ACCESSORIES')
    shop_name           = models.ForeignKey('Shop' , on_delete = models.CASCADE)
    product_image    = models.CharField(max_length = 700 ,default = None )

    class Meta:
        ordering = ['price']
    def __str__(self):
        return(self.type)


class TextAdv(models.Model):
    address1_text = models.CharField(max_length = 300 , default = None ,help_text = 'write you advertise here')
    address2_text = models.CharField(max_length = 300 , default = None ,help_text = 'write you advertise here')
    address3_text = models.CharField(max_length = 300 , default = None ,help_text = 'write you advertise here')


class MediaAdv(models.Model):
    homephoto1  = models.CharField(max_length = 700 ,default = None )
    homephoto2  = models.CharField(max_length = 700 ,default = None )
    homephoto3 = models.CharField(max_length = 700 ,default = None )

    home2photo1 = models.CharField(max_length = 700 ,default = None )
    home2photo2 = models.CharField(max_length = 700 ,default = None )
    home2photo3 = models.CharField(max_length = 700 ,default = None )

    cloth1photo1 = models.CharField(max_length = 700 ,default = None )
    cloth1photo2 = models.CharField(max_length = 700 ,default = None )
    cloth1photo3 = models.CharField(max_length = 700 ,default = None )


    cloth2photo1 = models.CharField(max_length = 700 ,default = None )
    cloth2photo2 = models.CharField(max_length = 700 ,default = None )
    cloth2photo3 = models.CharField(max_length = 700 ,default = None )


    cloth3photo1 = models.CharField(max_length = 700 ,default = None )
    cloth3photo2 = models.CharField(max_length = 700 ,default = None )
    cloth3photo3 = models.CharField(max_length = 700 ,default = None )


    cloth4photo1 = models.CharField(max_length = 700 ,default = None )
    cloth4photo2 = models.CharField(max_length = 700 ,default = None )
    cloth4photo3 = models.CharField(max_length = 700 ,default = None )



    phone1photo1 = models.CharField(max_length = 700 ,default = None )
    phone1photo2 = models.CharField(max_length = 700 ,default = None )
    phone1photo3 = models.CharField(max_length = 700 ,default = None )


    phone2photo1 = models.CharField(max_length = 700 ,default = None )
    phone2photo2 = models.CharField(max_length = 700 ,default = None )
    phone2photo3 = models.CharField(max_length = 700 ,default = None )


    phone3photo1 = models.CharField(max_length = 700 ,default = None )
    phone3photo2 = models.CharField(max_length = 700 ,default = None )
    phone3photo3 = models.CharField(max_length = 700 ,default = None )


    phone4photo1 = models.CharField(max_length = 700 ,default = None )
    phone4photo2 = models.CharField(max_length = 700 ,default = None )
    phone4photo3 = models.CharField(max_length = 700 ,default = None )

    cloth5photo = models.CharField(max_length = 700 ,default = None )
    phone5photo = models.CharField(max_length = 700 ,default = None )
