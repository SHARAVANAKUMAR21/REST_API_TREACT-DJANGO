from django.urls import path
from . import views

urlpatterns = [
    path('api/dreams/view/', views.view_dream, name='view_dream'),
    path('api/dreams/add/', views.add_dream, name='add_dream'),
    path('api/dreams/<int:dream_id>/', views.delete_dream, name='delete_dream'),
    path('api/dreams/update/<int:dream_id>/', views.update_dream, name='update_dream'), 
]
