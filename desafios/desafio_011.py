width = float(input("Informe a largura da parede metros: "));
height = float(input("Informe a altura em metros: "));

area = width * height;
paint = area /2;
print(f"Sua parede tem a dimensão de {width}x{height} e sua area é de {area}m²");
print(f"Para pintar essa parede vocẽ precisa de {paint} litros de tinta.");