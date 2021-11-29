from threading import Thread
import socket as ss
from time import sleep 
from pyautogui import alert
from string import ascii_letters
from random import choice

class client():
    def __init__(self):

        # Client_name: [obj_socket, ip, port] 
        self.clients = {}
        self.rooms = {}

        self.obj = self.init_tcp()

        
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
        #       Iniciando Threads do servidor        #
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
        Thread(target=self.testando_conex).start()
        Thread(target=self.accept_clients).start()


    # Iniciando servidor tcp ip
    def init_tcp(self):
        server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        server.bind((ss.gethostname, 34543))
        server.listen(5)
        return server

    # Testando a conexao dos cliente com o servidors
    def testando_conex(self):
        while True:
            try:
                for i, cli in self.client.items():
                    try:
                        cli[0].send(bytes("$", "utf-8"))
                        sleep(3)
                    except Exception:
                        Thread(target = self.desconect, args= [i,]).start()
            except RuntimeError:
                continue
    
    # Desconectando clientes
    def desconect(self, name):
        del self.client[name]
        alert(f"cliente: {name} desconectado!")

    # Aceitando clientes
    def accept_clients(self):
        while True:
            obj, dress = self.obj.accept()
            Thread(target=self.cadastrar, args = [obj, dress]).start()

    # Cadastrando clientes
    def cadastrar(self, obj, dress):
        obj.send(bytes("Conectado", "utf-8"))
        while True:
            name = self.recv(obj)
            if not name in self.clients:
                self.clients[name] = [obj, dress[0], dress[1]]
                obj.send(bytes("Cadastrado", "utf-8"))
                self.menu(name, obj)
            else:
                obj.send(bytes("Neu", "utf-8"))
                continue

    # Receber dados de um ciente
    def recv(self, obj):
        while True:
            dt = obj.recv(1024)
            if dt:
                return dt.decode("utf-8")

    # Menu do servidor para receber requests do cliente
    def menu(self, name, obj):
        while True:
            order = self.recv(obj)
            if order == "1":
                obj.send(bytes(self.send_client_name(name), "utf-8"))
            
            elif order == "2":
                self.connect_clientes(name, obj)
    
    # Enviando todos os clientes online no servidor 
    def send_client_name(self, name):
        final = list()
        for c in self.clients.keys():
            if c != name:
                final.append(c)
        return "\\".join(final)

    # Conectado dois clientes
    def connect_clientes(self, name, obj):
        # Enviando pedido de escolha do contato
        obj.send(bytes("cln", "utf-8"))
        resp = self.recv(obj)

        # Conferindo se o nome nao e o do proprio cliente
        # Conferindo se o cliente existe no programa
        if resp == name or not resp in self.clients.keys():
            obj.send(bytes("name_err", "utf-8"))
        else:
            # Conferindo se o cliente ja esta conectado em call ou nao
            for e in self.rooms.values():
                if resp in e:
                    # Se o cliente ja estiver conectado o funcao acaba
                    obj.send(bytes("Client_in_call", "utf-8"))
                    return 
            
            # Se o cliente nao estiver conectado em uma call a func continua daqui
            # Enviando pedido de entrada de call
            contact_obj = self.clients[resp][0]
            contact_obj.send(bytes(f"connect_{name}","utf-8"))

            # avisando que o pedido foi enviado
            obj.send(bytes("penv", "utf-8"))

            # Recebendo resposta do chamada pra call
            fn_answer = self.recv(contact_obj)

            # Conferindo se a conexao foi aceita ou rejeitada
            if fn_answer == "yeap":
                # Conexao aceita 
                contact_obj.send(bytes(self.clients[resp][1], "utf-8"))

                # Conferindo se a conexao foi iniciada
                if self.recv(obj) == "conction_accept":
                    self.rooms[self.__create_id] = [name, resp]

            else:
                # Avisando que a conexao foi rejeitada
                obj.send(bytes(f"cr_{resp}", "utf-8"))
    
    # Criando id das calls
    def __create_id(self):
        while True:
            values = [["1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"], ascii_letters]
            abc = [choice(choice(values)) for _ in range(0, 9)]
            abc.insert(3, "-")
            abc.insert(7, "-")
            if not abc in self.rooms.keys():
                return "".join(abc)  



    



