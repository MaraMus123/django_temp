from django.urls import path
from . import views

urlpatterns = [
    path('add_image/', views.Add.as_view(), name='add_image'),
    path('gallery/', views.gallery, name='gallery'),
]

