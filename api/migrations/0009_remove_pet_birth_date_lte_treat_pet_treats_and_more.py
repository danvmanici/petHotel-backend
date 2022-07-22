# Generated by Django 4.0.6 on 2022-07-22 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_pet_birth_date_lte_rename_pet_id_pettreat_pet_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='pet',
            name='birth_date_lte',
        ),
        migrations.AddField(
            model_name='treat',
            name='pet_treats',
            field=models.ManyToManyField(through='api.PetTreat', to='api.pet'),
        ),
        migrations.AddConstraint(
            model_name='pet',
            constraint=models.CheckConstraint(check=models.Q(('birth_date__lte', datetime.datetime(2022, 7, 22, 11, 29, 52, 351544, tzinfo=utc))), name='birth_date_lte'),
        ),
    ]
