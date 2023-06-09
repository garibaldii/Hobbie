from time import sleep
import math

fila = int(input("Quantas fileiras serão feitas? "))

soma_pe = 0
soma_trilho_painel = 0
soma_painel = 0
soma_conector = 0
soma_parafuso_m8 = 0
soma_chumbador = 0
soma_juncao = 0
soma_grampo_final = 0
soma_grampo_intermediario = 0

for f in range(1, fila + 1):
    while True:
        qtd_painel = int(input(f"\nQuantos painéis na fileira {f}: "))
        if qtd_painel % 2 == 0 and qtd_painel >= 4:
            break
        else:
            print("Estrutura solo só pode ser montada com número par de painéis")
    
    soma_painel += qtd_painel
    trilho_painel = qtd_painel * 2.5
    juncao_perfil = (trilho_painel / 6.4)
    pe = qtd_painel / 2
    conector = pe - 1
    parafuso_m8 = conector * 2
    chumbador = pe * 4
    grampo_final = fila * 8
    grampo_intermediario = (qtd_painel - 1) * 2

    soma_trilho_painel += trilho_painel
    soma_pe += pe
    soma_conector += conector
    soma_parafuso_m8 += parafuso_m8
    soma_chumbador += chumbador
    soma_juncao += juncao_perfil
    soma_grampo_intermediario += grampo_intermediario

    print("----------------------------------------------")
    print(f"Fila {f}:")
    print(f"Quantidade de painéis: {qtd_painel}")
    print(f"Quantidade de pés na fileira: {pe}")
    print(f"Quantidade de conector necessária: {conector}")
    print(f"Quantidade de metros de trilho necessários: {trilho_painel}")
    print(f"Quantidade de grampo final: 8")
    print(f"Quantidade de grampo intermediário: {grampo_intermediario}")
    print(f"Quantidade de junção: {juncao_perfil}")
    print(f"Quantidade de chumbador/ parabolt 75mm 3/8: {chumbador}")
    print(f"Quantidade de parafuso m8: {parafuso_m8}")
    print("----------------------------------------------")

for tempo in range(2):
    print("\n...")
    sleep(1)
print("\nPronto!")
sleep(1)

print(f"\nQuantidade total de painéis: {soma_painel}")
print(f"Quantidade total de pés: {soma_pe}")
print(f"Quantidade total de travessas (conector): {soma_conector}")
print(f"Quantidade total de metragem de trilhos: {math.ceil(soma_trilho_painel)}")
print(f"Quantidade total de grampo final: {grampo_final}")
print(f"Quantidade total de grampo intermediários: {soma_grampo_intermediario}")
print(f"Quantidade total de junção: {soma_juncao}")
print(f"Quantidade total de chumbador/ parabolt 75mm 3/8: {soma_chumbador}")
print(f"\nQuantidade total de parafusos M8: {soma_parafuso_m8}")