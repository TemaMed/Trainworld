from django.urls import path
from . import views

urlpatterns = [
    path('', views.head, name='head'),
    path('search1', views.search1, name='search1'),
    path('info_list', views.info_list, name='info_list'),
    path('get_port', views.get_port, name='get_port'),
    path('auth', views.auth, name='auth'),
    path('admin', views.admin, name='admin'),
    path('add_port', views.add_port, name='add_port'),
    path('add_train', views.add_train, name='add_train'),
    path('add_manager', views.add_manager, name='add_manager'),
    path('search', views.search, name='search'),
    path('delete', views.delete, name='delete')
    # path('contact/', views.contact, name='contact')
]
