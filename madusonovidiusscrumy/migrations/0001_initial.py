# Generated by Django 3.0.6 on 2020-05-16 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=50)),
                ('goal_id', models.IntegerField()),
                ('created_by', models.CharField(max_length=50)),
                ('moved_by', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madusonovidiusscrumy.GoalStatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goal_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_by', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=50)),
                ('moved_from', models.CharField(max_length=50)),
                ('moved_to', models.CharField(max_length=50)),
                ('time_of_action', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madusonovidiusscrumy.ScrumyGoals')),
            ],
        ),
    ]
