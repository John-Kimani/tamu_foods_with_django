# Generated by Django 4.1.3 on 2022-11-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1)),
                ('delivery_status', models.CharField(choices=[('P', 'pending'), ('D', 'delivered')], default='P', max_length=1, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tamueats.customer')),
            ],
        ),
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255)),
                ('food_description', models.TextField()),
                ('food_unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.IntegerField()),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('featured_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tamueats.foodproduct')),
            ],
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='food_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tamueats.foodproductcategory'),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='promotions',
            field=models.ManyToManyField(to='tamueats.discounts'),
        ),
        migrations.CreateModel(
            name='FoodOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('food_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tamueats.foodorder')),
                ('food_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tamueats.foodproduct')),
            ],
        ),
        migrations.AddField(
            model_name='foodorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tamueats.foodproduct'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamueats.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamueats.foodproduct')),
            ],
        ),
    ]