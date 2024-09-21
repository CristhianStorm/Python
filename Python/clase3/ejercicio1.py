def ingresar_numeros():
    numeros = []
    while True:
        numero = input("Ingrese un número (o 'n' para terminar): ")
        if numero.lower() == 'n':
            break
        numeros.append(float(numero))
    return numeros

def sumar_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def calcular_promedio(numeros):
    suma = sumar_numeros(numeros)
    promedio = suma / len(numeros)
    return promedio

def encontrar_max_min(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    return maximo, minimo

def numeros_mayores_que_promedio(numeros, promedio):
    mayores = [numero for numero in numeros if numero > promedio]
    return mayores

def main():
    numeros = ingresar_numeros()
    if len(numeros) == 0:
        print("No se ingresaron números.")
        return
    
    suma = sumar_numeros(numeros)
    promedio = calcular_promedio(numeros)
    maximo, minimo = encontrar_max_min(numeros)
    mayores = numeros_mayores_que_promedio(numeros, promedio)
    
    print(f"\nNúmeros ingresados: {numeros}")
    print(f"Suma de los números: {suma}")
    print(f"Promedio de los números: {promedio}")
    print(f"Número más grande: {maximo}")
    print(f"Número más pequeño: {minimo}")
    print(f"Números mayores que el promedio: {mayores}")

if __name__ == "__main__":
    main()
