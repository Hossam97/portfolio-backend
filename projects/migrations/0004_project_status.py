# Generated by Django 5.1.1 on 2024-09-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('finished', 'Finished'), ('in_progress', 'Still in progress')], default='finished', max_length=50, verbose_name='Project status'),
        ),
    ]
