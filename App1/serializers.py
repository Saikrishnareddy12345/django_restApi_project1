from rest_framework import serializers
from .models import Product,Product1


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = '__all__'
