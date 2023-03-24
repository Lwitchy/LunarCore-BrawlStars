from Titan.Bytestream.main import Writer

class LogicChangeAvatarNameMessage(Writer):
    def __init__(self):
        self.id = 201

    def encode(self):
        self.writeString(self.player.name)# Name
        self.writeVInt(0)# Name Cost