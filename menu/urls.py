from django.urls import path
from .views import menu_view, category_items, item_detail

urlpatterns = [
    path('', menu_view, name='menu'),
    #path('<int:category_id>/', category_items, name='category_items'),
    path('category/<int:category_id>/', category_items, name='category_items'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
]
