from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    course = models.CharField(max_length=200)
    reported = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name