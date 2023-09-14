from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.create_person),
    path('api/<int:user_id>/', views.get_update_delete_person),
]
