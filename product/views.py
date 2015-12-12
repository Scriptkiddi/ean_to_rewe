from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import ProductSerializer
from .models import Product, Price
import watson
from .utils import get_rewe_price_for_product, gather_information, send_simple_message


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Product.objects.all()
        ean = self.request.query_params.get('ean', None)
        nan = self.request.query_params.get('nan', None)
        query = self.request.query_params.get('q', None)
        if query:
            return watson.filter(Product, query)
        if ean is not None:
            print(queryset)
            queryset = queryset.filter(eans=ean)
            if len(queryset) == 0:
                self.send_mail_to_add_product(ean)
            elif len(queryset) == 1:
                self.update_price(queryset[0])
            else:
                send_simple_message("fritz@otlinghaus.it", ["fritz@otlinghaus.it"], "Error", "rewe stuff fuckup two products for 1 ean")
        if nan is not None:
            queryset = queryset.filter(nan=nan)
        return queryset

    def send_mail_to_add_product(self, ean):
        products, prices, eans = gather_information(ean)
        if len(products) == 1:
            products[0].save()
            prices[0].save()
            eans[0].save()
        else:
            send_simple_message("fritz@otlinghaus.it", ["fritz@otlinghaus.it"], "Add Product", "Ean number where we can not auto generate something")

    def update_price(self, product):
        Price.objects.create(product=product, price=get_rewe_price_for_product(product.nan))
