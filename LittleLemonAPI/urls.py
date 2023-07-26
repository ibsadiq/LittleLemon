from django.urls import path
from . import views


urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view()),
    path('menu-items/category', views.CategoryView.as_view()),
    path('groups/manager/users/', views.ManagerUsersView.as_view()),
    path('groups/manager/users/<int:pk>/', views.ManagerSingleUserView.as_view()),
    path('groups/delivery-crew/users/', views.DeliveryManagementView.as_view()),
    path('groups/delivery-crew/users/<int:pk>/', views.DeliveryManagementSingleView.as_view()),
    path('cart/menu-items/', views.CustomerCart.as_view()),
    path('orders/', views.OrdersView.as_view()),
    path('orders/<int:pk>/', views.SingleOrderView.as_view()),

]