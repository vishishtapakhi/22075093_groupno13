# Generated by Django 4.2.6 on 2023-11-04 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InstiPro', '0018_student_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_leave',
            old_name='roll_number',
            new_name='student_id',
        ),
    ]
