from random import randint
from time import sleep #faz o computador "dormir" por alguns segundos, pra dar a ideia de uma pausa
computador = randint(0,5) #faz o computador pensar um numero
print("-" * 20)
print ("Vou pensar em um número de 0 a 5, tente adivinhar")
print ("-" * 20)
jogador = int(input ("Em que número eu pensei?")) #jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("PARABÉNS! Você ganhou!")
else:
    print ("Você PERDEU! eu pensei no numero {}".format(computador))

