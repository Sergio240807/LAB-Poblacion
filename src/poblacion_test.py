from poblacion import * 
def lee_poblaciones_test(poblaciones):
    print('Prueba de poblaciones: ')
    print(poblaciones[:3])
    print(poblaciones[-3:])

def calcula_paises_test(poblaciones):
    print('Test calcula paises: ')
    paises = calcula_paises(poblaciones)
    print(paises)

def filtra_por_pais_test(poblaciones,nombre_o_codigo):
    print('Test filtra por pais: ')
    filtro_pais = filtra_por_pais(poblaciones,nombre_o_codigo)
    print(filtro_pais)

def filtra_por_paises_y_anyo_test(poblaciones,anyo,paises):
    print('Test filtra por paises y años: ')
    filtro_paises_y_anyos = filtra_por_paises_y_anyo(poblaciones,anyo,paises)
    print(filtro_paises_y_anyos)

def muestra_evolucion_poblacion_test(poblaciones,nombre_o_codigo):
    print('Test muestra evolucion poblacion: ')
    prueba = muestra_evolucion_poblacion(poblaciones,nombre_o_codigo)
    print(prueba)
def muestra_comparativa_paises_anyo_test(poblaciones,anyo,paises):
    print('Test muestra comparativa paises y año: ')
    prueba = muestra_comparativa_paises_anyo(poblaciones,anyo,paises)
    print(prueba)
if __name__=='__main__':
    poblaciones = lee_poblaciones('data/population.csv')
    lee_poblaciones_test(poblaciones)
    calcula_paises_test(poblaciones)
    filtra_por_pais_test(poblaciones,"Arab World")
    filtra_por_paises_y_anyo_test(poblaciones,'2016','Spain')
    muestra_evolucion_poblacion_test(poblaciones,'Arab World')
    muestra_comparativa_paises_anyo_test(poblaciones,'2010','Arab world')