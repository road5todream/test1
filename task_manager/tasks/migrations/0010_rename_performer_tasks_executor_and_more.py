# Generated by Django 4.1.3 on 2022-11-26 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_labels_options_alter_labels_name'),
        ('tasks', '0009_alter_relationlink_task_alter_tasks_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='performer',
            new_name='executor',
        ),
        migrations.AlterField(
            model_name='relationlink',
            name='task',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='label',
            field=models.ManyToManyField(blank=True, through='tasks.RelationLink', to='labels.labels', verbose_name='Метки'),
        ),
    ]