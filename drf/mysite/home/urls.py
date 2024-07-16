from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.redirect_to_food, name='redirect_to_food'),
]

