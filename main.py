import socket
import datetime

def scanner():
    print('''
    ########### Scanner de portas UDP/ TCP ############
    ===================================================
    Versão: 1.0.0
    Link do respositório: https://github.io
    Autor: Italo Roberto
    Data de criação: 04/10/2022
    ===================================================
    ''')
    alvo = input('Digite o IP/ Domínio: ')

    portas = []
    for porta in range(1, 995):
        client = socket.socket()
        client.settimeout(0.05)

        if client.connect_ex((alvo, porta)) == 0:
            print(f'Porta aberta: {porta}')
            portas.append(porta)
    print('Scanner finalizado! \n')

    pergunta = input('''
    ===============================================================================
    Deseja salvar a lista de portas encontradas em arquivo de texto na pasta atual?\n
    s=SIM, n=Não
    ===============================================================================
    ''')
    str(pergunta)

    if pergunta == 's':
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime('%d_%m_%Y-%H-%M')
        arquivo = open(f"RelatorioDePortas{dataFormatada}.txt", "x")
        arquivo.write(f'''
===========================
Lista de portas abertas:
===========================
HOST: {alvo}
DATA DO SCANNER: {dataAtual.strftime('%c')}
        ''')
        for p in portas:
            arquivo.write(f'\n{p}')
        arquivo.close()
    elif pergunta == 'n':
        print('Scanner de porta finalizado!')
    else:
        print('Opção inválida, programa finalizado')


if __name__ == '__main__':
    scanner()