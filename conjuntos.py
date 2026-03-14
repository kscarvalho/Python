#eliminar duplicidade
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
#obs. o set não trás na ordem

#conjuntos não suportam indexação por isso
#converter set para lista
numeros = {1, 2, 3, 2}
numeros = list(numeros)
numeros[0]

#loop em set
carros = {"gol", "celta", "palio"}
for carro in carros:
    print(carro)

#sabendo o indice
carros = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros) :
    print(f"{indice}: {carro} ") 

#union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

#intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

#difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

#issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#isdisjoint
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_c = {1, 0}


print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#adicionar add
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

#clear
sorteio = {1, 23}
sorteio # {1,23}
sorteio.clear()
sorteio # {}

#copy
sorteio = {1, 23}
sorteio # {1,23}
sorteio.copy()
sorteio # {1, 23}

#discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1) 
numeros.discard(45) 
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}

#pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros # {0, 1, 2, 3, 4, 5, 6, 7 8, 9}
numeros.pop() # 0 
numeros.pop() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9}

#remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros # {0, 1, 2, 3, 4, 5, 6, 7 8, 9}
numeros.remove(0) # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}
