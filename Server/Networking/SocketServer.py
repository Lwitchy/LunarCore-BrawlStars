import socket
from Server.Networking.ClientThread import ClientThread
from Logic.Messages.LogicMessageFactory import packets
from Logic.Commands.LogicCommandManager import server_commands, client_commands, loadClientCommands, loadServerCommands
from Logic.Instances.Player import Player
from Server.CSVReader.Reader import CSVReader
from Server.Database.Manager import DBManager
from Server.Helpers.Load import Loader
from threading import *

class SocketServer:
    def __init__(self) -> None:
        self.ip = "0.0.0.0"
        self.port = 9339
        self.server = socket.socket()
        self.logic_messagefactory = packets
        self.db = DBManager
        

    def bind(self):
        Player.last_playerLowID = None

        # Load Data to ram before start server
        self.db = self.db()
        try:
            Player.last_playerLowID = self.db.loadLastLowID()
        except Exception as e:
            print(e)
        self.db.close()

        if Player.last_playerLowID == None:
            Player.last_playerLowID = 0


        # Load Commands
        loadServerCommands()
        loadClientCommands()
        Player.server_commands = server_commands
        Player.client_commands = client_commands
        # Load Commands End

        Loader.init(self, Player, CSVReader)
        
        # Update Some Data and Start Threads
        Player.updateData()
        # Start Second Thread
        #EventRotation(Player).start()

        # Start Server
        self.server.bind((self.ip, self.port))
        print(f"""
Server Listening From Port: {self.port}""")

        while True:
            self.server.listen()
            client,address = self.server.accept()
            print(f"[+] Player Connected! ({address[0]})")
            ClientThread(client, address, self.logic_messagefactory).start()     
            #NetworkFilter().checkConnection(client, address, connect_time, connect_tries, self.clients, self.client_info, self.logic_messagefactory)