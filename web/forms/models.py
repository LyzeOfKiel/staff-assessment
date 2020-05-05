from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(User, related_name='student_courses')
    prof = models.ForeignKey(
        User,
        related_name='prof_courses',
        on_delete=models.CASCADE,
        default=None
    )
    tas = models.ManyToManyField(
        User,
        related_name='ta_courses'
    )


class FeedbackDefault(models.Model):
    rate = models.IntegerField()
    feedback = models.CharField(max_length=2000)
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class FeedbackCourse(FeedbackDefault):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )


class FeedbackProf(FeedbackDefault):
    prof = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class FeedbackTA(FeedbackDefault):
    TA = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
