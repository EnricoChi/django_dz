from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.all_goods, name='all-products'),
    path('<pk>/', views.view_prduct, name='view-product')
]
