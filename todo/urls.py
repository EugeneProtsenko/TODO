from django.urls import path

from todo.views import TodoListView

app_name = "todo"


urlpatterns = [
    path(
        "todos/",
        TodoListView.as_view(),
        name="todo-list",
    ),
]