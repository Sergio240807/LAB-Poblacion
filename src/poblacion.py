from collections import namedtuple
import csv
from matplotlib import pyplot as plt
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta_fichero):
    poblaciones = []
    with open(ruta_fichero,encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais,codigo,año, censo)
            poblaciones.append(tupla)
    return poblaciones

def calcula_paises(poblaciones):
    paises = set()
    for e in poblaciones:
        paises.add(e.pais)
    return sorted(paises)


def filtra_por_pais(poblaciones, nombre_o_codigo):
    datos_pais = []
    for e in poblaciones:
        if nombre_o_codigo == e.pais or nombre_o_codigo == e.codigo:
            datos_pais.append((e.año, e.censo))
    return datos_pais


def filtra_por_paises_y_anyo(poblaciones, anyo,paises):
    lista_de_tuplas = []
    for e in poblaciones:
        if e.año == anyo and e.pais in paises:
            lista_de_tuplas.append((e.pais,e.censo))
    return lista_de_tuplas

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    titulo = 'Evolución de la población en ' + nombre_o_codigo
    filtra_por_paise = filtra_por_pais(poblaciones, nombre_o_codigo)  # Llamar a la función y almacenar el resultado
    lista_años = []
    lista_habitantes = []
    
    for año, censo in filtra_por_paise:  # Iterar sobre el resultado de la función
        lista_años.append(año)
        lista_habitantes.append(censo)
    
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    titulo = "Población en el año " + str(anyo)
    filtra = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    lista_paises = []
    lista_habitantes = []
    for pais,censo in filtra:
        lista_paises.append(pais)
        lista_habitantes.append(censo)
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()