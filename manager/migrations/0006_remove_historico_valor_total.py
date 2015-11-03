# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20151103_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historico',
            name='valor_total',
        ),
    ]
