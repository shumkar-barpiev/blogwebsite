# Generated by Django 3.2.1 on 2021-05-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysociallinks',
            name='aboutmyself',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='mysociallinks',
            name='telegram',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mysociallinks',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mysociallinks',
            name='facebook',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mysociallinks',
            name='github',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mysociallinks',
            name='instagram',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mysociallinks',
            name='myportfolio',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mysociallinks',
            name='youtube',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
