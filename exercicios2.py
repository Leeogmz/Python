"""1) Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. 
O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
Teste o programa com o segundo valor numérico do input igual a 0 e também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem."""



""" 
try:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))   
    resultado = numero1 / numero2
except Exception as e:
    print(type(e), f'Erro: {e}')   
else:
    print(resultado)
finally:
   print("Programa encerrado!")    """


"""2) Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: 
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, 
armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, 
imprimindo a informação 'Nome não encontrado' caso ocorra o erro e imprimir o valor caso não ocorra nenhum.

Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro."""

"""idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    chave = input("Digite o nome do estudante: ")
    valor = idades[chave]
except KeyError:
    print('Nome não encontrado')
else:
    print(valor)"""

"""3) Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'."""

def converte_lista(lista):
    try:
        nova_lista = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return nova_lista
    finally:
        print('Fim da execução da função')