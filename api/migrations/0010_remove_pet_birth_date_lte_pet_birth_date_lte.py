# Generated by Django 4.0.6 on 2022-07-27 17:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_pet_birth_date_lte_treat_pet_treats_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='pet',
            name='birth_date_lte',
        ),
        migrations.AddConstraint(
            model_name='pet',
            constraint=models.CheckConstraint(check=models.Q(('birth_date__lte', datetime.datetime(2022, 7, 27, 17, 5, 41, 849921, tzinfo=utc))), name='birth_date_lte'),
        ),
    ]
