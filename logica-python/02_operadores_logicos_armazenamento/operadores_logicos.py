# Estudo de Operadores Lógicos e Armazenamento de Condições

# Exemplo 1: Condições compostas com "and"
idade = int(input("Qual a sua idade? "))
tem_carteira = input("Você tem carteira de motorista? (s/n): ").lower() == "s"

pode_dirigir = idade >= 18 and tem_carteira
print("Pode dirigir?", pode_dirigir)

# Exemplo 2: Condições compostas com "or"
trabalha_remoto = input("Você trabalha remotamente? (s/n): ").lower() == "s"
tem_transporte = input("Você tem transporte próprio? (s/n): ").lower() == "s"

vai_ao_escritorio = trabalha_remoto == False or tem_transporte
print("Vai ao escritório?", vai_ao_escritorio)

# Exemplo 3: Negação com "not"
tem_passagem = input("Tem passagem aérea? (s/n): ").lower() == "s"
embarque_negado = not tem_passagem
print("Embarque negado:", embarque_negado)

# Exemplo 4: Armazenando resultado lógico
senha_digitada = input("Digite a senha: ")
acesso_liberado = senha_digitada == "python123"
print("Acesso liberado?", acesso_liberado)

# Exemplo 5: Avaliação combinada
email_confirmado = True
telefone_verificado = False

autenticado = email_confirmado and telefone_verificado
print("Usuário autenticado?", autenticado)
