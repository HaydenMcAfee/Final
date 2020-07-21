from django.db import models


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=200)
    course_number = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    grade = models.CharField(max_length=1)

    def __str__(self):
        return self.course_name


class PreRequisite(models.Model):
    course_id = models.IntegerField(primary_key=True)
    prereq1 = models.IntegerField()
    prereq2 = models.IntegerField()

