from Titan.Bytestream.main import Reader


class LogicPurchaseOfferCommand(Reader):
    def __init__(self, client, player, initial_bytes) -> None:
        super().__init__(initial_bytes)
        self.id = 519
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        pass