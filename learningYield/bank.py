class Bank(): # let's create a bank, building ATMs
    crisis = False
    def create_atm(self):
      while not self.crisis:
            yield "$100"
hsbc = Bank() # when everything's ok the ATM gives you as much as you want
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.__next__())

print(corner_street_atm.__next__())
print([corner_street_atm.__next__() for cash in range(5)])

hsbc.crisis = True # crisis is coming, no more money!
print(corner_street_atm.__next__())
wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
print(corner_street_atm.__next__())
hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
print(corner_street_atm.__next__())
brand_new_atm = hsbc.create_atm() # build a new one to get back in business
for cash in brand_new_atm:
    print (cash)

