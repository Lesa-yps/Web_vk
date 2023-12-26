# Generated by Django 4.2.7 on 2023-12-26 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_question_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('avatar', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_number',
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.user'),
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.user'),
        ),
    ]
