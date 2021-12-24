salario = float(input("Salario do funcionario: "))
if salario <= 1250:
    novo = salario + (salario*15/100) #pra ler porcentagem é 15 por 100to do salario
else:
    novo = salario + (salario*10/100)
print("Quem ganhava RS{:.2f} , passa a ganhar R${:.2f}".format(salario,novo))
