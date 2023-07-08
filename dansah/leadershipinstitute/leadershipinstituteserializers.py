from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Course, Category, LeadershipInstitute


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class CourseSerializer(serializers.ModelSerializer):
    level = CategoryNameSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class LeadershipInstituteSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = LeadershipInstitute
        fields = "__all__"
