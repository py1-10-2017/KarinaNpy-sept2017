class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Bike's price:", self.price
        print "Maximum speed:", self.max_speed
        print "Total miles:", self.miles

    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles = self.miles - 5
        return self

bike1 = Bike(200, "25 mph", 350)
bike2 = Bike(500, "35 mph", 100)
bike3 = Bike(320, "30 mph", 230)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().displayInfo()
