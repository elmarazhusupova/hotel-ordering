from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class FoodCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSeriaLizers
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    # filter_fields = ['title']
    # search_fields = ['title']
    # ordering_fields = ['title']



class FoodUpdateView(generics.UpdateAPIView):
    serializer_class = FoodSeriaLizers
    queryset = Food.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    # filter_fields = ['title']
    # search_fields = ['title']
    # ordering_fields = ['title']


class FoodListView(generics.ListAPIView):
    serializer_class = FoodSeriaLizers
    queryset = Food.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    # filter_fields = ['title']
    # search_fields = ['title']
    # ordering_fields = ['title']



class FoodDeleteView(generics.DestroyAPIView):
    serializer_class = FoodSeriaLizers
    queryset = Food.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    # filter_fields = ['title']
    # search_fields = ['title']
    # ordering_fields = ['title']


class ApartmentCreateView(generics.CreateAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()


class ApartmentListView(generics.ListAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()


class ApartmentUpdateView(generics.UpdateAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()


class ApartmentDeleteView(generics.DestroyAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()



class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSeriaLizers
    queryset = Order.objects.all()


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSeriaLizers
    queryset = Order.objects.all()


class OrderUpdateView(generics.UpdateAPIView):
    serializer_class = OrderSeriaLizers
    queryset = Order.objects.all()


class OrderDeleteView(generics.ListAPIView):
    serializer_class = OrderSeriaLizers
    queryset = Order.objects.all()
#
#
# class Order_detailCreateView(generics.CreateAPIView):
#     serializer_class = Order_detailSeriaLizers
#     queryset = Order_detailSeriaLizers.objects.all()
#
#
#
# class Order_detailListView(generics.ListAPIView):
#     serializer_class = Order_detailSeriaLizers
#     queryset = Order_detailSeriaLizers.objects.all()
#
#
#
# class Order_detailUpdateView(generics.UpdateAPIView):
#     serializer_class = Order_detailSeriaLizers
#     queryset = Order_detailSeriaLizers.objects.all()
#
#
#
# class Order_detailDeleteView(generics.DestroyAPIView):
#     serializer_class = Order_detailSeriaLizers
#     queryset = Order_detailSeriaLizers.objects.all()