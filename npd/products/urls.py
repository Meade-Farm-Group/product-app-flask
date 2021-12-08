from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='product_home'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('create/', views.create_product, name='create_product'),
    path('<int:product_id>/commercial/', views.add_commercial_details, name='add_commercial_details'),
    path('<int:product_id>/commercial/edit', views.edit_commercial_details, name='edit_commercial_details'),
    path('<int:product_id>/packaging/', views.add_packaging_details, name="add_packaging_details"),
    path('<int:product_id>/packaging/edit', views.edit_packaging_details, name='edit_packaging_details'),
    path('<int:product_id>/operations/', views.add_operations_details, name='add_operations_details'),
    path('<int:product_id>/operations/edit', views.edit_operations_details, name='edit_operations_details'),
    path('<int:product_id>/edit/', views.edit_navigation, name='edit_navigation'),
]
