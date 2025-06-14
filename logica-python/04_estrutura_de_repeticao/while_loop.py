# Estudo de laços com WHILE

# Exemplo 1: Contando até 5
contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1

# Exemplo 2: Verificando senha
senha_correta = "python123"
entrada = ""
tentativas = 0

while entrada != senha_correta and tentativas < 3:
    entrada = input("Digite a senha: ")
    tentativas += 1

if entrada == senha_correta:
    print("Acesso liberado.")
else:
    print("Acesso negado.")

# Exemplo 3: Loop até entrada válida
resposta = ""
while resposta not in ["s", "n"]:
    resposta = input("Você quer continuar? (s/n): ").lower()

print("Resposta registrada:", resposta)

# Exemplo 4: Loop infinito controlado por condição
i = 0
while True:
    print(f"Executando... i = {i}")
    i += 1
    if i == 3:
        print("Interrompendo loop.")
        break
