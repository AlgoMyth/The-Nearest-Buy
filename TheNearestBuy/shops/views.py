from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.
  
class ReactView(APIView):
    
    serializer_class = ShopSerializer
  
    def get(self, request):
        shops = [ {"name": i.name,"address": i.address,"city":i.city} for i in Shop.objects.all()]
        return Response(shops)
  
    def post(self, request):
  
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)