from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from djongo import models


# Create your models here.
class product(models.Model):
    """
        Represents a product in the database. This model defines the
        structure of the product table in the database, including its fields,
        data types, etc.
    """
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    quantity = models.IntegerField(default=0)
    url_picture = models.TextField(max_length=250)
    location = models.TextField(max_length=250)
    lot_flag = models.BooleanField()
    price_lot_flag = models.BooleanField(default=False)
    alert_minimum_stock_flag = models.BooleanField()
    alert_expiration_date_flag = models.BooleanField()
    comments = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    department_id = models.TextField(max_length=50)
    unit_measure_id = models.TextField(max_length=50)

    def formatted_date(self):
        return self.date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    def formatted_last_update(self):
        return self.last_update.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


@receiver(pre_save, sender=product)
def set_date_on_create(sender, instance, **kwargs):
    # Set date only on creation
    if not instance.pk:
        instance.date = timezone.now()
    else:
        instance.last_update = timezone.now()
