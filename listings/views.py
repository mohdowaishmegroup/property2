from django.shortcuts import get_object_or_404, render, redirect
from .models import Listing
from rest_framework import viewsets
from .serializers import *
import requests
from rest_framework.response import Response


class ListingView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    

def displaydata(request):
    callapi=requests.get('http://127.0.0.1:8000/listings/r/view/')
    result=callapi.json()
    data=result['results']
    return render(request,'pages/index.html',{'data':data})



