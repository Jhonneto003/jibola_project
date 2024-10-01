from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StoreSerializer, CategorySerializer , ProductSerializer
from .models import Store, Products, Category
from User_service.models import CustomUser
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from django.http import Http404
from django.db.models import Q

# Create your views here.

class StoreCreationEndpoint(generics.CreateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetailEndpoint(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    authentication_classes = [TokenAuthentication]




    def get_queryset(self):
        # Get the logged-in user
        user = self.request.user
        
        # Filter stores by the logged-in user
        return Store.objects.filter(owner=user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        # Check if the user is the author of the blog post
    
        return obj



class CategoryCreationEndpoint(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes =[IsAuthenticated]
    queryset= Category.objects.all()
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer= CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryDetailEndpoint(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes =[IsAuthenticated]
    queryset= Category.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj


class ProductDetailEndpoint(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    authentication_classes = [TokenAuthentication]


    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        # Check if the user is the author of the blog post
        if obj.owner!= self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        return obj



class ProductCreateEndpoint(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductByCategoryEndpoint(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]

#     def queryset(self):
#         category_id = self.kwargs.get('category_id')

#         try:
#             category = Category.objects.get(id = category_id)
#         except Category.DoesNotExist:
#             raise Http404('Category does not exist')
        
#         return Products.objects.filter(category_id2=category_id)
    

class ProductByCategoryEndpoint(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise Http404('Category does not exist')

        return Products.objects.filter(category_id=category_id)


class ProductSearchEndpoint(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes =    [IsAuthenticated]
    queryset = Products.objects.all()
    
    def get_queryset(self):
        qs = super().get_queryset()
        value = self.request.query_params.get('name')
        cat = self.request.query_params.get('category')
        if value is not None or cat is not None:
            qs= qs.filter(Q(name__icontains =value) | Q(category=cat))
        return qs 

