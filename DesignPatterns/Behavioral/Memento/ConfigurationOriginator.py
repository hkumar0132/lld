from ConfigurationMemento import ConfigurationMemento

class ConfigurationOriginator:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def create_memento(self) -> ConfigurationMemento:
        return ConfigurationMemento(self.height, self.width)
    
    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def restore_memento(self, memento: ConfigurationMemento):
        self.height = memento.height
        self.width = memento.width