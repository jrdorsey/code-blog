# Generated by Django 3.0 on 2020-01-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0003_auto_20200131_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcodesnippet',
            name='caption',
            field=models.CharField(default='example.py', max_length=200),
            preserve_default=False,
        ),
    ]
