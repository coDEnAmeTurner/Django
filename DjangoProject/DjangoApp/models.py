from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    image = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.TextField(max_length=50, null=False)

    def __str__(self):
        return self.subject


class User(AbstractUser):
    pass




