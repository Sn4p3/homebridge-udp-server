import socket
import sys
import thread
import os
import serial

exit = False
state = "off"

SERVER_IP = "192.168.178.21"
SERVER_PORT = 1234
SERIAL_PORT = "/dev/tty.usbmodem142301"

def main():
    os.system("clear")
    print "                      +-----------------------------------+"
    print "                      | Server to connect Homebridge with |"
    print "                      |     Arduino to control IR-LED     |"
    print "                      +-----------------------------------+"
    print "\n[+] Initializing Server"
    server = makeServer()
    print "[+] Initializing Serial connection"
    ser = makeSerial()
    thread.start_new_thread( listen, (server, ser, ) )
    console(server, ser)

def makeServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "[+] Creating server at %s:%s" % (SERVER_IP, SERVER_PORT)
    print '[+] Binding server'
    sock.bind((SERVER_IP, SERVER_PORT))
    print "[+] Server successfully created"
    return sock

def makeSerial():
    ser = serial.Serial(SERIAL_PORT)
    ser.baudrate = 9600
    print "[+] Serial connection successfully created"
    return ser

def listen(sock, ser):
    print "[+] Start listening for connections"
    while exit == False:
        data, address = sock.recvfrom(4096)
        if data:
            state = str(data)
            print data
            if state == "on":
                ser.write('FFE01F')
            elif state == "off":
                ser.write('FF609F')

def console(sock, ser):
    while True:
        input = raw_input()
        if input == "exit":
            sock.close()
            ser.close()
            exit = True
            quit()
        elif input == "state":
            print 'current state: Light is %s' % state
        else:
            print '\nHelp:\n'
            print ' exit: close connection and exit script'
            print ' state: prints current state of light'
            print ''

main()
