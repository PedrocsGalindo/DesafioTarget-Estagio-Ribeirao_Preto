string = input("escreva uma palavra:  ")
contador = 0
for letra in string:
    if letra == "a" or letra == "A":
        contador += 1
if contador != 0:
    print ("Contem a letra 'a'")
    print ("E ela aparece " + str(contador) +" vezes")
else:
    print("Não contem a letra 'a'") 