import unittest
from app.database import Database
from app.models import Laptop, Customer, Order

class TestStore(unittest.TestCase):

    def setUp(self):
        self.db = Database(':memory:')

    def tearDown(self):
        self.db.close()

    def test_add_laptop(self):
        laptop = Laptop(None, 'Dell', 'XPS 13', 999.99)
        self.db.add_laptop(laptop)
        self.db.cursor.execute('SELECT * FROM laptops WHERE brand=?', (laptop.brand,))
        result = self.db.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Dell')

    def test_add_customer(self):
        customer = Customer(None, 'John Doe', 'john@example.com')
        self.db.add_customer(customer)
        self.db.cursor.execute('SELECT * FROM customers WHERE email=?', (customer.email,))
        result = self.db.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'John Doe')

    def test_add_order(self):
        laptop = Laptop(None, 'Dell', 'XPS 13', 999.99)
        customer = Customer(None, 'John Doe', 'john@example.com')
        self.db.add_laptop(laptop)
        self.db.add_customer(customer)
        order = Order(None, 1, 1, 2)
        self.db.add_order(order)
        self.db.cursor.execute('SELECT * FROM orders WHERE customer_id=?', (order.customer_id,))
        result = self.db.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[3], 2)

if __name__ == '__main__':
    unittest.main()
