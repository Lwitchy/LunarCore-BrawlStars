from Titan.Bytestream.main import Reader, Messaging
from Logic.Messages.Server.ServerHelloMessage import ServerHelloMessage

class ClientHelloMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)        
        self.id = 10100
        self.client = client
        self.player = player

    def decode(self):
        self.Protocol = self.readInt()
        self.KeyVersion = self.readInt()
        self.Major = self.readInt()
        self.Minor = self.readInt()
        self.Build = self.readInt()
        self.ContentHash = self.readString()
        self.DeviceType = self.readInt()
        self.AppStore = self.readInt()

    def process(self, db):
        Messaging(self.client).send(ServerHelloMessage(self.client, self.player))