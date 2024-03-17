from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Todo, Tag


class TodoListView(generic.ListView):
    model = Todo
    context_object_name = "todo_list"
    template_name = "todo/todo_list.html"
    paginate_by = 3


class TodoCreateView(generic.CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo:todo-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy("todo:todo-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def complete_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    return redirect('/')


def undo_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = False
    todo.save()
    return redirect('/')