# Generated by Django 4.2.6 on 2023-10-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstiPro', '0003_course_session_year_alter_customuser_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='student_images/'),
        ),
    ]