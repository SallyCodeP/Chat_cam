import pygame as gg
import cv2 as cv
import socket as ss
from threading import Thread
from random import randint
from pyautogui import confirm, alert

class client:
    def __init__(self):
        self.cliente_tcp = self.init_client_tcp()
        self.name = self.put_name()
        Thread(target=self.recv_invite).start()
        while True:
            querer = input("Pedir conexao (1) -> ")
            if querer == "1":
                self.pedir_conex()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Funções entre cliente e servidor tcp #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def init_client_tcp(self):
        '''Iniciando cliente do servidor tcp'''
        cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        cliente.bind((ss.gethostname(), randint(10000, 60000)))
        cliente.connect((ss.gethostname(), 17723))
        return cliente
    
    def recv_tcp_data(self):
        '''Receber dados do server tcp'''
        while True:
            data = self.cliente_tcp.recv(10000)
            if data:
                decode_data = data.decode("utf-8")
                if decode_data != "$":
                    return decode_data

    def put_name(self):
        '''Registrando nome do cliente no servidor'''
        while True:
            my_name = input("Name ---> ")
            if self.send(my_name):
                data = self.recv_tcp_data()
                if data == "accept":
                    print("Confirmado")
                    return my_name
                elif data == "nje":
                    print("Esse nome já existe!")
                    continue
                else:
                    continue
            else:
                continue

    def pedir_conex(self):
        self.cliente_tcp.send(bytes("want", "utf-8"))
        dado = self.recv_tcp_data()
        if dado == "wc":
            while True:
                resposta = input("Qual cliente você gostaria de se conectar? -> ")
                if self.send(resposta):
                    resposta = self.recv_tcp_data()
                    print(resposta)
                    if resposta == "Pedido enviado!":
                        resposta2 = self.recv_tcp_data()
                        print(resposta2)

                        if resposta2 == "Pedido aceito!":
                            pass
                            break
                    elif resposta == "Voce nao pode se conectar com vc msm!":
                        break
                        
                else:
                    continue

    def qnts_clientes(self):
        self.cliente_tcp.send(bytes("qntscli", "utf-8"))
        qnts = self.recv_tcp_data()
        qnts = qnts.split("\n")
        if len(qnts) > 0: 
            print(qnts)
        else:
            print("Apenas você está conectado!")

    def recv_invite(self):
        while True:
            invite = self.recv_tcp_data()
            if "invite quer conectar!\n" in invite:
                resposta = confirm(text=invite, title='conectar', buttons=['Conectar', 'Recusar'])
                self.cliente_tcp.send(bytes(resposta, "utf-8"))
                continue

    def send(self, msg):
        if "\\" in msg or "$" in msg:
           alert("Ha um caracter invalido na menssagem") 
           return False
        else:
            self.cliente_tcp.send(bytes(msg, "utf-8"))
            return True

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Funções entres clientes udp  #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def init_server_udp(self):
        self.net = ss.socket(ss.AF_INET, ss.SOCK_DGRAM)
        self.net.bind((ss.gethostname(), 57574))
        while True:
            message, dress = self.net.recvfrom(1000000)
            print(f"{dress[0]} is conect")
            message = message.decode("utf-8")
            if not message in self.client.keys():
                self.net.sendto(f"hi {message}".encode("utf-8"), dress)
                self.client[message] = [dress[0], dress[1]] 
                print(self.client)
            else:
                self.net.sendto(f"change the name".encode("utf-8"), dress)
 

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Funções entre cliente e servidor tcp #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def cam(self, mn):
        abc = cv.VideoCapture(0)
        while True:
            boolean, image = abc.read()
            if boolean:
                cv.imshow(mn, image)
                if cv.waitKey(1) == ord("p"):
                    break
    
    def init_window(self):
        gg.init()
        self.window = gg.display.set_mode((800, 500))
        while True:
            gg.display.update()

    
    

client()



