# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20150915_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='historico',
            new_name='historicos',
        ),
        migrations.AddField(
            model_name='historico',
            name='servicos',
            field=models.ManyToManyField(to='manager.Servico'),
        ),
    ]
