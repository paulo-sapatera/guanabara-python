km = float(input("Qual a distancia da viagem em KM?: "))
if km > 200:
    print("O valor da viagem é de R${}".format(km*0.45))
else:
    print("O valor da viagem é de R${}".format(km*0.50))
    