import datetime

class MonthlyBudget:
    def __init__(self,data,income,expenses,balance):
        self.date = data
        self.income = income
        self.expenses = expenses
        self.balance = balance
        
deposits = 100000
withdrawals = 25000
transfers = 35000
bill_electiricity = 6000
bill_water = 2500 
tax = 18000

expenses_ = withdrawals + transfers + bill_electiricity + bill_water + tax
blacnce_ = deposits - expenses_

budget_details = MonthlyBudget(datetime.date.today(), deposits, expenses_, blacnce_)

print()
print("Monthly Budget Summary")
print()
print('Date : ',budget_details.date)
print('Income : ',budget_details.income)
print('Expences : ',budget_details.expenses)
print('Current Balance : ',budget_details.balance)
