class cachorro:
    def __init__(self,nome,cor,acordando=True):
        self.nome = nome
        self.cor = cor
        self.acordando = acordando

    def latir(self):
        print("Suaua")
    
    def dormir(self):
        self.acordando = False
        print('zzzzzzz...')
