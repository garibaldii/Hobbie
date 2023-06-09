contador = 0
conta = ""
saldo = 0
lista_usuarios = []

def depositar(x):
    global saldo
    global conta
    conta += (f"Depósito de {x:.2f}\n")
    saldo += x
    print("-----------------------")
    print()
    if x < 0:
        print("Digite um valor válido!")
        print()
    pass

def sacar(y):
    global saldo
    global conta
    if y > saldo:
        print("-----------------------------------------------------")
        print(f"Saldo insuficiente, você tem R${saldo} na sua conta")
        print("-----------------------------------------------------")
        print()
    elif y > 500:
        print("Não ultrapasse o limite diário de R$500,00")
    else:
        conta += (f"Saque de {y:.2f}\n")
        saldo -= y
        print("-----------------------")
        print()
        pass

def extrato():
    print("---------Extrato----------")
    print()
    print(conta)
    print(f"Saldo Total: R${saldo}")
    print("--------------------------")
    
def intro():
    print("-----------------------")
    print("Banco Bank ")
    print()
    print("1- Depósito")
    print("2- Saque")
    print("3- Extrato")
    print("-----------------------") 
    print()
    
while True:
    intro()
    escolha = float(input("O que deseja? Digite 0 para sair do menu: "))
    print()
    if escolha == 0:
        break

    if escolha == 1:
        print()
        x = float(input("Digite o valor para depositar: "))
        depositar(x)
            
    elif escolha == 2:
        print()
        contador += 1
        if contador <= 3:
            y = float(input("Digite o valor para sacar: "))
            sacar(y)
        if contador > 3:
            print()
            print("Você já usou seus três saques diários...")
            print()
            
    elif escolha == 3:
        extrato()
        break    