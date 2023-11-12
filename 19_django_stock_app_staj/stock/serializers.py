from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchases, Sales

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  # read_only
    
    class Meta:
        model = Category
        fields = ("id", "name", "product_count")
        
    def get_product_count(self, obj):
        return Product.objects.filter(category=obj).count()
    
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stock",
        )

        read_only_fields = ("stock",) 
        

class CategoryProductSerializer(serializers.ModelSerializer):
    
    products = ProductSerializer(many=True, read_only = True)
    product_count = serializers.SerializerMethodField()  # read_only
    
    class Meta:
        model = Category
        fields = ("id", "name", "product_count", "products")
        
    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
    

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image'
        )
        
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'image',
            'address'
        )


class PurchasesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField() 
    firm = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()

    
    class Meta:
        model = Purchases
        fields = (
            "id",
            "user",
            "user_id",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            'category',
        )
        
    # def get_category(self, obj):
    #     product = Product.objects.get(id=obj.product_id)
    #     return Category.objects.get(id=product.category_id).name
    
    def get_category(self, obj):
        return obj.product.category.name
    
class SalesSerializer(serializers.ModelSerializer):
    
        user = serializers.StringRelatedField() 
        brand = serializers.StringRelatedField()
        product = serializers.StringRelatedField()
        product_id = serializers.IntegerField()
        brand_id = serializers.IntegerField()

        
        class Meta:
            model = Sales
            fields = (
                "id",
                "user",
                "user_id",
                "brand",
                "brand_id",
                "product",
                "product_id",
                "quantity",
                "price",
                "price_total",

            )
            

    
 
    