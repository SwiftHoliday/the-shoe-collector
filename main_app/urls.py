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
    path('shoes/<int:shoe_id>/assoc_seller/<int:seller_id>/', views.assoc_seller, name='assoc_seller'),
    path('sellers/', views.SellerList.as_view(), name='sellers_index'),
    path('sellers/create/', views.SellerCreate.as_view(), name='sellers_create'),
]