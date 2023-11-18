import json
from django.http import  HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import*
from django.db.models import Q


@csrf_exempt 
def viewAllPost(request):
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
        if serializer_add.is_valid():
            serializer_add.save()
        return HttpResponse(json.dumps({"status":"Added Successfully"}))
    else:
        return HttpResponse(json.dumps({"status":"Failed to Add"}))
    
@csrf_exempt
def register(request):
    if request.method=="POST":
        registerData=json.loads(request.body)
        print(registerData)
        serializer_reg=RegisterSerializer(data=registerData)
        if serializer_reg.is_valid():
            serializer_reg.save()
        return HttpResponse(json.dumps({"status":"Registered Successfully"}))
    else:
        return HttpResponse(json.dumps({"status":"Failed to Register"}))    

@csrf_exempt
def viewMyPost(request):
    if request.method == "POST":
        search_data = json.loads(request.body)
        getId = search_data["blog_id"]
        data = list(BlogModel.objects.filter(Q(blog_id__icontains=getId)).values())
        return HttpResponse(json.dumps(data))

@csrf_exempt    
def login(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"Logged In.."}))    