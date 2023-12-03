from django.urls import path

from playground import views


urlpatterns = [
    path('playground/hello', views.say_hello)
]
