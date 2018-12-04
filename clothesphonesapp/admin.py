from django.contrib import admin
from .models import *


class ProductInline(admin.TabularInline):
    model = Product



class ShopAdmin(admin.ModelAdmin):
    exclude             = ("num_of_share",)
    list_display        = ('shop_name' ,'shop_owner' , 'shop_location' , 'shop_phone' , 'num_of_share' , 'shop_type')
    list_filter         = ('shop_type' , )
    def get_queryset(self, request):
        qs = super(ShopAdmin, self).get_queryset(request)
        shop_owner = request.user
        if request.user.is_superuser:
            return qs
        return qs.filter(shop_owner=request.user)

    def changelist_view(self, request):
        if not request.user.is_superuser:
            self.list_display = ('shop_name' ,'shop_owner' , 'shop_location' , 'shop_phone' )
        return super(ShopAdmin , self).changelist_view(request)

    inlines         = [ProductInline]

admin.site.register(TextAdv)
admin.site.register(MediaAdv)
# admin.site.register(Product)
admin.site.register(Shop , ShopAdmin)
