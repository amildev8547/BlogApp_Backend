from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields=['blog_id','title','message']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterModel
        fields=['name','image','email','password']        