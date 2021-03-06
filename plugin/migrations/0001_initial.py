# Generated by Django 3.1 on 2020-09-19 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name Of Plugin')),
                ('description', models.CharField(max_length=150, verbose_name='Description Of Plugin')),
                ('folder_name', models.CharField(max_length=50, verbose_name='Folder Name Of Plugin')),
                ('status', models.BooleanField(verbose_name='Statue Of Plugin')),
            ],
        ),
        migrations.CreateModel(
            name='PluginOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='Key Of Plugin Option')),
                ('value', models.CharField(max_length=150, verbose_name='Value Of Plugin Option')),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='plugin.plugin', verbose_name='Plugin')),
            ],
        ),
    ]
