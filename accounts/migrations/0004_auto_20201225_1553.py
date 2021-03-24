# Generated by Django 3.0.6 on 2020-12-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201218_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='middle_name',
            field=models.CharField(max_length=255, null=True, verbose_name='middle name'),
        ),
    ]
