# Generated by Django 3.2.20 on 2023-09-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230908_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='slides',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='galerie',
            name='categorie',
            field=models.CharField(blank=True, choices=[('RENCONTRES', 'RENCONTRES'), ('PROJETS', 'PROJETS'), ('EVENEMENTS', 'EVENEMENTS'), ('REALISATIONS', 'REALISATIONS')], max_length=250, null=True),
        ),
    ]
