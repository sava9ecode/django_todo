# Generated by Django 4.2.3 on 2023-07-17 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0002_alter_category_options"),
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="category.category",
            ),
            preserve_default=False,
        ),
    ]