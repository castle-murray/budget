#!/usr/bin/env python3 


## COMMENTS!!!!!

import math as m

## here i am opening a list for monthly total. It's one of the only functions that will have to exist independently of a class
## ... I think.

monthly_total = []

## bill will be the parent class to debts and expenses. They all share the
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

    def pay_extra(self, extra):
        self.mnth_amt = self.mnth_amt + extra
        monthly_total.append(extra)

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
            print(total, " -- ", principal, " -- ", payments, "payments made.")
        #print(self.name,"has", payments, "payments at $",self.mnth_amt," per month")
        print(payments * self.mnth_amt, "paid to pay off", self.total_due)




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

