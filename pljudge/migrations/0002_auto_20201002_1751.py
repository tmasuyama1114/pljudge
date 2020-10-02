# Generated by Django 2.2.14 on 2020-10-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pljudge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='avg_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='平均取得単価'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='lower_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='損切りライン'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='upper_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='利確ライン'),
        ),
    ]
