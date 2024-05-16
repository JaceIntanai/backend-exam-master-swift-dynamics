from rest_framework import viewsets, filters
from rest_framework.response import Response
from ...models import Teacher, School
from ...serializers import TeacherSerializer, ClassroomSerializer
from ...filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        data = []
        for i, teacher_obj in enumerate(queryset):
            teachers_info = serializer.data[i]
            classrooms = teacher_obj.classrooms.all()
            classroom_serializer = ClassroomSerializer(classrooms, many=True)

            teachers_info['classrooms'] = classroom_serializer.data
            for teacher_obj_data in teachers_info['classrooms']:
                school_id = teacher_obj_data['school']
                school_name = School.objects.get(id=school_id).name
                teacher_obj_data['school_name'] = school_name
            data.append(teachers_info)

        return Response(data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = serializer.data

        classrooms = instance.classrooms.all()
        classroom_serializer = ClassroomSerializer(classrooms, many=True)

        data['classrooms'] = classroom_serializer.data
        for teacher_obj_data in data['classrooms']:
                school_id = teacher_obj_data['school']
                school_name = School.objects.get(id=school_id).name
                teacher_obj_data['school_name'] = school_name

        return Response(data)