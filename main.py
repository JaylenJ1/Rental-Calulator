class rentalIncome_Calculator():

  def rentalIncome(self, income, expenses, cashflow, cocr ):
    self.income = income
    self.expenses = expenses
    self.cashflow = cashflow
    self.cocr = cocr

  def calcuateIncome(self):
   laundry_income = int(input("Please enter the income amount for the Laundry: ")) 
   storage_income = int(input("Please enter the storage income amount: "))
   misc_income = int(input("Please enter the misc income amount: "))
   self.income = laundry_income + storage_income + misc_income
   print(f'Your total monthly income is ${self.income}.')

  def calculateExpenses(self):
    insurance = int(input("Enter insurace cost: "))
    sewer = int(input("Enter sewer/water cost: "))
    garbage = int(input("Enter garbage cost: "))
    hoa = int(input("Enter HOA Fee cost: "))
    lawn = int(input("Enter lawn/snow cost: "))
    vacancy = int(input("Enter vacancy cost: "))
    repairs = int(input("Enter repairs cost: "))
    prop= int(input("Enter Prop. Mgmt cost: "))
    mortage = int(input("Enter Mortage cost: "))

    self.expenses =(insurance + sewer + garbage + hoa + lawn + vacancy + repairs + prop + mortage )
    print(f'Your total mothly expenses will be ${self.expenses}.')
  
  def calculateCashflow(self):
    self.cashflow = self.income - self.expenses
    total_Cash_Flow = self.cashflow * 12
    print(f'Your total monthly cashflow will be ${self.cashflow}, your  annul cash flow will be ${total_Cash_Flow}.')

  
  def cashonCash(self):
    downpayment = int(input("Enter total downpayment: "))
    closing_cost = int(input("Enter total closing cost: "))
    rehab_budget = int(input("Enter total rehab_budget: "))
    misc = int(input("Enter total misc.: "))
    total_Investment = downpayment + closing_cost + rehab_budget + misc
    self.cocr = (self.cashflow / total_Investment) * 100
    print(f'Your Cash on Cash return is ${self.cocr}')



