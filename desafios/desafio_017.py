from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca  = float(input("Comprimento do cateto adjacente: "))
hi =  (co ** 2 + ca** 2) ** (0.5)
hiMath = hypot(co,ca)
print(f"A Hipotenusa vai medir {hi:.2f}")
print(f"A Hipotenusa vai medir usando math {hiMath:.2f}")