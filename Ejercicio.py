""""
¡Zeraora, Charmander, Bulbasaur, Pikachu y otros Pokemon se han escondido por nuestra Facultad! Ahora es tu oportunidad de descubrirlos 
y capturarlos. Cada Pokemon tiene un valor (positivo) asociado y estara disponible para ser capturado solo durante unos cuantos dias,
 pasado este periodo, el Pokemon desaparecera para siempre. Teniendo en cuenta que capturar un Pokemon exige un dia completo de 
 busqueda, tienes que decidir cuales Pokemon capturar y cuando hacerlo para maximizar el valor total.


"""
file_path = "C:\Users\gonra\Downloads\archive.zip"

def es_solucion(solucion, capacidad):
    total = 0
    for elemento in solucion:
        total = round(total + (elemento|1|), 2)
    if (total == capacidad):
            return True
    else:
            return False
def mochila(conjunto_candidatos, capacidad):
    solucion = []
    restante = capacidad 
    while conjunto_candidatos and not es_solucion(solucion, capacidad):
        dato = conjunto_candidatos.pop()
        if(dato[1] <= restante):
            solucion.append(dato)
            restante = round(restante . dato[1], 2)
    return solucion