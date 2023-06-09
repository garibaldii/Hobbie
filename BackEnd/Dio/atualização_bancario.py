import textwrap#

def menu(): #\t é utilizado para criar um espaçamento horizontal na saída de texto ou em strings.
    menu = '''\n
    ==================== MENU ====================
    [D]\tDepositar 
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova Conta
    [LC]\tListar Contas
    [NU]\tNovo Usuário
    [Q]\tSair
    ->'''
    return input(textwrap.dedent(menu))   #retorna qual opção o usuário digitou

def depositar(saldo, valor, extrato, /): # A barra de separação posicional indica a sequência esperada dos parâmetros na chamada da função. 
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@@ Operação falhou! O valor informado é inválido. @@@")
        
    return saldo, extrato

def sacar(*, saldo, valor, saque, extrato, limite, numero_saques, limite_saques): #o adicionar o "*", indica-se que todos esses parâmetros são obrigatórios e devem ser fornecidos como argumentos nomeados ao chamar a função. 
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operação Falhou! você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação Falhou! o valor de saque excede o limite. @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação Falhou! Número máximo de saques excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação Falhou! O valor informado é inválido. @@@")
    
    return saque, extrato

def exibir_extrato(saldo, / , * , extrato):
    
    
    print("\n==================== EXTRATO ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato ) #operador tenário, verifica se a variável extrato está vazia (ou seja, não contém nenhuma movimentação registrada). Se extrato estiver vazio, a expressão not extrato será avaliada como True, e a mensagem "Não foram realizadas movimentações." será impressa.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(SOMENTE NÚMERO): ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuário criado com sucesso! ====")

def filtrar_usuario(cpf, usuarios): #compreensão de lista para percorrer a lista de usuários e criar uma nova lista chamada usuarios_filtrados. A compreensão de lista é uma forma concisa de criar uma nova lista a partir de outra, aplicando uma condição. No caso dessa compreensão de lista, ela itera sobre cada usuario na lista usuarios e verifica se o valor da chave "cpf" desse usuario é igual ao CPF especificado. Se a condição usuario["cpf"] == cpf for verdadeira, o usuario é adicionado à lista usuarios_filtrados.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None #Em seguida, o código return usuarios_filtrados[0] if usuarios_filtrados else None faz o retorno da função. Se a lista usuarios_filtrados não estiver vazia (ou seja, houver pelo menos um usuário encontrado com o CPF especificado), ele retorna o primeiro usuário encontrado, acessando o elemento de índice zero da lista usuarios_filtrados. Caso contrário, se usuarios_filtrados estiver vazia, o valor retornado é None, indicando que nenhum usuário com o CPF especificado foi encontrado.

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f""\
            'Agência:\t{conta['agencia']}
            