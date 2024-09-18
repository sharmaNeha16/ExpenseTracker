import tkinter as tk
from inputexpenses import InputExpensesPage
from welcome import HomePage
from display_expense_amount import DisplayExpensesAmountPage
from display_expense_category import DisplayExpensesCategoryPage
from display_expense_detail import DisplayExpensesDetailPage

# Create the main application class
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.expenses_dict = {
            "Food":  [],
            "Transport": [],
            "Entertainment": []
        }

        # Set the title and size of the window
        self.title("Tkinter Navigation Example")
        self.geometry("700x500")

        # Container for frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Dictionary to hold frames
        self.frames = {}

        # Create frames
        for F in (HomePage, InputExpensesPage,DisplayExpensesAmountPage,DisplayExpensesCategoryPage,DisplayExpensesDetailPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # Place the frame in the container
            frame.grid(row=0, column=0, sticky="nsew")
            

        # Show the first frame
        self.show_frame("HomePage")

     

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        if page_name == "DisplayExpensesAmountPage" or page_name == "DisplayExpensesCategoryPage" or page_name == "DisplayExpensesDetailPage":
            frame.update()
        frame.tkraise()

    def get_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        return frame


    def get_dict(self):
        return self.expenses_dict




# Main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()