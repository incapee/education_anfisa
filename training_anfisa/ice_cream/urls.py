from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:pk>/', views.item, name='item'),
]
