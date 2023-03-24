from Logic.Instances.Player import Player
import sqlite3,json

class DBManager:
    def __init__(self) -> None:
        self.player_db = sqlite3.connect('db/players.db')
        self.chat_db = sqlite3.connect('db/chats.db')
        self.club_db = sqlite3.connect('db/clubs.db')
        self.banned_users_db = sqlite3.connect('db/banned_users.db')
        self.player_cursor = self.player_db.cursor()
        self.chat_cursor = self.chat_db.cursor()
        self.club_cursor = self.club_db.cursor()
        self.banned_cursor = self.banned_users_db.cursor()
        try:
            self.player_cursor.execute(f"CREATE TABLE IF NOT EXISTS main(high_id integer, low_id integer,auth text, data json)")
            self.club_cursor.execute(f"CREATE TABLE IF NOT EXISTS main(id integer, data json)")
            self.chat_cursor.execute(f"CREATE TABLE IF NOT EXISTS main(id integer, data json)")
            self.banned_cursor.execute(f"CREATE TABLE IF NOT EXISTS main(high_id integer, low_id integer, auth text, data json)")
        except Exception as e:
            print(e)


    def createPlayerAccount(self, hid, lid, token):
        player_data = {
            'high_id': Player.high_id,
            'low_id': Player.low_id,
            'token': Player.token,
            'name': Player.name,
            'name_set': Player.name_set,
            'trophies': Player.trophies,
            'high_trophies': Player.high_trophies,
            'collected_trophyroad': Player.collected_trophyroad,
            'exp_points': Player.exp_points,
            'thumbnail': Player.thumbnail,
            'name_color': Player.name_color,
            'region': Player.region,
            'unlocked_brawlers': Player.unlocked_brawlers,
            'unlocked_skins': Player.unlocked_skins,
            'unlocked_accessories': Player.unlocked_accessories,
            'unlocked_pins': Player.unlocked_pins,
            'selected_brawler': Player.selected_brawler,
            'brawler_newtags': Player.brawler_newtags,
            'selected_skins': Player.selected_skins,
            'selected_pins': Player.selected_pins,
            'selected_gadgets': Player.selected_gadgets,
            'selected_sp': Player.selected_sp,
            'brawlers_level': Player.brawlers_level,
            'brawlers_powerpoints': Player.brawlers_powerpoints,
            'brawlers_trophies': Player.brawlers_trophies,
            'brawlers_high_trophies': Player.brawlers_high_trophies
        }

        self.player_cursor.execute(f"INSERT INTO main(high_id, low_id, auth, data) VALUES(?,?,?,?)", (hid, lid, token, json.dumps(player_data, ensure_ascii=False)))
        self.player_db.commit()

    def loadPlayerAccount(self, hid, lid, tkn):
        try:
            self.player_cursor.execute("SELECT * from  main where high_id=? AND low_id=? AND auth=?", (hid, lid, tkn))
            loaded = self.player_cursor.fetchall()
            return json.loads(loaded[0][3])
        except:
            return None

    def updatePlayerData(self, hid, lid, tkn, item, value):
        self.player_cursor.execute("SELECT * from  main where high_id=? AND low_id=? AND auth=?", (hid, lid, tkn))
        loaded = self.player_cursor.fetchall()
        loaded = json.loads(loaded[0][3])
        loaded[item] = value
        self.player_cursor.execute("UPDATE main SET data=? WHERE high_id=? AND low_id=? AND auth=?", (json.dumps(loaded, ensure_ascii=False), hid, lid, tkn))
        self.player_db.commit()
        
    def updateAllPlayerData(self):
        pass

    def loadLastLowID(self):
        self.player_cursor.execute("SELECT MAX(low_id) from  main")
        id = self.player_cursor.fetchall()
        return id[0][0]

    def loadLastHighID(self):
        pass

    def loadLastClubID(self):
        pass

    def close(self):
        self.player_cursor.close()
        self.banned_cursor.close()
        self.chat_cursor.close()
        self.club_cursor.close()