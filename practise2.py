class Company:
    def __init__(self,name,location,establishedAt,balance):
        self.name=name
        self.location=location
        self.establishedAt=establishedAt
        self.balance=balance

    def getName(self):
        pass

    def getLocation(self):
        pass

    def getBalance(self):
        pass


class CarCompany(Company):
    def __init__(self, name, location, establishedAt, balance,cars):
        super().__init__(name, location, establishedAt, balance)
        self.cars=[]

    def getCoursCount(self):
        pass

    def addCar(self , prod):
        self.cars.append(prod)

    def sellCar(self):
        pass

    def getAllCars(self):
        pass


class MeatCompany(Company):
    def __init__(self, name, location, establishedAt, balance):
        super().__init__(name, location, establishedAt, balance)
        self.allMeatKg=[]
        


