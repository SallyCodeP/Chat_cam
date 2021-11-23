   
    def conect_clients(self, name):

            obj = self.client[name][0]
            obj.send(bytes("wc", "utf-8"))
            conect = self.__recv_data(obj)
            
            if conect != name:
                if not conect in self.dict_id.values():
                    if not conect in self.client.keys():
                        obj.send(bytes("Contato n encontrado!", "utf-8"))
                    else:
                        obj.send(bytes("Pedido enviado!", "utf-8"))
                        obj_cli = self.client[conect][0]
                        obj_cli.send(bytes(f"{name} quer conectar!\n", "utf-8"))
                        resposta = self.__recv_data(obj_cli)
                        if resposta == "conectar":
                            obj.send(bytes("Pedido aceito!", "utf-8"))
                        else:
                            obj.send(bytes("Conexao rejeitada!", "utf-8"))
                            
                        
                        self.dict_id[self.__create_id()] = [name, conect]
                else:
                    obj.send(bytes("Ja esta em uma chamada", "utf-8"))
            else:
                obj.send(bytes("Voce nao pode se conectar com vc msm!", "utf-8"))
        
    def __create_id(self):
        while True:
            values = [["1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"], ascii_letters]
            abc = [choice(choice(values)) for _ in range(0, 9)]
            abc.insert(3, "-")
            abc.insert(7, "-")
            if not abc in self.dict_id.keys():
                return "".join(abc)  