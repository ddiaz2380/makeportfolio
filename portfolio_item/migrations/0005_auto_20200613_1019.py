# Generated by Django 3.0.6 on 2020-06-13 10:19

from django.db import migrations, models
import django.db.models.deletion
import makeportfolio.helper


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('portfolio_item', '0004_auto_20200613_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetails',
            name='profile',
            field=models.OneToOneField(default=makeportfolio.helper.get_user_profile, on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
    ]
