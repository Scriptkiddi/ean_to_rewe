from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import ProductSerializer
from .models import Product
import watson


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
            queryset = queryset.filter(ean=ean)
        if nan is not None:
            queryset = queryset.filter(nan=nan)
        return queryset