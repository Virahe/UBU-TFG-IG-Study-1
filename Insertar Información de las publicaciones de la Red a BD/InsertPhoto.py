import mysql.connector
import re
from datetime import date, datetime, timedelta
from mysql.connector import errorcode
from InstagramAPI import InstagramAPI
import time

from datetime import datetime


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



#Introducir en la base de datos la informacion de la publicacion


#def getMediaData(user_id,IDpersona):
def getMediaData(IDpersona):
  try:
    all_posts = api.getTotalUserFeed(IDpersona)
  
 
    for post in all_posts:
    
            if "id" in post:
                IDpublicacion = str(post["id"])
                
            if "caption" in post:
                if post["caption"]:
                    if "text" in post["caption"]:
                        texto = str(post["caption"]["text"].encode("utf8"))
             
            if "taken_at" in post:
                timestamp = str(post["taken_at"])
                
                fecha = datetime.fromtimestamp(float(timestamp))
            
            
            try:
              cursor.execute(insertar_publicacion,(IDpublicacion, IDpersona, fecha, texto))
              cnx.commit()
              getMediaLikers(post["id"])
              getMediaHashtag(post["id"],texto)
              
            except:
              pass
  except:
    pass            
  return None
            
              
              
#Introducir en la base de datos la gente que ha interacionado
def getMediaLikers(media_id):
    api.getMediaLikers(media_id)

    likers = api.LastJson

    for liker in likers["users"]:
        IDpersona = liker["pk"]
        try:
          cursor.execute(insertar_publicacion_like,(media_id,IDpersona))
          cnx.commit()
        except:
          pass
    return None
    
#Introducir en la base de datos los hashtags de la publicacion
def getMediaHashtag(media_id,texto):
    
    hashtag_lista=re.findall(r"#(\w+)", texto)
    if hashtag_lista:
        for hashtag in hashtag_lista:
          try:
            cursor.execute(insertar_publicacion_hashtag, (media_id,hashtag))
            cnx.commit()
          except:
            pass
    return None

#quita los emojis
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')





insertar_publicacion = ("INSERT INTO publicacion (IDpublicacion, IDpersona, fecha, texto) VALUES (%s, %s, %s, %s)")
insertar_publicacion_like = ("INSERT INTO publicacion_like (IDpublicacion, IDpersona) VALUES (%s, %s)")
insertar_publicacion_hashtag = ("INSERT INTO publicacion_hashtag (IDpublicacion, hashtag) VALUES (%s, %s)")


#CONEXION A LA BASE DE DATOS
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




if __name__ == "__main__":
    #Loguearme
    nombre = raw_input("Introduce tu nombre: ")
    contrasena = raw_input("Introduce tu contrasena: ")
    api = InstagramAPI(nombre, contrasena)
    api.login()
    user_id = api.username_id

    investigar = []
    following = api.getTotalFollowings(user_id)
    investigar.append(following)
    f2 = parse(investigar[0])    
    
    numero=0
    for j in range(len(f2)):
      
      if numero > 0:
        time.sleep(1)
        IDpersona = f2[j].get("pk")
        
        
        print (j)
        print (IDpersona)
        
        
        #Meter en Publicacion la info:
        getMediaData(IDpersona)
      else:
        numero+=1
        
        
            
    cnx.close()
