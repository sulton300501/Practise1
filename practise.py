class Market:
    def __init__(self, product:dict,balance:float , name,adress):
        self.product=product
        self.balance=balance
        self.name=name
        self.adress=adress

    def getProduction(self):
        print(f"{self.product}")

    def add_product(self,prod:dict):
        self.product.update(prod)
       
    
    def remove_product(self,prod):
        if prod in self.product:
            self.product.pop(prod)
            return self.product

    def add_money(self , money):
        self.balance+=money

    def sell(self,tovar , soni):
        if tovar in self.product:
            self.balance+=self.product[tovar]*soni



    def __str__(self) :
        return f"""
Name: {self.name}
Products: {self.product}
Balance: {self.balance}
Adress: {self.adress}


"""


dict1 = {}
for i in range(int(input("Nechta product kiritasiz"))):
    dict1.update({input("product nomini kiriting"):int(input("Narxini kiriting"))})



market = Market(dict1 ,int(input("Balancingizni kiriting")),input("Dokon nomini kiriting"),input("adresni kiriting"))

while True:
    print("""
    1. getProductsInfo
    2. addProduct
    3.removeProduct
    4.addMoney
    5.sell
    6.Exit
    """)

    son=int(input("Iltimos sonni tanlang"))
    
    if son==1:
        market.getProduction()
    if son==2:
        dct2={input("Product nomini kiriting"):int(input("Narxini kiriting"))}
        market.add_product(dct2)
    if son==3:
        market.remove_product(input("qaysi productni ochirasiz"))
    if son==4:
        market.add_money(int(input("Qancha pul qo'shasiz")))
    if son==5:
        market.sell(input("Tovarni kiriting"),int(input("Sonini kiriting")))
    if son==6:
        break




