#Média dos salários
#Valores do Maior e do Menor salário
#Nome dos colaboradores que tem o maior e o menor salário
#O programa deve terminar quando digitar fim.

nome = input("Digite seu nome: ") 
media = 0
menor = 10000000
nomemaior = ""
nomemenor = ""
maior = 0
c = 0
while nome != "fim":
    s = 0
    salario = input("Digite seu salário: ")
    salario = float(salario)

    if salario < menor:
        menor = salario
        nomemenor = nome
    print("O menor salário é: ", menor, "do(a):", nomemenor)    

    if salario > maior:
        maior = salario
        nomemaior = nome
    print("O maior salário é: ", maior, "do(a):", nomemaior)

    nome = input("Digite seu nome:" )
    s = s + salario
    c = c + 1

media = s / c

print ("A média salarial dos funcionários é: ", media)