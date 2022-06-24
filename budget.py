#!/usr/bin/env python3 

import math as m
monthly_total = []
class bill:

    def __init__(self, name, due_date, mnth_amt):
        self.name = name
        self.due_date = due_date
        self.mnth_amt = mnth_amt 
        monthly_total.append(self.mnth_amt)

    def get_monthly(self):
        return self.mnth_amt

class debt(bill):
    def __init__(self, name, due_date, mnth_amt, total_due, int_rate):
        super().__init__(name, due_date, mnth_amt)
        self.total_due = float(total_due)
        self.int_rate = int_rate / 100
        monthly_total.append(self.mnth_amt)

    def get_intrest(self):
        intrest = (self.total_due * self.int_rate) / 12
        return intrest

    def get_principal(self):
        principal = self.mnth_amt - ((self.total_due * self.int_rate) / 12)
        return principal

    def after_payment(self):
        total = self.total_due - self.get_principal()
        return total

    def payoff_time(self):
        total = self.total_due
        payments = 0
        while total > 0:
            payments = payments + 1
            principal = round(self.mnth_amt - ((total * self.int_rate) / 12), 2)
            total = round(total - principal, 2)
        print(self.name,"has", payments, "payments at $",self.mnth_amt," per month")




class income:
    def __init__(self, name, amount, frequency):
        self.name = name
        self.amount = amount
        self.frequency = frequency

def get_monthly_total():
    total = 0.0
    for item in monthly_total:
        total = total + item
    return total

rent = bill("rent", 1, 1189.00)
storage = bill("storage", 1, 80.00)
water = bill("water", 1, 80.00)

snfvg = debt("Sean NFCU green", 10, 160.00, 7936.28, 16.9)
snfvb = debt("Sean NFCU blue", 14, 104.00, 5200.00, 13.24)
lnfmc = debt("Lauries NFCU MasterCard", 5, 279.00, 15032.92, 11.24)
lnfvb = debt("Lauries NFCU Visa", 5, 113.00, 5941.90, 11.24)

print(get_monthly_total())
