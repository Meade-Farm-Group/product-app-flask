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
    path('<int:product_id>/technical/', views.technical_navigation, name='technical_navigation'),
    path('<int:product_id>/technical/finished/', views.add_finished_specification, name='add_finished_specification'),
    path('<int:product_id>/technical/finished/edit', views.edit_finished_specification, name='edit_finished_specification'),
    path('<int:product_id>/technical/defect/', views.add_defect_specification, name='add_defect_specification'),
    path('<int:product_id>/technical/defect/<int:defect_spec_id>/edit', views.edit_defect_specification, name='edit_defect_specification'),
    path('<int:product_id>/technical/defect/view', views.product_defects, name='product_defects'),
    path('<int:product_id>/technical/defect/<int:defect_spec_id>/delete', views.delete_defect_specification, name='delete_defect_specification'),
]
