"""Exercício #7
Faça um programa que receba uma string e responda se ela tem alguma vogal, 
se sim, quais são? 
E também diga se ela é uma frase ou não."""

texto = input('Escreva algo!')
texto = texto.lower()                      

a = (texto.count('a')) 
e = (texto.count('e')) 
i = (texto.count('i'))          
o = (texto.count('o')) 
u = (texto.count('u')) 
espaco = (texto.count(' '))    

if (a > 0 or e > 0 or i > 0 or o > 0 or u > 0):       
    print("Foi encontrada ao menos uma vogal")
else:
    print("Não tem vogal")

if a > 0:                                            
    print(f"Econtramos a vogal A {a} vezes!")
if e > 0:
    print(f"Econtramos a vogal E {e} vezes!")
if i > 0:
    print(f"Econtramos a vogal I {i} vezes!")
if o > 0:
    print(f"Econtramos a vogal O {o} vezes!")
if u > 0:
    print(f"Econtramos a vogal U {u} vezes!")

if espaco > 0:
    print("Isso é uma frase e não uma palavra!")           
else:
    print("Isso é apenas uma palavra!")