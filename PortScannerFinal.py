import socket
import sys
import pyfiglet
from datetime import date, datetime
from queue import Queue
import threading

#Cria Banners
banner = pyfiglet.figlet_format("Bem vindo ao MyPortScanner")
print(banner)

banner2 = pyfiglet.figlet_format("Scanning....")

banner3 = pyfiglet.figlet_format("Finished!!")

#Variáveis Globais
open_port = []

q = Queue()

#Faz a resolução de nomes e testa pra ver se o host existe, está ativo.
def ip_alvo(nome):
    
    try:
        target = socket.gethostbyname(nome) #faz a resolução de nome
        print("\n[+] Escaneando IP de {}".format(nome))
        
    except socket.gaierror:
        print("\n [+] Hmmm, algo de errado não está certo com o nome de Host =/")
        sys.exit()

    return target

#Faz a varredura das portas
def scan(port):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.close
        return True

    except:
        return False

#Faz a execução dos diferentes modos e guarda as portas dentro da função Queue() para o thread usar
def op_mode(mode):
    
    if mode == "1":
        for port in range (1, 1024):
            q.put(port)
        
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

#Constroi os threads. O except é necessário para que não sejam dados erros caso uma das portas tenha serviços desconhecidos rodando por trás delas
def threads_builder():
    while not q.empty():
        port = q.get()
        if scan(port):
            try:
                print("\n [+] Port {0} is open, baby!! Service: {1}".format(port, socket.getservbyport(port)))
                open_port.append(port)
            except:
                continue
#Fazendo os diferentes threads para executarem as funções de escaneamento
def scan_threads(threads, mode):
   
    op_mode(mode)
    
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=threads_builder)
        thread_list.append(thread)
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()

    print("\n[+] Open ports summary:", open_port)



#Main do programa
if __name__ == '__main__':

    try:
        target = input("\n[+] Forneça o alvo que você quer escanear > ")
        target = ip_alvo(target)
        print('''\n [+] São implementados 5 modus operandi para essa ferramenta: 
        \n [+] 1 - Faz o escaneamento de portas de sistema [1-1024] 
        \n [+] 2 - Faz o escaneamento de portas registradas [1025 - 49152]
        \n [+] 3 - Faz o escaneamento de portas 49153 a 65535
        \n [+] 4 - Faz o escaneamento de todas as 65535 portas
        \n [+] 5 - Faz o esacaneamento de uma porta específica''')

        mode = input("\n[+] Escolha seu modus operandi > ")


        
        print("YY"*50)
        print("Escanenando Alvo: " + target)
        print("Início : " + str(datetime.now()))
        print(banner2)
        print("YY"*50)
        
        #Carimbo de tempo e hora
        
        t0 = datetime.now()
        scan_threads(100, mode)
        t1 = datetime.now()
        dt = t1 - t0 
        
        #Criação de um arquivo de log da execução com o timestamp
        
        with open("log.txt", 'a') as txt_file:
            print(("Portas abertas: "), open_port, datetime.now(), file=txt_file)

        print("YY"*50)
        print(banner3)
        print("\n [+] Escaneamento durou {} ".format(dt))
        print("YY"*50)
        
        #Interrompe a execução quando existe um input do teclado para tal
        
    except KeyboardInterrupt:
        print("\n [+] Um bom dia! Volte Sempre!!!!")
        sys.exit()
