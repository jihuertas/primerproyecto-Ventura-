from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='posts' ),
    path('post/<int:pk>', views.post_detalle, name='post_detalle' ),
    path('post/new', views.post_new, name='post_new' ),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit' ),

    path('autores', views.autores, name='autores' ),
    path('autor/<int:pk>', views.autor_detalle, name='autor_detalle' ),
    path('autor/new', views.autor_new, name='autor_new' ),
    path('autor/<int:pk>/del', views.autor_del, name='autor_del' ),
    path('autor/<int:pk>/edit', views.autor_edit, name='autor_edit'),


]
