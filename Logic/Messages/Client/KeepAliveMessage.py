from Titan.Bytestream.main import Reader, Messaging


class KeepAliveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.id = 0
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self, db):
        pass