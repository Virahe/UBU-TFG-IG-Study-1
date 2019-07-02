import mysql.connector

from datetime import date, datetime, timedelta
from mysql.connector import errorcode
from InstagramAPI import InstagramAPI
import time


def parse(lst):
    listReturn=[]
    for i in lst:
        d={}
        d["pk"]=i.get("pk")
        d["username"]=i.get("username")
        d["full_name"]=i.get("full_name")
        d["is_private"]=i.get("is_private")
        listReturn.append(d)
    return listReturn

def parsefriendship(lst):
    listReturn=[]
    d={}
    d["following"] = lst.get("following")
    d["is_private"] = lst.get("is_private")
    d["outgoing_request"] = lst.get("outgoing_request")
    listReturn.append(d)
    return listReturn



#else:
#  cnx.close()






insertar_persona = ("INSERT INTO persona (Idpersona, ciudad) VALUES (%s, %s)")

if __name__ == "__main__":
    nombre = raw_input("Introduce tu nombre: ")
    contrasena = raw_input("Introduce tu contrasena: ")
    api = InstagramAPI(nombre, contrasena)
    
    api.login()
    user_id = api.username_id

    investigar = []

    following = api.getTotalFollowings(user_id)
    

    investigar.append(following)

    f2 = parse(investigar[0])

    nombremysql = raw_input("Introduce tu nombre de mysql: ")
    contrasenamysql = raw_input("Introduce tu contrasena de mysql: ")
    databasemysql = raw_input("Introduce tu database de mysql: ")
    try:
      cnx = mysql.connector.connect(user=nombremysql, password=contrasenamysql,
                              database=databasemysql)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
        
    cursor = cnx.cursor()
        
    for j in range(len(f2)):
        IDpersona = f2[j].get("pk")
        
        informacion_persona = (IDpersona , "burgos")
        print (IDpersona)
        try:
          #Insertar informacion
          cursor.execute(insertar_persona, informacion_persona)
          
          #cursor.execute("select * from persona;")
          cnx.commit()
        except: 
          print("salto")
          pass
          
          
    
    cnx.close()

        
        
        
        
