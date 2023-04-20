from django.shortcuts import render
from .models import Location, Order, Inventory, OrderItem, Item, PreAdvice, PreAdviceItem, Transaction, Supplier, Customer, MoveTask
from .serializers import LocationSerializer, InventorySerializer, SupplierSerializer, CustomerSerializer, MoveTaskSerializer, OrderSerializer, OrderItemSerializer, ItemSerializer, PreadviceSerializer, PreadviceItemSerializer, TransactionSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class OrderList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ItemList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PreAdviceList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PreAdvice.objects.all()
    serializer_class = PreadviceSerializer


class PreAdviceDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PreAdvice.objects.all()
    serializer_class = PreadviceSerializer


class PreAdviceItemList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PreAdviceItem.objects.all()
    serializer_class = PreadviceItemSerializer


class PreAdviceItemDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PreAdviceItem.objects.all()
    serializer_class = PreadviceItemSerializer


class TransactionList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SupplierList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CustomerList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class MoveTaskList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MoveTask.objects.all()
    serializer_class = MoveTaskSerializer


class MoveTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MoveTask.objects.all()
    serializer_class = MoveTaskSerializer


class MoveTaskList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MoveTask.objects.all()
    serializer_class = MoveTaskSerializer


class MoveTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MoveTask.objects.all()
    serializer_class = MoveTaskSerializer


class InventoryList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
