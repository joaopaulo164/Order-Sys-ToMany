# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_remove_historico_valor_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
