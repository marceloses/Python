class cachorro:
    def __init__(self, nome,raca,tamanho):
        print("Inicializando a classe...")
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho

    def __del__(self):
        print("Removendo a instancia da classe: ")

    def latir(self):
        print("Uauauauauauuauau, Uauauauua: ")

def criar_cachorro():
    c = cachorro("Zeus","Preto",False)
    print(c.nome)

#c = cachorro("Preto","Shitzu")
#c.latir()
criar_cachorro()
    

        