import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




# Create another page frame
class DisplayExpensesAmountPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

       
    
        # Add a Label
        label = ttk.Label(self, text="Total Expense Amount", font=("Helvetica", 24))
        label.grid(row=0, column=0, padx=10, pady=10)

      

        # Add a button to navigate back to the home page
        button = tk.Button(self, text="Back to Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button.grid(row=2, columnspan=2, pady=20)


    def update(self):
        expenses = self.controller.get_dict()

        sum = 0
        for category in expenses.values():
            for y in category:
                sum = sum + float(y["Amount"])
        

        self.label2 = ttk.Label(self, text=f"£ {sum}" , font=("Helvetica", 18))
        self.label2.grid(row=1, column=0, padx=10, pady=10)