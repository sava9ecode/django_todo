from django.urls import path

from . import views


urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("edit_task/<int:pk>/", views.edit_task, name="edit_task"),
    path("mark_completed/<int:pk>/", views.mark_completed, name="mark_completed"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
    path("search/", views.search, name="search"),
]
