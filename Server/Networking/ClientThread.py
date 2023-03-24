import time
from threading import Thread
from Logic.Instances.Player import Player
from Server.Database.Manager import DBManager

clients = {}


class ClientThread(Thread):
    def __init__(self, client, address, msgfac) -> None:
        super().__init__()
        self.client = client
        self.address = address
        self.packets = msgfac
        self.player = Player()
        self.db = DBManager

    def recvall(self, length: int):
        data = b''
        while len(data) < length:
            s = self.client.recv(length)
            if not s:
                break
            data += s
        return data
    
    def log(self, text):
        print(f"({self.address[0]}) {text}")

    def run(self):
        if self.address[0] in clients:
            if(time.time() - clients[self.address[0]]) <= 5:
                self.log("[!!!]: Strange Connection Detected")
                self.client.close()
                return
            
        clients[self.address[0]] = time.time()
        self.player.address = self.address[0]
        self.db = self.db()
        try:
            while True:
                header = self.client.recv(7)
                if len(header) > 0:
                    last_packet = time.time()
                    id = int.from_bytes(header[:2], 'big')
                    length = int.from_bytes(header[2:5], 'big')
                    data = self.recvall(length)

                    if(id in self.packets):
                        self.log(f"[<<]: Packet ID: {id}")
                        message = self.packets[id](self.client, self.player, data)
                        message.decode()
                        message.process(self.db)
                    else:
                        self.log(f"Packet ID:{id} not handled")

                if time.time() - last_packet > 5:
                    self.CloseConnection()  

        except ConnectionAbortedError:
            self.CloseConnection()

        except ConnectionResetError:
            self.CloseConnection()

        except TimeoutError:
            self.CloseConnection()

        except WindowsError:
            pass

    def CloseConnection(self):
        try:       
            self.client.close()
            self.log(f"[-]: Player disconnected!")

        except Exception as e:
            print(e)