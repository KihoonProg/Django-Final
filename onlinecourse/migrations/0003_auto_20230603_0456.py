# Generated by Django 3.1.3 on 2023-06-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230603_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=550),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=5.0),
        ),
    ]
