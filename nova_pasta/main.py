import time
from Volei import cbv_meninas
from Principal import carta1, carta2, carta3, carta4, carta5, carta6, carta7, carta8
atributonovo=[]
#menu
print("*=*"*9)
time.sleep(1)
print("\n")
print("Matéria:Programação Orientada a Objetos\nAlunas:\n-Ádiles Naiandra\n-Ana Clara Andrade\n-Jamily Emanuelle\n-Vitória Shailia\nTurma:2°ano Vesrpetino Informática")
print("**"*9)
time.sleep(2)
nome=input("\nDigite o seu nome:")
time.sleep(2)
print("*=*"*9)
print("Olá,"+nome+", Seja bem-vindo(a) ao nosso jogo super trunfo da Cbv_Femina.")
while True:
  menu=int(input("\nVocê deseja:\n[1]Exibir as Cartas\n[2]Comparar as Cartas\n[3]Sair do Jogo\n\nR:"))
  print("*=*"*9)
  if menu==1:
    carta1.imprime_Carta()
    carta2.imprime_Carta()
    carta3.imprime_Carta()
    carta4.imprime_Carta()
    carta5.imprime_Carta()
    carta6.imprime_Carta()
    carta7.imprime_Carta()
    carta8.imprime_Carta()
    print()
  elif menu==2:
    print("vamos la")
