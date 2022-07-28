#!/usr/bin/env python3


# COMMENTS!!!!!


# here i am opening a list for monthly total. It's one of the only functions that will have to exist independently of a class
# ... I think.
monthly_income = []
monthly_bills = []
monthly_expenses = []

# bill will be the parent class to debts and expenses.


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
        # monthly_total.append(self.mnth_amt)

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
            principal = round((self.mnth_amt + extra) -
                              ((total * self.int_rate) / 12), 2)
            total = round(total - principal, 2)
            #print(total, " -- ", principal, " -- ", payments, "payments made.")
        print(payments, "\t", self.name, "\t",
              self.mnth_amt + extra, "\t", self.total_due)
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
        monthly_income.append(
            round(self.amount * ((52 / self.frequency) / 12), 2))

    def get_monthly_income(self):
        monthly_pay = 0
        monthly_pay = self.amount * ((52 / self.frequency) / 12)


def get_total(list_name):
    monthly_total = 0
    for item in list_name:
        monthly_total = monthly_total + item
    return monthly_total


rent = bill("rent", 1, 1189.00)
storage = bill("storage", 1, 80.00)
water = bill("water", 1, 80.00)
power = bill("power", 25, 135.00)
carins = bill("usaa insurance", 8, 126.00)
verph = bill("verizon phone", 23, 110.00)
googph = bill("google phones", 16, 80.00)
verint = bill("verizon fios", 28, 95.00)
netflix = bill("netflix", 16, 20.00)

snfvg = debt("S NFCU green", 10, 160.00, 7936.28, 16.9)
snfvb = debt("S NFCU blue", 14, 104.00, 5200.00, 13.24)
lnfmc = debt("L NFCU Master", 5, 279.00, 15032.92, 11.24)
lnfvb = debt("L NFCU Visa", 5, 113.00, 5941.90, 11.24)
spypl = debt("Seans paypal", 25, 75.50, 1809.73, 24.24)
lpypl = debt("laurie paypal", 25, 145.00, 4500.00, 24.24)
savings = debt("savings", 1, 0, 5000, 0.00)


#smokes = expense("cigarettes", 300.00)
smoke = expense("smoke", 100.00)
groceries = expense("food", 700.00)
formula = expense("formula", 150.00)
allowance = expense("elena allaowance", 40.00)


inmotion = income("InMotion Hosting", 2, 1900.00)
plasma = income("Octapharma", 0.5, 80.00)
#rigging = income("rigging", 4, 200.00)
#savings = debt("savings goal", 1, 0.0, 3000, 0.0)

savings.payoff_time(500)
snfvg.payoff_time(0)
snfvb.payoff_time(0)
lnfmc.payoff_time(0)
lnfvb.payoff_time(0)
spypl.payoff_time(0)
lpypl.payoff_time(0)
# savings.payoff_time(500)

print("total income is", get_total(monthly_income))
print("Total Bills", get_total(monthly_bills))
print(get_total(monthly_income) - get_total(monthly_bills), "left over.")
print("other expenses", get_total(monthly_expenses))
print("final", get_total(monthly_income) -
      get_total(monthly_bills) - get_total(monthly_expenses))
