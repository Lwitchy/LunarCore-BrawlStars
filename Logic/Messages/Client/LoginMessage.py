from Titan.Bytestream.main import Reader, Messaging
from Logic.Messages.Server.LoginOkMessage import LoginOkMessage
from Logic.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
import hashlib
import random
import time


class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.id = 10101
        self.client = client
        self.player = player

    def decode(self):
        self.high_id = self.readInt()
        self.low_id = self.readInt()
        self.token = self.readString()
        self.major = self.readInt()
        self.minor = self.readInt()
        self.build = self.readInt()


    def process(self,db):
        def generateToken():
            current_time = str(int(time.time()))
            random_num = str(random.random())
            token_str = current_time + random_num
            hashed_token = hashlib.sha1(token_str.encode('utf-8')).hexdigest()
            return hashed_token
            
        if self.low_id == 0:
            self.player.last_playerLowID += 1
            self.player.token = generateToken()
            self.player.low_id = self.player.last_playerLowID
            db.createPlayerAccount(self.player.high_id, self.player.low_id, self.player.token)
            # Login Message
            Messaging(self.client).send(LoginOkMessage(self.client, self.player))
            Messaging(self.client).send(OwnHomeDataMessage(self.client, self.player))            

        elif self.low_id != 0:
            self.player.high_id = self.high_id
            self.player.low_id = self.low_id
            self.player.token = self.token
            player_data = db.loadPlayerAccount(self.high_id, self.low_id, self.token)
            if player_data:
                self.loadPlayerData(player_data)
            else:
                print("Account not in database. Please clear data/cache")
            # Login Message
            Messaging(self.client).send(LoginOkMessage(self.client, self.player))
            Messaging(self.client).send(OwnHomeDataMessage(self.client, self.player))              

    def loadPlayerData(self, data):
        self.player.name = data['name']
        self.player.name_set = data['name_set']
        self.player.trophies = data['trophies']
        self.player.high_trophies = data['high_trophies']
        self.player.collected_trophyroad = data['collected_trophyroad']
        self.player.exp_points = data['exp_points']
        self.player.thumbnail = data['thumbnail']
        self.player.name_color = data['name_color']
        self.player.region = data['region']   
        self.player.unlocked_brawlers = data['unlocked_brawlers']     
        self.player.unlocked_skins = data['unlocked_skins']
        self.player.unlocked_accessories = data['unlocked_accessories']
        self.player.unlocked_pins = data['unlocked_pins']
        self.player.selected_brawler = data['selected_brawler']
        self.player.brawler_newtags = data['brawler_newtags']
        self.player.selected_skins = data['selected_skins']
        self.player.selected_pins = data['selected_pins']
        self.player.selected_gadgets = data['selected_gadgets']
        self.player.selected_sp = data['selected_sp']
        self.player.brawlers_level = data['brawlers_level']
        self.player.brawlers_powerpoints = data['brawlers_powerpoints']
        self.player.brawlers_trophies = data['brawlers_trophies']
        self.player.brawlers_high_trophies = data['brawlers_high_trophies']
        


    