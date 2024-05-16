from django_filters import FilterSet, filters, CharFilter, NumberFilter


# code here
from .models import School, Classroom, Teacher, Student

class SchoolFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(FilterSet):
    school__name = CharFilter(field_name='school__name', lookup_expr='icontains')

    class Meta:
        model = Classroom
        fields = ['school__name']

class TeacherFilter(FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    gender = CharFilter(field_name='gender', lookup_expr='exact')
    classrooms_year = NumberFilter(field_name='classrooms__year', lookup_expr='exact')
    classrooms_section = NumberFilter(field_name='classrooms_section', lookup_expr='exact')
    classrooms_school_name = CharFilter(field_name='classrooms__school__name', lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender', 'classrooms_year', 'classrooms_section', 'classrooms_school_name']

class StudentFilter(FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    gender = CharFilter(field_name='gender', lookup_expr='exact')
    classroom__year = CharFilter(field_name='classroom__year', lookup_expr='exact')
    classroom__section = CharFilter(field_name='classroom__section', lookup_expr='exact')
    classroom__school__name = CharFilter(field_name='classroom__school__name', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'classroom__year', 'classroom__section', 'classroom__school__name']