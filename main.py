import machine
import time

marche_avantdroit = machine.Pin(2,machine.Pin.OUT)
mdroite_recul = machine.Pin(15,machine.Pin.OUT)
marche_avantgauche = machine.Pin(16,machine.Pin.OUT)
mgauche_recul = machine.Pin(4,machine.Pin.OUT)
def marcheavant():
    marche_avantdroit.value(1)
    mdroite_recul.value(0)
    marche_avantgauche.value(1)
    mgauche_recul.value(0)
def tourner_droite():
    marche_avantdroit.value(1)
    mdroite_recul.value(0)
    marche_avantgauche.value(0)
    mgauche_recul.value(0)
def reculer():
    mdroite_recul.value(1)
    marche_avantdroit.value(0)
    mgauche_recul(1)
    marche_avantgauche.value(0)
def stop():
    marche_avantdroit.value(0)
    mdroite_recul.value(0)
    marche_avantgauche.value(0)
    mgauche_recul.value(0)
def tourner_gauche():
    marche_avantdroit.value(0)
    mdroite_recul.value(0)
    marche_avantgauche.value(1)
    mgauche_recul.value(0)

import network
import socket
reso = network.WLAN(network.AP_IF)
reso.active(True)
reso.config(essid='3asbateur2feuj98',password='Babheu76',authmode=3)
com_net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
com_net.bind (("192.168.4.1", 1865))
while True:
    reception = com_net.recvfrom(1024)
    print(reception[0].decode())
    if reception[0].decode() == "av":
        marcheavant()
    if reception[0].decode() == "rc":
        reculer()
    if reception[0].decode() == "g":
        tourner_gauche()
    if reception[0].decode() == "d":
        tourner_droite()
    if reception[0].decode() == "s":
        stop()
    time.sleep(0.05)
