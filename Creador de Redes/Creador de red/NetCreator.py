from InstagramAPI import InstagramAPI
import time

def getUserID(dictionary):
    return str(dictionary.get("users")[0]["pk"])

def preparse(lst):
    print("esto lo hago")
    listReturn = []
    for i in lst:
        print "easy pisi"
        d = {}
        d["users"] = i.get("users")
        listReturn.append(d)
        print "easi pisi?"
    #listReturn=parse(listReturn)
    print (listReturn)
    print("salgo")
    return listReturn

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


def buscaPalabra(palabras,biografia):
    time.sleep(7)
    biografia=biografia.lower()
    for word in palabras:
        if word in biografia:
          if word == "burg" and ("mburg" in biografia or "sburg" in biografia or "nburg" in biografia or "burger" in biografia):
            print 'casi'
          else:
        
            print 'success',
            return True
    return False




if __name__ == "__main__":
    nombre = raw_input("Introduce tu nombre: ")
    contrasena = raw_input("Introduce tu contrasena: ")
    api = InstagramAPI(nombre, contrasena)
    api.login()
    user_id = api.username_id


#5api.getUsernameInfo(user_id)
#print(api.LastJson)
#time.sleep(20)
investigar = []

following = api.getTotalFollowings(user_id)
#followers = api.getTotalFollowers(user_id)


investigar.append(following)
#investigar.append(followers)


#print (investigar)
solicitud=0
for i in range(3):
    try:
        #print ("INVESTIGAR A: ",investigar[i])
        f2 = parse(investigar[i])
        #print (f2)

        for j in range(len(f2)):
            try:
                time.sleep(4)
                identificador = f2[j].get("pk")

                print "////////////////////////////////////////////////////////////INVESTIGAR A:", f2[j].get("username")
                #print(identificador)
                api.getTotalFollowings(identificador)
                #api.getTotalFollowers(identificador)

                amigos_segundo_grado=api.LastJson
                #print(amigos_segundo_grado)
                amigos2 = parse(amigos_segundo_grado.get("users"))
                #print(amigos2)
                print (len(amigos2))
                if len(amigos2) <= 2000:
                    print "Numero de Amigos Razonable"
                    api.getUsernameInfo(f2[j].get("pk"))
                    #print(api.LastJson)
                    time.sleep(10)
                    for l in range(len(amigos2)):
                        try:

                            
                            #print(amigos2[l].get("username"))
                            identificador2 = amigos2[l].get("pk")
                            #print ".",
                            print (l), amigos2[l].get("username"), "  Amigo: ",j+1," Solicitud: ",solicitud, ""
                            api.getUsernameInfo(identificador2)
                            informacion=api.LastJson
                            #print(informacion)
                            #print(informacion.get("user").get("biography"))

                            palabras=[]
                            palabras=input("Introduce los terminos de busqueda")
                            #"carde adijo","carde ajimeno","o a",
                            biografia=informacion.get("user").get("biography")
                            if buscaPalabra(palabras,biografia):
                                print "entro"
                                time.sleep(6)
                                api.userFriendship(identificador2)
                                amistad = parsefriendship(api.LastJson)

                                if amistad[0].get("outgoing_request") == False and amistad[0].get("following") == False:
                                    solicitud += 1
                                    print(".")
                                    print("-------------------------ENVIO DE PETICION----------------------------")

                                    print ("Amigo: ",j+1," Solicitud: ",solicitud)
                                    time.sleep(11)
                                    try:
                                        api.follow(identificador2)
                                    except:
                                        print "a este no le sigo"
                                    print(amigos2[l].get("username"))
                                    print biografia

                                    time.sleep(4)
                                #else:
                                    #print ("Siguiendo")
                                # api.follow(identificador)
                        except:
                            print "ESTE AMIGO DA PROBLEMAS"



                        #print biografia
                        time.sleep(5)
                else:
                    print "Demasiados Amigos"


            except:
                print("adios")
    except:
        print("Y este fuera")
