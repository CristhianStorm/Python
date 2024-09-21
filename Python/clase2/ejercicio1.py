'''
Crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par o si
ambos los on
'''
n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese otro: "))

if ((n1%2 ==0) and (n2%2 ==0)):
    print("Ambos son pares")
elif ((n1%2 ==0) and (n2%2 !=0)):
    print(f"{n1} es par")
    print(f"{n2} es impar")
elif ((n1%2 !=0) and (n2%2 ==0)):
    print(f"{n1} es impar")
    print(f"{n2} es par")
else:
    print("Los dos numeros son impares")
