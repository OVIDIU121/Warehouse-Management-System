from django.test import TestCase
from .models import Customer, Supplier, Item


# Creates a test data object for a Customer model.
class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(
            name='John Smith', address='123 Main St', code='ABC123')

    def test_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_code_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('code').max_length
        self.assertEqual(max_length, 255)

    def test_str_representation(self):
        customer = Customer.objects.get(id=1)
        expected_str = f'Name: {customer.name}, Address: {customer.address}, Code: {customer.code}'
        self.assertEqual(str(customer), expected_str)


# Creates a TestCase for a Supplier model.
class SupplierModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Supplier.objects.create(
            name='ABC Corp', address='456 Main St', code='XYZ789')

    def test_name_label(self):
        supplier = Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_code_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('code').max_length
        self.assertEqual(max_length, 255)

    def test_str_representation(self):
        supplier = Supplier.objects.get(id=1)
        expected_str = f'Name: {supplier.name}, Address: {supplier.address}, Code: {supplier.code}'
        self.assertEqual(str(supplier), expected_str)


# Class TestCase to test a item model.
class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        supplier = Supplier.objects.create(
            name='ABC Corp', address='456 Main St', code='XYZ789')
        Item.objects.create(name='Widget', sku='WID001', description='A useful widget',
                            weight=1.5, height=2.0, width=2.0, depth=1.0, supplier=supplier)

    def test_name_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_str_representation(self):
        item = Item.objects.get(id=1)
        expected_str = f'Name: {item.name}, Sku: {item.sku}, Description: {item.description}'
        self.assertEqual(str(item), expected_str)
