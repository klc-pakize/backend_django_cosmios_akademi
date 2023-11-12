from django.db import models
from django.contrib.auth.models import User

class UpdateCreate(models.Model):
    createds = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
class Brand(models.Model):
    name = models.CharField(max_length=25, unique=True)
    image = models.TextField()
    
    def __str__(self):
        return self.name
    
class Product(UpdateCreate):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="b_products")
    stock = models.PositiveSmallIntegerField(blank=True, default=0)

    
    def __str__(self):
        return self.name
    
class Firm(UpdateCreate):
    name = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    image = models.TextField()


    def __str__(self):
        return self.name

class Purchases(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name="purchases")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="b_purchases")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="purchase")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    
    def __str__(self):
        return f'{self.product} - {self.quantity}'
    
class Sales(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="b_sales")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sale")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    
    def __str__(self):
        return f'{self.product} - {self.quantity}'