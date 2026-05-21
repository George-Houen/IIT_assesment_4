import tkinter as tk
from typing import Any
from config import (
    HEADER,
    SUB_HEADER
)

class App(tk.Tk):
    def __init__(self, *args : Any, **kwargs : Any):
        super().__init__(*args, **kwargs)

        #setup:
        self.title("IIT assignment 4 - u3324971")
        self.geometry("500x500")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.header = tk.Frame(self, relief="raised", border=2)
        self.header.grid(row=0, column=0, sticky="nsew")
        tk.Label(self.header, text="IIT assignment 4", **HEADER).grid(column=0, row=0, sticky="w")
        tk.Label(self.header, text="u3324971", **SUB_HEADER).grid(column=0, row=1, sticky="w")

        self.body = tk.Frame(self)
        self.body.grid(row=1, column=0)

        #entry feilds etc:

        self.in_var_loan_amount = tk.StringVar(self, "")
        self.in_var_interest_rate = tk.StringVar(self, "")
        self.in_var_loan_term = tk.StringVar(self, "")
        self.in_var_monthly_income = tk.StringVar(self, "")
        self.in_var_monthly_expenses = tk.StringVar(self, "")

        tk.Label(self.body, text="loan amount").grid(column= 0, row=0)
        tk.Label(self.body, text="interest rate").grid(column= 0, row=1)
        tk.Label(self.body, text="loan term").grid(column= 0, row=2)
        tk.Label(self.body, text="monthly income").grid(column= 0, row=3)
        tk.Label(self.body, text="monthly expenses").grid(column= 0, row=4)

        tk.Entry(self.body, textvariable=self.in_var_loan_amount).grid(column= 1, row=0)
        tk.Entry(self.body, textvariable=self.in_var_interest_rate).grid(column= 1, row=1)
        tk.Entry(self.body, textvariable=self.in_var_loan_term).grid(column= 1, row=2)
        tk.Entry(self.body, textvariable=self.in_var_monthly_income).grid(column= 1, row=3)
        tk.Entry(self.body, textvariable=self.in_var_monthly_expenses).grid(column= 1, row=4)

        tk.Button(self.body, text="calculate", command=self.calc_pipeline).grid(column=0, row=5, columnspan=2)

    def calc_pipeline(self):
        self.get_user_input_values()

    def get_user_input_values(self) -> dict[str, float] | None:
        """retreive input values from entry feilds and check them

        Returns:
            dict[str, float] | None: values for each entry feild input, None if error
        """
        feilds = {
            "loan_amount" : self.in_var_loan_amount,
            "interest_rate" : self.in_var_interest_rate,
            "monthly_expenses" : self.in_var_monthly_expenses,
            "loan_term" : self.in_var_loan_term,
            "monthly_income" : self.in_var_monthly_income
        }

        values : dict[str, float] = {}

        for k, v in feilds.items():
            try:
                values[k] = float(v.get())
            except ValueError:
                print(f"please enter {k} as a valid number")
                return None
        return values
        

        


if __name__ == "__main__":
    App().mainloop()