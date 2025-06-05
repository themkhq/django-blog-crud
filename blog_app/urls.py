from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog_list"),
    path("create/", views.create, name="blog_create"),
    path("update/<int:id>/", views.update, name="blog_update"),
    path("delete/<int:id>/", views.delete, name="blog_delete"),
]