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


if __name__ == "__main__":
    App().mainloop()