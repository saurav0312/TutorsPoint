from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.ImageField()

    def __str__(self):
        return self.name