contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-6543"},
  "joao@gmail.com": {"nome": "João", "telefone": "1234-6543"},
  "maria@gmail.com": {"nome": "Maria", "telefone": "1234-9568"}
}

contatos["guilherme@gmail.com"]["telefone"] # 1234-6543

#iterar sobre o dicionario
#não é a forma mais indicada
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)    