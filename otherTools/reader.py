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

