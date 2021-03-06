"""
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. MS. Fábio H. Cabrini
Atividade: Checkpoint NMAP em python
Alunos:
Filipe Grahl - RM 86663
Victor Dias Gonçavez - RM 88582
"""


import socket
import sys
import pyfiglet
from datetime import datetime
from queue import Queue
import threading

banner = pyfiglet.figlet_format("Bem vindo ao MyPortScanner")
print(banner)

banner2 = pyfiglet.figlet_format("Scanning....")

banner3 = pyfiglet.figlet_format("Finished!!")

transport = ' '

open_port = []

q = Queue()

def getServiceName(port, proto):
    
    try:
        name = socket.getservbyport(int(port), proto)
    except:
        return None
    
    return name

def ip_alvo(nome):
    
    try:
        target = socket.gethostbyname(nome) #faz a resolução de nome
        print("\n[+] Escaneando IP de {}".format(nome))
        
    except socket.gaierror:
        print("\n [+] Hmmm, algo de errado não está certo com o nome de Host =/")
        sys.exit(1)

    return target

def scan_udp(port):

    Message = "pingpong"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        if s == -1:
            print("\n[+] Criação do socket UDP falhou T.T")
        
        icmp = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        if icmp == -1:
            print("\n[+] Criação do socket ICMP falhou T.T")

        try:
            s.sendto(Message.encode('utf_8'), (target, port))
            icmp.settimeout(1)
            data, addr = icmp.recvfrom(1024)

        except socket.timeout:
            serv = getServiceName(int(port), 'udp')
            if not serv:
                pass
            else:
                return True
        except socket.error as e:
            
            if (e.errno == socket.errno.ECONNREFUSED):
                print(e("Conexão recusada"))
            
            s.close
            icmp.close
    except:
        return False

def scan(port):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target, port))
        s.close
        return True

    except:
        return False

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


def threads_builder():
    while not q.empty():
        port = q.get()

        if transport == "1":
            if scan_udp(port):
                try:
                    print("\n [+] Port {0} is open, baby!! Service: {1} Transport: UDP".format(port, getServiceName(port, 'udp')))
                    open_port.append(port)

                except socket.timeout:
                    
                    serv = getServiceName(port)
                    if not serv:
                        pass
                    else:
                        print('Port {0} is open, baby!! Service: {1}}'.format(port, getServiceName(port, 'udp')))
                except:
                    print("\n [+] Port {} is open, baby!! Service: Unknown Transport: UDP".format(port))
                    open_port.append(port)
                    continue
            
        elif transport == "2":
            if scan(port):
                try:
                    print("\n [+] Port {0} is open, baby!! Service: {1} Transport: TCP".format(port, socket.getservbyport(port)))
                    open_port.append(port)
                except:
                    print("\n [+] Port {0} is open, baby!! Service: Unknown Transport: TCP".format(port))
                    open_port.append(port)
                    continue
        
        else:
            print("[+] Por favor, colabore e coloque a entrada certa. (1 ou 2)")
            sys.exit(1)

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
        transport = input("\n [+] Escolha 1 para UDP e 2 para TCP > ")

        print("YY"*50)
        print("Escanenando Alvo: " + target)
        print("Início : " + str(datetime.now()))
        print(banner2)
        print("YY"*50)
        
        t0 = datetime.now()
        scan_threads(100, mode)
        t1 = datetime.now()
        dt = t1 - t0 
        
        with open("log.txt", 'a') as txt_file:
            print(("Portas abertas: "), target, open_port, datetime.now(), file=txt_file)

        print("YY"*50)
        print(banner3)
        print("\n [+] Escaneamento durou {} ".format(dt))
        print("YY"*50)
    
    except KeyboardInterrupt:
        print("\n [+] Um bom dia! Volte Sempre!!!!")
        sys.exit(1)