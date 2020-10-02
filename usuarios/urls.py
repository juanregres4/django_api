from django.urls import path
from usuarios import views

urlpatterns = [
    path('users/', views.HelloApiView.as_view()),
    path('usuarios/', views.UsersApiView.as_view()),
    path('usuarios/<int:pk>', views.UserManageApi.as_view()),
    path('productos/', views.ProductosList.as_view()),
    path('productos/<int:pk>', views.ProductosManage.as_view()),
    path('carrito/', views.CarritoListAPI.as_view()),
    path('carrito/<int:pk>', views.CarritoManageAPI.as_view()),
    path('orden/', views.OrdenListAPI.as_view()),
    path('orden/<int:pk>', views.OrdenManageAPI.as_view()),
]