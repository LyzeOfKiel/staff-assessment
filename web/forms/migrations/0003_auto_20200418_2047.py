# Generated by Django 3.0.5 on 2020-04-18 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0002_auto_20200418_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdefault',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Course'),
        ),
        migrations.AlterField(
            model_name='feedbackdefault',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]