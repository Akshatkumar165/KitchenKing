# Generated by Django 3.1.2 on 2020-10-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201010_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des_line1',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='des_line2',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='des_line3',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='des_line4',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='des_line5',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
