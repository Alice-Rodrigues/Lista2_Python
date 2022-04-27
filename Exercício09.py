#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

lista = [numero1, numero2, numero3]

lista.sort(key=float, reverse=True)

print("decrescente: ", lista)
