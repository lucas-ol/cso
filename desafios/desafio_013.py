salario = float (input("Qual é o salario do funcionário? R$"));

novo = salario + (salario * 0.15)
print(f"O funcionário recebia R${salario:.2f}, com 15% de aumento ele passa a receber R${novo:.2f}")