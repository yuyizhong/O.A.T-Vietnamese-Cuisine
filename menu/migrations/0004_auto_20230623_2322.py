# Generated by Django 3.2.19 on 2023-06-23 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_menu_menuitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['category', 'name']},
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='type',
            new_name='category',
        ),
    ]
