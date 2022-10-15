from django.urls import path
from .views import BikesView, BikeView, OrderView


urlpatterns = [
    path('bikes/', BikesView.as_view()),
    path('bikes/<int:pk>/', BikeView.as_view(), name='bike_detail'),
    path('order/<int:pk>/', OrderView.as_view(), name='order_detail')
]


