from django.urls import path
from .views import hotel_view, show_view, update_view, delete_view

urlpatterns = [
    path("", hotel_view, name='hotel_urls'),
    path("show/", show_view, name='show_urls'),
    path("update/<int:pk>", update_view, name="update_urls"),
    path("delete/<int:pk>", delete_view, name="delete_urls")
]
