# Generated by Django 3.0.6 on 2020-06-12 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_item', '0004_auto_20200611_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_item.PortfolioCategory'),
        ),
    ]
