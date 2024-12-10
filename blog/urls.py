from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal' ),
    path('autores', views.autores, name='autores' ),
    path('<int:pk>', views.detalle, name='detalle_post' ),
    path('new', views.post_new, name='post_new' ),
    path('ji', views.ji, name='ji' ),
    path('post/new', views.post_new, name='post_new' ),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit' ),
]
