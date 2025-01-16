'''
Crea una clase llamada Tablet para representar una tableta digital
Los atributos que debe contener son:
creador(cadena de texto)
tamano_pantalla (flotante)
num_cores (entero)
apps (lista de cadenas de texto)
status (False: apagado, True: encendido)
Los métodos que debe contener la clase son:
__init__(self, creador, tamano_pantalla, num_cores)
power_on(self)
Cambia el status de apagado a encendido
power_off(self)
Cambia el status de encendido a apagado
install_app(self, app) (no instalar la app si ya existe)
Añade una nueva app a la lista
uninstall_app(self, app)
Elimina la app de la lista.
'''
import os
#-----Declaracion clases-----#
class Tablet:
    def __init__(self,creador,tamano_pantalla,num_cores):
        self.creador=creador
        self.tamano_pantalla=float(tamano_pantalla)
        self.num_cores=int(num_cores)
        self.status=False
        self.apps=[]

    def power_on(self):
        if self.status==True:
            return "La tablet ya esta encendida"
        else:
            self.status=True
            return "La tablet se ha encendido"

    def power_off(self):
        if self.status==False:
            return "La tablet ya esta apagada"
        else:
            self.status=False
            return "La tablet se ha apagado"

    def install_app(self,app):
        for i in self.apps:
            if i==app:
                return "La app ya esta instalada"
        self.apps.append(app)
        return f"Se ha instalado {app}"

    def uninstall_app(self,app):
        for i in self.apps:
            if i==app:
                self.apps.remove(app)
                return f"Se ha desinstalado {app}"
        return "La app no esta instalada"

    def show_apps(self):
        for app in self.apps:
            print(app)

#-----Declaracion variables-----#
salir=False
tablet=Tablet("Samsung",23.5,2)

#-----Main-----#
while(salir==False):
    print("1. Enceder tablet")
    print("2. Apagar tablet")
    print("3. Instalar app")
    print("4. Desinstalar app")
    print("5. Mostrar apps instaladas")
    print("S. Salir")
    match(input("Que quieres hacer? ")):
        case "1":
            print(tablet.power_on())
        case "2":
            print(tablet.power_off())
        case "3":
            if tablet.status:
                appUser=input("Que app vas a instalar? ")
                print(tablet.install_app(appUser))
            else:
                print("La tablet esta apagada")
        case "4":
            if tablet.status:
                appUser=input("Que app vas a desinstalar? ")
                print(tablet.uninstall_app(appUser))
            else:
                print("La tablet esta apagada")
        case "5":
            if tablet.status:
                tablet.show_apps()
            else:
                print("La tablet esta apagada")
        case "S":
            salir=True
        case _:
            print("Esa no es una opcion valida")
    os.system("pause")
    os.system("cls")