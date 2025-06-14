# Calculadora simples com funções

def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Erro: divisão por zero"

print("🧮 Calculadora Simples")
print("Operações: +  -  *  /")
op = input("Escolha a operação: ")
x = float(input("Primeiro número: "))
y = float(input("Segundo número: "))

if op == "+":
    print("Resultado:", somar(x, y))
elif op == "-":
    print("Resultado:", subtrair(x, y))
elif op == "*":
    print("Resultado:", multiplicar(x, y))
elif op == "/":
    print("Resultado:", dividir(x, y))
else:
    print("Operação inválida.")
# Dica: Use funções para organizar as operações matemáticas.
# Dica: Use input() para receber os números e a operação do usuário.