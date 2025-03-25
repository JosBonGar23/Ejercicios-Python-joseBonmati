# coding=utf-8
__Author__="José Gaspar Sánchez García"


# Función que determina si un numero es primo.

def fibonacci(n) :
    vector = []

    if n<1 :
        return vector
    elif n==1 :
        vector.append(1)
        return vector
    elif n >= 2:
        # Primeros dos valores de la serie de Fibonacci
        vector.append(1)
        vector.append(1)

        # Bucle para completar la serie
        for i in range(2, n):
            siguiente = vector[i - 1] + vector[i - 2]
            vector.append(siguiente)
        
    elif n==1 :
        vector[0]=1

    return vector; # Retorno de la función

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero=int(input("Introduzca un numero: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero,fibonacci(numero)))

if __name__== "__main__" :
   main()
