from django.urls import path
from chat_app import views

urlpatterns = [
    path('', views.Homeview, name='Homeview'),
    path('<str:room_name>/<str:username>/', views.Roomview, name='Roomview'),
]
