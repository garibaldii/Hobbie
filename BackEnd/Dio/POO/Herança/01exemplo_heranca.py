# # Herança simples -> Quando a classe filha herda apenas uma classe pai;
# # Herança Múltipla -> Quando uma classe filha herda várias classes pai.

# Herança Simples:
#     class a:
#         pass
#     class b:
#         pass
#     class c(a, b): Herança Múltipla, estende de duas classes, filha de 'a' e 'b'.
#         pass


#Exemplo:

    
class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor!")
    
    def __str__(self):
        return self.cor
        
           
class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim, estou carregado' if self.carregado == True else 'Não estou carregado'}") 


# Moto = motocicleta("Preta", "ABC1234", 2)
# Moto.ligar_motor()

# Carro = carro("Branco", "XDE0098", 4)
# Carro.ligar_motor()

Caminhao = caminhao("Roxo", "GFD8712", 8, False)
Caminhao.ligar_motor()
Caminhao.esta_carregado()
print(Caminhao)