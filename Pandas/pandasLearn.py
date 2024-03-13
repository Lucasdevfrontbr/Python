import pandas as py

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
}

DadoCliente = py.DataFrame(dados)

# Exibir o DataFrame
print("DataFrame original:")
print(DadoCliente)
print()

# Calcular a média de idade
media_idade = DadoCliente['Idade'].mean()

# Exibir a média de idade
print("Média de idade:", media_idade,"anos")

# Somar os valores da coluna 'Idade'
soma_idades = DadoCliente['Idade'].sum()

# Exibir a soma das idades
print("A Soma das idades é:", soma_idades,"anos")

MaximoIdades= DadoCliente['Idade'].max()

MinimoIdades=DadoCliente['Idade'].min()

print("A idade maxima é", MaximoIdades,"anos.", "A minima",MinimoIdades,"anos")


# Usar o método describe() para obter estatísticas descritivas
descricao = DadoCliente.describe()

# Exibir as estatísticas descritivas
print(descricao)

#filtragem
dados_menor_ou_igual_a_30= DadoCliente[DadoCliente['Idade'] <= 30]

# Exibir os dados filtrados
print(dados_menor_ou_igual_a_30)