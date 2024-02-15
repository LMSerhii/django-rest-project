from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pizza
from .serializers import PizzaSerializer


# Create your views here.

# class PizzaAPIView(generics.ListAPIView):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer


class PizzaAPIView(APIView):
    def get(self, request):
        lst = Pizza.objects.all().values()
        return Response({'pizzas': list(lst)})

    def post(self, request):
        post_new = Pizza.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({"post": model_to_dict(post_new)})
