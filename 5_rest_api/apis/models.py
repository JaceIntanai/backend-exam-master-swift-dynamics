from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    name_abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ( {self.name_abbreviation} )"

class Classroom(models.Model):
    year = models.IntegerField()
    section = models.CharField(max_length=1)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year}/{self.section}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
