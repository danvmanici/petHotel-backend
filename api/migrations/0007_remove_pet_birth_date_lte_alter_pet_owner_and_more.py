# Generated by Django 4.0.6 on 2022-07-21 13:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_pet_birth_date_lte_pet_birth_date_lte'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='pet',
            name='birth_date_lte',
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.owner'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pets', to='api.species'),
        ),
        migrations.AddConstraint(
            model_name='pet',
            constraint=models.CheckConstraint(check=models.Q(('birth_date__lte', datetime.datetime(2022, 7, 21, 13, 3, 23, 958180, tzinfo=utc))), name='birth_date_lte'),
        ),
    ]
