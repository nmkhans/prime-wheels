# Generated by Django 5.0.6 on 2024-07-03 05:17

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_car_quantity'),
        ('comments', '0003_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.expressions.Case, related_name='comment', to='car.car'),
        ),
    ]
