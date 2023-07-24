from django.contrib import admin
from .models import Product, Profile, Addres
# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Addres)
