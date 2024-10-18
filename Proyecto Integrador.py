#Librerías necesarias
import requests
#CONVERTIDOR DE MONEDAS
#Se usa requests para poder proceder con la API, 

apiKey = '674d77136b883c339c4f77dd' #Esta es mi API key personal

def obtenerTasas():
    url = 'https://v6.exchangerate-api.com/v6/674d77136b883c339c4f77dd/latest/USD' #Al abrir este link salen los rates de dólar a otras monedas
    respuesta = requests.get(url)
    datos = respuesta.json()
    if respuesta.status_code!= 200: #este código de estatus significa que el request con get fue exitoso
        #en este link explica como tal como funciona: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200
        print('Hubo un error en la recuperación de los datos')
        return None
    return datos['conversion_rates'] #esto es lo que nos interesa realmente de datos

def operacionMatematica(cantidad, origen, tasas,destino):
    if origen!='USD': #si el origen es distinto de dólares, usa la tasa de la moneda origen
        cantidad = cantidad / tasas[origen]
    return cantidad*tasas[destino]
        
#TABLA DE AMORTIZACIÓN
def tablaAmortizacion(monto,interes,meses):
    tabla=[] #Crea una tabla vacía para ahí poner los strings correspondientes a cada periodo
    saldo=monto #Con el monto inicia la operación
    interes=(interes/12)/100 #Al ser una tabla de amortización mensual, se divide el interés anual y luego entre 100 para pasarlo a decimal
    cuota=(monto*interes)/(1-(1+interes)**(meses*-1)) #Usando la fórmula de cuota=(capital*interés)/(1-(1+interés)^(-meses))

    tabla.append('Periodo, Cuota, Pago de Interés, Amortización, Saldo\n') #Encabezados de la tabla
    for mes in range(meses):
        if mes==0:
            fila0=f'{mes},-,-,-,${saldo}\n' #Caso especial del inicio, sólo hay saldo
            tabla.append(fila0)
        else: #Fuera del caso inicial
            pagoInteres=saldo*interes
            amortizacion=cuota-pagoInteres
            saldo=saldo-amortizacion
            fila=f'{mes},${cuota},${pagoInteres},${amortizacion},${saldo}\n'
            tabla.append(fila)
            
    with open('amortizacion.csv','w+') as file: #Abre o crea el archivo en caso de que no exista
        file.writelines(tabla)
    return 'El proceso fue exitoso y el resultado de la tabla de amortización se encuentra en el archivo "amortizacion.csv"'
    
def inversion(capital_inicial,periodos,interes):
    tasadecimal=interes/100
    tabla=[] #Crea una tabla vacía para ahí poner los strings correspondientes a cada periodo
    tabla.append('Periodo, Capital Inicial, Intereses, Capital Final \n') #Encabezado de la tabla
    capital_anterior=capital_inicial
    for i in range(1,periodos+1): #iteración para agregar los datos actualizados como texto a tabla
        intereses=tasadecimal*capital_anterior
        capital_nuevo=capital_anterior+intereses
        fila=f'{i},${capital_anterior},${intereses},${capital_nuevo}\n'
        tabla.append(fila)
        capital_anterior=capital_nuevo
    with open('inversion.csv','w+') as file:
        file.writelines(tabla)
    return 'El proceso fue exitoso y el resultado de la inversión se encuentra en el archivo "inversion.csv"'

def menu():
    print('Bienvenido al simulador bancario')
    print('')
    print('Estas son las opciones disponibles:')
    print('1. Convertidor de monedas')
    print('2. Tabla de amortización')
    print('3. Simulador de inversión (interés capitalizado)')
    print('4. Salir')
    print('')

def main():
    inicia=True
    while inicia==True:
        menu()
        opcion=int(input('Selecciona una opción de la lista: '))
        if opcion==1:
            tasas = obtenerTasas()
            cantidad = float(input('Cantidad a convertir: '))
            origen = str(input('Moneda de origen: '))
            destino = str(input('Moneda destino: '))
            origen = origen.upper() #Pone en mayúsculas el input
            destino = destino.upper() #Pone en mayúsculas el input
            if destino not in tasas or origen not in tasas: #Validación de inputs
                print('Error, la moneda de origen o destino ingresada es incorrecta. Reinicia el simulador')
            else:
                resultado= operacionMatematica(cantidad,origen,tasas,destino)
                print(f'{cantidad} {origen} son {resultado:.2f} {destino} con el tipo de cambio actual')
        elif opcion==2:
            monto=int(input('Monto del préstamo: '))
            meses=int(input('Meses: '))
            interes=int(input('Tasa de interés anual: '))
            print(tablaAmortizacion(monto,interes,meses)) #Display del mensaje de ejecución exitosa
        elif opcion==3:
            capital_inicial=int(input('Monto a invertir: '))
            periodos=int(input('Años: '))
            interes=int(input('Tasa de interés anual: '))
            print(inversion(capital_inicial,periodos,interes)) #Display del mensaje de ejecución exitosa
        elif opcion==4: #Fin del programa
            print('Hasta pronto')
            inicia=False
        else: #Validación de inputs
            print('La opción seleccionada no es válida, reintenta con una opción del menú')
            inicia=False

main()    