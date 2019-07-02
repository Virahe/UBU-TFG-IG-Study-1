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


insertar_amistad = ("INSERT INTO persona_sigue (IDseguidor, IDseguido) VALUES (%s, %s)")
insertar_ignorado = ("INSERT INTO ignorados (IDpersona) VALUES (%s)")





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
        time.sleep(1)
        IDseguidor = f2[j].get("pk")
        
        
        print (j)
        print (IDseguidor)
        '''api.getUsernameInfo(IDseguidor)
        info=api.LastJson
        try:
          if (info.get("user").get("following_count")>=2000):'''
        try:
          if (False):
            try:
              identificador=IDseguidor
              cursor.execute(insertar_ignorado, (identificador, ))
              cnx.commit()
            except:
              pass
          else:     
            amistades=api.getTotalFollowings(IDseguidor)
              
            
            #time.sleep(10)
            for i in amistades:
              #print("llego")
              IDseguido=i.get("pk")
              
              
              informacion_amistad = (IDseguidor , IDseguido)
              try:      
                #Insertar informacion
                cursor.execute(insertar_amistad, informacion_amistad)
                cnx.commit()
                print(j," -> ",IDseguidor," -> ",IDseguido)
              except: 
                #print("salto")
                pass
        except:
          try:
              identificador=IDseguidor
              cursor.execute(insertar_ignorado, (identificador, ))
              cnx.commit()
          except:
              pass
          pass    
            
    cnx.close()
