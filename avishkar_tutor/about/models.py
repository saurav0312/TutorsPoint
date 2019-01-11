from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.FileField(upload_to='files')

    def __str__(self):
        return self.name


#class student(models.Model):
 #   username = models.CharField(max_length=100)
  #  password = models.CharField(max_length=20)
   # reg_no=models.IntegerField(default=0)
    #email_id = models.EmailField(max_length=200)

    #def __str__(self):
     #   return self.username + ' - ' + self.reg_no








