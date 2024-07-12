# mange the monthly budget
# inputs deposits, withdrawals, money transfers, bill payments, and tax payments
# output  income, expenses, and balance

import datetime

class MonthlyBudget:

    def __init__(self,data,incom,expenses,balance):
        self.date = data
        self.income = incom
        self.expenses = expenses
        self.balance = balance


deposits = 100000
withdrawals = 2500
transfers = 35000
bill = 6000 + 2500
tax = 18000

#culculat the balance and expenses
blacnce_ = deposits-(withdrawals + transfers + bill + tax)
expenses_ = withdrawals + transfers + bill + tax

#start the clz add the addribut 
budget_details = MonthlyBudget(datetime.date.today(), deposits, expenses_, blacnce_)

# output summary
print("Monthly Budget Summary")
print('Date : ',budget_details.date)
print('Income : ',budget_details.income)
print('Expences : ',budget_details.expenses)
print('Current Balance : ',budget_details.balance)