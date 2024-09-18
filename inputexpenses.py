import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




# Create another page frame
class InputExpensesPage(tk.Frame):

    def display_result(entry1,entry2,entry3, controller):
        # Get the values from the input fields
        input1 = entry1.get()
        input2 = entry2.get()
        input3 = entry3.get()
        
        # Concatenate the inputs
        result = f"Expenses saved with input: {input1}, {input2}, {input3}"
        expenses = controller.get_dict()
        expenses[input2].append({
            "Amount" : input1,
            "Description": input3
        })

        expenses = controller.get_dict()
        sum = 0
        for category in expenses.values():
            for y in category:
                sum = sum + float(y["Amount"])

        # Show the result in a message box
        messagebox.showinfo("Result", result)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Add a Label
        label = tk.Label(self, text="Input Expenses", font=("Helvetica", 24))
        label.grid(row=0, column=0, padx=10, pady=10)


        # Create labels and entries for three inputs
        label1 = ttk.Label(self, text=" expense amount:")
        label1.grid(row=1, column=0, padx=10, pady=10)
        entry1 = ttk.Entry(self)
        entry1.grid(row=1, column=1, padx=10, pady=10)

        label2 = ttk.Label(self, text="expense category:")
        label2.grid(row=2, column=0, padx=10, pady=10)
        options = ["Food", "Transport", "Entertainment"]
        entry2 = ttk.Combobox(self, values=options)
        entry2.current(0)
        entry2.grid(row=2, column=1, padx=15, pady=10)
        #entry3.bind("<<ComboboxSelected>>", on_select)

        label3 = ttk.Label(self, text="description:")
        label3.grid(row=3, column=0, padx=10, pady=10)
        entry3 = ttk.Entry(self)
        entry3.grid(row=3, column=1, padx=10, pady=10)


        # Create a button to display the result
        submit_button = tk.Button(self, text="Submit", command=lambda: InputExpensesPage.display_result(entry1, entry2, entry3, controller))
        submit_button.grid(row=4, columnspan=2, pady=20)


        # Add a button to navigate back to the home page
        button = tk.Button(self, text="Back to Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button.grid(row=5, columnspan=2, pady=20)

    
