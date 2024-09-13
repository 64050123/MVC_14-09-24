class Model:
    def __init__(self):
        # Store key-value data
        self.data = {}

    def get_data(self):
        """
        Get the stored data.
        """
        return self.data

    def set_data(self, key, value):
        """
        Set a key-value pair in the data.
        """
        self.data[key] = value
