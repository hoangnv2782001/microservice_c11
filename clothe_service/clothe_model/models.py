from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models


# This is our model for user registration.
class Clothes(models.Model):
    # The following are the fields of our table.
    clothe_id = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    size = models.IntegerField()
    color = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    #
    # # It will help to print the values.
    # def __str__(self):
    #     return '%s %s %s %s %s' % (self.product_id, self.product_category,
    #                                self.product_name, self.availability, self.price)
