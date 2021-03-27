'''
@param : cursor
@note  : permet de recuperer le 
'''
import mysql.connector
def connexion(_host, _user, _password, _dbName=None):
    mydb = mysql.connector.connect(
        host= _host, 
        user = _user, 
        password = _password, 
        db = _dbName)
    return mydb

host = "127.0.0.1"
password = ""
user = 'root'
dbname = 'test'

cnx = connexion(host, user, password, dbname)
cursor = cnx.cursor()

def getBillets(cursor): 
    requete = "SELECT * FROM billets"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    return resultat

def rechercherBillet(cursor,mot) : 
    requete = "SELECT * FROM billets WHERE titre LIKE '%{}%'".format(mot)
    cursor.execute(requete)
    resultat = cursor.fetchall()
    return resultat

def setBillet(cursor) : 
    titre = input('Titre :')
    contenu = input("Contenus : ")
    requete = "INSERT INTO billets(titre, contenu) VALUES (%s,%s)" 
    valeur = (titre, contenu)
    cursor.execute(requete, valeur)

"""
billets = getBillets(cursor)

for billet in billets :
    print("Id : ",billet[0])
    print( "Titre : ",billet[1])
    print( "Contenus :",billet[2], "\n")
"""
setBillet(cursor)
cnx.commit()

mot = input("Entrer le mot à rechercher : ")
recherche = rechercherBillet(cursor,mot)

longueur = len(recherche)

if (longueur == 0 ):
    print("Le mot : ", mot, " n'existe pas")
else : 
    print("La recherche a envoyé : ", longueur, "Resultat(s)")
    for billet in recherche : 
        print("Id : ",billet[0])
        print( "Titre : ",billet[1])
        print( "Contenus :",billet[2], "\n")

