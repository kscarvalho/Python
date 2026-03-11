#append
lista = []

lista.append(1)
lista.append("Python")
lista.append(["40", "30", "20"])

print(lista)

#clear
lista = []

lista.append(1)
lista.append("Python")
lista.append(["40", "30", "20"])

lista.clear()

print(lista)

#copy
lista = ["40", "30", "20"]

lista.copy()

print(lista)

#count
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vemelho")
cores.count("azul")
cores.count("verde")

#extend
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#indice
linguagens = ["python", "js", "c"]

print(linguagens.index("java"))
print(linguagens.index("python"))

#pop
linguagens = ["python", "js", "c"]

linguagens.pop() #csharp
linguagens.pop() #java
linguagens.pop() #c
linguagens.pop(0) #python

#remove
linguagens = ["python", "js", "cb"]
linguagens.remove("c")
input(linguagens)

#reverse
linguagens = ["python", "js", "c"]
linguagens.reverse()
print(linguagens)

#sort OBS tambem tem o sorted
leiguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()

leiguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)

leiguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))

leiguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)

#len
linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens)

#
