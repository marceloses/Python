
'''

'''

class jiu_jitsu:
    # def > explicita a definição da função naquele ponto
    # : indica que o código está identado abaico da função
    # __init__ > chamada de "método construtor" possui a responsabilidade de criar o objeto daquela classe
    def __init__(self,kimono,rasghurd,faixa):
        self.kimono = kimono
        self.rasguard = rasghurd
        self.faixa = faixa 

        # Definindos os metodos, os metodos são funcções que estão dentreo uma classe, e passamos os argumentos
        # Self > passando o primeiro argumanto
    def exercicio(self):
            print("Aquecimento! ")
        
    def lutas(self):
            print("Finalizacao... ")

    def equipes(self):
            print("Competindo! ")

    def __str__(self):
          return f"jiu_jitsu: kimono={self.kimono}, rasquard={self.rasguard},exercicio={self.faixa}"


    # Preciso instanciar o meu objeto, pra isso eu uso uma variavel e instancio o meu objeto na classe
#jiu = jiu_jitsu("Branco","Azul","Preta")
#jiu.exercicio()
#jiu.lutas()
#jiu.equipes()

jiu_1 = jiu_jitsu ("Amarelo," ," Cinza"," Rosa")
print(jiu_1)

  
      

