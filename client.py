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
#print LOGIN 
IPPORT = direccion[1].split(":")
SERVER = IPPORT[0]
SIPPORT = int(IPPORT[1])
#print IPPORT[0]
#print IPPORT[1]
	# Contenido que vamos a enviar
#try: 
	# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, SIPPORT))
#except SocketError 
    #print "Error: No server listening at 193.147.73.20 port 5555" 

print "Enviando: " + metodo
my_socket.send(metodo + '\r\n')
data = my_socket.recv(1024)
print 'Recibido -- ', data
if data ==  "SIP/2.0 100 Trying \r\n SIP/2.0 180 Ring \r\n SIP/2.0 200 OK":
    metodo = "ACK"
    print "Enviando: " + metodo
    my_socket.send(metodo + '\r\n')
    
#print "Terminando socket..."

# Cerramos todo
#my_socket.close()
#print "Fin."
