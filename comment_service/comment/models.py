from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models


# This is our model for user registration.
class Comment_Detail(models.Model):
    # The following are the fields of our table.
    product_id = models.CharField(max_length=10)
    comment = models.TextField()
    is_active = models.IntegerField()
    user_id = models.IntegerField()

    # # It will help to print the values.
    # def __str__(self):
    #     return '%s %s %s %s %s' % (self.product_id, self.product_category,
    #                                self.product_name, self.availability, self.price)
