# coding: utf-8
# Author: Leo M.H & Axel H
#Modulen som kopplar PostgresSQL till databasen pg.server.mah.se
import psycopg2
#Modul som hjälper till att skapa ett slumpmässigt ID
import random
#Installerar och importerar ramverket Flask
pip install Flask
from flask import flask

#Huvudfunktionen
def main():
    #Kopplar till databasen aj9099, pg.server.mah.se
    try:
        con = psycopg2.connect(
            host = "pgserver.mah.se",
            database = "ah8140",
            user = "ah8140",
            password = "pzvieemm")

    cur = con.cursor()

@route("/")
def index(cur, con):
    '''
    Startsida
    '''
    
    if request.query.info != "":
        info = request.query.info

    return template("index", articles=list_articles(), info=info)

@route('/akademigastrologi/<pagename>/')
def show_article(pagename, info = ""):
    """Displays a single article (loaded from a text file)."""
    
    file = open("akademigastrologi/" + pagename + ".txt", "r", encoding ="utf-8")
    text = file.read()
    
    if request.query.info != "":
        info = request.query.info

    return template("article", article=pagename, text=text, info=info)

@route('/akademigastrologi/<pagename>')
def delete_article(pagename):
    ''' 
    Deletes chosen article and redirects
    '''
    try:
        file = remove("wiki/" + pagename + ".txt")

        redirect("/?info=" + pagename + " borttagen")

    except FileNotFoundError:
        redirect ("/=info=" + pagename + " kan inte hittas")


    
    cur.execute("insert into traveler (persID, name, email, phone) values({}, '{}', '{}', {})".format(id_in, name_in, email_in, phone_in))
    con.commit() #Måste commit() för att reflektera den inmatade datan
