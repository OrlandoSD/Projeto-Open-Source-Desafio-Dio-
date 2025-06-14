# Exercícios de Variáveis e Tipos em Python

# 1. Declaração de variáveis
nome = "Orlando"
idade = 30
altura = 1.75
tem_carteira = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Tem carteira de motorista?", tem_carteira)

# 2. Entrada de dados (input) e casting
cidade = input("Digite o nome da sua cidade: ")
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2025
idade_calculada = ano_atual - ano_nascimento

print(f"Olá, {nome}, você tem aproximadamente {idade_calculada} anos e mora em {cidade}.")

# 3. Verificando tipos
print("Tipo da variável 'nome':", type(nome))
print("Tipo da variável 'idade':", type(idade))
print("Tipo da variável 'altura':", type(altura))
print("Tipo da variável 'tem_carteira':", type(tem_carteira))
print("Tipo da variável 'cidade':", type(cidade))

# 4. Operações simples
a = 10
b = 3
soma = a + b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
potencia = a ** b

print(f"{a} + {b} = {soma}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")
