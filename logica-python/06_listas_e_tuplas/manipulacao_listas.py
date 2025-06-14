# Manipulando listas e tuplas em Python

# LISTAS - mutáveis

# Criando uma lista
frutas = ["maçã", "banana", "uva"]
print("Lista original:", frutas)

# Acessando elementos
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Adicionando elementos
frutas.append("laranja")
print("Após append:", frutas)

# Inserindo em posição específica
frutas.insert(1, "abacaxi")
print("Após insert:", frutas)

# Removendo elementos
frutas.remove("banana")
print("Após remove:", frutas)

# Ordenando a lista
frutas.sort()
print("Lista ordenada:", frutas)

# Iterando sobre a lista
for fruta in frutas:
    print("Fruta:", fruta)

# Tamanho da lista
print("Total de frutas:", len(frutas))


# TUPLAS - imutáveis

# Criando uma tupla
dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
print("Tupla completa:", dias_da_semana)

# Acessando elementos
print("Primeiro dia:", dias_da_semana[0])
print("Último dia:", dias_da_semana[-1])

# Iterando sobre uma tupla
for dia in dias_da_semana:
    print("Dia:", dia)

# Verificando existência
if "domingo" in dias_da_semana:
    print("É dia de descanso!")
# Tamanho da tupla
print("Total de dias:", len(dias_da_semana))