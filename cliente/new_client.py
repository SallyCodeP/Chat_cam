import socket as ss
from random import randint
import cv2 as cv
from threading import Thread
from random import randint

class client:
    def __init__(self) -> None:
        # Definindo nome do cliente e sua conexao com o servidor
        self.conect, self.name = self.init_client_tcp()


    # Iniciando cliente do servidor tcp
    def init_client_tcp(self):
        cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        cliente.bind((ss.gethostname(), randint(10000, 60000)))
        cliente.connect((ss.gethostname(), 17723))
        return cliente, self.put_name()

    # Registrando nome do cliente no servidor
    def _put_name(self):
        while True:
            my_name = input("Name ---> ")
            if self.send(my_name):
                data = self.recv_tcp_data()
                if data == "Cadastrado":
                    print("Confirmado")
                    return my_name
                elif data == "Neu":
                    print("Esse nome já existe!")
                    continue
                else:
                    continue
            else:
                continue

    # Receber dados do server tcp
    def recv_tcp_data(self):
        while True:
            data = self.cliente_tcp.recv(10000)
            if data:
                decode_data = data.decode("utf-8")
                if decode_data != "$":
                    if not "//" in decode_data:
                        return decode_data
                    else:
                        return decode_data.split("//")

    