#Modulen som kopplar PostgresSQL till databasen pg.server.mah.se
import psycopg2
#Modul som hjälper till att skapa ett slumpmässigt ID
import random

#Huvudfunktionen
def main():
    #Kopplar till databasen aj9099, pg.server.mah.se
    try:
        con = psycopg2.connect(
            host = "pgserver.mah.se",
            database = "ah8140",
            user = "ah8140",
            password = "pzvieemm")

