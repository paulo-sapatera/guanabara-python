velo = int(input("Digite a velocidade em que o carro está: "))
multa = (velo - 80) * 7
if velo > 80:
    print ("Você excedeu a velocidade permitida de 80km/h")
    print ("A multa é de R${}".format (multa))
else: 
    print("Você está dentro do limite de velocidade permitido")
