# Generated by Django 4.2.5 on 2023-11-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_roll', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('s_branch', models.CharField(max_length=10)),
                ('s_section', models.CharField(max_length=5)),
            ],
        ),
    ]
