import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




# Create another page frame
class DisplayExpensesDetailPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

       


    
    def update(self):

        for widgets in self.winfo_children():
            widgets.destroy()
         # Add a Label
        label = tk.Label(self, text="Expense Detail", font=("Helvetica", 24))
        label.grid(row=0, column=0, padx=10, pady=10)


        expenses = self.controller.get_dict()

        gridrow = 1
        ttk.Label(self, text="category" , font=("Helvetica", 14)).grid(row=gridrow, column=0, padx=10, pady=10)
        ttk.Label(self, text="amount" , font=("Helvetica", 14)).grid(row=gridrow, column=1, padx=10, pady=10)
        ttk.Label(self, text="description" , font=("Helvetica", 14)).grid(row=gridrow, column=2, padx=10, pady=10)

        gridrow = gridrow + 1


        for category in expenses.keys():
            for y in expenses[category]:
                amount = float(y["Amount"])
                description = y["Description"]
                ttk.Label(self, text=f"{category}:" , font=("Helvetica", 14)).grid(row=gridrow, column=0, padx=10, pady=10)
                ttk.Label(self, text=f"{amount}" , font=("Helvetica", 14)).grid(row=gridrow, column=1, padx=10, pady=10)
                ttk.Label(self, text=f"{description}" , font=("Helvetica", 14)).grid(row=gridrow, column=2, padx=10, pady=10)
                gridrow = gridrow + 1

        


        # Add a button to navigate back to the home page
        self.button = tk.Button(self, text="Back to Home Page",
                           command=lambda: self.controller.show_frame("HomePage"))
        self.button.grid(row=gridrow, columnspan=2, pady=20)