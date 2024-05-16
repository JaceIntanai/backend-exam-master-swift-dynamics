# Backend-Exam-Master-Swift-Dynamics

## Question 1 find tailing zero
### Run
```bash
cd 1_find_tailing_zero/
python main.py
```
### Explain
> Find tailing zeroes of number factorial. The method used to calculate the numbers using the factorial function, then find the number of factorial numbers obtained, and then use the rstrip function to remove the last 0's. Then take the number of factorial numbers at the beginning and subtract the number of factorial numbers after subtracting 0 to get the number of last 0 numbers.

## Question 2 index of max
### Run
```bash
cd 2_index_of_max/
python main.py
```
### Explain
> The method is to find the maximum number in the list by max function and then find an index of the maximum number by index function in the list.

## Question 3 number to thai
### Run
```bash
cd 3_number_to_thai/
python main.py
```
### Explain
> The method is to check digits from back to the front and check the position and digit_str to predict numerals and units in thai numbers have 3 problems are _1, 1_, 2_ in these cases I check and turn to fig thai number

## Question 4 number to roman
### Run
```bash
cd 4_number_to_roman/
python main.py
```
### Explain
> The method is to fix roman numerals and number units to keep the character and use division as a measure of which number units to use in the calculation by selecting the number unit from largest to lowest. After dividing, take the obtained values ​​to determine how many of these characters will be used, going until they are complete. The numbers that can be achieved are 1-3999 because from 4000 onwards special roman numerals characters will be used.

## Question 5 rest api
### Run
```bash
cd 5_rest_api/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
API url : http://localhost:8000/api/v1/
```
### Explain
> API by Django rest framework for Schools, Classroom, Teacher and Student with serializer and filter by django_filter
```
School
 - GET: http://localhost:8000/api/v1/schools/?name=...
 -- get schools detail list by name filter
 - GET: http://localhost:8000/api/v1/schools/<id>/
 -- get school detail by school id
 - POST: http://localhost:8000/api/v1/schools/
 -- create new school by detail in body json
 -- example : 
    {
        "name": "กาญจนานุเคราะห์",
        "name_abbreviation": "ก.น.",
        "address": "กาญจนบุรี"
    }
 - PUT: http://localhost:8000/api/v1/schools/<id>/
 -- update or replace an existing resource identified by   school id
 - DELETE: http://localhost:8000/api/v1/schools/<id>/
 -- delete school by id
```
```
Classroom
 - GET: http://localhost:8000/api/v1/classrooms/?school__name=...
 -- get classrooms detail list by school__name or school(id) filter
 - GET: http://localhost:8000/api/v1/classrooms/<id>/
 -- get classroom detail by classroom id
 - POST: http://localhost:8000/api/v1/classrooms/
 -- create new classroom by detail in body json
 -- example : 
    {
        "year": 4,
        "section": 1,
        "school": 1
    }
 - PUT: http://localhost:8000/api/v1/classrooms/<id>/
 -- update or replace an existing resource identified by   classroom id
 - DELETE: http://localhost:8000/api/v1/classrooms/<id>/
 -- delete classroom by id
```
```
Teacher
 - GET: http://localhost:8000/api/v1/teachers/?first_name=&last_name&gender=&classrooms__year=4&classrooms__section=&classrooms__school__name=
 -- get teachers detail list by first_name or last_name or gender or classrooms__year or classrooms__section or classrooms__school__name filter
 - GET: http://localhost:8000/api/v1/teachers/<id>/
 -- get teacher detail by teacher id
 - POST: http://localhost:8000/api/v1/teachers/
 -- create new teacher by detail in body json
 -- example : 
    {
        "first_name" : "หอม",
        "last_name" : "หวาน",
        "gender" : "หญิง",
        "classrooms" : [1]
    }
 - PUT: http://localhost:8000/api/v1/teachers/<id>/
 -- update or replace an existing resource identified by   teacher id
 - DELETE: http://localhost:8000/api/v1/teachers/<id>/
 -- delete teacher by id
```
```
Student
 - GET: http://localhost:8000/api/v1/students/?first_name=&last_name&gender=&classroom__year=&classroom__section=&classroom__school__name=
 -- get students detail list by first_name or last_name or gender or classroom__year or classroom__section or classroom__school__name filter
 - GET: http://localhost:8000/api/v1/students/<id>/
 -- get student detail by student id
 - POST: http://localhost:8000/api/v1/students/
 -- create new student by detail in body json
 -- example : 
    {
        "first_name" : "หอม",
        "last_name" : "หวาน",
        "gender" : "หญิง",
        "classroom" : 1
    }
 - PUT: http://localhost:8000/api/v1/students/<id>/
 -- update or replace an existing resource identified by   student id
 - DELETE: http://localhost:8000/api/v1/students/<id>/
 -- delete student by id
```Shows the process request status as in processing or completed.
