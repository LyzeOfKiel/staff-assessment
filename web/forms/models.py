from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(User, related_name='courses')


class FeedbackDefault(models.Model):
    rate = models.IntegerField()
    feedback = models.CharField(max_length=2000)
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
