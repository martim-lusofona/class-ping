from django.db import models
from django.contrib.auth.models import User

class SchoolClass(models.Model):
    label = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return self.label

class Course(models.Model):
    label = models.CharField(max_length=50)
    
    classes = models.ManyToManyField(SchoolClass)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.label

class Student(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.number}: {self.name}"

class Session(models.Model):
    uuid = models.UUIDField()
    open_time = models.TimeField()
    is_active = models.BooleanField()

    students = models.ManyToManyField(Student, through='SessionStudent')
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name="sessions")

    def __str__(self):
        return f"Session at {self.open_time}"

class SessionStudent(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} joined {self.session} at {self.joined_at}"

