# aqui é for iterável
texto = input("Informe um texto: ")
VOGAIS = "aeiou"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()


# aqui é for range
for numero in range(0, 15):
    print(numero)