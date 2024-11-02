# Generated by Django 4.2.5 on 2023-11-10 07:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacultyView', '0002_remove_student_s_name_student_s_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_year',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
            preserve_default=False,
        ),
    ]
