<h1>Port Scanner - Python</h1>
<p>Scrit de checagem de portas UDP/TCP, utiliznado Python 3</p>
<span>Versão: 1.0.0</span>
<hr>

<div>
    <strong>Pré requisitos:</strong>
    <ul>
        <li>Python 3.6 ou superior instalado.</li>
        <li>Noção básica de endereçamento IP.</li>
    </ul>
</div>

<div>
    <strong>Instruções de utilização.</strong>
    <p>Realize o clone do repositório:</p>
 `git clone https://github.com/Italo-Roberto/port_scanner_python`

<p>Execute o script (via cmd/terminal):</p>
    `python3 ./port_scanner_python/main.py`

<p>Será pedido IP/HOSTNAME do alvo a ser realizado teste:</p>
    `ex: 192.168.0.1 ou 127.0.0.1`

<p>Aguarde execução do programa, serão exibidas apenas as portas que estiverem abertas no host alvo</p>

<p>Ao final da verificação o programa irá perguntar se deseja salvar em arquivo de texto o resultado do scanner:</p>
    `===============================================================================
    Deseja salvar a lista de portas encontradas em arquivo de texto na pasta atual?
    s=SIM, n=Não
    ===============================================================================`

<p>Se marcado 's' SIM, será gerado um arquivo texto com a potas abertas, se 'n' NÃO, o programa será encerrado</p>

</div>