class pwskills(object):
    def __init__(self,price, name):
        self.__course_price = price
        self.__discount = 0.0
        self.name = name

    @property
    def course_price(self):
        self.__course_price = self.__course_price - (self.__course_price * (self.__discount/100))
        return f"course price is: INR {self.__course_price}"

    @property
    def discount(self):
        #print(type(self.__discount))
        return self.__discount

    @discount.setter
    def discount(self, newDiscount):
        self.__discount = newDiscount
        return self.__discount

    @course_price.setter
    def course_price(self, newPrice):
        self.__course_price = newPrice
        return self.__course_price    
    
    def course_details(self):
        if self.__discount != 0.0:
            print("Course enrolled: ",self.name)
            print("Course Price: ", self.course_price)
            print("Discount applied: ",self.discount)
        else:
            print("Course enrolled: ",self.name)
            print("Course Price: ", self.course_price)