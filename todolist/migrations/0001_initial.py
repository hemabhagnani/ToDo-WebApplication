# Generated by Django 3.2 on 2021-05-25 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Low', max_length=100)),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2021-05-25')),
                ('due_date', models.DateField(default='2021-05-25')),
                ('status', models.IntegerField(default=0, max_length=20)),
                ('priority', models.ForeignKey(default='Low', on_delete=django.db.models.deletion.CASCADE, to='todolist.priority')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
