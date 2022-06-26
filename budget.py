#!/usr/bin/env python3 


## COMMENTS!!!!!


## here i am opening a list for monthly total. It's one of the only functions that will have to exist independently of a class
## ... I think.
monthly_income = []
monthly_bills = []
monthly_expenses = []

## bill will be the parent class to debts and expenses. 
class bill: 

    def __init__(self, name, due_date, mnth_amt):
        self.name = name
        self.due_date = due_date
        self.mnth_amt = mnth_amt 
        monthly_bills.append(self.mnth_amt)

    def get_monthly(self):
        return self.mnth_amt

class debt(bill):
    def __init__(self, name, due_date, mnth_amt, total_due, int_rate):
        super().__init__(name, due_date, mnth_amt)
        self.total_due = float(total_due)
        self.int_rate = int_rate / 100
        ##monthly_total.append(self.mnth_amt)

    def pay_extra(self, extra):
        self.mnth_amt = self.mnth_amt + extra
        monthly_bills.append(extra)

    def get_intrest(self):
        intrest = (self.total_due * self.int_rate) / 12
        return intrest

    def get_principal(self):
        principal = self.mnth_amt - ((self.total_due * self.int_rate) / 12)
        return principal

    def after_payment(self):
        total = self.total_due - self.get_principal()
        return total

    def payoff_time(self, extra):
        total = self.total_due
        monthly_bills.append(extra)
        payments = 0
        while total > 0:
            payments = payments + 1
            principal = round((self.mnth_amt + extra) - ((total * self.int_rate) / 12), 2)
            total = round(total - principal, 2)
            #print(total, " -- ", principal, " -- ", payments, "payments made.")
        print(payments, "\t", self.name, "\t", self.mnth_amt + extra, "\t", self.total_due)
       # print(self.name,"has", payments, "payments at $",self.mnth_amt," per month")
       # print(payments * self.mnth_amt, "paid to pay off", self.total_due)


class expense(bill):
    def __init__(self, name, mnth_amt):
        self.name = name
        self.mnth_amt = mnth_amt
        monthly_expenses.append(round(mnth_amt, 2))

class income:
    def __init__(self, name, frequency, amount):
        self.name = name
        self.amount = amount
        self.frequency = frequency
        monthly_income.append(round(self.amount * ((52 / self.frequency) / 12), 2))

    def get_monthly_income(self):
        monthly_pay = 0
        monthly_pay = self.amount * ((52 / self.frequency) / 12)

def get_total(list_name):
    monthly_total = 0
    for item in list_name:
        monthly_total = monthly_total + item
    return monthly_total

