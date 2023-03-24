from Titan.Bytestream.main import Writer


class AvailableServerCommand(Writer):
    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.id = 24111
        self.client = client
        self.player = player
        self.commandID = commandID
    def encode(self):
        if self.commandID in self.player.server_commands:
            self.writeVInt(self.commandID)
            self.player.server_commands[self.commandID].encode(self)