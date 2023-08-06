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
