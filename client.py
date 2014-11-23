#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

	#Cliente SIP

if len(sys.argv) != 3:
	sys.exit("Usage: python client.py method receiver@IP:SIPport")

metodo = sys.argv[1]
direccion = sys.argv[2].split("@")
	# Dirección IP y puerto del servidor.
LOGIN = direccion[0]
IPPORT = direccion[1].split(":")
SERVERIP = IPPORT[0]
SIPPORT = int(IPPORT[1])

	# Contenido que vamos a enviar

	# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVERIP, SIPPORT))
#REGISTER sip:luke@polismassa.com SIP/2.0\r\n\r\n
line = " sip:" + LOGIN + "@" + "SIP /2.0\r\n\r\n"
envio = metodo + line
print "Enviando: " + envio
my_socket.send(envio)
try: 
    data = my_socket.recv(1024)
    print 'Recibido -- ', data
    if data ==  "SIP/2.0 100 Trying\r\n\r\nSIP/2.0 180 Ring\r\n\r\nSIP/2.0 200 OK\r\n\r\n":
        metodo = "ACK"
        envio = metodo + line
        print "Enviando: " + envio 
        my_socket.send(envio)
except socket.error:
    print "Error: No server listening at " + SERVERIP + " port " + str(SIPPORT)   
#print "Terminando socket..."

# Cerramos todo
my_socket.close()
#print "Fin."
