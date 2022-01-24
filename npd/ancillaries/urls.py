from django.urls import path
from . import views

urlpatterns = [
    path('defects/', views.view_defects, name='view_defects'),
    path('defects/add', views.add_defect, name='add_defect'),
    path('defects/<int:defect_id>/delete', views.delete_defect, name='delete_defect'),
]
