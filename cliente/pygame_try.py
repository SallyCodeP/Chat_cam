import pygame as gg
import cv2 as cv
import socket as ss
from threading import Thread

class client():
    def __init__(self):
        self.client, self.server = self.init_client()
        
        
    
    
    def init_client(self):
        while True:
            self.my_name = input("Name ---> ")
            cliente = ss.socket(ss.AF_INET, ss.SOCK_DGRAM)
            cliente.sendto(bytes(self.my_name.encode("utf-8")), (ss.gethostname(), 57574))
            data, server = cliente.recvfrom(10000)
            print(data)
            if data.decode("utf-8") == f"hi {self.my_name}":
                return [client, server]
            elif data.decode("utf-8") == "change the name":
                print("Esse nome já existe!")
                continue
            else:
                continue

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



