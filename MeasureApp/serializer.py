from rest_framework import serializers

from .models import UnitMeasure


class InUnitMeasureSerializer(serializers.ModelSerializer):
    """
    This class is a UnitMeasure serializer;
    it defines the features for each input field.
    """
    name: str = serializers.CharField(max_length=100, required=True,
                                      allow_blank=False)
    abbreviation: str = serializers.CharField(max_length=50, required=True,
                                              allow_blank=False)
    description: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True, allow_null=True)

    class Meta:
        model = UnitMeasure
        fields = ("name", "abbreviation", "description")


class OutUnitMeasureSerializer(serializers.ModelSerializer):
    """
    This class is a UnitMeasure serializer;
    it defines the features for each output field.
    """
    name: str = serializers.CharField(max_length=100, required=True)
    abbreviation: str = serializers.CharField(max_length=50, required=True)
    description: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True)

    class Meta:
        model = UnitMeasure
        fields = ("name", "abbreviation", "description")


class OutInitMeasureWithIdSerializer(OutUnitMeasureSerializer):
    """
    This class is a UnitMeasure serializer;
    it defines the features for each output field,
     furthermore, the _id field is converted to a string.
    """
    _id = serializers.CharField()
    name: str = serializers.CharField(max_length=100, required=True)
    abbreviation: str = serializers.CharField(max_length=50, required=True)
    description: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True, allow_null=True)
    date = serializers.DateTimeField()
    last_update_date = serializers.DateTimeField()

    class Meta:
        model = UnitMeasure
        fields = ("_id", "name", "abbreviation", "description", "date",
                  "last_update_date")
