import mysql.connector

#connect()-funktio palauttaa tietokantayhteyden, joka sijoitetaan muuttujaan

connection = mysql.connector.connect(
        host='127.0.0.1', #localhost
        port=3306,
        database='flight_game',
        user='flight_game',
        password='flight_game',
        autocommit=True,
        collation='utf8mb4_general_ci',
        )