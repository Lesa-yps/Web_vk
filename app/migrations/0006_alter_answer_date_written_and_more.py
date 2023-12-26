# Generated by Django 4.2.7 on 2023-12-26 20:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_answer_like_remove_question_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_written',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_written',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
