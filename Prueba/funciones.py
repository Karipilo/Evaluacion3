jugadores=[]

def menu():
    while True:
        print("*****Menú eShirlitos*****")
        print("1.Registrar puntajes torneo")
        print("2.Listar todos los puntajes")
        print("3.Imprimir por Tipo")
        print("4.Salir del programa")
        print("---------------------")
        while True:
            opcion=int(input("Ingrese su opcion:"))
            try:
                if 1<= opcion <=4:
                    break
                else:
                    print("Opcion no valida")
            except:
                print("Se espera que ingrese numeros")
        return opcion
    
def registrar():
    id_jugador=input("Ingresa ID del jugador: ").lower()
    nombre=input("Ingresa nombre y apellido del jugador: ").lower()
    valorant=int(input("Ingresa puntaje en VALORANT: "))
    fornite=int(input("Ingresa puntaje en FORTNITE: "))
    fifa=int(input("Ingresa puntaje en FIFA: "))
    tipo=input("Ingresa tipo de jugador (Principiante - Avanzado - Experto): ").lower()

    jugador={
        "id_jugador":id_jugador,
        "nombre":nombre,
        "valorant":valorant,
        "fortnite":fornite,
        "fifa":fifa,
        "tipo":tipo
    }
    jugadores.append(jugador)
    print(jugador)
    print("Datos guardados correctamente")

def listar():
    print("ID\tNombret\tValorant\tFortnite\tFifa\tTipo")
    for jugador in jugadores:
        print(f"{jugador["id_jugador"]}\t{jugador["nombre"]}\t{jugador["valorant"]}\t{jugador["fortnite"]}\t{jugador["fifa"]}\t{jugador["tipo"]}")

def imprimir():
    tipo=input("Ingresa tipo de jugador (Principiante - Avanzado - Experto): ").lower()
    jugador_ok=[jugador for jugador in jugadores if jugador["tipo"]==tipo]
    if not jugador_ok:
        print("No se encontro este tipo de jugador")

    nombre_archivo=f"{tipo}.txt"
    with open(nombre_archivo,"w") as archivo:
        archivo.write("ID\tNombret\tValorant\tFortnite\tFifa\tTipo\n")
        for jugador in jugadores:
            archivo.write(f"{jugador["id_jugador"]}\t{jugador["nombre"]}\t{jugador["valorant"]}\t{jugador["fortnite"]}\t{jugador["fifa"]}\t{jugador["tipo"]}\n")
    print(f"Los puntajes de los jugadores estan almacenados en {tipo} y se guardaron en {nombre_archivo} ")











        




        














       # ∕  {}