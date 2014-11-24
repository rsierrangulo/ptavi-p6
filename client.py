#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

comandos = sys.argv

if len(comandos) != 3:
    sys.exit('Usage: python client.py method receiver@IP:SIPport')

METODO = comandos[1].upper()
LISTA_1 = comandos[2].split("@")
LOGIN = LISTA_1[0]
LISTA_2 = LISTA_1[1].split(":")
SERVER = LISTA_2[0]
PORT = int(LISTA_2[1])


LINE = METODO + " sip:" + LOGIN + "@" + SERVER + " SIP/2.0\r\n\r\n"

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

try:
    print "Enviando: " + LINE
    my_socket.send(LINE)

    data = my_socket.recv(1024)

    print 'Recibido -- ', data

    respuesta = "SIP/2.0 100 Trying\r\n\r\n"
    respuesta += "SIP/2.0 180 Ring\r\n\r\n"
    respuesta += "SIP/2.0 200 OK\r\n\r\n"

    if data == respuesta:
        ACK = "ACK" + " sip:" + LOGIN + "@" + SERVER + " SIP/2.0\r\n\r\n"
        print "Enviando ACK: " + ACK
        my_socket.send(ACK)
        data = my_socket.recv(1024)

    print "Terminando socket..."
except socket.error:
    print "Error: No server listening at " + SERVER + " port " + str(PORT)


my_socket.close()
print "Fin."
