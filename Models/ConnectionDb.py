from tokenize import String
import mysql.connector


class ConnectionDB:
    cnn = mysql.connector.connect(host="localhost",user="root",password="1234",database="poo")

    def RegisterPlayer(self, option):

        mycursor = ConnectionDB.cnn.cursor()
        sql = "INSERT INTO jugadores (option_player) VALUES (%s)"
        val = (option,)
        mycursor.execute(sql, val)
        ConnectionDB.cnn.commit()
        print(mycursor.rowcount, "registro insertado")

    def GetOptionPlayers(self):
        print("Listar opciones seleccionadas")
        mycursor = ConnectionDB.cnn.cursor()
        mycursor.execute("SELECT * FROM jugadores")
        myresult = mycursor.fetchall()

        for x in myresult:
            print("La opcion seleccionada es %s" % x[1],)

    def DeletePlayers(self):
        mycursor = ConnectionDB.cnn.cursor()
        sql = "DELETE FROM jugadores"
        mycursor.execute(sql)
        ConnectionDB.cnn.commit()
        print(mycursor.rowcount, "record(s) deleted")