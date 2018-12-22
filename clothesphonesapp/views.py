from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import Http404


# Create your views here.


def home(request):
    phoneshop1   = Shop.objects.filter(shop_type= "PHONES").order_by("-num_of_share")[0]
    phoneshop2   = Shop.objects.filter(shop_type= "PHONES").order_by("-num_of_share")[1]
    phoneshop3   = Shop.objects.filter(shop_type= "PHONES").order_by("-num_of_share")[2]
    clothesshop1   = Shop.objects.filter(shop_type= "CLOTHES").order_by("-num_of_share")[0]
    clothesshop2   = Shop.objects.filter(shop_type= "CLOTHES").order_by("-num_of_share")[1]
    clothesshop3   = Shop.objects.filter(shop_type= "CLOTHES").order_by("-num_of_share")[2]
    queryset = TextAdv.objects.all()
    queryset2 = MediaAdv.objects.all()
    context = {
        'object_list': queryset,
        'object_list2': queryset2,
        'phoneshop1' : phoneshop1,
        'phoneshop2' : phoneshop2,
        'phoneshop3' : phoneshop3,
        'clothesshop1' : clothesshop1,
        'clothesshop2' : clothesshop2,
        'clothesshop3' : clothesshop3,
        }


    return(render(request , 'home.html' , context))

def clothes_shops(request):
    clothes_shop = Shop.objects.filter(shop_type= "CLOTHES").order_by("-num_of_share")
    queryset = MediaAdv.objects.all()
    queryset2 = TextAdv.objects.all()
    context = {
        'object_list3': queryset,
        'object_list': clothes_shop,
        'object_list2': queryset2

    }
    return render(request, "ClothesShop.html", context)




def clothes(request, pk=None):
    shop = Shop.objects.get(id=pk)
    Shop.objects.filter(id=pk).update(num_of_share = int(shop.num_of_share) +1)
    product= Product.objects.filter(shop_name = shop)
    queryset2 = TextAdv.objects.all()
    queryset = MediaAdv.objects.all()


    context = {
        'shops': shop,
        'products' : product,
        'object_list2': queryset2,
        'object_list' : queryset

    }
    return render(request, 'clothes.html' , context)



def mobiles_shops(request):
    phones_shop = Shop.objects.filter(shop_type= "PHONES").order_by("-num_of_share")
    queryset2 = TextAdv.objects.all()
    queryset = MediaAdv.objects.all()

    context= {
        'object_list': phones_shop,
        'object_list2': queryset2,
        'object_list3': queryset,


    }
    return(render(request , 'MobileShop.html' , context))



def mobiles(request , pk= None):
    shop = Shop.objects.get(id=pk)
    Shop.objects.filter(id=pk).update(num_of_share = int(shop.num_of_share) +1)
    product = Product.objects.filter(shop_name = shop)
    queryset2 = TextAdv.objects.all()
    # queryset = MediaAdv.objects.all()


    context= {
        'shops' : shop ,
        'products' : product,
        'object_list2': queryset2,
        'object_list' : queryset

    }

    return(render(request , 'mobiles.html' , context))
