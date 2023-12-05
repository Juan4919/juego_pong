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
"""
def mover_mano()->str:
    return "Derecha"


def recibirMano(mano):
    if mano == "izquierda":
        print("Zurda")
    else:
        print("Derecha")

recibirMano( mover_mano() )            
"""
"""
def nombres(apellido):
    return "Jose Alfredo "+apellido

def apellidos(apellidos):
    return apellidos

nombres_apellidos = nombres( apellidos("Perez Ruiz") )
print(nombres_apellidos)
"""
file_imagenes = {
            "drcha":["electric00_drcha.png","electric01_drcha.png","electric02_drcha.png"],
            "izqda":["electric00_izqda.png","electric01_izqda.png","electric02_izqda.png"]
        }

lado= "drcha"


def pruebita(lado):
    imagenprueba={}
    for lado in file_imagenes:
        imagenprueba[lado]=[]
        for nombre_fichero in file_imagenes[lado]:
            imagen = f"pongapp/images/raquetas/imagen00"
            imagenprueba[lado].append(imagen)
    return imagenprueba   

respuesta= pruebita(lado)

