class Customer:

    cus_list = []

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob = 0

    def createCustomer(self):
        Customer.cus_list.append(self)

    def searchCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                return e

    def updateCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                e.name = self.name
                e.age = self.age
                e.mob = self.mob

    def deleteCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                Customer.cus_list.remove(e)
