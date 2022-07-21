# Generated by Django 4.0.6 on 2022-07-21 10:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_pet_birth_date_lte_pet_birth_date_lte'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='pet',
            name='birth_date_lte',
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddConstraint(
            model_name='pet',
            constraint=models.CheckConstraint(check=models.Q(('birth_date__lte', datetime.datetime(2022, 7, 21, 10, 45, 10, 545818, tzinfo=utc))), name='birth_date_lte'),
        ),
    ]
