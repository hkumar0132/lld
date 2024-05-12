class ConfigurationMemento:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width