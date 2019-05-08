import mysql.connector

from datetime import date, datetime, timedelta
from mysql.connector import errorcode



try:
  cnx = mysql.connector.connect(user='NOMBRE', password='CONTRASEÑA',
                              host='127.0.0.1',
                              database='NOMBREBASEDEDATOS')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
#else:
#  cnx.close()

cursor = cnx.cursor()

insertar_persona = ("INSERT INTO persona "
                    "(Idpersona, ciudad) "
                    "VALUES (%s, %s)")

informacion_persona = (IDpersona , "burgos")

#Insertar informacion
cursor.execute(insertar_persona, informacion_persona)
