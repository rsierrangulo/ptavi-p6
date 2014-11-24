#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor SIP
"""

import SocketServer
import sys
import os


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            line = self.rfile.read()
            if not line:
                break
            METHODS = ['INVITE', 'ACK', 'BYE']
            Method = line.split(" ")[0]
            print "El cliente nos manda " + line
            if not Method in METHODS:
                self.wfile.write("SIP/2.0 405 Method Not Allowed\r\n\r\n")
            if Method == 'INVITE':
                respuesta = "SIP/2.0 100 Trying\r\n\r\n"
                respuesta += "SIP/2.0 180 Ring\r\n\r\n"
                respuesta += "SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(respuesta)
            elif Method == 'ACK':
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + sys.argv[3]
                print "Vamos a ejecutar", aEjecutar
                os.system(aEjecutar)
                print(" Ha terminado la ejecución de fich de audio")
            elif Method == 'BYE':
                respuesta = "SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(respuesta)
            else:
                self.wfile.write("SIP/2.0 400 Bad Request\r\n\r\n")

if __name__ == "__main__":
    try:
        LISTEN_PORT = int(sys.argv[2])
        sys.argv[3]
    except IndexError:
        sys.exit("Usage: python server.py IP port audio_file")
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", LISTEN_PORT), EchoHandler)
    print "Listening..."
    serv.serve_forever()
