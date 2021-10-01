# Generated by Django 3.2.6 on 2021-09-29 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
        ('api', '0017_payout_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='payoutaddress',
            name='referral',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='referral.referral'),
        ),
        migrations.AddField(
            model_name='payoutaddress',
            name='referral_amount',
            field=models.BigIntegerField(default=0),
        ),
    ]