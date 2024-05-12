from ConfigurationOriginator import ConfigurationOriginator
from ConfigurationMemento import ConfigurationMemento
from Caretaker import Caretaker

class Client:

    caretaker = Caretaker()

    originator = ConfigurationOriginator(10, 20)
    memento : ConfigurationMemento = originator.create_memento()
    caretaker.add_memento(memento)

    originator.set_height(30)
    originator.set_width(40)
    memento : ConfigurationMemento = originator.create_memento()
    caretaker.add_memento(memento)

    originator.set_height(15)
    originator.set_width(35)  
    memento : ConfigurationMemento = originator.create_memento()
    caretaker.add_memento(memento)

    # current_memento : ConfigurationMemento = caretaker.undo()
    # originator.restore_memento(current_memento)

    # current_memento : ConfigurationMemento = caretaker.undo()
    # originator.restore_memento(current_memento)

    # current_memento : ConfigurationMemento = caretaker.undo()
    # if (current_memento):
    #     originator.restore_memento(current_memento)

    print("HEIGHT: ", originator.height, originator.width)

