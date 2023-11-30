"""
from figura_class import Raqueta,Pelota
from pantallas import Partida

juego=Partida()
juego.bucle_fotograma()
"""
"""
objetoRaqueta = Raqueta(0,500)

objetoPelota = Pelota(0,300)

print( objetoRaqueta.derecha )
print( objetoRaqueta.izquierda )
print( objetoRaqueta.arriba )
print( objetoRaqueta.abajo )
print("#######################")
print( objetoPelota.derecha )
print( objetoPelota.izquierda )
print( objetoPelota.arriba )
print( objetoPelota.abajo )


def datosPersonales(*parametros):
    for datos in parametros:
        print(datos)


datosPersonales("Jose","Martinez",25,True,[1,2,3])
"""

def mover_mano()->str:
    return "Derecha"


def recibirMano(mano):
    if mano == "izquierda":
        print("Zurda")
    else:
        print("Derecha")

recibirMano( mover_mano() )            