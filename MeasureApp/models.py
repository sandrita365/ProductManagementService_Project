from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from djongo import models


# Create your models here.
class UnitMeasure(models.Model):
    """
    This class is a model; it defines all the database's features and fields.
    """
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def formatted_date(self):
        return self.date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    def formatted_last_update_date(self):
        return self.last_update_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


@receiver(pre_save, sender=UnitMeasure)
def set_date_on_create(sender, instance, **kwargs):
    # Set date only on creation
    if not instance.pk:
        instance.date = timezone.now()
    else:
        instance.last_update_date = timezone.now()
