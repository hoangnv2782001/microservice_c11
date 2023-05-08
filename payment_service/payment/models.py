from django.db import models

# Create your models here.
from django.db import models


# This is our model for user registration.
class payment_status(models.Model):
    ### The following are the fields of our table.
    username = models.CharField(max_length=50)
    order_id = models.IntegerField(null=True)
    mode_of_payment = models.CharField(max_length=20)
    mobile = models.CharField(max_length=12)
    status = models.CharField(max_length=15)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s %s %s ' % (
        self.username, self.product_id, self.price, self.quantity, self.mode_of_payment, self.mobile, self.status)
