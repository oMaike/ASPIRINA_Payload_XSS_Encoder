import base64
import urllib.parse
import html
from colorama import Fore, Style  # Importa a biblioteca para cores

def exibir_menu():
    print(Fore.BLUE + """
 .S_SSSs      sSSs   .S_sSSs     .S   .S_sSSs     .S   .S_sSSs     .S_SSSs    
.SS~SSSSS    d%%SP  .SS~YS%%b   .SS  .SS~YS%%b   .SS  .SS~YS%%b   .SS~SSSSS   
S%S   SSSS  d%S'    S%S   `S%b  S%S  S%S   `S%b  S%S  S%S   `S%b  S%S   SSSS  
S%S    S%S  S%|     S%S    S%S  S%S  S%S    S%S  S%S  S%S    S%S  S%S    S%S  
S%S SSSS%S  S&S     S%S    d*S  S&S  S%S    d*S  S&S  S%S    S&S  S%S SSSS%S  
S&S  SSS%S  Y&Ss    S&S   .S*S  S&S  S&S   .S*S  S&S  S&S    S&S  S&S  SSS%S  
S&S    S&S  `S&&S   S&S_sdSSS   S&S  S&S_sdSSS   S&S  S&S    S&S  S&S    S&S  
S&S    S&S    `S*S  S&S~YSSY    S&S  S&S~YSY%b   S&S  S&S    S&S  S&S    S&S  
S*S    S&S     l*S  S*S         S*S  S*S   `S%b  S*S  S*S    S*S  S*S    S&S  
S*S    S*S    .S*P  S*S         S*S  S*S    S%S  S*S  S*S    S*S  S*S    S*S  
S*S    S*S  sSS*S   S*S         S*S  S*S    S&S  S*S  S*S    S*S  S*S    S*S  
SSS    S*S  YSS'    S*S         S*S  S*S    SSS  S*S  S*S    SSS  SSS    S*S  
       SP           SP          SP   SP          SP   SP                 SP   
       Y            Y           Y    Y           Y    Y                  Y 
   
                                                                                                          
""" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "xwitter: @yott4ma1k3" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "github.com/oMaike" + Style.RESET_ALL)
    
    print("\nBem-vindo ao ASPIRINA !")
    print("Escolha uma opção de encode abaixo:\n")

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def encode_url(text):
    return urllib.parse.quote(text)

def encode_html(text):
    return html.escape(text)

def encode_utf8(text):
    return text.encode('utf-8').hex()  # Retorna a representação hexadecimal do UTF-8

def encode_unicode(text):
    # Converte cada caractere para seu valor Unicode (ex: 'a' -> '\u0061')
    return ''.join([f'\\u{ord(char):04x}' for char in text])

def encode_hex(text):
    # Converte cada caractere para seu valor hexadecimal (ex: 'a' -> '61')
    return ''.join([f'\\x{ord(char):02x}' for char in text])

def main():
    # Exibe o menu inicial
    exibir_menu()

    # Solicita o payload XSS (ou qualquer texto) do usuário
    payload = input("Digite o payload XSS (ou qualquer texto): ")

    # Pergunta ao usuário qual codificação ele deseja
    print("\nEscolha o tipo de codificação:")
    print("1 - Base64")
    print("2 - URL Encoding")
    print("3 - HTML Entities")
    print("4 - UTF-8 (Hexadecimal)")
    print("5 - Unicode Encoding")
    print("6 - Hex Encoding")
    escolha = input("Digite o número da opção desejada: ")

    # Aplica a codificação escolhida
    if escolha == "1":
        resultado = encode_base64(payload)
        print(f"\nResultado em Base64: {resultado}")
    elif escolha == "2":
        resultado = encode_url(payload)
        print(f"\nResultado em URL Encoding: {resultado}")
    elif escolha == "3":
        resultado = encode_html(payload)
        print(f"\nResultado em HTML Entities: {resultado}")
    elif escolha == "4":
        resultado = encode_utf8(payload)
        print(f"\nResultado em UTF-8 (Hexadecimal): {resultado}")
    elif escolha == "5":
        resultado = encode_unicode(payload)
        print(f"\nResultado em Unicode Encoding: {resultado}")
    elif escolha == "6":
        resultado = encode_hex(payload)
        print(f"\nResultado em Hex Encoding: {resultado}")
    else:
        print("\nOpção inválida! Por favor, execute o programa novamente.")

if __name__ == "__main__":
    main()
