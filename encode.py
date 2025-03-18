import base64
import urllib.parse
import html

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