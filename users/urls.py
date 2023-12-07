from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_register, name="register"),
    path('login/', user_login, name="login"),
    path('members/', member_page, name="members"),
    path('logout/', user_logout, name="logout"),
]
