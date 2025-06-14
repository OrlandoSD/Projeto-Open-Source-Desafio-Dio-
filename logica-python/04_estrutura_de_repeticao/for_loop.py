# Estudo de laços com FOR

# Exemplo 1: Contando de 1 a 5
for i in range(1, 6):
    print(f"Número: {i}")

# Exemplo 2: Iterando sobre uma lista
frutas = ["maçã", "banana", "abacaxi"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Exemplo 3: Somando números pares de 0 a 10
soma = 0
for numero in range(0, 11, 2):
    soma += numero
print("Soma dos pares:", soma)

# Exemplo 4: Imprimindo caracteres de uma string
texto = "Python"
for letra in texto:
    print(letra)

# Exemplo 5: Laço aninhado (tabuada)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
