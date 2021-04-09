class Cardholder:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        return 'Your deposite was succsessful ', self.name, ' Your balance is now: ', self.balance

    def whitdraw(self,amount):
        if self.balance < amount:
            return "You´r balance is : ", self.balance, ".", " Your whitdraw exeeds your funds"
        else:
            self.balance -= amount
            return "Your whitdraw was successful. Your balance is now: ", self.balance
    def mybalance(self):
        return "Your balance is ", self.balance

bank1 = Cardholder("Christer", 500)
print(bank1.mybalance())
print(bank1.deposite(500))

print(bank1.deposite(500))

print(bank1.whitdraw(2000))
print(bank1.whitdraw(1000))




