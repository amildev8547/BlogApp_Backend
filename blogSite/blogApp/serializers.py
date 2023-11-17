from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.BlogSerializer):
    class Meta:
        model=BlogModel
        fields=['blog_id','title','message']