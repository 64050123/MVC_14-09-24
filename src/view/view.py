import tkinter as tk
from tkinter import simpledialog

class View:
    def __init__(self):
        """
        Initialize the GUI components using Tkinter.
        """
        # GUI Setup
        self.root = tk.Tk()
        self.root.title("MVC GUI")
        
        # Label for the GUI
        self.label = tk.Label(self.root, text="Python MVC GUI")
        self.label.pack(pady=10)
        
        # Text box to display data in the GUI
        self.text_box = tk.Text(self.root, height=10, width=40)
        self.text_box.pack(pady=10)

        # Button to trigger user input dialogs
        self.input_button = tk.Button(self.root, text="Enter Data", command=self.get_gui_input)
        self.input_button.pack(pady=5)

        # Dictionary to hold data entered via the GUI
        self.gui_data = {}

    def display_data(self, data):
        """
        Display data both in the terminal and in the GUI text box.
        """
        # Terminal output
        for key, value in data.items():
            print(f"{key}: {value}")

        # GUI output - clear the text box before displaying new data
        self.text_box.delete(1.0, tk.END)
        for key, value in data.items():
            self.text_box.insert(tk.END, f"{key}: {value}\n")

    def get_user_input(self, prompt):
        """
        Get user input from the terminal.
        """
        return input(prompt)

    def get_gui_input(self):
        """
        Get user input via GUI dialog boxes.
        """
        key = simpledialog.askstring("Input", "Enter a key:", parent=self.root)
        value = simpledialog.askstring("Input", "Enter a value:", parent=self.root)
        if key and value:
            # Store input in the GUI's data dictionary
            self.gui_data[key] = value
            # Display data in the GUI and terminal
            self.display_data(self.gui_data)

    def run_gui(self):
        """
        Run the Tkinter main loop to keep the GUI running.
        """
        self.root.mainloop()
