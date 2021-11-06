import socket as ss
from random import choice
from threading import Thread
from string import ascii_letters
from time import sleep

class video():
    def __init__(self):
        self.client = dict()
        self.id = list()
        self.server = self.init_server_tcp()
        Thread(target=self.qnts_conectados).start()
        Thread(target=self.testando_conex).start()
        Thread(target=self.accept_client).start()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #  Iniciando funções do servidor #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def init_server_tcp(self):      
        tcp = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        tcp.bind((ss.gethostname(), 17723))
        tcp.listen(5)
        return tcp  

    def qnts_conectados(self):
        while True:
            print(f"{len(self.client.keys())} clientes conectados!")
            sleep(3)

    def testando_conex(self):
        while True:
            try:
                for i, cli in self.client.items():
                    try:
                        cli[0].send(bytes("$", "utf-8"))
                        sleep(3)
                    except Exception:
                        del self.client[i]
            except RuntimeError:
                print(self.client)
                print(f"{i} desconectado!")
                continue
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #  Aceitando e nomeando clientes #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def accept_client(self):
        while True:
            obj, dress = self.server.accept()
            print(f"cliente {dress[0]} conectado!")
            name = self.__get_name(obj)
            self.client[name] = [obj, dress, ""]

    
    def __get_name(self, obj):
        while True:
            name = self.__recv_data(obj)
            if name in self.client.keys():
                obj.send(bytes("nje", "utf-8"))
                continue
            else:
                obj.send(bytes("accept" ,"utf-8"))
                return name

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #  Estabelecendo conexão entre clientes  #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def conect_clients(self):
        id = self.__create_id()
        no_id = [names for names, cli in self.client.items() if len(cli[2]) != 0]
        print(no_id)
        
    def __create_id(self):
        while True:
            values = [["1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"], ascii_letters]
            abc = [choice(choice(values)) for _ in range(0, 9)]
            abc.insert(3, "-")
            abc.insert(7, "-")
            if not abc in self.id:
                return "".join(abc)  

    
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #  Receber dados do cliente  #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def __recv_data(self, obj):
        while True:
            data = obj.recv(100000)
            if data:
                return data.decode("utf-8")



video()