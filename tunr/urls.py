from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cities/', views.CityList.as_view(), name='city_list'),
    path('cities/<int:pk>', views.CityDetail.as_view(), name='city_detail'),
    path('attractions/', views.AttractionList.as_view(), name="attraction_list"),
    path('attractions/<int:pk>', views.AttractionDetail.as_view(), name="attraction_detail"),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail')
]
