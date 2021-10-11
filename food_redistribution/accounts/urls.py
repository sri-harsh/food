from django.urls import path
from . import views


urlpatterns = [
	path('restaurant/', views.register_restaurant, name='restaurant-register'),
	path('foodredis/', views.register_food_redistributor, name='foodredis-register'),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
]