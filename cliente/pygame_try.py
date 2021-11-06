import pygame as gg
import cv2 as cv
import socket as ss
from threading import Thread
from random import randint

class client:
    def __init__(self):
        self.cliente_tcp = self.init_client_tcp()
        self.name = self.put_name()
    
    def put_name(self):
        while True:
            my_name = input("Name ---> ")
            self.cliente_tcp.send(bytes(my_name, "utf-8"))
            data = self.recv_tcp_data()
            if data == "accept":
                print("Confirmado")
                return my_name
            elif data == "nje":
                print("Esse nome já existe!")
                continue
            else:
                continue

    def request_video_chat(name):
        pass
    
    def init_client_tcp(self):
        cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        cliente.bind((ss.gethostname(), randint(10000, 60000)))
        cliente.connect((ss.gethostname(), 17723))
        return cliente
    

    def recv_tcp_data(self):
        while True:
            data = self.cliente_tcp.recv(10000)
            if data:
                return data.decode("utf-8")

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

    def send_to_other():
        pass

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
 

client()



