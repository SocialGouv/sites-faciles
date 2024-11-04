# Generated by Django 5.0.8 on 2024-09-02 17:27

import content_manager.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_manager", "0043_rename_analyticssettings_customscriptssettings"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customscriptssettings",
            options={"verbose_name": "Custom scripts"},
        ),
        migrations.AddField(
            model_name="customscriptssettings",
            name="use_tarteaucitron",
            field=models.BooleanField(
                default=False,
                help_text='See <a href="https://sites-faciles.beta.numerique.gouv.fr/documentation/gestion-des-cookies/">Documentation</a>',
                verbose_name="Use Tarteaucitron?",
            ),
        ),
        migrations.AlterField(
            model_name="cmsdsfrconfig",
            name="header_brand",
            field=models.CharField(
                blank=True,
                default="Intitulé officiel",
                help_text='Institution brand as defined on <a href="https://www.info.gouv.fr/marque-de-letat/le-bloc-marque">official page</a>.',
                max_length=200,
                verbose_name="Institution (header)",
            ),
        ),
        migrations.AlterField(
            model_name="customscriptssettings",
            name="body_scripts",
            field=content_manager.models.MonospaceField(
                blank=True,
                help_text="Allows for scripts to be placed at the end of the <body> tag of the website pages.",
                null=True,
                verbose_name="Scripts in the <body> section",
            ),
        ),
        migrations.AlterField(
            model_name="customscriptssettings",
            name="head_scripts",
            field=content_manager.models.MonospaceField(
                blank=True,
                help_text="Allows for scripts to be placed in the <head> tag of the website pages.",
                null=True,
                verbose_name="Scripts in the <head> section",
            ),
        ),
    ]