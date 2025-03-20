from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title