# Whatsapp-Bot
> Bot de Spam de mensagem utilizando Python 3

## Como executar?
Na linha 17 do código, basta colocar o link fonte da mensagem, e colocar a tag de texto do HTML, ao inspecionar o site, é possivel verificar se está usando p, span, hr, etc... Ao executar o arquivo, terá um intervalo de 20 segundos até começar o flood.
<br>

Para executar o arquivo é necessário instalar as seguintes bibliotecas:
<br>
<br>

### BeautifulSoup

> A biblioteca BeautifulSoup serve para extrair informações de arquivos HTML e XML, nesse caso estou buscando a origem das mensagens em sites, então estou extraindo de um arquivo HTML. Para instalar, execute no CMD: 
```
pip install beautifulsoup4
```

### Requests 
> Uma biblioteca HTTP para coleta do URL que será lido pelo BautifulSoup.
> Para instalar, execute no CMD:
```
pip install requests
```

### PyAutoGUI

>Biblioteca para pegar o controle do Teclado, para teclar ENTER após cada mensagem.
Para instalar, execute no CMD: 
```
pip install pyautogui
```
