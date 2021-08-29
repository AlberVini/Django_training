from django.db import models

class Task(models.Model):

    OPTIONS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255, default='No title')
    description = models.TextField(default='No description')
    status = models.CharField(
        max_length=5,
        choices=OPTIONS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
