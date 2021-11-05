import socket as ss
from random import choice
from threading import Thread

class video():
    def __init__(self):
        self.client = dict()
        self.id = dict()
        self.server = self.init_server_tcp()
        Thread(target=self.accept_client).start()


    
    def init_server_tcp(self):      
        tcp = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        tcp.bind((ss.gethostname(), 14641))
        tcp.listen(5)
        tcp.send()
        return tcp  

    def accept_client(self):
        while True:
            obj, dress = self.server.accept()
            name = self.__get_name(obj)
            self.client[name] = [obj, dress]

    def conect_clients(self):
        id = self.__create_id(self.id.keys())
        for n in self.client.keys():
            for e in self.id.values():
                if not n in e[0]
        self.id[id] 

    @staticmethod
    def __create_id(lista):
        while True:
            values = [["1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"], ascii_letters]
            abc = [choice(choice(values)) for _ in range(0, 9)]
            abc.insert(3, "-")
            abc.insert(7, "-")
            if not abc in lista:
                return "".join(abc)  

    def __get_name(self, obj):
        while True:
            name = self.__recv_data(obj)
            if name in self.client.keys():
                obj.send(bytes("nje", "utf-8"))
                continue
            else:
                obj.send(bytes("accept" ,"utf-8"))
                return name

    def __recv_data(self, obj):
        while True:
            data = obj.recv(100000)
            if data:
                return data.decode("utf-8")



video()