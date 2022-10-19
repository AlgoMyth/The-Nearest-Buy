from django.http import HttpResponse
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.

def HomePage(request):
    return HttpResponse('This is the home page')
  
class ReactView(APIView):
    
    serializer_class = ShopSerializer
  
    def get(self, request):
        shops = [ {"name": i.name,"latitude": i.latitude,"longitude":i.longitude,"item_desc":i.item_desc,"cost":i.cost} for i in Shop.objects.all()]
        return Response(shops)
  
    def post(self, request):
  
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)