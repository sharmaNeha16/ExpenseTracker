import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




# Create another page frame
class DisplayExpensesCategoryPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Add a Label
        label = tk.Label(self, text="Total Expense Category", font=("Helvetica", 24))
        label.grid(row=0, column=0, padx=10, pady=10)


        # Add a button to navigate back to the home page
        button = tk.Button(self, text="Back to Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button.grid(row=5, columnspan=2, pady=20)

    
    def update(self):
        expenses = self.controller.get_dict()

        gridrow = 1
        for category in expenses.keys():
            sum = 0
            ttk.Label(self, text=f"{category}:" , font=("Helvetica", 18)).grid(row=gridrow, column=0, padx=10, pady=10)

            for y in expenses[category]:
                sum = sum + float(y["Amount"])

            ttk.Label(self, text=f"{sum}" , font=("Helvetica", 18)).grid(row=gridrow, column=1, padx=10, pady=10)
            gridrow = gridrow + 1

        