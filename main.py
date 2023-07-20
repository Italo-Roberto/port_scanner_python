import socket
import datetime

def scanner():
    print('''
    ########### Port scanner for UDP/ TCP ############
    ===================================================
    Version: 1.0.0
    Repository link: https://github.com/Italo-Roberto/port_scanner_python
    Author: Italo Roberto
    Created at: 04/10/2022
    ===================================================
    ''')
    target = input('Digite o IP/ Domínio: ')

    ports = []
    for port in range(1, 995):
        client = socket.socket()
        client.settimeout(0.05)

        if client.connect_ex((target, port)) == 0:
            print(f'Porta aberta: {port}')
            ports.append(port)
    print('Finnish Scan! \n')

    ask = input('''
    ===============================================================================
    Deseja salvar a lista de portas encontradas em arquivo de texto na pasta atual?\n
    s=SIM, n=Não
    ===============================================================================
    ''')
    str(ask)

    if ask == 's':
        currentDate = datetime.datetime.now()
        formatDate = currentDate.strftime('%d_%m_%Y-%H-%M')
        file = open(f"RelatorioDePortas{formatDate}.txt", "x")
        file.write(f'''
===========================
Open ports list:
===========================
HOST: {target}
DATA DO SCANNER: {currentDate.strftime('%c')}
        ''')
        for p in ports:
            file.write(f'\n{p}')
        file.close()
    elif ask == 'n':
        print('Port scanner finnished!')
    else:
        print('OInvalid option, program closed')


if __name__ == '__main__':
    scanner()
