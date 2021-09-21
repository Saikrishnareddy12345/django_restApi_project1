from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.App1overview,name='App1overview'),
    path('list/',views.showall1,name='list'),
    path('list1/', views.showall, name='list1'),
    path('detail/<int:pk>', views.ViewProduct, name='detail'),
    path('create/', views.CreateProduct,name='create'),
    path('update/<int:pk>', views.updateProduct,name='update'),
    path('delete/<int:pk>', views.deleteProduct, name='delete')
]