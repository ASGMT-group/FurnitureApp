from django.urls import path
from .import views
urlpatterns = [
   path("", views.home, name='home'),
   # path("filter", views.filter, name='filter'),
   path("coll", views.collections, name='collection'),
   path('rate/<int:item_id>/', views.rate_item, name='rate_item'),
   path('detail/<int:item_id>/', views.item_detail, name='detail'),
   path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
   path('mycart/', views.display_cart, name='cart'),
   path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]