# Generated by Django 5.0.3 on 2024-03-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_rename_tags_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
