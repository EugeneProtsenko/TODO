from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Todo, Tag


class TodoListView(generic.ListView):
    model = Todo
    context_object_name = "todo_list"
    template_name = "todo/todo_list.html"
    # paginate_by = 5


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    # paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("taxi:manufacturer-list")