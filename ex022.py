nome = str(input("Digite seu nome: ")).strip()
print("Seu nome em maiusculo é: {}".format (nome.upper ()))
print("Seu nome em minusculo é: {}".format (nome.lower ()))
print("Seu nome tem {} letras".format (len(nome) - nome.count(' '))) #seria a quantidade de letras ao todo - os espaços
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))   #nesse caso o find é usado pra achar o primeiro espaço, logo ele mostra quantos caracteres tem a primeira palavra.