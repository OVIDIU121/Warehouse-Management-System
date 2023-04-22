from rest_framework import serializers
from .models import Inventory, Location, Order, OrderItem, Item, PreAdvice, PreAdviceItem, Transaction, Supplier, Customer, MoveTask

# Convert model instances into a format that can be easily transferred over the network, such as JSON.


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        extra_kwargs = {
            'url': {'LocationList': 'LocationDetail-detail'},
            'delete': {'read_only': False},
        }


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class PreadviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAdvice
        fields = '__all__'


class PreadviceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAdviceItem
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class MoveTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveTask
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        extra_kwargs = {
            'url': {'InventoryList': 'InventoryDetail-detail'},
            'delete': {'read_only': False},
        }
