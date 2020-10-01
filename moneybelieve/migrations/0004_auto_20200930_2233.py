# Generated by Django 2.2.14 on 2020-09-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneybelieve', '0003_auto_20200930_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='unit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='保有数量'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='avg_price',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=10, null=True, verbose_name='平均取得単価'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='lower_price',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=10, null=True, verbose_name='損切りライン'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='upper_price',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=10, null=True, verbose_name='利確ライン'),
        ),
    ]
