from django.db import models


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Task name"
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Task content"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    deadline = models.DateField(
        verbose_name="Deadline",
        null=True,
        blank=True
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Done"
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name="tasks"
    )

    def __str__(self):
        return f"{self.name} ({'Is done' if self.is_done else 'In progress'})"


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Tag name"
    )

    def __str__(self):
        return self.name
