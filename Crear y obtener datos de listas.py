import random

def creaLista(s,m):
    #donde s es el tamaño de la lista y m el valor máximo
    lista = []
    for i in range (s):
        #va dentro del for para que se repita la instrucción size veces
        numAleatorio = random.randint(-m,m)
        lista.append(numAleatorio)
    return lista

def imprimeLista(A):
    for i in range (len(A)):
        print(f'lista [{i}] = {A[i]}')

def multiplosLista(A,x):
    lista = []
    for i in range(len(A)):
        residuo = A[i]%x
        # si la lista es de 3 números evalúa para 0, 1 y 2 entonces con la A[i] referencia a un elemento particular de la lista
        #si se hiciera con for i in A, no referenciaría al elemento de la lista y por eso no pondría el índice y solo el número 
        if  residuo==0:
            lista.append(i)
    return lista

def sumaLista(A):
    suma=0
    for i in range(len(A)):
        suma+=A[i]
    return suma

def menorLista(A):
    #se podría hacer con min?????
    minimo = A[0]
    #se le asigna primero el valor de A[0] a mínimo porque se espera siempre un valor inicial en la lista
    for i in A:
        #para i (un número) en cada número de la lista
        if i < minimo:
            #se sigue la misma lógica de comparación que para encontrar el número menor en una lista de inputs
            minimo = i
            #si i es menor a minimo, el nuevo valor de minimo es i y se compara con el resto de números en la lista
    return minimo
        
def menu():
    print('1. Imprime')
    print('2. Múltiplos')
    print('3. Suma')
    print('4. Menor')
    print('5. Salir')
    print('')
    
def main():
    t = int(input('Introduce el tamaño de la lista: '))
    x = int(input('Introduce un número para el rango de la lista: '))
    print('')
    A = creaLista(t,x)
    sigue = True
    
    while sigue == True:
        menu()
        opcion = int(input('Introduce una opción: '))
        if opcion == 1:
            imprimeLista(A)
            
        elif opcion == 2:
            x = int(input('Introduce el número para ver si tiene múltiplos en la lista: '))
            print(multiplosLista(A,x))
            
        elif opcion == 3:
            print(sumaLista(A))
        
        elif opcion == 4:
            print(menorLista(A))
            
        elif opcion == 5:
            print('Nos vemos')
            sigue = False
            
        else:
            print('ERROR. OPCIÓN INCORRECTA')
            sigue = False

main()