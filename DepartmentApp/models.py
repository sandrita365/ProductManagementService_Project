from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from djongo import models


# Create your models here.
class Department(models.Model):
    """
    Represents a department in the database. This model defines the
    structure of the Department table in the database, including its fields,
    data types, etc.

    Fields:
    - _id: The unique identifier of the department(ObjectIdField)
    - name: The name of the department (CharField).
    - description: A description of the department (TextField).
    """

    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def formatted_date(self):
        return self.date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    def formatted_last_update_date(self):
        return self.last_update_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


@receiver(pre_save, sender=Department)
def set_date_on_create(sender, instance, **kwargs):
    # Set date only on creation
    if not instance.pk:
        instance.date = timezone.now()
    else:
        instance.last_update_date = timezone.now()
