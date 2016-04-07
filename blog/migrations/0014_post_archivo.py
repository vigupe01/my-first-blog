# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160406_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
