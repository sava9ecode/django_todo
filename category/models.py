from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def number_of_tasks(self):
        return self.tasks.count()
