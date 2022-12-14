from django.contrib.auth.models import User
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=200)


class Subject(models.Model):
    subject = models.CharField(max_length=200, null=True)


class Courses(models.Model):
    course = models.CharField(max_length=300, null=True)


class Professor(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200, null=True)
    picture = models.CharField(max_length=800, null=True)
    rating = models.FloatField(default=5.0)


class Review(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading = models.CharField(max_length=900, null=True)
    review = models.CharField(max_length=200)
    rating = models.FloatField(default=5.0)
    courses = models.CharField(max_length=800, null=True)
    # courses = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
    review_check = models.BooleanField(null=True)

    # def __str__(self):
    #     return self.user_review
