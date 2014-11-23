#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os 

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            #SIP/2.0 200 OK\r\n\r\n
            line = self.rfile.read()
            line = line.split()
            if not line:
                break
            # Si no hay más líneas salimos del bucle infinito
            if line[0] == "INVITE":
                print "INVITE recibido"
                self.wfile.write("SIP/2.0 100 Trying\r\n\r\nSIP/2.0 180 Ring\r\n\r\nSIP/2.0 200 OK\r\n\r\n")
                
            elif line[0] == "ACK":
                print "ACK recibido" 
                # aEjecutar es un string con lo que se ha de ejecutar en la shell 
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 <' + fichero_audio 
                print "Vamos a ejecutar", aEjecutar 
                os.system(aEjecutar) 

            elif line[0] == "BYE":
                print "BYE recibido"
                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
            elif line[0] == "CANCEL" or line[0] == "REGISTER" or line[0] == "OPTIONS":
                print "metodo no disponible recibido"
                self.wfile.write("SIP/2.0 Method Not Allowed\r\n\r\n") 
            else:
                print "petición incorrecta recibida"
                self.wfile.write("SIP/2.0 400 Bad Request\r\n\r\n") 
            
            

if __name__ == "__main__":
    if len(sys.argv) != 4:
	    sys.exit("Usage: python server.py IP port audio_file")
    else:
        print "Listening..."
    # Creamos servidor de eco y escuchamos
    fichero_audio = sys.argv[3] 
    PORT = int(sys.argv[2])
    serv = SocketServer.UDPServer(("", PORT), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
