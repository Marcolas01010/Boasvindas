Numeros = int(input ("Qual é o numero que gostaria de escolher de 0 a 10 ?"))
if (Numeros== 4) :
    print("Parabéns Escolheu o numero certo")
if (Numeros!= 4) :
    print("Ohh, Não é o numero correto...")

print("Qual das perguntas é verdadeira")
print(" Onde fica Portugal?")
print("1: Ásia | 2: América | 3: Europa| 4: Africa")
Resultado2 = int(input("Qual é a resposta certa ?"))
if (Resultado2 == 3 ) :
    print("Acertou!")
if (Resultado2 !=4) :
    print("Ups! Errou")

print("Quem descobriu Brasil ?")
print ("1 : Pedro Álvares Cabral | 2 : A Castela | 3 : D.afonso Henriques | 4: Vasco da Gama")
Resultado3 = int(input("Qual é a certa ?"))
if (Resultado3==1) :
    print("Parabéns vc acertou!")
if (Resultado3!=1) :
    print("Ups, errou")
Usuario = int(input("Quantas respostas acertou ?"))
if(Usuario==3) :
    print("Acertou tudo , Ganhou o prémio de 230$")
if(Usuario!=3)  :
    print("Ups, não acertou tudo")