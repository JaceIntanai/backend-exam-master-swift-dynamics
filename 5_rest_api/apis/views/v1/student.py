from rest_framework import viewsets, filters
from rest_framework.response import Response
from ...models import Student, School
from ...serializers import StudentSerializer, ClassroomSerializer
from ...filters import StudentFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        data = []
        for i, student_obj in enumerate(queryset):
            student_info = serializer.data[i]
            classroom = student_obj.classroom
            classroom_serializer = ClassroomSerializer(classroom)

            student_info['classroom'] = classroom_serializer.data
            school_id = student_info['classroom']['school']
            school_name = School.objects.get(id=school_id).name
            student_info['classroom']['school_name'] = school_name
            data.append(student_info)

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = serializer.data

        classroom = instance.classroom
        classroom_serializer = ClassroomSerializer(classroom)

        data['classrooms'] = classroom_serializer.data
        school_id = data['classroom']['school']
        school_name = School.objects.get(id=school_id).name
        data['classroom']['school_name'] = school_name

        return Response(data)