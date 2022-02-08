from django.urls import path
from .views import *





urlpatterns = [
    path('food/create/', FoodCreateView.as_view()),
    path('food/update/', FoodUpdateView.as_view()),
    path('food/list/', FoodListView.as_view()),
    path('food/delete/', FoodDeleteView.as_view()),
    path('apartment/create/', ApartmentCreateView.as_view()),
    path('apartment/update/', ApartmentUpdateView.as_view()),
    path('apartment/list/', ApartmentListView.as_view()),
    path('apartment/delete/', ApartmentDeleteView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/list/', OrderListView.as_view()),
    path('order/update/', OrderUpdateView.as_view()),
    path('order/delete/', OrderDeleteView.as_view()),
]
    # path('order_detail/create/', Order_detailCreateView.as_view()),
    # path('order_detail/list/', Order_detailListView),
    # path('order_detail/update/', Order_detailUpdateView.as_view()),
    # path('order_detail/delete/', Order_detailDeleteView.as_view()),