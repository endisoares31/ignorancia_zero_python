"""
Escreva o jogo do chute.
Nele você deve sortear um número inteiro entre 1 e 100 e pedir
para o usuário advinhar o número que você escolheu

Para cada chute do usuário você deve imprimir uma dica, se
ele chutou baixo de mais ou alto demais

Uma vez que o usuário acerte o chute o programa imprime uma
mensagem e também o número de chutes que o usuário deu

OBS: Use o statement break

Exemplo:

>>>
Tente advinhar o número que eu estou pensando
Seu Chute: 50
Você deve chutar mais alto!
Seu Chute: 75
Você deve chutar mais alto!
Seu Chute: 87
Você deve chutar mais alto!
Seu Chute: 93
Você deve chutar mais alto!
Seu Chute: 97
Você deve chutar mais baixo!
Seu Chute: 95
Parabens você acertou!!
Você chutou 6 vezes
>>>

"""
import random

num = random.randint(1, 100)

chutes = 0

print("Tente advinhar o número que eu estou pensando")

while True:
    chute = int(input("Seu Chute: "))
    chutes += 1
    if chute == num:
        break
    elif chute < num:
        print("Você deve chutar mais alto!")
    else:
        print("Você deve chutar mais baixo!")


print("Parabens você acertou!!")
print("Você chutou %i vezes"%chutes)
