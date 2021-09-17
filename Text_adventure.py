import tkinter as tk
import actions as act
import predicates as pre
import simple_unlock_door_game
from Book import Book
from typing import Dict

def main():
    window = tk.Tk()
    # main window
    window.title = "Text Adventure"

    # This controls what is shown in the text box
    text_box_str = tk.StringVar()
    text_box_str.set("hello")
    text_box = tk.Label(window, textvariable=text_box_str)
    text_box.pack()

    # Holds all buttons
    buttons = tk.Frame(window)


    simple_book:Book = simple_unlock_door_game.this_book
    
    def update_window():
        for button in buttons.winfo_children():
            button.destroy()
        text_box_str.set(simple_book.get_text())

        print(len(simple_book.get_valid_options()))

        for option in simple_book.get_valid_options():
            def button_action_test(option_inner):
                simple_book.apply_option(option_inner)
                update_window()
            
            button = tk.Button(
                buttons, 
                command=lambda o=option: button_action_test(o),
                text=option.text
                )

            button.pack()
        buttons.pack()
        for name in simple_book.stats.keys():
            print(name, simple_book.stats[name])
        print("")
    update_window()
    window.mainloop()




if __name__ == "__main__":
    main()