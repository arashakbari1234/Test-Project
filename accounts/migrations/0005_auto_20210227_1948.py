# Generated by Django 3.1.7 on 2021-02-27 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='excercises',
            new_name='exercises',
        ),
    ]