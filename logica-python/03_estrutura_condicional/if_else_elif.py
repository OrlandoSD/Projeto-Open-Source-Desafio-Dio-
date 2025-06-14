# Estruturas Condicionais: if, else, elif

# Exemplo 1: if simples
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")

# Exemplo 2: if...else
nota = float(input("Digite sua nota final: "))
if nota >= 6.0:
    print("Aprovado!")
else:
    print("Reprovado!")

# Exemplo 3: if...elif...else
dia = input("Digite um dia da semana: ").lower()

if dia == "segunda":
    print("Dia de café forte.")
elif dia == "sexta":
    print("Dia de comemorar o fim da semana!")
elif dia == "domingo":
    print("Dia de descanso.")
else:
    print("Mais um dia comum.")

# Exemplo 4: múltiplas condições
tem_chuva = input("Está chovendo? (s/n): ").lower() == "s"
tem_guarda_chuva = input("Você tem guarda-chuva? (s/n): ").lower() == "s"

if tem_chuva and not tem_guarda_chuva:
    print("Fique em casa ou se molhe!")
elif tem_chuva and tem_guarda_chuva:
    print("Use o guarda-chuva!")