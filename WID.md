```txt
__        _____   ____    __        ___           _     ___   ____        
\ \      / /_ _| |  _ \   \ \      / / |__   __ _| |_  |_ _| |  _ \  ___  
 \ \ /\ / / | |  | | | |   \ \ /\ / /| '_ \ / _` | __|  | |  | | | |/ _ \ 
  \ V  V /_ | | _| |_| |    \ V  V / | | | | (_| | |_   | |  | |_| | (_) |
   \_/\_/(_)___(_)____(_)    \_/\_/  |_| |_|\__,_|\__| |___| |____/ \___/

```

Imports:

```python
import os
from termcolor import colored
import random
import requests
import hashlib

``` 
These are the Libs used in the project

In the main file, there is the following system:
```python
def randomban():

    bannet = str(random.randint(1,4))
    
    if bannet == '1':
        screen()
        ban1()

    elif bannet == '2':
        screen()
        ban2()

    elif bannet == '3':
        screen()
        ban3()

    elif bannet == '4':
        screen()
        ban4()

    else:
        print(colored('Error on Banner', 'red', 'on_grey', ['bold']))
        pass
```
The ```screen()``` function boils down to this:
```python
def screen():

    os.system('clear')
```
The banner functions come down to this:
```python
def ban1():

    ban1 = r"""
    [#] Yyax
    [~] Hi Ken
    [~] Hi Barbie
    
_____________________________

The Yool Framework team warns: we aren't responsible for the misuse of our tool"""

    print(colored(ban1, 'magenta', '', ['bold']))

def ban2():

    ban2 = r"""
▓██   ██▓ ▒█████   ▒█████   ██▓         █████▒█     █░
 ▒██  ██▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██   ▒▓█░ █ ░█░
  ▒██ ██░▒██░  ██▒▒██░  ██▒▒██░       ▒████ ░▒█░ █ ░█ 
  ░ ▐██▓░▒██   ██░▒██   ██░▒██░       ░▓█▒  ░░█░ █ ░█ 
  ░ ██▒▓░░ ████▓▒░░ ████▓▒░░██████▒   ░▒█░   ░░██▒██▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░    ▒ ░   ░ ▓░▒ ▒  
 ▓██ ░▒░   ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░    ░       ▒ ░ ░  
 ▒ ▒ ░░  ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░       ░ ░     ░   ░  
 ░ ░         ░ ░      ░ ░      ░  ░              ░    
 ░ ░ 
 
 The Yool Framework team warns: we aren't responsible for the misuse of our tool"""

    print(colored(ban2, 'red', '', ['bold']))

def ban3():

    ban3 = r"""
██╗   ██╗ ██████╗  ██████╗ ██╗         ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██╔═══██╗██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
 ╚████╔╝ ██║   ██║██║   ██║██║         █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
  ╚██╔╝  ██║   ██║██║   ██║██║         ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
   ██║   ╚██████╔╝╚██████╔╝███████╗    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

The Yool Framework team warns: we aren't responsible for the misuse of our tool
"""
    print(colored(ban3, 'yellow', '', ['bold']))

def ban4():

    ban4 = r"""
 █████ █████                                                                █████      
░░███ ░░███                                                                ░░███       
 ░░███ ███    ██████   ██████   ██████   ██████   ██████   ██████   ██████  ░███       
  ░░█████    ███░░███ ███░░███ ███░░███ ███░░███ ███░░███ ███░░███ ███░░███ ░███       
   ░░███    ░███ ░███░███ ░███░███ ░███░███ ░███░███ ░███░███ ░███░███ ░███ ░███       
    ░███    ░███ ░███░███ ░███░███ ░███░███ ░███░███ ░███░███ ░███░███ ░███ ░███      █
    █████   ░░██████ ░░██████ ░░██████ ░░██████ ░░██████ ░░██████ ░░██████  ███████████
   ░░░░░     ░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░░░░░░ 

The Yool Framework team warns: we aren't responsible for the misuse of our tool
"""
    print(colored(ban4, 'cyan', '', ['bold']))
```
The framework's first tool: Nmap, for its execution, this def was used:
```python
def nmap():

    nmapopt = r"""
    
    [#] IP or URL: """
    
    nmaptype = r"""
    
    [1] Help
    [2] Padron
    [3] OS Scan
    
    Choose a type: """
    
    nchoose = input(colored(nmapopt, 'red', '', ['bold']))

    ntchoose = input(colored(nmaptype, 'red', '', ['bold']))

    if ntchoose == '1':
        ntchoose = '--help'

    elif ntchoose == '2':
        ntchoose = ''

    command = f"nmap {nchoose} {ntchoose}"
    os.system(command)
```
Of all the tools, this one is the simplest, ⭐ (and half a star) of ⭐⭐⭐⭐⭐⭐⭐

Now, a tool capable of creating and writing files so heavy that they would occupy a datacenter: Crunch

The Crunch's code is ⭐⭐⭐ of ⭐⭐⭐⭐⭐⭐⭐
```python
def crunch():

    copt = r"""

    [1] Help
    [2] Skip to crunch
    
    Choose an option: """

    coptmin = r"""

    [#] Please, insert the Min: """

    coptmax = r"""
    
    [#] Please, insert the Max: """

    coptchar = r"""
    
    [#] Please, insert the Charset: """

    copto = r"""

    [#] Please, insert the Output Name: """

    chelp = r"""
    
    Min & Max: Defines the size of each output line (ex: min 1 max 4 ! Output: a, ab, abc, abcd)
    
    Charset: Defines the digits that will be used in the wordlist generation
    
    Output: Defines the output name"""

    coptprefix = r"""
    [#] Please, insert a prefix (Enter for none): """

    copt_choose = input(colored(copt, 'white', '', ['bold']))

    if copt_choose == '1':
        print(colored(chelp, 'green', '', ['bold']))

    else:
        coptmin_choose = input(colored(coptmin, 'white', '', ['bold']))

        coptmax_choose = input(colored(coptmax, 'white', '', ['bold']))

        coptchar_choose = input(colored(coptchar, 'white', '', ['bold']))

        copto_choose = input(colored(copto, 'white', '', ['bold']))

        crunchcommand = crunchcommand = f"sudo crunch {coptmin_choose} {coptmax_choose} {coptchar_choose} -o {copto_choose}"

        os.system(crunchcommand)
```
of this time, the code got a bit big

Now, the 3rd Tool: Hydra: one of the best brute force tool (included on kali linux)
```python
def hydra():

    hoptlogin = r"""

    [#] For User:
    [1] Wordlist
    [2] Preset
    
    [#] Choose an option: """

    hoptlogin_choose = input(colored(hoptlogin, 'white', '', ['bold']))

    if hoptlogin_choose == '1':
        hydrausr = '-L'
        hoptusername = input(colored('\n  [#] User Wordlist: ', 'white', '', ['bold']))

    elif hoptlogin_choose == '2':
        hydrausr = '-l'
        hoptusername = input(colored('\n  [#] User Name: ', 'white', '', ['bold']))
    
    hoptpass = r"""

    [#] For Pass:
    [1] Wordlist
    [2] Preset
    
    [#] Choose an option: """

    hoptpass_choose = input(colored(hoptpass, 'white', '', ['bold']))

    if hoptpass_choose == '1':
        hydrapass = '-P'
        hoptpassname = input(colored('\n  [#] Pass Wordlist: ', 'white', '', ['bold']))

    elif hoptpass_choose == '2':
        hydrapass = '-p'
        hoptpassname = input(colored('\n  [#] Pass Name: ', 'white', '', ['bold']))

    hoptProcess = r"""
    
    [1] SSH
    [2] FTP
    [3] HTTP
    [4] HTTPS
    [5] Telnet
    [6] POP3
    [7] IMAP
    [8] SMB
    [9] RDP
    [10] LDAP

    [#] Choose an option: """

    hoptProcess_choose = str(input(colored(hoptProcess, 'white', '', ['bold'])))

    if hoptProcess_choose == '1':
        hydraProcess = 'ssh'

    elif hoptProcess_choose == '2':
        hydraProcess = 'ftp'

    elif hoptProcess_choose == '3':
        hydraProcess = 'http'

    elif hoptProcess_choose == '4':
        hydraProcess = 'https'

    elif hoptProcess_choose == '5':
        hydraProcess = 'telnet'

    elif hoptProcess_choose == '6':
        hydraProcess = 'pop3'

    elif hoptProcess_choose == '7':
        hydraProcess = 'imap'

    elif hoptProcess_choose == '8':
        hydraProcess = 'smb'

    elif hoptProcess_choose == '9':
        hydraProcess = 'rdp'

    elif hoptProcess_choose == '10':
        hydraProcess = 'ldap'

    hopttarget = r"""
    [#] Insert the Target IP: """

    hopttarget_choose = input(colored(hopttarget, 'white', '', ['bold']))

    hydracommandFinal = f"hydra {hydrausr} {hoptusername} {hydrapass} {hoptpassname} {hydraProcess}://{hopttarget_choose}"
```
and with 91 lines, it is classified as ⭐⭐⭐⭐⭐ of ⭐⭐⭐⭐⭐⭐⭐

The rest of the tools are separate files so ir doesn't suit me to explain all funcs and so much code in a single MarkDown file
i'll put the full code in the end

but
instead of tools, i'll show you the system of choices
```python
def opt():

    sopt = r"""
    
    [1] nmap (Needs Nmap installed)
    [2] Yyax - Info
    [3] Crunch
    [4] Hydra
    [5] Adress by Coords
    [6] CheckStatus
    [7] Crypter
    [8] Decrypt
    [9] Fake SMS
    [10] Ip Info
    [11] Reader
    [12] Tool Downloader
    [0] Exit
    
    Choose an option: """
    
    choose = input(colored(sopt, 'white', '', ['bold']))
    
    if choose == '1':
        nmap()
    elif choose == '2':
        yyax()
    elif choose == '0':
        os.system('exit')
    elif choose == '3':
        crunch()
    elif choose == '4':
        hydra()
    elif choose == '5':
        os.system('python otherTools/adress_coords.py')
    elif choose == '6':
        os.system('python otherTools/checkstatus.py')
    elif choose == '7':
        os.system('python otherTools/crypter.py')
    elif choose == '8':
        os.system('python otherTools/decrypt.py')
    elif choose == '9':
        os.system('python otherTools/fake-sms.py')
    elif choose == '10':
        os.system('python otherTools/ip-info.py')
    elif choose == '11':
        os.system('python otherTools/reader.py')
    elif choose == '12':
        os.system('python otherTools/Tools.py')
    
    else:
        print(colored('Wrong Answer, try again', 'red', '', ['bold']))

```

Now, the tools:

```python
#adress-coords.py

import os
import requests
from termcolor import colored

BANNER = r"""
   ____     ______     ______      _____    _____    _____  
  (    )   (_  __ \   (   __ \    / ___/   / ____\  / ____\ 
  / /\ \     ) ) \ \   ) (__) )  ( (__    ( (___   ( (___   
 ( (__) )   ( (   ) ) (    __/    ) __)    \___ \   \___ \  
  )    (     ) )  ) )  ) \ \  _  ( (           ) )      ) ) 
 /  /\  \   / /__/ /  ( ( \ \_))  \ \___   ___/ /   ___/ /  
/__(  )__\ (______/    )_) \__/    \____\ /____/   /____/   
                                                            

"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_endereco(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        endereco = data.get("display_name")
        return endereco
    return None

clear_screen()
print("\033[1;34m" + BANNER + "\033[0m")

# Solicitar as coordenadas do usuário
latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

endereco = obter_endereco(latitude, longitude)

if endereco:
    print("Endereço encontrado:")
    print(endereco)
    
    # Salvar o endereço em um arquivo de texto
    with open("adress.txt", "w") as arquivo:
        arquivo.write(endereco)
        print("\n" + colored("Endereço salvo no arquivo 'adress.txt'.", "blue"))
else:
    print("Endereço não encontrado.")

```

```python
#checkstatus.py
import os
import requests
import time

BANNER = r"""
 $$$$$$\ $$$$$$$$\  $$$$$$\ $$$$$$$$\ $$\   $$\  $$$$$$\  
$$  __$$\\__$$  __|$$  __$$\\__$$  __|$$ |  $$ |$$  __$$\ 
$$ /  \__|  $$ |   $$ /  $$ |  $$ |   $$ |  $$ |$$ /  \__|
\$$$$$$\    $$ |   $$$$$$$$ |  $$ |   $$ |  $$ |\$$$$$$\  
 \____$$\   $$ |   $$  __$$ |  $$ |   $$ |  $$ | \____$$\ 
$$\   $$ |  $$ |   $$ |  $$ |  $$ |   $$ |  $$ |$$\   $$ |
\$$$$$$  |  $$ |   $$ |  $$ |  $$ |   \$$$$$$  |\$$$$$$  |
 \______/   \__|   \__|  \__|  \__|    \______/  \______/ 
                                                          
                                                          
                                                          
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_estado_site(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("\033[92mO site está ativo.\033[0m")  # Mensagem em verde quando o site está ativo
            else:
                print("\033[91mO site está inativo.", response.status_code, "\033[0m")  # Mensagem em vermelho quando o site está inativo
        except requests.exceptions.RequestException:
            print("Ocorreu um erro ao verificar o estado do site.")

        time.sleep(0.5)

clear_screen()
print("\033[1;34m" + BANNER + "\033[0m")

url = input("Digite a URL do site que deseja verificar o estado: ")
verificar_estado_site(url)

```

```python
#crypter.py
import os
import hashlib
from termcolor import colored

# Função para limpar a tela e exibir o banner em vermelho
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(colored("                                                      ", "blue"))
    print(colored("                                                      ", "blue"))
    print(colored("   █████████                                  █████   ", "blue"))
    print(colored("  ███░░░░░███                                ░░███    ", "blue"))
    print(colored(" ███     ░░░  ████████  █████ ████ ████████  ███████  ", "blue"))
    print(colored("░███         ░░███░░███░░███ ░███ ░░███░░███░░░███░   ", "blue"))
    print(colored("░███          ░███ ░░░  ░███ ░███  ░███ ░███  ░███    ", "blue"))
    print(colored("░░███     ███ ░███      ░███ ░███  ░███ ░███  ░███ ███", "blue"))
    print(colored(" ░░█████████  █████     ░░███████  ░███████   ░░█████ ", "blue"))
    print(colored("  ░░░░░░░░░  ░░░░░       ░░░░░███  ░███░░░     ░░░░░  ", "blue"))
    print(colored("                         ███ ░███  ░███               ", "blue"))
    print(colored("                        ░░██████   █████              ", "blue"))
    print(colored("                         ░░░░░░   ░░░░░               ", "blue"))
    print("                                                                       ")
    print(colored("Nós não nos responsabilizamos pelo mau uso desta ferramenta", "blue"))
    print("                                                                       ")
    print("                                                                       ")
# Função para exibir as opções de criptografia
def exibir_opcoes():
    print("[01] MD5")
    print("[02] Y4X Level 7 crypt")
    print("[03] SHA")
    print("[04] R7G Level 11 crypt")
    print("[05] FLK Level 21 crypt")
    print("[06] H1X Level 53 crypt")
    print(colored("[07] Fucking 9517 crypt", "red"))
    print(colored("[08] I don't know", 'yellow', 'on_red'))
    print(colored("[09] XTC Neg 3917", 'green', 'on_blue'))

    
# Função para criptografar o texto usando a tecnologia MD5
def criptografar_md5(texto):
    md5_hash = hashlib.md5()
    md5_hash.update(texto.encode('utf-8'))
    return md5_hash.hexdigest()

# Função para criptografar o texto usando a tecnologia SHA
def criptografar_sha(texto):
    sha_hash = hashlib.sha256()
    sha_hash.update(texto.encode('utf-8'))
    return sha_hash.hexdigest()

# Função para criptografar o texto usando a criptografia Y4X Level 7
def criptografar_y4x(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 7)
        else:
            criptografado += char
    return criptografado

# Função para criptografar o texto usando a criptografia R7G Level 11
def criptografar_r7g(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 11)
        else:
            criptografado += char
    return criptografado

# Função para criptografar o texto usando a criptografia FLK Level 21
def criptografar_flk(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 21)
        else:
            criptografado += char
    return criptografado

# Função para criptografar o texto usando a criptografia H1X
def criptografar_h1x(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 53)
        else:
            criptografado += char
    return criptografado

#dumb chatgpt

def criptografar_fcking(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 9517)
        else:
            criptografado += char
    return criptografado
    
#no way

    
def criptografar_sla(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 1733)
        else:
            criptografado += char
    return criptografado
    
def criptografar_xtc(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 8932)
        else:
            criptografado += char
    return criptografado


# Limpa a tela e exibe o banner em vermelho
limpar_tela()

# Pede ao usuário um texto para codificar
Pcrypt = input("Texto para ser criptografado: ")

# Exibe as opções de criptografia
exibir_opcoes()

# Pede ao usuário para escolher uma opção
escolha = input("Escolha uma opção: ")


# Verifica a escolha do usuário e executa a criptografia correspondente
if escolha in ["1", "01"]:
    texto_criptografado = criptografar_md5(Pcrypt)
elif escolha in ["2", "02"]:
    texto_criptografado = criptografar_y4x(Pcrypt)
elif escolha in ["3", "03"]:
    texto_criptografado = criptografar_sha(Pcrypt)
elif escolha in ["4", "04"]:
    texto_criptografado = criptografar_r7g(Pcrypt)
elif escolha in ["5", "05"]:
    texto_criptografado = criptografar_flk(Pcrypt)
elif escolha in ["6", "06"]:
    texto_criptografado = criptografar_h1x(Pcrypt)
elif escolha in ["7", "07"]:
    texto_criptografado = criptografar_fcking(Pcrypt)
elif escolha in ["8", "08"]:
    texto_criptografado = criptografar_sla(Pcrypt)
elif escolha in ["9", "09"]:
    texto_criptografado = criptografar_xtc(Pcrypt)
else:
    print("Opção inválida!")

# Exibe o resultado da criptografia
print("Texto criptografado:   \n\n", texto_criptografado)

```

```python
#decrypt.py
import os

BANNER = r"""
$$$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$$\ $$\     $$\ $$$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  _____|$$  __$$\ $$  __$$\\$$\   $$  |$$  __$$\\__$$  __|
$$ |  $$ |$$ |      $$ /  \__|$$ |  $$ |\$$\ $$  / $$ |  $$ |  $$ |   
$$ |  $$ |$$$$$\    $$ |      $$$$$$   | \$$$$  /  $$$$$$$  |  $$ |   
$$ |  $$ |$$  __|   $$ |      $$  __$$<   \$$  /   $$  ____/   $$ |   
$$ |  $$ |$$ |      $$ |  $$\ $$ |  $$ |   $$ |    $$ |        $$ |   
$$$$$$$  |$$$$$$$$\ \$$$$$$  |$$ |  $$ |   $$ |    $$ |        $$ |   
\_______/ \________| \______/ \__|  \__|   \__|    \__|        \__|   
                                                                      
                                                                      
                                                                         
                                                                                           
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para descriptografar o texto usando a tecnologia MD5
def descriptografar_md5(texto_criptografado):
    return texto_criptografado

# Função para descriptografar o texto usando a tecnologia SHA
def descriptografar_sha(texto_criptografado):
    return texto_criptografado

# Função para descriptografar o texto usando a criptografia Y4X Level 7
def descriptografar_y4x(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 7)
        else:
            descriptografado += char
    return descriptografado

# Função para descriptografar o texto usando a criptografia R7G Level 11
def descriptografar_r7g(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 11)
        else:
            descriptografado += char
    return descriptografado

# Função para descriptografar o texto usando a criptografia FLK Level 21
def descriptografar_flk(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 21)
        else:
            descriptografado += char
    return descriptografado

# Função para descriptografar o texto usando a criptografia H1X
def descriptografar_h1x(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 53)
        else:
            descriptografado += char
    return descriptografado
    
def descriptografar_fck(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 9517)
        else:
            descriptografado += char
    return descriptografado


    
def descriptografar_sla(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 1733)
        else:
            descriptografado += char
    return descriptografado
    

def main():
    clear_screen()
    print("\033[1;31m" + BANNER + "\033[0m")

    # Pede ao usuário um texto criptografado para descriptografar
    texto_criptografado = input("Texto criptografado: ")

    # Exibe as opções de descriptografia
    print("[01] MD5")
    print("[02] Y4X Level 7 crypt")
    print("[03] SHA")
    print("[04] R7G Level 11 crypt")
    print("[05] FLK Level 21 crypt")
    print("[06] H1X")
    print("[7] fck")
    print("[8] sla")
    # Pede ao usuário para escolher uma opção
    escolha = input("Escolha uma opção: ")

    # Verifica a escolha do usuário e executa a descriptografia correspondente
    if escolha in ["1", "01"]:
        texto_descriptografado = descriptografar_md5(texto_criptografado)
    elif escolha in ["2", "02"]:
        texto_descriptografado = descriptografar_y4x(texto_criptografado)
    elif escolha in ["3", "03"]:
        texto_descriptografado = descriptografar_sha(texto_criptografado)
    elif escolha in ["4", "04"]:
        texto_descriptografado = descriptografar_r7g(texto_criptografado)
    elif escolha in ["5", "05"]:
        texto_descriptografado = descriptografar_flk(texto_criptografado)
    elif escolha in ["6", "06"]:
        texto_descriptografado = descriptografar_h1x(texto_criptografado)
    elif escolha in ["7", "07"]:
        texto_descriptografado = descriptografar_fck(texto_criptografado)
    elif escolha in ["8", "08"]:
        texto_descriptografado = descriptografar_sla(texto_criptografado)
    else:
        print("Opção inválida!")

    # Exibe o resultado da descriptografia
    print("Texto descriptografado:", texto_descriptografado)

if __name__ == "__main__":
    main()

```

```python
#fake-sms
import os
import requests

BANNER = r"""
$$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\        $$$$$$\  $$\      $$\  $$$$$$\  
$$  _____|$$  __$$\ $$ | $$  |$$  _____|      $$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ |      $$ /  $$ |$$ |$$  / $$ |            $$ /  \__|$$$$\  $$$$ |$$ /  \__|
$$$$$\    $$$$$$$$ |$$$$$  /  $$$$$\          \$$$$$$\  $$\$$\$$ $$ |\$$$$$$\  
$$  __|   $$  __$$ |$$  $$<   $$  __|          \____$$\ $$ \$$$  $$ | \____$$\ 
$$ |      $$ |  $$ |$$ |\$$\  $$ |            $$\   $$ |$$ |\$  /$$ |$$\   $$ |
$$ |      $$ |  $$ |$$ | \$$\ $$$$$$$$\       \$$$$$$  |$$ | \_/ $$ |\$$$$$$  |
\__|      \__|  \__|\__|  \__|\________|       \______/ \__|     \__| \______/ 
                                                                               
                                                                               
                                                                               
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class SMSAnonimo:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def enviar_sms(self):
        numero_alvo = input("Qual o número alvo? ")
        mensagem = input("Mensagem para ser enviada?  ")
        
        url = "https://rest.nexmo.com/sms/json"
        payload = {
            "api_key": self.api_key,
            "api_secret": self.api_secret,
            "from": "NEXMO_NUMBER",  # Número fornecido pela Nexmo
            "to": numero_alvo,
            "text": mensagem
        }
        
        try:
            response = requests.post(url, data=payload)
            data = response.json()
            
            if data["messages"][0]["status"] == "0":
                print("SMS enviado com sucesso!")
                print("Message ID:", data["messages"][0]["message-id"])
            else:
                print("Erro ao enviar o SMS:", data["messages"][0]["error-text"])
        except Exception as e:
            print("Erro ao enviar o SMS:", str(e))

clear_screen()
print("\033[1;34m" + BANNER + "\033[0m")

# Substitua as informações abaixo pelas suas credenciais da Nexmo
api_key = input("Sua key nexmo?  ")
api_secret = input("Sua api secret (nexmo)?  ")

sms_anonimo = SMSAnonimo(api_key, api_secret)
sms_anonimo.enviar_sms()

```

```python
#ip-info.py
import os
import requests

BANNER = r"""
$$$$$$\ $$$$$$$\        $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
\_$$  _|$$  __$$\       \_$$  _|$$$\  $$ |$$  _____|$$  __$$\ 
  $$ |  $$ |  $$ |        $$ |  $$$$\ $$ |$$ |      $$ /  $$ |
  $$ |  $$$$$$$  |$$$$$$\ $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |
  $$ |  $$  ____/ \______|$$ |  $$ \$$$$ |$$  __|   $$ |  $$ |
  $$ |  $$ |              $$ |  $$ |\$$$ |$$ |      $$ |  $$ |
$$$$$$\ $$ |            $$$$$$\ $$ | \$$ |$$ |       $$$$$$  |
\______|\__|            \______|\__|  \__|\__|       \______/ 
                                                              
                                                              
                                                             
                                                                                                         
                                                                                                         
                                                                                                         
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_dados_ip(ip, chave_acesso):
    url = f"http://api.ipstack.com/{ip}?access_key={chave_acesso}"
    response = requests.get(url)
    dados = response.json()

    ip = dados['ip']
    cidade = dados['city']
    estado = dados['region_name']
    pais = dados['country_name']
    latitude = dados['latitude']
    longitude = dados['longitude']
    coordenadas = f"{latitude}, {longitude}"

    return ip, cidade, estado, pais, latitude, longitude, coordenadas

def salvar_dados_em_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Informações do IP:\n")
        arquivo.write(f"IP: {dados[0]}\n")
        arquivo.write(f"Cidade: {dados[1]}\n")
        arquivo.write(f"Estado/Província: {dados[2]}\n")
        arquivo.write(f"País: {dados[3]}\n")
        arquivo.write(f"Latitude: {dados[4]}\n")
        arquivo.write(f"Longitude: {dados[5]}\n")
        arquivo.write(f"Coordenadas: {dados[6]}\n")

def main():
    clear_screen()
    print("\033[1;34m" + BANNER + "\033[0m")

    ip = input("Digite o IP que deseja analisar: ")
    chave_acesso = input("Digite a chave de acesso à API ipstack: ")

    dados = obter_dados_ip(ip, chave_acesso)

    if dados:
        nome_arquivo = "Yyax-ipinfo.txt"
        salvar_dados_em_arquivo(nome_arquivo, dados)
        print(f"As informações do IP foram salvas no arquivo '{nome_arquivo}'.")
    else:
        print("Não foi possível obter as informações do IP.")

if __name__ == "__main__":
    main()

```

```python
#reader.py 
import os
from termcolor import colored

BANNER = r"""
                                                                
    _/_/_/                              _/                      
   _/    _/    _/_/      _/_/_/    _/_/_/    _/_/    _/  _/_/   
  _/_/_/    _/_/_/_/  _/    _/  _/    _/  _/_/_/_/  _/_/        
 _/    _/  _/        _/    _/  _/    _/  _/        _/           
_/    _/    _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/            
                                                                
                                                                

"""
OPTIONS = r"""
 [01] Save
 [02] Print
 [03] Print & Save
 [00] Quit
          """
def limpar_tela():
    os.system('clear')

def write():
    with open(output_name, "w") as arquivo:
          arquivo.write(arq_content)
    print("\n" + colored("Content save", "blue"))


def read_arq(arq_adress):
    with open(arq_adress, 'r') as arquivo:
        content = arquivo.read()
    return content


limpar_tela()
print("\033[1;34m" + BANNER + "\033[0m")
arq_adress = input(colored("Caminho do arquivo alvo:  ", "magenta"))
output_name = input(colored("nome do output (inclua .txt ou outras extensões):  ",  "magenta"))
arq_content = read_arq(arq_adress)

print(colored(OPTIONS, "blue"))
tttt = input(colored("\n\n Escolha uma opção:  ", "blue"))

if tttt in ["1", "'1'", "01", "'01'"]:
    write()
elif tttt in ["2", "'2'", "02", "'02'"]:
    print(arq_content)
elif tttt in ["3", "'3'", "03", "'03'"]:
    print(arq_content)
    write()
elif tttt in ["0", "00"]:
    input("Para sair, digite q e pressione Enter...   ") 
    os.system("clear")
else:
     print(colored("Resposta invalida, reinicie o programa com Ctrl + C ", "red"))

input("Pressione Enter para continuar...") 
os.system("clear")

```

```python
#Tools.py
import os

BANNER = r"""
$$$$$$$$\  $$$$$$\   $$$$$$\  $$\       $$$$$$\  
\__$$  __|$$  __$$\ $$  __$$\ $$ |     $$  __$$\ 
   $$ |   $$ /  $$ |$$ /  $$ |$$ |     $$ /  \__|
   $$ |   $$ |  $$ |$$ |  $$ |$$ |     \$$$$$$\  
   $$ |   $$ |  $$ |$$ |  $$ |$$ |      \____$$\ 
   $$ |   $$ |  $$ |$$ |  $$ |$$ |     $$\   $$ |
   $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\\$$$$$$  |
   \__|    \______/  \______/ \________|\______/ 
                                                 
                                                                                                   
                                                                                                   
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("------ Ferramenta Yyax ------")
    print("[1] DDoS")
    print("[2] Phishing")
    print("[3] Hackear Wifi")
    print("[4] AntiLogs")
    print("[5] Info Gathering")
    print("[6] Virus")
    print("[7] Tools")
    print("[0] Sair")

def executar_ferramenta(link_git):
    os.system("git clone " + link_git)
    pasta = link_git.split("/")[-1].split(".")[0]
    os.chdir(pasta)
    os.system("bash install.sh")
    os.chdir("..")
    os.system("rm -rf " + pasta)

while True:
    clear_screen()
    print("\033[1;34m" + BANNER + "\033[0m")
    exibir_menu()
    opcao = input("Digite o número da categoria que deseja executar (0 para sair): ")

    if opcao == "0":
        break

    elif opcao == "1":
        links = [
            "https://github.com/b3-v3r/hunner",
            "https://github.com/palahsu/DDoS-Ripper.git",
            "https://github.com/pembriahmad/DDOS",
            "https://github.com/Alygnt/fl00d-wifi",
            "https://github.com/cyweb/hammer",
            "https://github.com/biyivi/biyivi_ataque_DDos",
            "https://github.com/gkbrk/slowloris.git",
            "https://github.com/Lucky1376/ORION-Bomber",
            "https://github.com/HyukIsBack/KARMA-DDoS.git",
            "https://github.com/antichristone/antichristone_x86"
        ]
        for link in links:
            executar_ferramenta(link)

    elif opcao == "2":
        links = [
            "https://github.com/An0nUD4Y/blackeye",
            "https://github.com/princekrvert/Asura.git",
            "https://github.com/htr-tech/nexphisher.git",
            "https://github.com/foxlitegor/fisher",
            "https://github.com/noob-hackers/grabcam",
            "https://github.com/LiNuX-Mallu/CAM-DUMPER.git",
            "https://github.com/thewhiteh4t/seeker",
            "https://github.com/Bafomet666/Bigbro",
            "https://github.com/noob-hackers/ighack",
            "https://github.com/Abominate34/Ghost",
            "https://github.com/AzeemIdrisi/PhoneSploit-Pro.git",
            "https://github.com/AngelSecurityTeam/Cam-Hackers",
            "https://github.com/techchipnet/CamPhish"
        ]
        for link in links:
            executar_ferramenta(link)

    elif opcao == "3":
        links = [
            "https://github.com/drygdryg/OneShot",
            "https://github.com/Neo23x0/Loki"
        ]
        for link in links:
            executar_ferramenta(link)

    elif opcao == "4":
        links = [
            "https://github.com/claprusshow/ANTILOGS"
        ]
        for link in links:
            executar_ferramenta(link)

    elif opcao == "5":
        links = [
            "https://github.com/mxrch/GHunt",
            "https://github.com/snooppr/snoop.git",
            "https://github.com/3xploitGuy/webscrape.git",
            "https://github.com/TechnicalMujeeb/TM-scanner",
            "https://github.com/stanislav-web/OpenDoor.git",
            "https://github.com/Deadpool2000/IPicker.git",
            "https://github.com/th3unkn0n/osi.ig.git",
            "https://github.com/viewerdiscretion/sashay.git",
            "https://github.com/Ranginang67/beyawak"
        ]
        for link in links:
            executar_ferramenta(link)

    elif opcao == "6":
        links = [
            "https://github.com/ZechBron/zVirus-Gen",
            "https://github.com/ytisf/theZoo",
            "https://github.com/cyberknight777/PhoneSploit"
        ]
        for link in links:
            executar_ferramenta(link)

    elif opcao == "7":
        links = [
            "https://github.com/adi1090x/termux-style",
            "https://github.com/saintmalik/Ethicaltools.git",
            "https://github.com/ZechBron/Mega-File-Stealer",
            "https://github.com/IlayTamvan/Report",
            "https://github.com/ShTasrif/cybersh"
        ]
        for link in links:
            executar_ferramenta(link)

input("Pressione Enter para continuar...") 
os.system("clear")

```