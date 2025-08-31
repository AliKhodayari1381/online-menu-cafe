from django.urls import path
from .views import review_list, add_review



urlpatterns = [
    path('', review_list, name='reviews'),
    path('add/', add_review, name='add_review'),
]

