from rest_framework import serializers

from .models import Course, LeadershipInstitute


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LeadershipInstituteSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = LeadershipInstitute
        fields = "__all__"
