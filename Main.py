import os
from Server import Server
from PluginManager import PluginManager

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234
SERIAL_PORT = "/dev/tty.usbmodem142301"

def main():
    os.system("clear")
    print "                      +-----------------------------------+"
    print "                      | Server to connect Homebridge with |"
    print "                      |     Arduino to control IR-LED     |"
    print "                      +-----------------------------------+"
    pluginManager = PluginManager()
    server = Server(SERVER_IP, SERVER_PORT, pluginManager)
    server.listen()
    #console(server, pluginManager)
    input = raw_input()

def console(server, pluginManager):
    while True:
        input = raw_input()
        if input == "exit":
            server.sock.close()
            pluginManager.close()
            quit()
        else:
            print '\nHelp:\n'
            print ' exit: close connection and exit script'
            print ''

if __name__ == '__main__':
    main()
