import socket as ss
from random import choice
from threading import Thread
from string import ascii_letters
from time import sleep

class video():
    def __init__(self):
        self.client = dict()
        self.dict_id = dict()
        self.server = self.init_server_tcp()
        Thread(target=self.qnts_conectados).start()
        Thread(target=self.testando_conex).start()
        Thread(target=self.accept_client).start()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #  Iniciando funções do servidor #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def menu(self, name):
        while True:
            dt = self.__recv_data(self.client[name][0])
            if dt == "want":
                self.conect_clients(name)

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
            self.client[name] = [obj, dress]
            Thread(target=self.menu, args=[name,]).start()


    
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
    
    def conect_clients(self, name):
            obj = self.client[name][0]
            obj.send(bytes("wc", "utf-8"))
            conect = self.__recv_data(obj)
            if not conect in self.dict_id.values():
                if not conect in self.client.keys():
                    obj.send(bytes("Contato n encontrado!", "utf-8"))
                else:
                    obj.send(bytes("Pedido enviado!", "utf-8"))
                    obj_cli = self.client[conect][0]
                    obj_cli.send(f"{name} quer conectar!\n")
                    resposta = self.__recv_data(obj_cli)
                    if resposta == "conectar":
                        obj.send(bytes("Pedido aceito!", "utf-8"))
                    else:
                        obj.send(bytes("Conexao rejeitada!", "utf-8"))
                        
                    
                    self.dict_id[self.__create_id()] = [name, conect]
            else:
                obj.send(bytes("Ja esta em uma chamada", "utf-8"))

        
    def __create_id(self):
        while True:
            values = [["1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"], ascii_letters]
            abc = [choice(choice(values)) for _ in range(0, 9)]
            abc.insert(3, "-")
            abc.insert(7, "-")
            if not abc in self.dict_id.keys():
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