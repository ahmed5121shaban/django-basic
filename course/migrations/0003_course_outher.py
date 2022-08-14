# Generated by Django 4.1 on 2022-08-14 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_course_content_course_imag_course_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='outher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_course', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]