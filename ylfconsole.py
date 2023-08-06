import os
from termcolor import colored
import random

def screen():

    os.system('clear')

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

def yyax():

    yinfo = r"""
    
    https://github.com/Yyax13
    
    yyax.13#0000
    
    Instagram @rvnggroup
    
    TikTok @rvngyyax"""

    print(colored(yinfo, 'blue', '', ['bold']))



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

def main():

    randomban()
    opt()

main()

#'grey',
#            'red',
#           'green',
#          'yellow',
#         'blue',
#        'magenta',
#       'cyan',
#      'white'

finalInput_coloredColor = str(random.randint(1,6))

if finalInput_coloredColor == '1':
    finaltext_color = 'red'
elif finalInput_coloredColor == '2':
    finaltext_color = 'green'
elif finalInput_coloredColor == '3':
    finaltext_color = 'yellow'
elif finalInput_coloredColor == '4':
    finaltext_color = 'blue'
elif finalInput_coloredColor == '5':
    finaltext_color = 'magenta'
elif finalInput_coloredColor == '6':
    finaltext_color = 'cyan'

finalInput_colored = f"colored(finaltext, '{finaltext_color}', '', ['bold', 'blink'])"
input(finalInput_colored)