while True:
    print("0 - Sair \n 1 - Soma\n 2 Subtrair \n 3 - Dividir\n 4-Multiplicar\n")
    escolha= int(input("Qual sua Operação quer ?"))
    if escolha == 0:
        print("Saiu da Calculadora")
        break
    Numeros= int(input("Qual o primeiro numero quer ?"))
    Numero2= int(input("Qual o segundo numero ?"))

    if escolha == 1:
        print(Numeros+Numero2)
    if escolha ==2:
        print(Numeros-Numero2)
    if escolha == 3:
        print(Numeros/Numero2)
    if escolha == 4:
        print(Numeros*Numero2)









