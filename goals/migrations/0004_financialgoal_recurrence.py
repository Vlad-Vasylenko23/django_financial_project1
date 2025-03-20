# Generated by Django 5.1.6 on 2025-03-22 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_remove_financialgoal_notification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialgoal',
            name='recurrence',
            field=models.CharField(choices=[('daily', 'Щоденно'), ('weekly', 'Щотижня'), ('monthly', 'Щомісячно')], default='monthly', max_length=10),
        ),
    ]
