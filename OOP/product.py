class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self. price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        status = "Sold"
        return self

    def add_tax(self):
        tax = []
        price = price + price * tax
        return self

    def sale_return(self):
        reason = ""
        if reason == "Defective":
            status = "Defective"
            price = 0
            return self
        elif reason == "Like new":
            status = "For Sale"
            return self
        elif reason == "Open box":
            status = "Used"
            price = price - price * 0.2
            return self
        else:
            return self

    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Product Name: " + str(self.item_name)
        print "Product weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + self.status
