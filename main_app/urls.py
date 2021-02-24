from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='shoes_index'),
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='shoes_detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('shoes/<int:shoe_id>/assoc_seller/<int:seller_id>/', views.assoc_seller, name='assoc_seller'),
    path('shoes/<int:shoe_id>/add_photo/', views.add_photo, name='add_photo'),
    path('sellers/', views.SellerList.as_view(), name='sellers_index'),
    path('sellers/create/', views.SellerCreate.as_view(), name='sellers_create'),
    path('sellers/<int:pk>/', views.SellerDetail.as_view(), name='sellers_detail'),
    path('sellers/<int:pk>/update/', views.SellerUpdate.as_view(), name='sellers_update'),
    path('sellers/<int:pk>/delete/', views.SellerDelete.as_view(), name='sellers_delete'),
]