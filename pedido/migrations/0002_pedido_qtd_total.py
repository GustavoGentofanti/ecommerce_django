# Generated by Django 4.1 on 2022-08-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade total'),
            preserve_default=False,
        ),
    ]
