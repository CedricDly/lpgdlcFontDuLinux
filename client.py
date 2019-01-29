#coding: utf-8

# Nom : Client.py
# Auteur : Les p'tits gars d'la côte
# Résumé : Client permettant de se connecter au servo moteur et à la caméra de la Raspberry Pi

import socket
import signal
import os
import sys
import argparse
import re



class Client:
    """Client permettant de demander la prise de photos, la réception des clichés et faire bouger le servomoteur"""
    def __init__(self, IP, PortCamera, PortServo):
        self.__skCamera = 0 #Socket de la Camera
        self.__skServo = 0  #Socket du servo-moteur
        self.__ip = IP #tartget IP
        self.__portCamera = PortCamera #Camera port 
        self.__portServo = PortServo #Servo Port


    def conToRaspberry(self):
        '''Connects to Raspberry PI camera and servo sockets'''
        self.__skCamera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__skServo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.__skCamera.connect((self.__ip, self.__portCamera))
        self.__skServo.connect((self.__ip, self.__portServo))
        

        print("Connection successfully established with %s" %(self.__ip))

    def prendrePhoto(self):
        '''Send a request to capture a photo'''
        self.__skCamera.send(str.encode("PHOTO"))
        response = self.recv(1)

        ##TO DO : Recuperer la photo (voir du cote de la rasp comment est envoyee la photo)

    def bougerServo(self, angle):
        '''Send a request to move servo from input angle'''

        request = "MOVE" + str(angle)

        self.__skServo.send(str.encode(request))


if(__name__=="__main__"):

    parser = argparse.ArgumentParser()
    parser.add_argument("i", help="IP of the Raspberry Pi",type=str)
    parser.add_argument("cp", help="Port for the Camera", type=int)
    parser.add_argument("sp",  help="Port for the Servo", type=int)
    args = parser.parse_args()

    if(args.cp > 65536 or args.sp > 65536):
        print("ERROR") ##REPLACE
    else:
        pat = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        if(not(pat.match(args.i))):
            print("error") ##REPLACE
        else:
            client = Client(args.i, args.cp, args.sp)
            
            client.conToRaspberry()

            print("Commandes disponibles :\n")
            print("HELP --> aide")
            print("PHOTO --> prendre une photo")
            print("MOVE --> suivi du nombre de degrés, déclenche la rotation du servo")

            while(1):

                for line in sys.stdin:
                    line = line.rstrip('\n')
                    if(line == "HELP"):
                        print("HELP --> aide")
                        print("PHOTO --> prendre une photo")
                        print("MOVE --> suivi du nombre de degrés (sans espace), déclenche la rotation du servo")
                    elif(line=="PHOTO"):
                        client.prendrePhoto()
                    elif(line[0:4]=="MOVE"):
                        angle = line[4:]
                        try:
                            iAngle = int(angle)
                            if(iAngle > 180 or iAngle < -180):
                                print("Error : La valeur d'angle doit être comprise entre -180 et 180")
                            else:
                                client.bougerServo(iAngle)
                        except ValueError:
                            print("Error : la valeur d'angle est incorrecte")

        
