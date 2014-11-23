#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            line = line.split()
            if not line:
                break
            if line[0] == "INVITE":
                print "INVITE recibido"
                self.wfile.write("SIP/2.0 100 Trying \r\n SIP/2.0 180 Ring \r\n SIP/2.0 200 OK")
            elif line[0] == "ACK"
                print "ACK recibido" 
            elif line[0] == "BYE" 
                self.wfile.write("SIP/2.0 200 OK")
            # Si no hay más líneas salimos del bucle infinito
            

if __name__ == "__main__":
    if len(sys.argv) != 4:
	    sys.exit("Usage: python server.py IP port audio_file")
    else:
        print "Listening..."
    # Creamos servidor de eco y escuchamos

    PORT = int(sys.argv[2])
    serv = SocketServer.UDPServer(("", PORT), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
