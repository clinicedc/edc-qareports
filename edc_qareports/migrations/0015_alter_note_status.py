# Generated by Django 4.2.11 on 2024-08-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_qareports", "0014_alter_note_options_alter_note_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Data is pending"),
                    ("not_available", "Data not available"),
                ],
                max_length=25,
                null=True,
            ),
        ),
    ]