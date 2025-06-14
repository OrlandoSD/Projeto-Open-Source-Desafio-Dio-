# Estudo sobre dicionários em Python

# Criando um dicionário simples
usuario = {
    "nome": "Orlando",
    "idade": 30,
    "cidade": "São Paulo"
}

print("Informações do usuário:", usuario)

# Acessando valores
print("Nome:", usuario["nome"])
print("Idade:", usuario.get("idade"))

# Adicionando novos dados
usuario["profissão"] = "Programador"
print("Após adicionar profissão:", usuario)

# Atualizando valores
usuario["idade"] = 31
print("Idade atualizada:", usuario)

# Removendo dados
del usuario["cidade"]
print("Após remover cidade:", usuario)

# Iterando sobre chave-valor
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# Verificando existência de uma chave
if "nome" in usuario:
    print("O nome do usuário está registrado.")

# Criando um dicionário de listas
turma = {
    "alunos": ["Ana", "Lucas", "João"],
    "notas": [8.5, 7.0, 9.2]
}

print("Turma:", turma)
# Acessando lista dentro do dicionário
print("Primeiro aluno:", turma["alunos"][0])