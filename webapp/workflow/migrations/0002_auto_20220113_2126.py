# Generated by Django 3.2.11 on 2022-01-13 21:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0010_remove_duplicate_indices'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workflow',
            old_name='work_name',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='workflowtask',
            name='task',
        ),
        migrations.AddField(
            model_name='workflowtask',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 21, 26, 42, 987938)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workflowtask',
            name='task_id',
            field=models.CharField(default='', help_text='Celery ID for the Task that was run', max_length=255, unique=True, verbose_name='Task ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workflowtask',
            name='task_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.taskresult'),
        ),
    ]
