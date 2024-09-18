
import tkinter as tk
from tkinter import ttk

def create_tab1(parent):
    """Creates the first tab."""
    frame = ttk.Frame(parent)
    label = ttk.Label(frame, text="This is Tab 1")
    label.pack(padx=10, pady=10)

    # Add more widgets for tab 1 here
    entry1 = ttk.Entry(frame)
    entry1.pack(padx=10, pady=10)
    

    return frame

def create_tab2(parent):
    """Creates the second tab."""
    frame = ttk.Frame(parent)
    label = ttk.Label(frame, text="The total amount spent is £40")
    label.pack(padx=10, pady=10)

    # Add more widgets for tab 2 here
    entry2 = ttk.Entry(frame)
    entry2.pack(padx=10, pady=10)
    

    return frame

def create_tab3(parent):
    """Creates the third tab."""
    frame = ttk.Frame(parent)
    label = ttk.Label(frame, text="This is Tab 3")
    label.pack(padx=10, pady=10)

    # Add more widgets for tab 3 here
    entry3 = ttk.Entry(frame)
    entry3.pack(padx=10, pady=10)

    #button3 = ttk.Button(frame, text="Submit", command=lambda: print("Tab 3 Entry:", entry3.get()))
    #button3.pack(padx=10, pady=10)

    return frame

# Main application window
root = tk.Tk()
root.title("Multi-Tab Tkinter Application")

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Create tabs and add them to the Notebook
tab1 = create_tab1(notebook)
tab2 = create_tab2(notebook)
tab3 = create_tab3(notebook)

# Add tabs to the Notebook
notebook.add(tab1, text="Total amount spent")
notebook.add(tab2, text="Total amount spent in each category.")
notebook.add(tab3, text="List of all expenses")

# Pack the Notebook widget
notebook.pack(expand=True, fill='both')

# Start the Tkinter event loop
root.mainloop()





# Create another page frame
class InputExpensesPage(tk.Frame):

    def create_tab1(parent):
        """Creates the first tab."""
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text="This is Tab 1")
        label.pack(padx=10, pady=10)

        # Add more widgets for tab 1 here
        entry1 = ttk.Entry(frame)
        entry1.pack(padx=10, pady=10)
        
        return frame

    def create_tab2(parent):
        """Creates the second tab."""
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text="The total amount spent is £40")
        label.pack(padx=10, pady=10)

        # Add more widgets for tab 2 here
        entry2 = ttk.Entry(frame)
        entry2.pack(padx=10, pady=10)       

        return frame

    def create_tab3(parent):
        """Creates the third tab."""
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text="This is Tab 3")
        label.pack(padx=10, pady=10)

        # Add more widgets for tab 3 here
        entry3 = ttk.Entry(frame)
        entry3.pack(padx=10, pady=10)

        #button3 = ttk.Button(frame, text="Submit", command=lambda: print("Tab 3 Entry:", entry3.get()))
        #button3.pack(padx=10, pady=10)

        return frame

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        
        # Create a Notebook widget
        notebook = ttk.Notebook(root)

        # Create tabs and add them to the Notebook
        tab1 = create_tab1(notebook)
        tab2 = create_tab2(notebook)
        tab3 = create_tab3(notebook)

        # Add tabs to the Notebook
        notebook.add(tab1, text="Total amount spent")
        notebook.add(tab2, text="Total amount spent in each category.")
        notebook.add(tab3, text="List of all expenses")

        # Pack the Notebook widget
        notebook.grid(row=0, column=0, padx=10, pady=10)


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
        submit_button = tk.Button(self, text="Submit", command=lambda: InputExpensesPage.display_result(entry1, entry2, entry3))
        submit_button.grid(row=4, columnspan=2, pady=20)


        # Add a button to navigate back to the home page
        button = tk.Button(self, text="Back to Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button.grid(row=5, columnspan=2, pady=20)
