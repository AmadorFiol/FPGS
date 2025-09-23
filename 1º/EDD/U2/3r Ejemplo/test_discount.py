import unittest
from discount import *

class TestDiscount(unittest.TestCase):

   # Compra 1(más de 100, 3 productos, código promo del 20)
   def test_compra_1(self):
      print("Test 1")
      total, discount=calculate_discount(120,3,"DESC20")
      self.assertEqual(round(total,2),78.00)
      self.assertEqual(discount, 35)

   # Compra 2 (menos de 100, 4 productos, codigo promo del 10)
   def test_compra_2(self):
      print("Test 2")
      total, discount=calculate_discount(80, 4, "DESC10")
      self.assertEqual(round(total,2),68.00)
      self.assertEqual(discount, 15)

   # Compra 3 (menos de 100, 6 productos, sin codigo)
   def test_compra_3(self):
      print("Test 3")
      total, discount=calculate_discount(50, 6)
      self.assertEqual(round(total,2),45.00)
      self.assertEqual(discount, 10)

   # Compra 4 (más de 100, 5 productos, sin codigo)
   def test_compra_4(self):
      print("Test 4")
      total, discount=calculate_discount(150, 5)
      self.assertEqual(round(total,2),112.50)
      self.assertEqual(discount, 25)

   # Compra 5 (más de 100, 7 productos, con codigo promo 20)
   def test_compra_5(self):
      print("Test 5")
      total, discount=calculate_discount(200, 7, "DESC20")
      self.assertEqual(round(total,2),120.00)
      self.assertEqual(discount, 40)

if __name__ == '__main__':
   unittest.main()
