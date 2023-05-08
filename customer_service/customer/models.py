from django.db import models

# Create your models here.
# from __future__ import unicode_literals
from django.db import models
from tensorflow.distribute.experimental.rpc.kernels.gen_rpc_ops import case


# This is our model for user registration.
class Accout(models.Model):
    ### The following are the fields of our table.
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=50)


class Address(models.Model):
    numhome = models.IntegerField()

    street = models.CharField(max_length=200)

    district = models.CharField(max_length=220)

    city = models.CharField(max_length=200)

    country = models.CharField(max_length=200)

class FullName(models.Model):
    firstname = models.CharField(max_length=200)

    lastname = models.CharField(max_length=200)

class Customer(models.Model):
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    fullname = models.ForeignKey(FullName,on_delete=True)
    address = models.ForeignKey(Address,on_delete=True)
    accout = models.ForeignKey(Accout,on_delete=True)
