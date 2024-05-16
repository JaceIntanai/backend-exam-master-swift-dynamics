from rest_framework import viewsets
from rest_framework.response import Response
from ...models import Classroom, Teacher, Student, School
from ...serializers import ClassroomSerializer, TeacherSerializer, StudentSerializer
from ...filters import ClassroomFilter

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        data = []
        for i, class_obj in enumerate(queryset):
            classroom_info = serializer.data[i]
            school_id = classroom_info['school']
            school_name = School.objects.get(id=school_id).name
            teachers = Teacher.objects.filter(classrooms=class_obj)
            teacher_serializer = TeacherSerializer(teachers, many=True)
            students = Student.objects.filter(classroom=class_obj)
            student_serializer = StudentSerializer(students, many=True)

            classroom_info.update({
                'school_name': school_name,
                'teachers': teacher_serializer.data,
                'students': student_serializer.data,
            })
            data.append(classroom_info)

        return Response(data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = serializer.data

        school_id = data['school']
        school_name = School.objects.get(id=school_id).name
        teachers = Teacher.objects.filter(classrooms=instance)
        teacher_serializer = TeacherSerializer(teachers, many=True)
        students = Student.objects.filter(classroom=instance)
        student_serializer = StudentSerializer(students, many=True)

        data.update({
            'school_name': school_name,
            'teachers': teacher_serializer.data,
            'students': student_serializer.data,
        })

        return Response(data)