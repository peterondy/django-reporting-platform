# Generated by Django 4.1.1 on 2022-09-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_alter_reports_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
