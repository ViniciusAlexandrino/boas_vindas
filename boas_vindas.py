# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Solicita a idade do usuário e converte para inteiro
idade = int(input("Digite sua idade: "))

# Verifica se o usuário é um administrador (independente de maiúsculas/minúsculas)
if nome.lower() == 'admin':
    print(f"Olá {nome.title()}. Deseja acessar os relatórios?")

# Verifica se a idade é maior ou igual a 18
elif idade >= 18:
    print(f"Olá {nome.title()}, você é adulto")

# Verifica se a idade está entre 13 e 17
elif idade >= 13:
    print(f"Olá {nome.title()}, você é adolescente")
    
# Verifica se a idade é 12 ou menos
elif idade <= 12:
    print(f"Olá {nome.title()}, você é criança")