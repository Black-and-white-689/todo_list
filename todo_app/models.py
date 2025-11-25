from django.db import models


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = "Urgent"
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"

    name = models.CharField(
        max_length=255,
        verbose_name="Task_name"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Task_description"
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
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        verbose_name="Priority"
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name="tasks",
        verbose_name="tags",
    )

    def __str__(self):
        return f"{self.name} ({'Is done' if self.is_done else 'In progress'})"


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Tag_name"
    )

    def __str__(self):
        return self.name
