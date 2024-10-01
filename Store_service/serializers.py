from rest_framework import serializers
from .models import Store, Category, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields= '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields= '__all__'
        model= Category


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields= '__all__'
        model= Store