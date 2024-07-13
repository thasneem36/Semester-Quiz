import datetime

class MonthlyBudget:
    date = None
    income = 0
    expenses = 0
    blacnce = 0
        
deposits = 100000
withdrawals = 25000
transfers = 35000
electiricity = 6000
water = 2500 
tax = 18000

expenses_ = withdrawals + transfers + electiricity + water + tax
blacnce_ = deposits - expenses_

budget = MonthlyBudget()
budget.date = datetime.date.today()
budget.income = deposits
budget.expenses = expenses_
budget.blacnce = blacnce_

print("Monthly Budget Summary")
print('Date : ',budget.date)
print('Income : ',budget.income)
print('Expences : ',budget.expenses)
print('Current Balance : ',budget.blacnce)