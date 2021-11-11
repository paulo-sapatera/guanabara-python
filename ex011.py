preco = float(input("Digite o preço do produto: "))
novo = preco - (preco*5/100)
print ("O valor do produto é de R${} e o novo valor com 5% de desconto é R${}.".format (preco,novo))
#nesse caso, preco*5/100 daria só o valor do desconto, ai tu tem q por preco "-" menos o desconto.
