from django.shortcuts import render
from django.views import generic

from todo.models import Todo


class TodoListView(generic.ListView):
    model = Todo
    context_object_name = "todo_list"
    template_name = "todo/todo_list.html"
    # paginate_by = 5
