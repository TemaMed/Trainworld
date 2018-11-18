from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_list, name='info_list'),
    path('get_port', views.get_port, name='get_port'),
    path('admin/', views.admin, name='admin'),
    path('admin/auth', views.auth, name='auth'),
    path('admin/add_port', views.add_port, name='add_port'),
    #path('contact/', views.contact, name='contact')
]
