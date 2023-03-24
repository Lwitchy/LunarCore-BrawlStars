from Titan.Bytestream.main import Writer

class OwnHomeDataMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.version = 0
        self.client = client
        self.player = player
    
    def encode(self):
        # Write OwnHomeData yourself
        # If u need example like this
        # self.LogicDailyData()
        # Also if u wonder why I used functions instead of classes 
        # beacuse performance create new class for every player is slow I think
        pass

    def LogicDailyData(self):
        pass

    def LogicConfData(self):
        pass

    def ClientHome(self):
        pass

    def ClientAvatar(self):
        pass