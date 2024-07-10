from rest_framework import serializers

from .models import Department


class InDepartmentSerializer(serializers.ModelSerializer):
    name: str = serializers.CharField(max_length=200, required=False)
    description: str = serializers.CharField(
        max_length=200, required=False, allow_blank=True, allow_null=True
    )

    class Meta:
        model = Department
        fields = ("name", "description")


class OutSerializer(serializers.ModelSerializer):
    """
    This class is a Department serializer; it defines the features for each
    output field,
     furthermore, the _id field is converted to a string.
    """
    _id = serializers.CharField()
    name = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=250, required=False,
                                        allow_blank=True, allow_null=True)
    date = serializers.DateTimeField()
    last_update_date = serializers.DateTimeField()

    class Meta:
        model = Department
        fields = ("_id", "name", "description", "date", "last_update_date")

    def get__id(self, obj):
        return str(obj._id)
#