#Aprsentação do Grupo:
    print("\nObjetivos do Jogo:\n\n-Escolha uma carta\n-Escolha umas das características da Jogadora\n-Compare o valor da característica escolhida com o seu adversário\n-O Vencedor é aquele que tiver o maior valor do atributo escolhido")
      #Exibri Cartas:
      #4 Cartas disponiveis para o usúuario/4 Cartas para comparação:
    jogadora1=carta1
    jogadora2=carta2
    jogadora3=carta3
    jogadora4=carta4
    comparar5=carta5
    comparar6=carta6
    comparar7=carta7
    comparar8=carta8
    time.sleep(1)
    print("*=*"*15)
    print(f"As Jogadoras disponiveis para o jogo são:\n\n1-{carta1.Nome}\n2-{carta2.Nome}\n3-{carta3.Nome}\n4-{carta4.Nome}\n")
    time.sleep(1)
    print("*=*"*15)
    escolha=int(input("Escolha umas das opções:\n\n1\n2\n3\n4\n\nR:"))
    print("*=*"*15)
    comp=0
    while True:
      if escolha==1:
        escolha=jogadora1
        atributonovo=carta1.atributovalor(escolha, comp)
        break
      elif escolha==2:
        escolha=jogadora2
        atributonovo=carta2.atributovalor(escolha, comp)
        break
      elif escolha==3:
        escolha=jogadora3
        atributonovo=carta3.atributovalor(escolha, comp)
        break
      elif escolha==4:
        escolha=jogadora4
        atributonovo=carta4.atributovalor(escolha, comp)
        break
      else:
        print("Opção Inválida:(\n")
        print("*=*"*15)
        time.sleep(2)
        escolha=int(input("Escolha umas das opções:\n\n1\n2\n3\n4\n\nR:"))
        print("*=*"*15)
      #Cartas Para Comparação
      
    time.sleep(1)
    print("*=*"*9)
    print(f"Qual dessas jogadoras será sua adversária?\n\n1-{carta5.Nome}\n2-{carta6.Nome}\n3-{carta7.Nome}\n4-{carta8.Nome}\n")
    time.sleep(4)
    opcoes=int(input("\nEscolhas umas das opções:\n\n1\n2\n3\n4\n\nR:"))
      
    while True:
      if opcoes==1:
        opcoes=comparar5
        print("*=*"*9)
        time.sleep(1)
        print(f"Você escolheu a jogadora,{opcoes.Nome}.")
        print("*=*"*9)
        print("*=*"*9)
        time.sleep(2)
        if atributonovo[1]==1:
          print(f"A Jogadora tem: {opcoes.Idade} Anos.")
          print("Vamos começar o jogo,Boa Sorte:)")
          print("*=*"*9)
          time.sleep(2)
          carta5.comparar(atributonovo[0], opcoes.Idade, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==2:
          print(f"A Jogadora Pesa: {opcoes.Peso} Kg.")
          print("Vamos começar o jogo,Boa Sorte:)")
          print("*=*"*9)
          time.sleep(2)
          carta5.comparar(atributonovo[0], opcoes.Peso, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==3:
          print(f"A Altura da Jogadora é: {opcoes.Altura} m.")
          print("Vamos começar o jogo,Boa Sorte:)")
          print("*=*"*9)
          time.sleep(2)
          carta5.comparar(atributonovo[0], opcoes.Altura, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==4:
          print(f"Anos de carreira da jogadora: {opcoes.Carreira} Anos.")
          print("Vamos começar o jogo,Boa Sorte:)")
          print("*=*"*9)
          time.sleep(2)
          carta5.comparar(atributonovo[0], opcoes.Carreira, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==5:
          print(f"A quantidade de medalhas da jogadora: {opcoes.Medalhas}.")
          print("Vamos começar o jogo,Boa Sorte:)")
          print("*=*"*9)
          time.sleep(2)
          carta5.comparar(atributonovo[0], opcoes.Medalhas, escolha.Nome, opcoes.Nome)
          break
      if opcoes==2:
        opcoes=comparar6
        print("*=*"*9)
        time.sleep(1)
        print(f"Você escolheu a jogadora,{opcoes.Nome}.")
        print("*=*"*9)
        print("Vamos começar o jogo, Boa Sorte:)!")
        print("*=*"*9)
        if atributonovo[1]==1:
          print(f"A Jogadora tem: {opcoes.Idade} Anos.")
          print("*=*"*15)
          time.sleep(2)
          carta6.comparar(atributonovo[0], opcoes.Idade, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==2:
          print(f"A Jogadora Pesa: {opcoes.Peso} Kg.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*15)
          time.sleep(2)
          carta6.comparar(atributonovo[0], opcoes.Peso, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==3:
          print(f"A Altura da Jogadora é: {opcoes.Altura} m.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*15)
          time.sleep(2)
          carta6.comparar(atributonovo[0], opcoes.Altura, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==4:
          print(f"Anos de carreira da jogadora: {opcoes.Carreira} Anos.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta6.comparar(atributonovo[0], opcoes.Carreira, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==5:
          print(f"A quantidade de medalhas da jogadora: {opcoes.Medalhas}.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta6.comparar(atributonovo[0], opcoes.Medalhas, escolha.Nome, opcoes.Nome)
          break
      if opcoes==3:
        opcoes=comparar7
        print("*=*"*9)
        time.sleep(1)
        print(f"Você escolheu a jogadora,{opcoes.Nome}.")
        print("*=*"*9)
        print("Vamos começar o jogo, Boa Sorte:)!")
        print("*=*"*9)
        if atributonovo[1]==1:
          print(f"A Jogadora tem: {opcoes.Idade} Anos.")
          print("*=*"*9)
          time.sleep(2)
          carta7.comparar(atributonovo[0], opcoes.Idade, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==2:
          print(f"A Jogadora Pesa: {opcoes.Peso} Kg.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta7.comparar(atributonovo[0], opcoes.Peso, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==3:
          print(f"A Altura da Jogadora é: {opcoes.Altura} m.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta7.comparar(atributonovo[0], opcoes.Altura, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==4:
          print(f"Anos de carreira da jogadora: {opcoes.Carreira} Anos")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta7.comparar(atributonovo[0], opcoes.Carreira, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==5:
          print(f"A quantidade de medalhas da jogadora: {opcoes.Medalhas}.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta7.comparar(atributonovo[0], opcoes.Medalhas, escolha.Nome, opcoes.Nome)
          break
      if opcoes==4:
        opcoes=comparar8
        print("*=*"*9)
        time.sleep(1)
        print(f"Você escolheu a jogadora,{opcoes.Nome}.")
        print("*=*"*9)
        print("Vamos começar o jogo, Boa Sorte:)!")
        print("*=*"*9)
        if atributonovo[1]==1:
          print(f"A Jogadora tem: {opcoes.Idade} Anos.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta8.comparar(atributonovo[0], opcoes.Idade, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==2:
          print(f"A Jogadora Pesa: {opcoes.Peso} Kg.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta8.comparar(atributonovo[0], opcoes.Peso, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==3:
          print(f"A Altura da Jogadora é: {opcoes.Altura} m.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta8.comparar(atributonovo[0], opcoes.Altura, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==4:
          print(f"Anos de carreira da jogadora: {opcoes.Carreira} Anos.")
          print("Vamos começar o jogo, Boa Sorte:)!")
          print("*=*"*9)
          time.sleep(2)
          carta8.comparar(atributonovo[0], opcoes.Carreira, escolha.Nome, opcoes.Nome)
          break
        elif atributonovo[1]==5:
          print(f"A quantidade de medalhas da jogadora: {opcoes.Medalhas}.")
          print("*=*"*9)
          time.sleep(2)
          carta8.comparar(atributonovo[0], opcoes.Medalhas, escolha.Nome, opcoes.Nome)
          break
      else:
        print("Opção Inválida")
        print("*=*"*9)
        time.sleep(2)
        opcoes=int(input("\nEscolhas umas das opções:\n\n1\n2\n3\n4\n:"))
        print("*=*"*9)
  elif menu==3:
    carta1.sairprog()
  else:
    print('Opção Inválida')