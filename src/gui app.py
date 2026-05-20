import tkinter as tk
from typing import Any

class App(tk.Tk):
    def __init__(self, *args : Any, **kwargs : Any):
        super().__init__(*args, **kwargs)