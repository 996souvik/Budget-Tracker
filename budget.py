#Create a Budget Planner system

#First we create a "BudgetPlaneer" Class
class Budgetplanner:
    def __init__(self):
        
        self.monthly_income = 0
        self.monthly_expenses = {}
        
    def add_income(self, income):
        self.monthly_income += income
        
    def add_expenses(self, category, amount):
        
        if category in self.monthly_expenses:
            self.monthly_expenses[category] += amount
        else:
            self.monthly_expenses[category] = amount
            
    def get_total_expenses(self):
        return sum(self.monthly_expenses.values())
    def get_balance(self):
        return self.monthly_income - self.get_total_expenses()
    def get_expenses_by_category(self):
        return self.monthly_expenses
    
    def reset_budget(self):
        
        self.monthly_income = 0
        self.monthly_expenses = {}
        
if __name__ == "__main__":
    planner = Budgetplanner()
    
    
    while True:
        print("\nPersonal Budget Planner")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. View Total Expenses")
        print("4. View balance")
        print("5. View Expenses By cetegory")
        print("6. Reset Budget")
        print("7. Quit")
        
        
        choice = input("Enter Your Choice: ")
        
        if choice == "1":
            
            income = float(input("Enter Income Amount: "))
            planner.add_income(income)
            print("Income Added Succesfully.")
            
        elif choice == "2":
            
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            planner.add_expenses(category, amount)
            print("Expanse added successfully. ")
            
        elif choice == "3":
            total_expenses = planner.get_total_expenses()
            print(f"Total Expenses: {total_expenses}")
            
        elif choice == "4":
            balance = planner.get_balance()
            print(f"Balance : {balance}")
            
        elif choice == "5":
            
            expenses_by_category = planner.get_expenses_by_category()
            print(f"Expenses by category: ")
            for category, amount in expenses_by_category.items():
                print(f"{category}: {amount}")
                
        elif choice == "6":
            
            planner.reset_budget()
            print("budget reset successfully. ")
            
        elif choice == "7":
            
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again")
            
            
        
        
            
    
    
    