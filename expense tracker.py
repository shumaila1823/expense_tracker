import json
import os
from prettytable import PrettyTable

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    
    expenses = load_expenses()
    expenses.append({
        'title': title,
        'amount': amount,
        'category': category
    })
    save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    table = PrettyTable()
    table.field_names = ["Title", "Amount", "Category"]
    total = 0
    for exp in expenses:
        table.add_row([exp['title'], f"${exp['amount']:.2f}", exp['category']])
        total += exp['amount']
    
    print(table)
    print(f"Total Expenses: ${total:.2f}")

def search_by_category():
    category = input("Enter category to search: ")
    expenses = load_expenses()
    filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    
    if not filtered:
        print(f"No expenses found in category '{category}'.")
        return
    
    table = PrettyTable()
    table.field_names = ["Title", "Amount", "Category"]
    for exp in filtered:
        table.add_row([exp['title'], f"${exp['amount']:.2f}", exp['category']])
    
    print(table)

def main_menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_by_category()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
