#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


import SocketServer
import sys
import os

comandos = sys.argv

if len(comandos) != 4:
    sys.exit("Usage: python server.py IP port audio_file")

SERVER = comandos[1]
PORT = int(comandos[2])
FICH_AUDIO = comandos[3]


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Clase para un servidor SIP
    """

    def handle(self):
        """
        Método handle
        """
        while 1:
            line = self.rfile.read()
            print "El cliente nos manda " + line
            lista = line.split(" ")
            metodo = lista[0]
            metodos = ['CANCEL', 'OPTIONS', 'REGISTER']

            if not line:
                break

            if metodo == "INVITE":
                respuesta = "SIP/2.0 100 Trying\r\n\r\n"
                respuesta += "SIP/2.0 180 Ring\r\n\r\n"
                respuesta += "SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(respuesta)
            elif metodo == "ACK":
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 <' + FICH_AUDIO
                os.system('chmod 755 mp32rtp')
                os.system(aEjecutar)
            elif metodo == "BYE":
                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
            elif metodo in metodos:
                self.wfile.write("SIP/2.0 405 Method Not Allowed\r\n\r\n")
            else:
                self.wfile.write("SIP/2.0 400 Bad Request\r\n\r\n")

if __name__ == "__main__":
    """
    Procedimiento principal
    """

    serv = SocketServer.UDPServer((SERVER, PORT), EchoHandler)
    print "Listening..."
    serv.serve_forever()
