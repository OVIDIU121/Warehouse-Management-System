# Generated by Django 4.2 on 2023-04-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_item_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.supplier'),
        ),
        migrations.AlterField(
            model_name='preadvice',
            name='preadvice_status',
            field=models.CharField(choices=[('P', 'Pending'), ('R', 'Received'), ('S', 'Partially received')], max_length=1),
        ),
    ]
