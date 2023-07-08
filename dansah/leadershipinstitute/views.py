from rest_framework import status, generics
from rest_framework.response import Response

from .leadershipinstituteserializers import (
    CategorySerializer,
    CourseSerializer,
    LeadershipInstituteSerializer,
)
from .models import Course, Category, LeadershipInstitute


class CoursesView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request):
        result = Course.objects.all()
        if not result:
            return Response(
                {"status": "Leadership institute courses not available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})


class CourseDetailView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        course = self.get_course(pk=pk)
        if course is None:
            return Response(
                {"status": "fail", "message": f"Course with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(course)
        return Response({"status": "success", "result": serializer.data})


class CoursesByCategoryView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_course_by_category(self, level):
        try:
            return Course.objects.filter(level__name__contains=level)
        except:
            return None

    def get(self, request):
        level = request.query_params.get("level", None)
        print(level)
        courses = self.get_course_by_category(level)
        print(courses)
        if courses is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Error retrieving courses with level: {level}",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(courses, many=True)
        return Response({"status": "success", "result": serializer.data})


class CategoryView(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        result = Category.objects.all()
        if not result:
            return Response(
                {"status": "Leadership institute categories not available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})


class LeadershipInstituteView(generics.GenericAPIView):
    serializer_class = LeadershipInstituteSerializer
    queryset = LeadershipInstitute.objects.all()

    def get(self, request):
        result = LeadershipInstitute.objects.all()
        if not result:
            return Response(
                {"status": "Leadership institute not available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})
