# MyPortScanner

## About
**MyFirstPortScanner** é um script escrito em Python de escaneamento de porta feito para varrer as portas lógicas de um dispositivo de rede utilizando requisições TCP e se aproveitando do Triple-Handshake. 

Um de seus diferenciais é a utilização de Threads para agiliar o processo de varredura.

Futuramente pretende-se implementar o escaneamento de portas UDPs e o reconhecimento do Sistema Operacional que está rodando no dispositivo escaneado.

## Preview

![Prévia](/Image_Port/MyPortScannerPNG.PNG)

## Pré-requisitos e Instalação

![Pré-req](/Image_Port/Imports.PNG)

Essas são as bibliotecas básicas usadas para que o script funcione de maneira apropriada. Os módulos socket, sys e threading são nativos da biblioteca do Python3 padrão. Datetime e queue são módulos que precisam ser instalados, bem como o modulo de criação de banners em ASCII pyfiglet.
 
 ### Socket
 A biblioteca socket faz o bind nas portas que queremos escanear por meio de requisições TCP. E faz a resolução de nomes de hosts.
 
 ### Sys
 
 A biblioteca sys é utilizada para saida do programa em exceções.
 
 ### Pyfiglet
 
 A biblioteca faz um texto virar um banner em caracteres ASCII.
 
 ### Datetime
 
 Faz a busca da data e hora. 
 
 ### Queue
 
Esse módulo é utilizado para implementar pilhas ou filas que podem ser consumidas por múltiplos processos. Uma vez que estamos utilizando threads para executar o escaneamento de portas, se faz necessário o acesso seguro de todos os threads as váriaveis, que no nosso caso são os números das portas lógicas. 
Sem esse módulo se faria necessário a utilização de locks e o tratamento adequado de quando liberar cada variável novamente para o uso. É muito mais prático utilizá-la para que já sejam implementados todas as seguranças necessárias. 

Para mais informações veja o documenteo queue fornecido nas referências.

### Thread

Essa biblioteca é nativa do Python desde o Python 2.7. Ela possibilita a utilização de threads para executar o scritp. 
De forma simplificada, ela separa o processo principal do programa em sub-processos (threads) que executarão de forma independente dentro do ambiente do processo principal para que a execução do script seja feita de forma mais rápida.

Sem essa biblioteca o tempo dispendido na espera do escaneamento de todas as portas seria muito grande.

Para mais informações veja o documento threading fornecido nas referências

## Considerações sobre Input

As entradas que devem ser fornecidas para o script devem estar no formato de nome ou IP da seguinte forma:
  
  Para Nomes de Host:
    
    Deve-se colocá-lo sem o 'www' e 'http(s)'. Exemplo: scanme.nmap.org
  
  Para IPs:
    
    Deve-se dar como entrada um input no formato de IPv4, separando os octetos por pontos. Exemplo: 127.0.0.1 

## Modos de Operação

![Mode](/Image_Port/Mode.PNG)

## Exemplo de Output

![Host](/Image_Port/Host.PNG)

O output também fornece um arquivo log.txt para guardar a saida

## Video de Execução

## Considerações Finais

## Referências

### Queue
    
    https://docs.python.org/3/library/queue.html#module-queue

### Threading
    
    https://docs.python.org/3/library/threading.html

### Pyfiglet

    https://pypi.org/project/pyfiglet/0.7/
    
### Escaneamento de Portas
  
    https://null-byte.wonderhowto.com/how-to/sploit-make-python-port-scanner-0161074/
    
 Texto muito bom sobre tipos de escaneamento de portas e como funcionam.
 
    https://www.techrepublic.com/blog/it-security/list-open-ports-and-listening-services/
  
 Texto sobre fingerprints de SO
 
    https://cutt.ly/VE0gsYf
 
 Tutorial sobre threading

 
 
