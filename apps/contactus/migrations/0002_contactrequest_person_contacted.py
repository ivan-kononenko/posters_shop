# Generated by Django 3.0.7 on 2020-07-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='person_contacted',
            field=models.BooleanField(default=False),
        ),
    ]
