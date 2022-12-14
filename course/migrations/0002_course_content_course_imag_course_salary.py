# Generated by Django 4.1 on 2022-08-11 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='imag',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='coursephoto/%y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='salary',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
