import sys
import threading
import time
from tkinter import messagebox

from pynput.mouse import *
import keyboard

class Service:


    def __init__(self, entry_ms, entry_s):
        self.hotkey_id = "F1"
        self.basic_current_hotkey = None
        self.on_current_hotkey = None
        self.entry_ms = entry_ms
        self.entry_s = entry_s
        self.mouse = Controller()
        self.running = False
        self.click_thread = None

    # Save the input values
    def save_values(self):
        try:
            millisecond = int(self.entry_ms.get())
            second = int(self.entry_s.get())
            print(f"Millisecond: {millisecond}, Second: {second}")
        except ValueError:
            print("Please enter valid Numbers")

    # check if the inputs are right
    @staticmethod
    def validate_inputs(value):
        return value.isdigit() or value == ""

    # Autoclick Function
    def _autoclick_loop(self):
        # Runs until self.running == False
        while self.running:
            # Read the Values
            ms = int(self.entry_ms.get())
            s = int(self.entry_s.get())
            interval = s + ms / 1000.0

            # Start clicking
            self.mouse.click(Button.left)

            # Pause
            print("Click")
            time.sleep(interval)

    # Set Hotkey
    def setup_hotkey(self, new_hotkey=None, change=False):
        # if the window is clicked, set a new hotkey
        if change:
            messagebox.showinfo("Change Hotkey", "Press a new Hotkey")

            # window to set a new hotkey
            new_hotkey = keyboard.read_key()
            print(f"New Hotkey was set as: {new_hotkey}")

        # Delete the olf Hotkey, otherwise you got more than one hotkey
        if self.hotkey_id:
            try:
                keyboard.remove_hotkey(self.hotkey_id)
            except Exception as e:
                print(f"Error, while deleting the old Hotkey: {e}")
                
        
        # make the clicker work
        def toggle():
            if self.running:
                self.running = False
                print("Stop clicking")
            else:
                self.running = True
                print("Start clicking")
                if not self.click_thread or not self.click_thread.is_alive():
                    self.click_thread = threading.Thread(target=self._autoclick_loop, daemon=True)
                    self.click_thread.start()

        # set new hotkey
        keyboard.add_hotkey(new_hotkey or self.basic_current_hotkey, toggle)
        self.basic_current_hotkey = new_hotkey or self.basic_current_hotkey
        print(f"Hotkey '{self.basic_current_hotkey}' set")

        # Show after hotkey was changed
        if change:
            messagebox.showinfo("Nice", f"New Hotkey: '{self.basic_current_hotkey}'")
        if self.on_current_hotkey and self.basic_current_hotkey:
            self.on_current_hotkey(self.basic_current_hotkey)

    # Exit Function
    @staticmethod
    def exit_call():
        sys.exit()

