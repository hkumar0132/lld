from Command import ICommand

class RemoteController:

    def set_command(self, command: ICommand):
        self.command = command

    def press_button(self):
        self.command.execute()
