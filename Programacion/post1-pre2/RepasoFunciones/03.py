#Funcion que recibe diccionario{user,pass} y verifique el login devolviendo un bool, user t es CARLOS y pass t es 1234

def loginVerify(login):
    if(login["user"]=="CARLOS" and login["pass"]=="1234"):
        return True
    else:
        return False
    
userInput=input("Cual es tu usuario? ")
passInput=input("Y cual es la contraseña? ")

print(loginVerify(login={"user":userInput,"pass":passInput}))