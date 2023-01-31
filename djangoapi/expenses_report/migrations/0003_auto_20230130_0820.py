# Generated by Django 3.2.16 on 2023-01-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_report', '0002_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(max_length=50),
        ),
    ]