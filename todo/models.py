from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Todo(models.Model):
    action = models.CharField(max_length=255)
    date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name="todos")
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.action
