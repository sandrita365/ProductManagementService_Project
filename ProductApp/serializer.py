from rest_framework import serializers

from .models import product


class InSerializer(serializers.ModelSerializer):
    description: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True, allow_null=True)
    url_picture: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True, allow_null=True)
    location: str = serializers.CharField(max_length=250, required=False,
                                          allow_null=True, allow_blank=True)
    comments: str = serializers.CharField(max_length=250, required=False,
                                          allow_null=True, allow_blank=True)
    price_lot_flag: str = serializers.BooleanField(default=False)

    class Meta:
        model = product
        fields = ("name", "description", "quantity", "url_picture",
                  "location", "lot_flag",
                  "price_lot_flag", "alert_minimum_stock_flag",
                  "alert_expiration_date_flag", "comments", "date",
                  "last_update", "department_id",
                  "unit_measure_id")


class OutSerializerAllFields(serializers.ModelSerializer):
    _id = serializers.CharField()
    description: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True, allow_null=True)
    url_picture: str = serializers.CharField(max_length=250, required=False,
                                             allow_blank=True, allow_null=True)
    location: str = serializers.CharField(max_length=250, required=False,
                                          allow_null=True, allow_blank=True)
    price_lot_flag: str = serializers.BooleanField(required=False)
    comments: str = serializers.CharField(max_length=250, required=False,
                                          allow_null=True, allow_blank=True)
    date = serializers.DateTimeField()
    last_update = serializers.DateTimeField()

    class Meta:
        model = product
        fields = ("_id", "name", "description", "quantity", "url_picture",
                  "location", "lot_flag",
                  "price_lot_flag", "alert_minimum_stock_flag",
                  "alert_expiration_date_flag", "comments", "date",
                  "last_update", "department_id",
                  "unit_measure_id")
