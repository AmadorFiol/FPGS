#Crear lista de dos valores, el [0] es usrname y el [1] es pssw
#Mas tarde pide un input de dos valores (usr y pswwd) y si son iguales al de la lista manda mensaje "Login correcto",
#sino envia mensaje "Login incorrecto"
login=["UserName","1234"]
usr=input("Escriba el nombre de usuario: ")
pswd=input("Escriba la contraseña: ")
if(login[0]==usr and login[1]==pswd):
    print("Login correcto")
else:
    print("Login incorrecto")