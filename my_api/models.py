from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    psw_hash = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    token = models.CharField(max_length=150, null=True)
    ttl = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.login

class FibDB(models.Model):
    value = models.IntegerField()

    def __int__(self):
        return self.value

# Create your models here.
