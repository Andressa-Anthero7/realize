# Generated by Django 4.1.10 on 2023-09-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0003_landingpage_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landingpage',
            name='valor',
        ),
        migrations.AddField(
            model_name='landingpage',
            name='bairro',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='info_complementares',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='padrao_imovel',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='qtde_vaga_garagem',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='status_imovel',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='tipo_imovel',
            field=models.CharField(max_length=30),
        ),
    ]
