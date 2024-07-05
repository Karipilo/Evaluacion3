import funciones as f
jugadores=[]
jugador={}

opcion=0
while opcion !=4:
    opcion=f.menu()
    if opcion==1:
        f.registrar()
    if opcion==2:
        f.listar()
    if opcion==3:
        f.imprimir()