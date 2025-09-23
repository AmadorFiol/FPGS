class Store:
    def __init__(self):
        self.products={}

    def add_product(self,name,price,stock):
        if name not in self.products:
            self.products[name]={'price':price,'stock':stock}
            return True
        return False

    def update_stock(self,name,stock):
        if name in self.products:
            self.products[name]['stock']+=stock
            return True
        return False

    def aply_discount(self,name,amount):
        if name in self.products and 0<amount<100:
            product=self.products[name]
            product['price']-=product['price']*(amount/100)
            return True
        return False
    
    def get_product_info(self,name):
        return self.products.get(name)

    def purchase_product(self,name,amount):
        if name in self.products:
            product=self.products[name]
            if amount<=product['stock']:
                product['stock']-=amount
                return True
        return False

    def __str__(self):
        return "\n".join(
            [f"{name}: Precio={product['price']}, Stock={product['stock']}" for name,product in self.products.items()]
            )



def main():
    store=Store()

    store.add_product("Laptop",1000,10)
    store.add_product("Phone",1000,10)
    print(store)

    print(store.get_product_info("Laptop"))

if __name__=="__main__":
    main()
