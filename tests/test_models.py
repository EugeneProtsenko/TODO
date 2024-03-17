from datetime import datetime

from django.test import TestCase

from todo.models import Tag, Todo


class ModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag),
                         f"{tag.name}")

    def test_todo_str(self):
        tag = Tag.objects.create(name="test", )
        todo = Todo.objects.create(action="test",
                                   date=datetime.now(),
                                   is_done=False)
        todo.tags.set([tag])
        self.assertEqual(str(todo), todo.action)
