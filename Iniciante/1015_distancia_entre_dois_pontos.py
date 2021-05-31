entrada_1 = input().split()
entrada_2 = input().split()

x1, y1 = entrada_1
x2, y2 = entrada_2

distancia = (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2))
saida = distancia ** (1/2)
print(f"{saida:.4f}")
