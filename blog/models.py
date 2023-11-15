from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    dob = models.DateField()
    country = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}_{self.name}"




