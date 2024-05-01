def nome(
        argumento_posicional,*pacote_de_argumentos
):
    print(
        argumento_posicional,
        pacote_de_argumentos
    )

nome ('Python')

def nome2(argumento_nomeado='Não tem nada',**pacote_de_nomeado):
    print(
        argumento_nomeado,
        pacote_de_nomeado
    )

nome2 ('a')