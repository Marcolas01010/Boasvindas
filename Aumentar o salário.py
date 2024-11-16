ordenado = int(input ("Qual é o teu ordenado atual ?"))
if ordenado < 500 :
    salario_final= ordenado * 0.15 + ordenado
    print("Ok, recebeu um aumento de 15% :) ,agora seu salário atual é",salario_final)
elif ordenado > 500 and ordenado < 1000 :
    salario_final_2 = ordenado * 0.10 + ordenado
    print("Ok,recebeu um aumento de 10%  :), agora seu salário atual é",salario_final_2)
elif ordenado > 1000 :
    salario_final_3 = ordenado * 0.05 + ordenado
    print("Ok, recebeu um aumento de 5% :), agora seu salário atual é ",salario_final_3)



