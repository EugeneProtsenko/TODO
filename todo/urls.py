from django.urls import path

from todo.views import TodoListView, TagListView, TagUpdateView, TagDeleteView, TagCreateView, TodoCreateView, \
    TodoUpdateView, TodoDeleteView, complete_task, undo_task

app_name = "todo"


class TodUpdateView:
    pass


urlpatterns = [
    path(
        "",
        TodoListView.as_view(),
        name="todo-list",
    ),
    path(
        "create/",
        TodoCreateView.as_view(),
        name="todo-create",
    ),
    path(
        "<int:pk>/update/",
        TodoUpdateView.as_view(),
        name="todo-update",
    ),
    path(
        "<int:pk>/delete/",
        TodoDeleteView.as_view(),
        name="todo-delete",
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
    path('complete_task/<int:pk>/', complete_task, name='complete-task'),
    path('undo_task/<int:pk>/', undo_task, name='undo-task'),

]