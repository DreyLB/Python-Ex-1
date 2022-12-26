from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Programa'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('\033[0;31m')
        cabecalho('Saindo do Sistema')
        print('\033[m')
        break
    else:
        cabecalho('\033[0;31mErro: Digite uma opção válida.\033[m')
    sleep(1)

