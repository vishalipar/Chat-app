from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepageview),
    path('room/', views.roomview, name="room"),
]
