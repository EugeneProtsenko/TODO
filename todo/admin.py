from django.contrib import admin

from todo.models import Tag, Todo

admin.site.register(Tag)
admin.site.register(Todo)
