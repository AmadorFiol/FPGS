import unittest
from store import Store

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store=Store()

    #ADD_PRODUCT
    #Test 1: Add none existent product
    def test_add_noneExistent_prod(self):
        self.assertTrue(self.store.add_product("Product",1000,5))
        product=self.store.products.get("Product")
        self.assertEqual(product['stock'],5)

    #Test 2: Add already existent product
    def test_add_existent_prod(self):
        self.store.add_product("Product",1000,5)
        self.assertFalse(self.store.add_product("Product",1000,10))
        product=self.store.products.get("Product")
        self.assertNotEqual(product['stock'],10)
    
    #UPDATE_STOCK
    #Test 3: update_stock of none existent product
    def test_update_stock_noneExistent_prod(self):
        self.assertFalse(self.store.update_stock("Product",1))

    #Test 4: update_stock of existent product
    def test_update_stock_existent_prod(self):
        self.store.add_product("Product",1000,5)
        self.assertTrue(self.store.update_stock("Product",1))
        product=self.store.products.get("Product")
        self.assertEqual(product['stock'],6)


    #APPLY_DISCOUNT
    #Test 5: apply discount of none existent product
    def test_apply_discount_noneExistent_prod(self):
        self.assertFalse(self.store.aply_discount("Product",1))

    #Test 6: apply discount of existent product
    def test_apply_discount_existent_prod(self):
        self.store.add_product("Product",1000,5)
        self.assertTrue(self.store.aply_discount("Product",50))
        product=self.store.products.get("Product")
        self.assertEqual(product['price'],500)


    #GET
    #Test 7: get none existent product
    def test_get_noneExistent_prod_info(self):
        self.assertNotEqual(self.store.get_product_info("Product"),{'price':1000,'stock':5})

    #Test 8: get existent product
    def test_get_existent_prod_info(self):
        self.store.add_product("Product",1000,5)
        product=self.store.products.get("Product")
        self.assertEqual(self.store.get_product_info("Product"),product)

    #PURCHASE_PRODUCT
    #Test 98: purchase none existent product or not suffice stock
    def test_purchase_noneExistent_product(self):
        self.assertFalse(self.store.purchase_product("Product",1))
        self.store.add_product("Product",1000,5)
        self.assertFalse(self.store.purchase_product("Product",6))

    #Test 10: purchase existent product
    def test_purchase_existent_product(self):
        self.store.add_product("Product",1000,5)
        self.assertTrue(self.store.purchase_product("Product",1))
        product=self.store.products.get("Product")
        self.assertEqual(product['stock'],4)


if __name__=="__main__":
    unittest.main()