from django.db import models

class Teacher(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    email_id=models.EmailField(max_length=200)

    def __str__(self):
        return self.username + ' - ' + self.email_id


class Student(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    reg_no=(models.IntegerField())

    def __str__(self):
        return self.username




