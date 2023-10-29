from django.urls import path
from . import views

urlpatterns = [

path('login/', views.sign_in, name="login_view"),
path('logout/', views.logout_view, name="logout"),
path('register/', views.register_view, name='register')
]