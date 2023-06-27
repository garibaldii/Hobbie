#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

peca_1 = input()
peca_2 = input()

lista_1 = peca_1.split()
lista_2 = peca_2.split()

qtd_1 = int(lista_1[1])
qtd_2 = int(lista_2[1])

valor_1 = float(lista_1[-1])
valor_2 = float(lista_2[-1])

total = ((qtd_1 * valor_1) + (qtd_2 * valor_2))

print(f"VALOR A PAGAR: R$ {total:.2f}")