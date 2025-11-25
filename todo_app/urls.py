from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    toggle_status,
)


app_name = "todo"


urlpatterns = [
    path("", index, name="index"),
     # Tasks
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/toggle/",
        toggle_status,
        name="task-toggle"),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    # Tags
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"),
]