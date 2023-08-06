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
