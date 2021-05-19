# Generated by Django 3.2 on 2021-05-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20210505_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['due_date']},
        ),
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='Incomplete', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2021-05-06'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2021-05-06'),
        ),
    ]