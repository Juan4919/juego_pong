from figura_class import Raqueta,Pelota

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
"""

def datosPersonales(*parametros):
    for datos in parametros:
        print(datos)


datosPersonales("Jose","Martinez",25,True,[1,2,3])
