import math

reiniciar = True

while reiniciar:
    painel_total = int(input("Digite a quantidade de painéis do seu kit solo: "))
    fila = int(input("Digite quantas filas você vai distribuir esses painéis: "))
    
    placas_necessarias = 0
    
    if painel_total % 2 == 0:
    
        for i in range(1, fila + 1):
            qtd_painel = int(input(f"Digite a quantidade de painel que será distribuida na fila {i}: "))
            
            if qtd_painel > painel_total:
                print("@@@ \nVocê excedeu a quantidade total do kit @@@")
                break
            
            
                