# Generated by Django 3.2 on 2023-04-22 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_auto_20230422_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteToy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='deleted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='favorite_toy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='cats', to='cats.favoritetoy'),
            preserve_default=False,
        ),
    ]