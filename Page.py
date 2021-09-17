import tkinter as tk
from typing import List
from Option import Option

"""
This is one page of a book

"""
class Page:
    def __init__(self):
        self._options = []
        self._text = ""
        self._text_gen = None
    
    def set_text(self, text):
        self._text = text
        #self._text_gen = None

    def set_text_gen(self, func):
        self._text_gen = func

    def get_text(self, state) -> str:
        if ((self._text_gen == None)):
            return self._text
        else:
            print("here")
            return self._text_gen(state)


    def add_option(self, str, action, predicate, stats):
        option = Option(str, action, predicate, stats)
        self.add_option(option)
    
    def add_options(self, options: List[Option]):
        for option in options:
            self.add_option(option)
    
    def add_option(self, option):
        self._options.append(option)

    def show_state(self):
        self.text_box_var.set(self._text)
        for option in self._options:
            string_var = tk.StringVar()
            string_var.set(option.text)
            button = tk.Button(self.button_box, command=option.action, stringvarible=string_var)


