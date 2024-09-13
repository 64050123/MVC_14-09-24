from src.model.model import Model
from src.view.view import View
import threading

class Controller:
    def __init__(self):

        self.model = Model()
        self.view = View()

    def run(self):

        # Initial display of data (empty at the start)
        self.view.display_data(self.model.get_data())

        # Start the GUI in a separate thread
        gui_thread = threading.Thread(target=self.view.run_gui)
        gui_thread.start()

        # Terminal-based input loop
        while True:
            key = self.view.get_user_input("Enter a key (terminal): ")
            value = self.view.get_user_input("Enter a value (terminal): ")
            self.model.set_data(key, value)
            self.view.display_data(self.model.get_data())
