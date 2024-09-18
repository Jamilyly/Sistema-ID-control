import time
class cbv_meninas:
  #amigos construtor
    def __init__(self,nome,idade,peso,altura,carreira,medalhas):
  #atributos da classe
        self.Nome=nome
        self.Idade=idade
        self.Peso=peso
        self.Altura=altura
        self.Carreira=carreira
        self.Medalhas=medalhas


      
  
#métodos classe
    def imprime_Carta(self):
      print("*=*"*9)
      print(f"Nome:{self.Nome}")
      print(f"Idade da Jogadora:{self.Idade}Anos")
      print(f"Peso da Jogadora:{self.Peso}Kg")
      print(f"Altura da Jogadora:{self.Altura}m")
      print(f"Carreira da Jogadora:{self.Carreira}Anos")
      print(f"Quantidade de Medalhas:{self.Medalhas}")

  #Comparar as cartas
    def comparar(self, x, y, cartaJ, cartaA):
      if x > y:
        print(f"Com {x} sendo maior que {y}")
        print(f"O vencedor é: {cartaJ}\n\nParabéns!\nVocê ganhou!")
      elif x == y:
        print("Os dois valores são iguais\nO resultado é um empate!")
      else:
        print(f"Com {y} sendo maior que {x}")
        print(f"O vencedor é: {cartaA}.")
        print(f"Sinto muito, você perdeu:(")
    def sairprog(self):
      print("Você Saiu do Jogo")
      exit()

    def atributovalor(self, escolha, num):
      print(f"Você escolheu a jogadora,{escolha.Nome}.")
      time.sleep(1)
      print("*=*"*15)
      time.sleep(2)
      print("Vamos começar o jogo!!")
      print("*=*"*15)
      time.sleep(2)
      atributo=int(input(f"Quais característica da,{escolha.Nome},você quer compara?\n\n1-Idade\n2-Peso\n3-Altura\n4-Carreira\n5-Medalhas\n\nR:"))
      while True:
        if atributo==1:
          print(f"A Jogadora tem: {escolha.Idade} Anos.")
          atributo=escolha.Idade
          num=1
          break
        elif atributo==2:
          print(f"A Jogadora Pesa:{escolha.Peso}Kg.")
          atributo=escolha.Peso
          num=2
          break
        elif atributo==3:
          print(f"A Altura da Jogadora é:{escolha.Altura}m")
          atributo=escolha.Altura
          num=3
          break
        elif atributo==4:
          print(f"Anos de carreira da jogadora:{escolha.Carreira} Anos")
          atributo=escolha.Carreira
          num=4
          break
        elif atributo==5:
          print(f"A quantidade de medalhas da jogadora:{escolha.Medalhas}.")
          atributo=escolha.Medalhas
          num=5
          break
        else:
          print("Opção Inválida")
          print("*=*"*15)
          time.sleep(2)
          atributo=int(input(f"Quais característica da,{escolha.Nome},você quer comparar!\n\n1-Idade\n2-Peso\n3-Altura\n4-Carreira\n5-Medalhas\n\nR:"))
      return atributo, num
    
    