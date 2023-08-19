frase ="Teste testado"
print(f"O tamanho da string é {len(frase)}")
print(f"A quantidade de T é {frase.count('T')}")
print(f"O index do primeiro t é {frase.find('t')}")
print(f"Existe a palavra Tes {frase in 'teste'}")
print(f"Texto capitalize {frase.capitalize()} e title, {frase.title()}")
frase.strip()

print(frase.split("e").join("e"))
print(frase[2::2])
print(frase[:2])
print(frase[1:5:2])