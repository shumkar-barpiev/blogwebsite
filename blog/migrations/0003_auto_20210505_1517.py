# Generated by Django 3.2.1 on 2021-05-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210505_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posttimg',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=450, null=True, unique_for_date='publish'),
        ),
    ]
