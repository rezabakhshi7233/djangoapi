from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        managed = True
        fields = ('id', 'url', 'name', 'language', 'price')
