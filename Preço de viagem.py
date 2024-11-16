print("As opções são, CARRO , Comboio e Avião.")
print("1- Carro custa 0.5 euros / km")
print("Comboio custa 0.3 euros /km")
print("Avião custa 0.7/km")
Viagens = input("Qual viagem o senhor/a gostaria ?")
Km = float(input("Quanto Km irá percorrer"))

Carro= 0.5
Comboio= 0.3
Avião= 0.7

Custo_Total_Carro = Carro*Km
Custo_Total_Comboio= Comboio*Km
Custo_Total_Avião = Avião*Km

if (Viagens == "Carro") :
    print(Custo_Total_Carro)
if (Viagens== "Comboio") :
    print(Custo_Total_Comboio)
if (Viagens=="Avião"):
    print(Custo_Total_Avião)




