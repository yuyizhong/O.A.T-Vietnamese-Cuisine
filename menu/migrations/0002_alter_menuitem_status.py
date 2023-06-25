# Generated by Django 3.2.19 on 2023-06-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('approved', 'Approved'), ('hidden', 'Hidden')], default='draft', max_length=10),
        ),
    ]
