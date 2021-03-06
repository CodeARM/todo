# Generated by Django 3.0.5 on 2020-07-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aof', models.CharField(default='none', max_length=75)),
                ('describe', models.CharField(default='none', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='area',
            field=models.CharField(default='none', max_length=75),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.CharField(default='inbox', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='when',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='task',
            name='where',
            field=models.CharField(default='tbd', max_length=10),
        ),
    ]
