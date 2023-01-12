numero9 = 0
numero3 = 0

a = (int(input("Digite um numero: ")), int(input("Digite um numero: ")),
     int(input("Digite um numero: ")), int(input("Digite um numero: ")))
numero9 = a.count(9)
print("o numero 9 apareceu {} vezes.".format(numero9))

if 3 in a:
  numero3 = a.index(3) + 1
  print("o numero 3 apareceu pela 1 vez na posição {}".format(numero3))
else:
  print("o numero 3 não aparece em nenhuma posição dos numeros digitados")

np = 0
for c in a:
  if c % 2 == 0:
    np += 1
print("{} dos numeros digitados são pares".format(np))