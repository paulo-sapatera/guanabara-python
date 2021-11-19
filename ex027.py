n = str(input("Digite seu nome completo: ")).strip()
nome = n.split() #vai separar o nome todo, cada palavra tem uma contagem de caracteres em vez de uma p frase toda
print("Seu primeiro nome é {}".format(nome[0])) #como vai ta separado em uma lista, a primeira palavra é a 0
print("Seu ultimo nome é {}".format(nome[len.nome]-1)) #len conta quantas palavras tem