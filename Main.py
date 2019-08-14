#definiendo metodo para hacer el ciclo de perdir un numero entero en la opcion del menu
from Mapeo import Graphviz
salir = False
opcion = 0

def pedir_numero_entero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Elige la opcion: "))
            correcto = True
        except:
            ("Introduce la opcion correcta! ")      
    return num

if __name__ == '__main__':
    #ciclo de opciones dependiente de la opcion a elegir
    map = Graphviz()  
    while not salir:    
        print("")
        print ("-----------------Menu------------------")
        print("1    Mapeo por filas")
        print("2    Mapeo por columnas")
        print("3    Salir")
        opcion =  pedir_numero_entero()

        if opcion == 1:
            fila = int(input('Ingrese la fila: '))
            columna = int(input('Ingrese la columna: '))
            posFila = int(input('Ingrese posicion en fila: '))
            posColumna = int(input('Ingrese posicion en columna: '))
            k = int(posFila*columna+posColumna)
            map.generar_grafico(fila, columna, posFila, posColumna, k, "Mapeo_fila")
        elif opcion == 2:
            fila = int(input('Ingrese la fila: '))
            columna = int(input('Ingrese la columna: '))
            posFila = int(input('Ingrese posicion en fila: '))
            posColumna = int(input('Ingrese posicion en columna: '))
            k = int(posColumna*fila+posFila)
            map.generar_grafico(fila,columna,posFila,posColumna, k, "Mapeo_columna")
        elif opcion == 3:
            salir = True
        else:                   
            print("Introduce un numero entre 1 y 5")
    print("Programa terminado!!")



   