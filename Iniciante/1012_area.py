entrada = input().split()
a, b, c = entrada
pi = 3.14159
raio = float(c)

area_triangulo = (float(a) * float(c)) / 2  # a
area_circulo = pi * raio ** 2  # b
area_trapezio = ((float(a) + float(b)) / 2) * float(c)  # c
area_quadrado = float(b) ** 2
area_retangulo = float(a) * float(b)

print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")
