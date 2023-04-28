

valor_rs1 = [75, 85, 95, 125, "porto alegre"]
valor_rs2 = [85, 95, 105, 135]

estado = input("Qual estado? ")
cidade = input("Qual cidade?")
peso = int(input("Qual o peso? "))
nota_fiscal = int(input("Qual o valor da NF? "))

if estado == "sc":
    valor_sc1 = [46.43, 59.28, 66.93, 114.34, "florianopolis", "florianópolis"]
    valor_sc2 = [44.21, 56.45, 64.52, 98.00, "blumenau", "joinville", "jaraguá do sul", "jaragua do sul", "chapecó", "chapeco"]
    valor_sc3 = [46.43, 59.28, 66.93, 114.34]
    
    if cidade in valor_sc1:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_sc1[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_sc1[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_sc1[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_sc1[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.51 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
        
    elif cidade in valor_sc2:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_sc2[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_sc2[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_sc2[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_sc2[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.45 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
    else:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_sc3[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_sc3[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_sc3[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_sc3[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.51 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
elif estado == "pr":
    valor_pr1 = [36.84, 47.05, 53.77, 81.67,"curitiba", "pinhais", "são josé dos pinhais",  "sao josé dos pinhais", "são jose dos pinhais", "colombo"]
    valor_pr2 = [36.84, 47.05, 53.77, 81.67, "londrina", "cambé", "cambe", "maringá", "maringa", "apucarana", "arapongas", "sarandi"]
    valor_pr3 = [36.69, 49.40, 55.78, 95.28]
    
    if cidade in valor_pr1:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_pr1[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_pr1[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_pr1[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_pr1[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.45 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
         
    elif cidade in valor_pr2:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_pr2[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_pr2[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_pr2[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_pr2[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.45 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
        
    else:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_pr3[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_pr3[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_pr3[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_pr3[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.51 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)

elif estado == "ms":
    seguro = (0.005 * nota_fiscal)
    valor_ms1 = [40.62, 44.44, 58.57, 100.04, "campo grande"]
    valor_ms2 = [49.15, 62.76, 70.87, 121.01]
    if cidade in valor_ms1:
        pedagio = int(peso/100) * 7.8
        if peso < 30:
            valor_peso = valor_ms1[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_ms1[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_ms1[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_ms1[3]
        elif peso > 100:
            pedagio = int(peso/100) * 4.2
            valor_peso = (0.87 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
          
    else:
        seguro = (0.005 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_ms2[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_ms2[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_ms2[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_ms2[3]
        elif peso > 100:
            pedagio = int(peso/100) * 7.8
            valor_peso = (1.05 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
        
elif estado == "rs":
    seguro = (0.0065 * nota_fiscal)
    valor_rs1 = [75, 85, 95, 125, "porto alegre"]
    valor_rs2 = [85, 95, 105, 135]
    if cidade in valor_rs1:
        if peso < 30:
            valor_peso = valor_rs1[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_rs1[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_rs1[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_rs1[3]
        elif peso > 100:
            pedagio = int(peso/100) * 7.5
            valor_peso = (1.2 * peso) + pedagio
        valor_final = valor_peso + seguro
        print(valor_final)
    else:
        seguro = (0.0075 * nota_fiscal)
        if peso < 30:
            valor_peso = valor_rs1[0]
        elif peso > 30 and peso < 50:
            valor_peso = valor_rs1[1]
        elif peso > 50 and peso < 70:
            valor_peso = valor_rs1[2]
        elif peso > 71 and peso < 100:
            valor_peso = valor_rs1[3]
        elif peso > 100:
            pedagio = int(peso/100) * 7.5
            valor_peso = (1.5 * peso) + pedagio
            valor_final = valor_peso + seguro
            print(valor_final)
            