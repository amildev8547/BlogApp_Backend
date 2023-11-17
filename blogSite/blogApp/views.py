import json
from django.http import  HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import*


@csrf_exempt 
def viewAll(request):
    if request.method=="POST":
        studentList=BlogModel.objects.all()
        serializers = BlogSerializer(studentList, many=True)
        return HttpResponse(json.dumps(serializers.data))
    
