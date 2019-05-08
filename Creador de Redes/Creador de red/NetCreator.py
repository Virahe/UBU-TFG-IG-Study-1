from InstagramAPI import InstagramAPI
import time

def getUserID(dictionary):

    return str(dictionary.get("users")[0]["pk"])

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

if __name__ == "__main__":
    nombre = raw_input("Introduce tu nombre: ")
    contrasena = raw_input("Introduce tu contrasena: ")
    api = InstagramAPI(nombre, contrasena)
    api.login()
    user_id = api.username_id


following = api.getTotalFollowings(user_id)

api.userFriendship(6014524088L)
print(api.LastJson)
#api.follow(6014524088L)

f2 = parse(following)
print (f2)

for i in range(len(f2)):
    try:
        identificador = f2[i].get("pk")
        print(f2[i].get("username"))
        api.follow(identificador)
    except:
        print("Oops!")
        print("Next entry.")
        print()
        time.sleep(300)
