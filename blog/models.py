from django.db import models

from .choice import AuthorStatus
from django.db.models import QuerySet

class AuthorQuerySet(QuerySet):
    def active(self):
        return self.filter(status=AuthorStatus.ACTIVE)


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    objects = AuthorQuerySet.as_manager()
    status = models.CharField(choices=AuthorStatus,
                              validators=[AuthorStatus.validator],
                              null=True,
                              max_length=64)
    address = models.TextField()
    email = models.EmailField()
    dob = models.DateField()
    country = models.CharField(max_length=255)



    def __str__(self):
        return f"{self.id}_{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to="resume")

