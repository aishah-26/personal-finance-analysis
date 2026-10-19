import matplotlib.pyplot as plt 

print("Welcome to Personal Finance Analysis!")

income=2500
expenses=1800
savings=income - expenses

print("Monthly income: £", income)
print("Monthly expenses: £", expenses)
print("Monthly savings: £", savings)

savings_rate= (savings/income)*100
print("Savings rate:", savings_rate, "%")

def calculate_savings(income, expenses):
    return income-expenses 

monthly_savings= calculate_savings(2500, 2000)
print("Updated monthly savings: £", monthly_savings)

# Anonymised monthly transactions 

transactions = [ 
    {"category": "Food", "amount": 250}, 
    {"category": "Transport", "amount":90},
    {"category": "Shopping", "amount": 120},
    {"category": "Food", "amount":80},
    {"category": "Bills", "amount":150},
    {"category": "Transport", "amount": 40},
    {"category": "Entertainment", "amount": 60},
]

#Calculate total spending 
total_spending=0

for transaction in transactions:
    total_spending += transaction["amount"]

print("\n--- Monthly Expenses Analysis ---")
print("Total spending: £", total_spending)

# Calculate spending by category

spending_by_category = {}

for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]

    if category in spending_by_category:
        spending_by_category[category] += amount 
    else:
        spending_by_category[category] = amount 

print("\n--- Spending by Category ---")

for category, amount in spending_by_category.items():
    print(f"{category}: £{amount}")

#calculate percentage of total spending by category 
print("\n--- Spending Percentages---")

for category, amount in spending_by_category.items():
    percentage = (amount/total_spending)*100
    print(f"{category}: {percentage:.2f}%")

#identify the highest spending category 

highest_category = max(spending_by_category, key=spending_by_category.get)
print("\n--- Highest Spending Category---")
print(f"Your highest spending category is {highest_category}, "
      f"at £{spending_by_category[highest_category]}.")

# Create a bar chart of spending by category 


# Create a professional bar chart of spending by category
categories = list(spending_by_category.keys())
amounts = list(spending_by_category.values())

plt.figure(figsize=(9, 6))
bars = plt.bar(categories, amounts)

plt.title("Monthly Spending by Category", fontsize=16)
plt.xlabel("Spending Category")
plt.ylabel("Amount (£)")

# Display the amount above each bar
for bar in bars:
    amount = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        amount,
        f"£{amount}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("spending_by_category.png", dpi=300, bbox_inches="tight")
plt.show()

print("Chart saved as spending_by_category.png")

