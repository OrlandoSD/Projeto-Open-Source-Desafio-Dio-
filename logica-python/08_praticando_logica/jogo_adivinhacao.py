# Jogo de adivinhação: o computador escolhe um número entre 1 e 10

import random

numero_secreto = random.randint(1, 10)
tentativas = 0
palpite = 0

print("🔢 Jogo de Adivinhação! Tente acertar o número entre 1 e 10.")

while palpite != numero_secreto:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Tente um número mais alto.")
    elif palpite > numero_secreto:
        print("Tente um número mais baixo.")

print(f"Parabéns! Você acertou com {tentativas} tentativa(s).")
# Dica: Você pode usar o módulo random para gerar números aleatórios.
# Dica: Use o método randint para escolher um número entre 1 e 10.