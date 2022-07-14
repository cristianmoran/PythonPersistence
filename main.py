
from datetime import datetime
import random
from Menu.MenuFactory import MenuFactory
from Models.ConnectionDb import ConnectionDB
from Models.SessionObject import SessionObject
from Session.SessionFactory import SessionFactory

print("Bienvenido al juego carta mayor")
random.seed(-6789)
cnn = ConnectionDB()

while True:
    cnn.GetOptionPlayers()
    print("")
    print("")
    print("Que desea realizar")
    print(" 1) Jugar como invitado")
    print(" 2) Jugar como jugador")
    print(" 3) Registrarse")
    print(" 4) Salir")
    opcion = int(input('Opcion: '))
    
    if opcion == 4:
        cnn.DeletePlayers()

    menu = MenuFactory.ObtenerMenu(opcion)

    cnn.RegisterPlayer(opcion)



    if menu is not None:
        menu.Ejecutar()