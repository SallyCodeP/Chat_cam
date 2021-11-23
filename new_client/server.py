from os import O_BINARY
from threading import Thread
import net_configs as net
import socket as ss
from time import sleep 
from pyautogui import alert

class client():
    def __init__(self):

        # Client_name: [obj_socket, ip, port] 
        self.clients = {}

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
                obj.send(bytes("Nome em uso!", "utf-8"))
                continue

    # Receber dados de um ciente
    def recv(self, obj):
        while True:
            dt = obj.recv(1024)
            if dt:
                return dt.decode("utf-8")

    def menu(self, name, obj):
        while True:
            order = self.recv(obj)
            if order == "1":
                obj.send(bytes(self.send_client_name(name), "utf-8"))
            
            elif order == "2":
                pass
    
    def send_client_name(self, name):
        final = list()
        for c in self.clients.keys():
            if c != name:
                final.append(c)
        return "\\".join(final)




    



