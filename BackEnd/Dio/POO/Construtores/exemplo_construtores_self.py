# métodos especiais são métodos usados para se referir a ações dentro de uma classe:
#     __init__; Método Inicializador, quando uma classe é inicializada. 
#     __del__; Método Destrutor, quando uma instância/objeto é destruído 

class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        print("Inicizalizando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instância...")
    
    def falar(self):
        print("au au")
        
def criar_cachorro():
    c = Cachorro("Aladim", "Branco e Preto", False)
    print(c.nome)
    return c
        
# c = Cachorro("Rex", "Amarelo")
# c.falar()

criar_cachorro() 