import socket as ss

class net:
    def init_tcp(self):
        server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        server.bind((ss.gethostname, 34543))
        server.listen(5)
        return server

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
                continue
