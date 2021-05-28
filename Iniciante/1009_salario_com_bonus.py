nome_vendedor = input()
salario_fixo = float(input())
vendas_no_mes = float(input())

valor_comissao = vendas_no_mes * 0.15
total = salario_fixo + valor_comissao

print(f"TOTAL = R$ {total:.2f}")
