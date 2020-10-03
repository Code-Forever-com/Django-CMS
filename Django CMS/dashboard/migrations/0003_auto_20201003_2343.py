# Generated by Django 3.1 on 2020-10-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_menu_is_dash'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_key', models.CharField(max_length=50, verbose_name='Blog Key')),
                ('blog_value', models.CharField(max_length=50, verbose_name='Blog Value')),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
