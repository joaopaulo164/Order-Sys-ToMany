# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_servico_historicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.IntegerField(max_length=10),
        ),
    ]
