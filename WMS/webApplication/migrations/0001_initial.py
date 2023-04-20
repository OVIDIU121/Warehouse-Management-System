# Generated by Django 4.2 on 2023-04-20 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('unit_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_on_hand', models.IntegerField(default=0)),
                ('reorder_point', models.IntegerField()),
                ('reorder_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('FULFILLED', 'Fulfilled'), ('CANCELED', 'Canceled')], default='PENDING', max_length=20)),
                ('order_date', models.DateField()),
                ('destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_destination_location', to='webApplication.location')),
            ],
        ),
        migrations.CreateModel(
            name='PreAdvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preadvice_number', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('RECEIVED', 'Received')], default='PENDING', max_length=20)),
                ('scheduled_arrival_date', models.DateField()),
                ('destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_advice_destination_location', to='webApplication.location')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('INBOUND', 'Inbound'), ('OUTBOUND', 'Outbound')], max_length=20)),
                ('transaction_date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApplication.item')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApplication.location')),
            ],
        ),
        migrations.CreateModel(
            name='PreAdviceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApplication.item')),
                ('preadvice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApplication.preadvice')),
            ],
        ),
        migrations.AddField(
            model_name='preadvice',
            name='items',
            field=models.ManyToManyField(through='webApplication.PreAdviceItem', to='webApplication.item'),
        ),
        migrations.AddField(
            model_name='preadvice',
            name='source_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_advice_source_location', to='webApplication.location'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApplication.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApplication.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='webApplication.OrderItem', to='webApplication.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='source_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_source_location', to='webApplication.location'),
        ),
    ]