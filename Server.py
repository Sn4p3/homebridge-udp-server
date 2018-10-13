import socket
import json
import thread

class Server(object):

    def __init__(self, ip, port, pluginManager):
        super(Server, self).__init__()
        self.pluginManager = pluginManager
        self.exit = False

        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print "[+] Creating server at %s:%s" % (ip, port)
        print '[+] Binding server'
        self.sock.bind((ip, port))
        print "[+] Server successfully created"
        #thread.start_new_thread( self.listen, () )


    def listen(self):
        print "[+] Start listening for connections"
        while self.exit == False:
            data, address = self.sock.recvfrom(4096)
            if data:
                jsonData = json.loads(data)
                plugin = self.pluginManager.getPlugin(jsonData["plugin"])
                thread.start_new_thread( plugin.execute, (jsonData["var"], jsonData["value"],) )
