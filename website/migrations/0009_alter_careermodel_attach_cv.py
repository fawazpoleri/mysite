# Generated by Django 4.2.17 on 2025-02-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_careermodel_alter_promo_promo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='attach_cv',
            field=models.FileField(upload_to='attachment_cv/'),
        ),
    ]
