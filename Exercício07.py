#Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

lista_dos_numeros = [numero1, numero2, numero3]

print("Menor número: ", min(lista_dos_numeros), "\nMenor número: ", max(lista_dos_numeros))
