from datetime import date
ano = int(input("Digite o ano a ser analisado, se digitar 0, analisara o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != ano % 400 == 0: # até o AND ta só os divisiveis por 4, só que ano bisexto tem outras regras, que estão pra frente do AND
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} NÃO é BISSEXTO".format(ano))
