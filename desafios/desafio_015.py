dias = int(input("Quantos dias alugados?"));
km = float(input("Quantos Km ridados?"));

pago = dias * 60+(km*0.15);

print(f"O total a pagar é {pago}")