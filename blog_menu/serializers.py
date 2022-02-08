from rest_framework import serializers
from .models import *

class FoodSeriaLizers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class OrderSeriaLizers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class Order_detailSeriaLizers(serializers.ModelSerializer):
    class Meta:
        model = Order_detail
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


