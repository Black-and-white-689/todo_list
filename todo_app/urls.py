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
)


app_name = "todo_app"


urlpatterns = [
    path("", index, name="index"),
    #  Tasks
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
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
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
]