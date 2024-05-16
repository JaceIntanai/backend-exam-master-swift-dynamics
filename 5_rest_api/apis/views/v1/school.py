from rest_framework import viewsets
from rest_framework.response import Response
from ...models import School, Teacher, Student, Classroom
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        data = []
        for i, school_obj in enumerate(queryset):
            school_info = serializer.data[i]
            classrooms_count = school_obj.classrooms.count()
            teachers_count = Teacher.objects.filter(classrooms__school=school_obj).distinct().count()
            students_count = Student.objects.filter(classroom__school=school_obj).count()
            school_info.update({
                'classrooms_count': classrooms_count,
                'teachers_count': teachers_count,
                'students_count': students_count,
            })
            data.append(school_info)

        return Response(data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        classrooms_count = Classroom.objects.filter(school=instance).count()
        teachers_count = Teacher.objects.filter(classrooms__school=instance).distinct().count()
        students_count = Student.objects.filter(classroom__school=instance).count()

        data = serializer.data
        data.update({
            'classrooms_count': classrooms_count,
            'teachers_count': teachers_count,
            'students_count': students_count,
        })

        return Response(data)