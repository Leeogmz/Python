import matplotlib.pyplot as plt
from random import choice

estudantes = ["joao", "Maria", "Jose"]
notas = [8.5, 9, 6.5]


plt.bar(x = estudantes, height = notas)

estudantes2 = ["joao", "Maria", "Jose", "Ana"]

sorteio = choice(estudantes2)

print(sorteio)



