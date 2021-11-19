frase = str(input("Digite uma frase: ")).upper().strip() #aumentar toda a frase pra encontrar todo tipo de letra A, strip p tirar espaços
print("A letra A aparece {} vezes na frase".format(frase.count("A"))) #count A é pra contar os A's
print("A primeira letra A apareceu na posição {}".format(frase.find("A"))) #find pra encontrar o primeiro A
print("A ultima letra A apareceu na posição {}".format(frase.rfind("A"))) #usando Rfind, o programa começa a procurar pelo final