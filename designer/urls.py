from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='designer-home'),
    path('horn/', views.horn, name='designer-horn'),
    path('dipole/', views.dipole, name='designer-dipole'),
]
