# Generated by Django 3.2.8 on 2021-11-02 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=None)),
                ('ciudad', models.CharField(max_length=255, null=True, verbose_name='Ciudad')),
                ('pais', models.CharField(max_length=255, null=True, verbose_name='Pais')),
                ('descripcion', models.CharField(max_length=255, null=True, verbose_name='Descripcion')),
                ('n_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
