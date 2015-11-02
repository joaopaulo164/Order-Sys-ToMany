# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20150916_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='historicos',
        ),
    ]
