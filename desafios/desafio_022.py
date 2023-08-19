nome = input("Informe seu nome completo:").strip()
print(f"Seu nome em letras maiúsculas é: {nome.upper()}")
print(f"Seu nome em letras minúsculas é: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)- nome.count(' ')} de caracteres")
print(f"O primeiro nome tem {nome.find(' ')} letras")

