import matplotlib.pyplot as plt

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense Added Successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']} | Category: {expense['category']}")
    print()


def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: ₹{total}\n")


def show_graph():
    if not expenses:
        print("No data to display.\n")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct='%1.1f%%'
    )

    plt.title("Expense Distribution")
    plt.show()


while True:
    print("====== RUPAY TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        total_expense()

    elif choice == '4':
        show_graph()

    elif choice == '5':
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")