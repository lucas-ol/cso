import random


n1 = input("Informe o nome do primeiro aluno: ")
n2 = input("Informe o nome do segundo aluno: ")
n3 = input("Informe o nome do terceiro aluno: ")
n4 = input("Informe o nome do quarto aluno: ")

list = [n1, n2, n3, n4]
escolhido = random.choice(list)
print(f"O aluno escolhido foi {escolhido}")