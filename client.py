#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

if len(sys.argv) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")

METHOD = sys.argv[1]

# Dirección IP del servidor.
SERVER = sys.argv[2].split("@")[1].split(":")[0]
try:
    PORT = int(sys.argv[2].split(":")[1])
except ValueError:
    sys.exit("receiver@IP:SIPport; Port: Int required") 
# Contenido que vamos a enviar
LINE = sys.argv[2].split(":")[0]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print "Enviando: " + METHOD + " sip:" + LINE + " SIP/2.0\r\n\r\n"
my_socket.send(METHOD + " sip:" + LINE + " SIP/2.0\r\n\r\n")
#En caso de que nuestro servidor no haya sido lanzado
try:
    data = my_socket.recv(1024)
except socket.error:
    sys.exit("Error: No server listening at " + SERVER + " PORT " + str(PORT))
print 'Recibido -- ', data

if METHOD == 'INVITE':
    #He recibido los tres mensajes a la vez, en una misma línea
    METHOD = 'ACK'
    print "Enviando: " + METHOD + " sip:" + LINE + " SIP/2.0\r\n\r\n"
    my_socket.send(METHOD + " sip:" + LINE + " SIP/2.0\r\n\r\n")

print "Terminando socket..."
# Cerramos todo
my_socket.close()
print "Fin."
