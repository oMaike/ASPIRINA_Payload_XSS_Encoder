# ASPIRINA
[![Twitter](https://img.shields.io/twitter/follow/Ghcjm60SUve6BMa?style=social&logo=twitter&label=Follow%20me)](https://twitter.com/Ghcjm60SUve6BMa)

[![LinkedIn](https://img.shields.io/badge/Connect%20with%20me-blue?style=social&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/maike-gabriel-rosa-876673282)


![Image](https://github.com/user-attachments/assets/8f8fd99a-c1d5-420f-908a-bbb8e769d2b0)



Codificador de Payloads XSS

Este é um programa em Python que permite codificar payloads XSS (ou qualquer texto) em diferentes formatos de encoding, como Base64, URL Encoding, HTML Entities, UTF-8 (Hexadecimal), Unicode Encoding e Hex Encoding. Ele foi projetado para ajudar a testar e entender como diferentes técnicas de codificação podem ser usadas em cenários de segurança, como bypass de filtros XSS.

# Como Funciona

O programa solicita que o usuário insira um payload (ou qualquer texto) e, em seguida, oferece uma lista de opções de codificação. Dependendo da escolha do usuário, o payload é codificado no formato selecionado e o resultado é exibido na tela.

# Opções de Codificação

O programa suporta as seguintes técnicas de codificação:

Base64: Codifica o texto em Base64.

Exemplo: <script>alert('XSS')</script> → 
PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=

URL Encoding: Codifica o texto para ser usado em URLs.

Exemplo: <script>alert('XSS')</script> → 
%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E

HTML Entities: Converte caracteres especiais em entidades HTML.

Exemplo: <script>alert('XSS')</script> → 
&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;

UTF-8 (Hexadecimal): Converte o texto para sua representação hexadecimal em UTF-8.

Exemplo: <script>alert('XSS')</script> → 
3c7363726970743e616c657274282758535327293c2f7363726970743e

Unicode Encoding: Converte cada caractere para seu valor Unicode.

Exemplo: <script>alert('XSS')</script> → \u003c\u0073\u0063\u0072\u0069\u0070\u0074\u003e\u0061\u006c\u0065\u0072\u0074\u0028\u0027\u0058\u0053\u0053\u0027\u0029\u003c\u002f\u0073\u0063\u0072\u0069\u0070\u0074\u003e

Hex Encoding: Converte cada caractere para seu valor hexadecimal.

Exemplo: <script>alert('XSS')</script> → \x3c\x73\x63\x72\x69\x70\x74\x3e\x61\x6c\x65\x72\x74\x28\x27\x58\x53\x53\x27\x29\x3c\x2f\x73\x63\x72\x69\x70\x74\x3e

# Como Usar

Execute o programa:

Salve o código em um arquivo, por exemplo, encoder.py

Execute o arquivo com Python:

# bash
python encoder.py

Insira o payload:

O programa solicitará que você insira um payload XSS (ou qualquer texto).

Exemplo de entrada:

<script>alert('XSS')</script>
Escolha a codificação:

O programa exibirá uma lista de opções de codificação.
Digite o número correspondente à técnica desejada.

Veja o resultado:

O programa exibirá o payload codificado no formato escolhido.

# Exemplo de Uso

Entrada:
Digite o payload XSS (ou qualquer texto): <script>alert('XSS')</script>

Escolha o tipo de codificação:
1 - Base64
2 - URL Encoding
3 - HTML Entities
4 - UTF-8 (Hexadecimal)
5 - Unicode Encoding
6 - Hex Encoding

Digite o número da opção desejada: 1

Saída:

Resultado em Base64: PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=

# Requisitos

Python 3.x

# Aplicações

Este programa pode ser útil para:

Testar técnicas de bypass de filtros XSS.

Entender como diferentes tipos de encoding funcionam.

Codificar strings para uso em contextos específicos (URLs, HTML, JavaScript, etc.).

# Observações
Uso Ético: Este programa é destinado apenas para fins educacionais e de teste em ambientes controlados. Nunca use técnicas de XSS em sistemas reais sem permissão explícita.

Personalização: Sinta-se à vontade para modificar o código para adicionar novas funcionalidades ou melhorar as existentes.
