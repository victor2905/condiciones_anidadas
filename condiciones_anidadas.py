print("*********")
print("Conversor")
print("*********")
print("\n")
print("---Siga las instrucciones---")

print("Presione 1. Si desea convertir de número a palabras")
print("Presione 2. Si desea convertir de palabras a número")
print("Presione 3. Si desea salir de conversor\n")
print("Nota: debe definirse valores entre 1 y 10")

parametro = int(input("Ingrese el parámetro deseado: "))

if parametro == 1:
    numero_letra = int(input("¿Cuál es el número que desea convertir en palabras? "))
    if numero_letra == 1:
        print("UNO")
    elif numero_letra == 2:
        print("DOS")
    elif numero_letra == 3:
        print("TRES")
    elif numero_letra == 4:
        print("CUATRO")
    elif numero_letra == 5:
        print("CINCO")
    elif numero_letra == 6:
        print("SEIS")
    elif numero_letra == 7:
        print("SIETE")
    elif numero_letra == 8:
        print("OCHO")
    elif numero_letra == 9:
        print("NUEVE")
    elif numero_letra == 10:
        print("DIEZ")
elif parametro == 2:
    letra_numero = input("Ingrese en palabras, número a convertir ")
    letra_numero = letra_numero.upper()
    if letra_numero == "UNO":
        print(str(1))
    elif letra_numero == "DOS":
        print(str(2))
    elif letra_numero == "TRES":
        print(str(3))
    elif letra_numero == "CUATRO":
        print(str(4))
    elif letra_numero == "CINCO":
        print(str(5))
    elif letra_numero == "SEIS":
        print(str(6))
    elif letra_numero =="SIETE":
        print(str(7))
    elif letra_numero == "OCHO":
        print(str(8))
    elif letra_numero == "NUEVE":
        print(str(9))
    elif letra_numero == "DIEZ":
        print(str(10))
