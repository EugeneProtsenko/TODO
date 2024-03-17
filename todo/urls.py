from django.urls import path

from todo.views import TodoListView, TagListView, TagUpdateView, TagDeleteView, TagCreateView

app_name = "todo"


urlpatterns = [
    path(
        "",
        TodoListView.as_view(),
        name="todo-list",
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),

]