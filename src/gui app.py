import tkinter as tk
from typing import Any
from config import (
    HEADER_FONT
)

class App(tk.Tk):
    def __init__(self, *args : Any, **kwargs : Any):
        super().__init__(*args, **kwargs)

        #setup:
        self.title("IIT assignment 4 - u3324971")
        self.geometry("500x500")

        self.header = tk.Frame(self)
        self.header.grid(row=0, column=0)
        tk.Label(self.header, text="IIT assignment 4", font=HEADER_FONT).grid(column=0, row=0)
        tk.Label(self.header, text="u3324971").grid(column=0, row=1)


if __name__ == "__main__":
    App().mainloop()