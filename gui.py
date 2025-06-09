import tkinter as window
from tkinter import *

#Create the application window
root = window.Tk()
root.title("AutoClicker")
root.geometry("500x500")


def create_gui():
    #Save the input values
    def save_values():
        millisecond = int(entry_millisecond.get())
        second = int(entry_second.get())
        print(f"Millisecond: {millisecond}, Second: {second}")

    #check if the inputs are right
    def validate_inputs(value):
        return value.isdigit() or value == ""

    vcmd = (root.register(validate_inputs), '%P')

    # Label for milliseconds
    label_millisecond = window.Label(root, text="Milliseconds")
    label_millisecond.grid(row = 1, column = 1, padx = 10)
    entry_millisecond = window.Entry(root, validate='key', validatecommand=vcmd)
    entry_millisecond.grid(row = 1, column = 1)

    # default for milliseconds
    entry_millisecond.insert(100, "100")

    # Label for seconds
    label_second = window.Label(root, text="Seconds")
    label_second.grid(row =1, column = 1, padx = 10)
    entry_second = window.Entry(root, validate='key', validatecommand=vcmd)
    entry_second.grid(row=1, column=1)

    # default for seconds
    entry_second.insert(0, "0")

    # Save the buttons
    save_button = window.Button(root, text="Save", command=save_values)
    save_button.grid(row=2, columnspan=2, pady=(20,10))


    # Start the window
    root.mainloop()