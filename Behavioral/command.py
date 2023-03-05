class MusicPlayer:
    def play(self):
        print("Music is playing...")

    def stop(self):
        print("Music is stopped.")

class Command:
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass

class PlayCommand(Command):
    def execute(self):
        self.receiver.play()

class StopCommand(Command):
    def execute(self):
        self.receiver.stop()

class Button:
    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()

player = MusicPlayer()
play_command = PlayCommand(player)
stop_command = StopCommand(player)

play_button = Button(play_command)
stop_button = Button(stop_command)

play_button.click()  # Output: Music is playing...
stop_button.click()  # Output: Music is stopped.
