numero = int(input("Informe o numero de 0 a 9999:"))
u = numero % 10
d = numero //10 % 10
c = numero // 100 % 10
m = numero //1000 %10
print(f"Analisando o número {numero}")
print(f"Unidade: {u} ")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")