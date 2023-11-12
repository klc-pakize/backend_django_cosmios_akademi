from django.shortcuts import render
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Brand, Product, Firm, Purchases, Sales
from .serializers import CategorySerializer, CategoryProductSerializer, BrandSerializer, FirmSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.query_params.get("name"):
            return CategoryProductSerializer
        return super().get_serializer_class()
    

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    
class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']

class PurchaseView(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['firm', 'product']
    search_fields = ['firm']    


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #! #############  ADD Product Stock ############
        
        purchase = request.data
        product = Product.objects.get(id=purchase["product_id"])
        product.stock += int(purchase["quantity"])
        product.save()
        
        #! #############################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)         

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        #! #############  UPDATE Product Stock ############
        purchase = request.data
        product = Product.objects.get(id=purchase["product_id"])
        
        sonuc = int(purchase["quantity"])- instance.quantity
        product.stock += sonuc
        product.save()
        #! #############################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #! #############  DELETE Product Stock ############
        product = Product.objects.get(id=instance.product_id)
        product.stock -= instance.quantity
        product.save()
        #! ###########################################
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    
class SalesView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand','product']
    search_fields = ['brand']
    
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #! #############  REDUCE Product Stock ############
        
        sales = request.data
        product = Product.objects.get(id=sales["product_id"])
        
        if int(sales["quantity"]) <= product.stock:
            product.stock -= int(sales["quantity"])
            product.save()
        else:
            data = {
                "message": f"Dont have enough stock, current stock is {product.stock}"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        #! #############################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        #!####### UPDATE Product Stock ########
        sale = request.data
        product= Product.objects.get(id=instance.product_id) 
        
        if int(sale["quantity"]) > instance.quantity:
            
            if int(sale["quantity"]) <= instance.quantity + product.stock:
                product.stock = instance.quantity + product.stock - int(sale["quantity"])
                product.save()
            else:
                data = {
                "message": f"Dont have enough stock, current stock is {product.stock}"
                }
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            
        elif instance.quantity >= int(sale["quantity"]):
            product.stock += instance.quantity - int(sale["quantity"])
            product.save()
         
        #!##################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        #!####### DELETE Product Stock ########
        product = Product.objects.get(id=instance.product_id)
        product.stock += instance.quantity
        product.save()
        #!##################################
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)