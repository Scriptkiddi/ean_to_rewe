__author__ = 'fritz'
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Product, Ean, Price

class PriceSerializer(ModelSerializer):

    class Meta:
        model = Price
        fields = ('price',)


class EanSerializer(ModelSerializer):

    class Meta:
        model = Ean
        fields = ('ean',)


class ProductSerializer(ModelSerializer):
    eans = EanSerializer(many=True)
    prices = PriceSerializer(many=True)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'nan', 'eans', 'prices')

    def create(self, validated_data):
        eans_data = validated_data.pop('eans')
        product = Product.objects.create(**validated_data)
        for ean_data in eans_data:
            Eans.objects.create(product=product, **ean_data)
        prices_data = validated_data.pop('prices')
        for price in prices_data:
            Eans.objects.create(product=product, **price)
        return product