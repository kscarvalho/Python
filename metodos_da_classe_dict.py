contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-6543"},
  "joao@gmail.com": {"nome": "João", "telefone": "1234-6543"},
  "maria@gmail.com": {"nome": "Maria", "telefone": "1234-9568"}
}

#clear
contatos.clear()
contatos # {}

#copy
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

#fromkeys
dict.fromkeys(["nome", "telefone"]) 

#get
contatos["chave"] #simulando um erro proposital

contatos.get("chave") #nome
contatos.get("chave", {}) #{}
contatos.get("guilherme@gmail.com", {}) # "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-6543"},

#items
contatos.items() # dict_items([("guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-6543"})])

#keys
print(contatos.keys()) # trás somente as chaves dos dicionarios

#pop
contatos.pop("guilherme@gmail.com") #{"nome": "Guilherme", "telefone": "1234-6543"}
contatos.pop("guilherme@gmail.com", {}) # {}

#setdefault
contato = {"nome": "Francisco", "telefone": "325689889"}
contato.setdefault("nome", "Giovana") #  "Guilherme" se o valor existir vai trazer
contato.setdefault("idade", 28) # 28 se o valor não existir, ele vai alterar

#update
contato = {
  "guilherme@gmail.com": {"nome": "Francisco", "telefone": "325689889"}
} 
contato.update({"guilherme": {"nome": "Gui"}})

contato.update({"giovana@gmail.com": {"nome": "Giovana", "telefona": "3256899899"}})

#value
contatos.values() #retorna os valores amarrados as chaves

#in para verificação
resultado = "guilherme@gmail.com" in contatos #True
print(resultado)
resultado = "megui@gmail.com" in contatos #False
print(resultado)
resultado = "idade" in contatos["guilherme@gmail.com"] #flase
print(resultado)
resultado = "telefone" in contatos["guilherme@gmail.com"] #True
print(resultado)

#del
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["klebio@gmail.com"]