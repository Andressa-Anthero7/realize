# Generated by Django 4.1.9 on 2023-08-05 03:30

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0003_alter_landingpage_imagem_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_10',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_6',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_7',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_8',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagem_9',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/'),
        ),
    ]
