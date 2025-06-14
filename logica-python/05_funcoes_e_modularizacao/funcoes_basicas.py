# Estudo de funções em Python

# Exemplo 1: Função simples sem parâmetro
def saudacao():
    print("Olá! Seja bem-vindo ao mundo das funções!")

saudacao()

# Exemplo 2: Função com parâmetros
def apresentar_usuario(nome, idade):
    print(f"Nome: {nome}, Idade: {idade} anos")

apresentar_usuario("Orlando", 30)

# Exemplo 3: Função que retorna valor
def quadrado(numero):
    return numero ** 2

resultado = quadrado(5)
print("O quadrado de 5 é:", resultado)

# Exemplo 4: Função com valor padrão (default)
def boas_vindas(nome="Visitante"):
    print(f"Olá, {nome}!")

boas_vindas()
boas_vindas("Maria")

# Exemplo 5: Função que verifica número par
def eh_par(numero):
    return numero % 2 == 0

print("4 é par?", eh_par(4))
print("7 é par?", eh_par(7))

# Exemplo 6: Modularização com funções auxiliares
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def menu_operacoes():
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    opcao = input("Opção: ")

    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(x, y))
    elif opcao == "2":
        print("Resultado:", subtrair(x, y))
    else:
        print("Opção inválida.")

menu_operacoes()
# Exemplo 7: Função com número variável de argumentos
def soma_varios(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total