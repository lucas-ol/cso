frase = input("Digite uma frase: ").strip()
print(f"A letra 'A' aparece {frase.lower().count('a')} vezes")
print(f"Ela aparece a primeira vez na posição {frase.lower().find('a')+1}")
print(f"A ultima letra 'A' aparece na posição {frase.lower().rfind('a')}")

