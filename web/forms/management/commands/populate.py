from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from forms.models import Course


class Command(BaseCommand):
    def create_data(self):
        PROF, created = Group.objects.get_or_create(name='Prof')

        prof1 = User(username='p1')
        prof1.set_password('p1')
        prof1.save()
        PROF.user_set.add(prof1)

        prof2 = User(username='p2')
        prof2.set_password('p2')
        prof2.save()
        PROF.user_set.add(prof2)

        STUDENT, created = Group.objects.get_or_create(name='Student')

        s1 = User(username='s1')
        s1.set_password('s1')
        s1.save()
        STUDENT.user_set.add(s1)

        s2 = User(username='s2')
        s2.set_password('s2')
        s2.save()
        STUDENT.user_set.add(s2)

        s3 = User(username='s3')
        s3.set_password('s3')
        s3.save()
        STUDENT.user_set.add(s3)

        course1 = Course(name='Math', prof=prof1)
        course1.save()
        course1.students.add(s1, s2)

        course2 = Course(name='Informatics', prof=prof2)
        course2.save()
        course2.students.add(s2, s3)

    def handle(self, *args, **options):
        self.create_data()
