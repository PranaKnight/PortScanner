''' 
Filipe Grahl RM 86663
Victor Dias Gonçalvez RM (Colocar RM)
'''

import socket
import sys
import pyfiglet
from datetime import date, datetime
from queue import Queue
import threading

#Cria os Banners

banner = pyfiglet.figlet_format("Bem vindo ao MyPortScanner")
print(banner)

banner2 = pyfiglet.figlet_format("Scanning....")

banner3 = pyfiglet.figlet_format("Finished!!")

open_port = []

q = Queue()

#Função para receber input tanto de um endereço IP quanto de um nome de domínio
def ip_alvo(nome):
    
    try:
        target = socket.gethostbyname(nome) #faz a resolução de nome
        print("\n[+] Escaneando IP de {}".format(nome))
        
    except socket.gaierror:
        print("\n [+] Hmmm, algo de errado não está certo com o nome de Host =/")
        sys.exit()

    return target

#Escaneamento propriamente

def scan(port):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.close
        return True

    except:
        return False

#Modos de operação e Range de portas
    
def op_mode(mode):
    
    if mode == "1":
        for port in range (1, 1024):
            q.put(port) #faz o recolhimento das portas
        
    elif mode == "2":
        for port in range (1025, 49152):
            q.put(port)
    
    elif mode == "3":
        for port in range (49153, 65535):
            q.put(port)

    elif mode == "4":
        for port in range (1, 65535):
            q.put(port)

    elif mode == "5":
        ports = input("\n [+] Insira as portas que quer escanear separadas por um espaço > ")
        ports = ports.split()
        ports = list(map(int,ports))
        for port in ports:
            q.put(port)

#Usando Threads para agilizar o processo de escaneamento.
def threads_builder():
    while not q.empty():
        port = q.get()
        if scan(port):
            print("\n [+] Port {0} is open, baby!! Service: {1}".format(port, socket.getservbyport(port)))
            open_port.append(port)

#Faz a construção das threads e a junção de todas novamente ao fim
def scan_threads(threads, mode):
   
    op_mode(mode)
    
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=threads_builder)
        thread_list.append(thread)
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()
    
    print("\n[+] Open ports summary:", open_port)

# Inicializando utilizando o próprio nome do prgrama
if __name__ == '__main__':

    #inputs necessários para o funcionamento
    target = input("\n[+] Forneça o alvo que você quer escanear > ")
    target = ip_alvo(target)
    print('''\n [+] São implementados 5 modus operandi para essa ferramenta: 
    \n [+] 1 - Faz o escaneamento de portas de sistema [1-1024] 
    \n [+] 2 - Faz o escaneamento de portas registradas [1025 - 49152]
    \n [+] 3 - Faz o escaneamento de portas 49153 a 65535
    \n [+] 4 - Faz o escaneamento de todas as 65535 portas
    \n [+] 5 - Faz o esacaneamento de uma porta específica''')

    mode = input("\n[+] Escolha seu modus operandi > ")

    try:
        
        print("YY"*50)
        print("Escanenando Alvo: " + target)
        print("Início : " + str(datetime.now()))
        print(banner2)
        print("YY"*50)
        
        t0 = datetime.now()
        scan_threads(100, mode)
        t1 = datetime.now()
        dt = t1 - t0  #Faz o cálculo de tempo de execução do escaneamento
        
        print("YY"*50)
        print(banner3)
        print("\n [+] Escaneamento durou {} ".format(dt))
        print("YY"*50)
    
    except KeyboardInterrupt:
        print("\n [+] Um bom dia! Volte Sempre!!!!")
        sys.exit()
