from tokenize import String
import mysql.connector


class ConnectionDB:

    def RegisterPlayer(self, option):
        cnn = mysql.connector.connect(host="localhost",user="root",password="1234",database="poo")

        mycursor = cnn.cursor()
        sql = "INSERT INTO jugadores (option_player) VALUES (%s)"
        val = (option,)
        mycursor.execute(sql, val)
        cnn.commit()
        print(mycursor.rowcount, "registro insertado")