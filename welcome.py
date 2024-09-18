import tkinter as tk
from tkinter import ttk

# # Create the main window
# root = tk.Tk()
# root.title("Expense Tracker")
# root.geometry("400x400")
# # Create a label with "Hello, World!"
# label = tk.Label(root, text="Welcome to Expense Tracker!", font=("Helvetica", 16))
# label.pack(pady=20)

#  # Add a button to navigate to another page
# button = tk.Button(self, text="Go to Another Page",
#                     command=lambda: controller.show_frame("AnotherPage"))
# button.pack()

# # Start the application
# root.mainloop()

# Create the HomePage frame
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Add a Label
        label = ttk.Label(self, text="Welcome to Expense Tracker", font=("Helvetica", 24))
        label.grid(row=0, columnspan=2, pady=20)

        # Add a button to navigate to another page
        button = tk.Button(self, text="Input Expense",
                           command=lambda: controller.show_frame("InputExpensesPage"))
        button.grid(row=1, columnspan=2, pady=20)

        
         # Add a button to navigate to another page
        button = tk.Button(self, text="Display Expense Amount",
                           command=lambda: controller.show_frame("DisplayExpensesAmountPage"))
        button.grid(row=2, columnspan=2, pady=20)

         # Add a button to navigate to another page
        button = tk.Button(self, text="Display Category Expenses",
                           command=lambda: controller.show_frame("DisplayExpensesCategoryPage"))
        button.grid(row=3, columnspan=2, pady=20)



         # Add a button to navigate to another page
        button = tk.Button(self, text="Display Expenses Detail",
                           command=lambda: controller.show_frame("DisplayExpensesDetailPage"))
        button.grid(row=4, columnspan=2, pady=20)

