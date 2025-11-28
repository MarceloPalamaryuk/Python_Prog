###ex1
lista1 = [i for i in range(1,11) if i % 2 == 0]
#print(lista1)

###ex2
lista2 = [i**2 for i in range(1,11)]
#print(lista2)

###ex3
lista3 = ["Maça", "Banana", "Mango", "Laranja"]
lista3_1 = [len(i) for i in lista3]
#print(lista3_1)

###ex4
nums = [1,2,3,4,5,6,7,8,9,10]
lista4 = [i for i in nums if i>5]
#print(lista4)

###ex5 e 7
lista5 = ["Ana", "Rui", "Marcelo", "Bia", "Zé", "João", "Alice"]
nome_A = [i.upper() for i in lista5 if i.startswith("A")]
#print(nome_A)

###ex6
nums = [1,2,3,4,5,6,7,8,9,10]
lista6 = [i*2 if i%3 == 0 else i for i in nums]
#print(lista6)

###ex8
frutas = ["Maça", "Banana", "Mango", "Laranja"]
lista8 = [len(i) if len(i)>5 else 0 for i in frutas]
print(lista8)
