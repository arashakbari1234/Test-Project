# Generated by Django 3.1.7 on 2021-02-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_exercise_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='excercises',
            field=models.ManyToManyField(to='accounts.Exercise'),
        ),
    ]
