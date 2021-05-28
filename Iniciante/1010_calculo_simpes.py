produto1 = input().split()
produto2 = input().split()

codigo, qtd, preco = produto1
codigo2, qtd2, preco2 = produto2

valor_total = (int(qtd)) * float(preco) + (int(qtd2)) * float(preco2)

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
