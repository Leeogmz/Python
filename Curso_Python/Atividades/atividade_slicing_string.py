#1º

nome_sobrenome = "LeonardoGomes"
nome = nome_sobrenome[:8]
sobrenome = nome_sobrenome[8:]
print(nome)
print(sobrenome)

#2º

string = input('Escreva algo: ')
remove = string[:-1]
print(remove)

#3º 
texto = input('Escreva algo: ')
possui_vogal = ("a" in texto) or ("e" in texto) or ("i" in texto) or ("o" in texto) or ("u" in texto)
print('Possui vogal? ', possui_vogal)


#4º
abc = 'ABC'
string2 = input('Escreva algo: ')
resultado = abc + string2
print(resultado)