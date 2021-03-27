import mysql.connector
mydbGeneric = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = ''
)

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    db ="pythonDataBase"
)

cursor = mydb.cursor()
def createDataBase(cursor, dbName) : 
    requete ="CREATE DATABASE {}".format(dbName)
    cursor.execute(requete)

def createTable(cursor, tableName) : 
    requete ="""CREATE TABLE {} 
    ( primary key int id, 
    varchar(100) nom, 
    varchar(100) categprie,
    float prix )""".format(tableName)
    cursor.execute(requete)

def connexion(_host, _user, _password, _dbName=""):
    mysql = mysql.Connector.connect(
        host= _host, 
        user = _user, 
        password = _password, 
        db = _dbName)
    return mydb.cursor()

   