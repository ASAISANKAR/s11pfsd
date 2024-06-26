# Generated by Django 4.0.3 on 2024-02-01 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0002_alter_jobdetails_salary_offered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='benefits',
            field=models.TextField(null='false'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='education',
            field=models.CharField(max_length=255, null='false'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='job_type',
            field=models.CharField(choices=[('fulltime', 'Full Time'), ('parttime', 'Part Time'), ('contract', 'Contract')], max_length=20, null='false'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='required_skills',
            field=models.TextField(null='false'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='work_location',
            field=models.CharField(max_length=255, null='false'),
        ),
    ]
