from Titan.Bytestream.main import Writer
from  os import urandom

class ServerHelloMessage(Writer):
    def __init__(self, client, player):
        self.id = 20100
        self.client = client
        self.player = player
    
    def encode(self):
        self.buffer = urandom(24)