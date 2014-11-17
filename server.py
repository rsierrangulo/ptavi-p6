#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys

comandos = sys.argv


SERVER = comandos[1]
PORT = int(comandos[2])
FICH_AUDIO = comandos[3]


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            line = self.rfile.read()
            print "El cliente nos manda " + line
            lista = line.split()
            metodo = lista[0]
            metodos = ['INVITE', 'ACK', 'BYE']
            if metodo == INVITE
                respuesta = "SIP/2.0 100 Trying\r\n\r\n"
                respuesta += "SIP/2.0 180 Ring\r\n\r\n"
                respuesta += "SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(respuesta)
            elif metodo == ACK
                print "recibido ACK"
            elif metodo == BYE
                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
            elif not metodo in metodos:
                self.wfile.write("SIP/2.0 405 Method Not Allowed\r\n\r\n")
            else:
                self.wfile.write("SIP/2.0 400 Bad Request\r\n\r\n")
                
                
                
                
                


            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(comandos) != 4:
        print "Usage: python server.py IP port audio_file"
    serv = SocketServer.UDPServer((SERVER, PORT), EchoHandler)
    print "Listening..."
    serv.serve_forever()
