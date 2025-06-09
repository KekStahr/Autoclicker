import tkinter as window
from tkinter import font
from service import Service

def create_gui():

    # Create the application window
    root = window.Tk()
    root.title("AutoClicker")
    root.geometry("300x300")
    custom_font = font.Font(family="Arial", size= 15)

    # Make a dynamic scale for a beautiful gui
    for i in range(5):  # row
        root.rowconfigure(i, weight=1)
    for i in range(3):  # column
        root.columnconfigure(i, weight=1)

    # Label for milliseconds
    window.Label(root, text="Milliseconds", font=custom_font).grid(row=1, column=2, sticky="s")
    entry_ms = window.Entry(root, font=custom_font, justify='center')
    entry_ms.grid(row=2, column=2, padx=10, sticky="n")
    entry_ms.insert(0, "100")#default value

    # Label for seconds
    window.Label(root, text="Seconds", font=custom_font).grid(row=1, column=1, sticky="s")
    entry_s = window.Entry(root, font=custom_font, justify='center')
    entry_s.grid(row=2, column=1, padx=10, sticky="n")
    entry_s.insert(0, "0") #default value

    # Insert the service with the entry
    svc = Service(entry_ms, entry_s)
    svc.setup_hotkey('F1')

    # Validate the Inputs
    validation = (root.register(Service.validate_inputs),'%P')
    entry_ms.configure(validate='key', validatecommand=validation)
    entry_s.configure(validate='key', validatecommand=validation)

    # Buttons
    frame_buttons = window.Frame(root)
    frame_buttons.grid(row=4, column=0, columnspan=3, pady=20)
    for i in range(2):
        frame_buttons.columnconfigure(i, weight=1)

    window.Button(frame_buttons, text="Save",command=svc.save_values,
                  font=custom_font).grid(row=1, column=1, padx=10, sticky="ew")          #Save Button

    window.Button(frame_buttons, text="Exit",command=svc.exit_call,
                  font=custom_font).grid(row=1, column=0, padx=10, sticky="ew")              #Exit Button

    # Show current Hotkey to start the Clicker
    hotkey_text = window.StringVar()
    hotkey_text.set(f"Change Hotkey (Current: F1)")

    # refresh the button
    def update_hotkey_label(new_key):
        hotkey_text.set(f"Change Hotkey (Current: {new_key})")

    # update the service function
    svc.on_current_hotkey = update_hotkey_label

    # Change the Button Name with the current Hotkey
    window.Button(frame_buttons, textvariable=hotkey_text,
                  command=lambda: svc.setup_hotkey(change=True),
                  font=custom_font).grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")

    # Start mit Default-Hotkey
    svc.setup_hotkey('F1')

    # Start the window
    root.mainloop()