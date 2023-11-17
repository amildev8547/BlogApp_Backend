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
    
@csrf_exempt
def addBlog(request):
    if request.method=="POST":
        blogData=json.loads(request.body)
        print(blogData)
        serializer_add=BlogSerializer(data=blogData)
        if serializer_add.is_vaild():
            serializer_add.save()
        return HttpResponse(json.dumps({"status":"Added Successfully"}))
    else:
        return HttpResponse(json.dumps({"status":"Failed to Add"}))