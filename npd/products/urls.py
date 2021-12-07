from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='product_home'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('create/', views.create_product, name='create_product'),
    path('<int:product_id>/commercial/', views.add_commercial_details, name='add_commercial_details'),
    path('<int:product_id>/commercial/edit', views.edit_commercial_details, name='edit_commercial_details'),
]