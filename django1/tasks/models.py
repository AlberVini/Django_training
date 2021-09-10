from django.db import models
from django.contrib.auth import get_user_model

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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # on_delete after del some user, all the tasks will be delete too
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
