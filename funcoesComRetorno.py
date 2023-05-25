notas = [8.5, 7.5, 6.5, 6.0]

def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"  

    return (media, situacao) 

resultado = boletim(notas)
print(resultado)


media, situacao = boletim(notas)

print(media)
print(situacao)


