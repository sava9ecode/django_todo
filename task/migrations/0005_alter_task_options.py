# Generated by Django 4.2.3 on 2023-10-09 22:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0004_task_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-created_at"]},
        ),
    ]
