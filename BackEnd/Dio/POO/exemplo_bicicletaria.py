class bike:
    
    def __init__(self, cor, modelo, ano, valor): #o self é uma referência explícita ao objeto. (esta é a instância do objeto que foi passado)
        self.cor = cor #'self.' se refere aos atributos da classe
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self): #métodos são funções dentro de uma classe!
        print(f"bi-bi")
        
    def parar(self): #métodos obrigatóriamente precisam de um argumento(self)
        print("Parou a bike")
    
    def correr(self):
        print(f"Pedalou a bike {self.modelo}")    
        
    def apresentacao(self):
        print(f"Sua bike é {self.modelo}, ano {self.ano}, cor {self.cor} e custa {self.valor}")

kaloi = bike("Vermelho", "kaloi", 2020, 5000)
kaloi.apresentacao()

kaloi.correr()

kaloi.buzinar()
