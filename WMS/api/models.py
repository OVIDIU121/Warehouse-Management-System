from django.db import models

# Creates a database model for the customer
class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}, Code: {self.code}'


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}, Code: {self.code}'


class Item(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # set null=True to allow existing rows to have no value
    depth = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name}, Sku: {self.sku}, Description: {self.description}'


class Location(models.Model):
    LOCATION_TYPES = (
        ('R', 'Racking'),
        ('M', 'Marshalling'),
        ('C', 'Container'),
    )
    name = models.CharField(max_length=255)
    location_type = models.CharField(max_length=1, choices=LOCATION_TYPES)
    max_capacity = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}, Type: {self.location_type}, Capacity: {self.max_capacity}'


class PreAdvice(models.Model):
    PREADVICE_STATUSES = (
        ('P', 'Pending'),
        ('R', 'Received'),
        ('S', 'Partially received')
    )
    preadvice_status = models.CharField(
        max_length=1, choices=PREADVICE_STATUSES)
    arrival_date = models.DateField()
    source_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f'Id: {self.id}, Status: {self.preadvice_status}, Date: {self.arrival_date}, Supplier: {self.source_supplier}'


class PreAdviceItem(models.Model):
    PREADVICE_STATUSES = (
        ('P', 'Pending'),
        ('R', 'Received'),
        ('S', 'Partially received')
    )
    preadvice_status = models.CharField(
        max_length=1, choices=PREADVICE_STATUSES)
    preadvice = models.ForeignKey(PreAdvice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    expected_quantity = models.IntegerField()
    received_quantity = models.IntegerField()
    received_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'Id: {self.id}, Status: {self.preadvice_status}, Item: {self.item}, Expected: {self.expected_quantity}, Recieved: {self.received_quantity}, Recieved Location: {self.received_location}'


class Order(models.Model):
    ORDER_STATUSES = (
        ('P', 'Pending'),
        ('F', 'Fulfilled'),
        ('C', 'Canceled'),
    )
    order_status = models.CharField(max_length=1, choices=ORDER_STATUSES)
    order_number = models.CharField(max_length=255)
    order_date = models.DateField()
    destination_customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'Id: {self.id}, Status: {self.order_status}, Date: {self.order_date}, Customer: {self.destination_customer}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    required_quantity = models.IntegerField()
    picked_quantity = models.IntegerField()

    def __str__(self):
        return f'Id: {self.order}, Item: {self.item}, Required: {self.required_quantity}, Picked: {self.picked_quantity}'


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Item: {self.item}, Location: {self.location}, Quantity: {self.quantity}'


class MoveTask(models.Model):
    MOVE_TASK_STATUS_CHOICES = [
        ('released', 'Released'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    move_task_status = models.CharField(
        max_length=20, choices=MOVE_TASK_STATUS_CHOICES, default='released')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    from_location = models.ForeignKey(
        Location, related_name='from_location', on_delete=models.CASCADE)
    to_location = models.ForeignKey(
        Location, related_name='to_location', on_delete=models.CASCADE)

    def __str__(self):
        return f'Status: {self.move_task_status}, Item: {self.item}, From: {self.from_location}, To: {self.to_location}'


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('inbound', 'Inbound from preadvice'),
        ('picking', 'Picking'),
    ]
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_TYPE_CHOICES, default='inbound')
    transaction_date = models.DateField(auto_now_add=True)
    from_location = models.ForeignKey(
        Location, related_name='from_trans_location', on_delete=models.CASCADE)
    to_location = models.ForeignKey(
        Location, related_name='to_trans_location', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Type: {self.transaction_type}, Date: {self.transaction_date}, From: {self.from_location}, To: {self.to_location}'
