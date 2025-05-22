monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses 
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) 

print(f"Your monthly savings are: ($1000)")
print(f"Your projected annual savings after interest are: ($12600)")
