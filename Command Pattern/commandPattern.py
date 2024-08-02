#•	Command Interface 
class Command:
    def execute(self):
        pass
    
#Concrete Command 
class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy()

#Reciever
class Editor:
    def copy(self):
        print("Text copied")

#	Invoker:
class Button:
    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()

#Client 
editor = Editor()
copyCommand = CopyCommand(editor)
button = Button(copyCommand)
button.click()  # Output: Text copied
