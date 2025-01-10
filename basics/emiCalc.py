# Variables
EMI = 45000
annual_interest_rate = 0.09
monthly_interest_rate = annual_interest_rate / 12
loan_tenure_months = 20 * 12

# Formula Calculation
loan_amount = (EMI * ((1 + monthly_interest_rate)**loan_tenure_months - 1)) / (monthly_interest_rate * (1 + monthly_interest_rate)**loan_tenure_months)

print("Eligible Loan Amount: ₹{:.2f}".format(loan_amount))
