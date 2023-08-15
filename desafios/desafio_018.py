from math import cos,radians,sin,tan
ang = float(input ("Informe o ângulo que vc deseja: "))
rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print(f"O ângulo de {ang} tem o SENO de {seno:.2f}")
print(f"O ângulo de {ang} tem o COSSENO de {seno:.2f}")
print(f"O ângulo de {ang} tem a TANGENTE de {tangente:.2f}")