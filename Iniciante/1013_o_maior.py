entrada = input().split()
a, b, c = entrada

maior_ab = ((int(a) + int(b) + abs(int(a) - int(b))) / 2)
maior_bc = ((int(b) + int(c) + abs(int(b) - int(c))) / 2)

if maior_ab > maior_bc:
    print(f"{int(maior_ab)} eh o maior")
else:
    print(f"{int(maior_bc)} eh o maior")
