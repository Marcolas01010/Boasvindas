print ("Qual moeda quer converter : [0] Dolar , [1] Real [2]pound  ")
moeda= int(input("Escolha a sua opção:"))

euros= float(input("Quantos euros deseja converter"))
dolar = euros * 1.08
real = euros * 6.17
pound = euros * 0.83
if moeda == 0:
    if dolar == 1:
        print("Vai ficar com",dolar, "dolar.")
    else:
        print("Vai ficar com", dolar, "dolares.")
if moeda == 1:
    print("Vai ficar com",real,"reais")
if moeda == 2:
    if pound == 1:
        print ("Vai ficar com",pound,"Pound")
    else:
        print("Vai ficar com",pound,"Pounds")

