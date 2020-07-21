from django.db import models


class Courses(models.Model):
    course_id = models.IntegerField()
    department = models.CharField(max_length=20)
    course_number = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    grade = models.CharField(max_length=1)


class PreRequisites(models.Model):
    course_id = models.IntegerField()
    prereq1 = models.IntegerField()
    prereq2 = models.IntegerField()