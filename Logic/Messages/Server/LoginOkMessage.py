from Titan.Bytestream.main import Writer

class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20104
        self.version = 0
        self.client = client
        self.player = player
    
    def encode(self):
        # Account ID
        self.writeInt(self.player.high_id)
        self.writeInt(self.player.low_id)

        # Home ID
        self.writeInt(self.player.high_id)
        self.writeInt(self.player.low_id)

        self.writeString(self.player.token) # Pass Token
        self.writeString() # Facebook ID
        self.writeString() # Gamecenter ID

        self.writeInt(29) # Major Version
        self.writeInt(258) # Build
        self.writeInt(1) # Minor Version

        self.writeString("dev")  # Environment

        self.writeInt(0) # Session Count
        self.writeInt(0) # Play Time Seconds
        self.writeInt(0) # Days Since Started Playing

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeInt(0)

        self.writeString()

        self.writeString(self.player.region) # Region
        self.writeString()

        self.writeInt(1)

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeVInt(0)

        self.writeString()

        self.writeVInt(1)  