🚀 Instalação Rápida
Copie e cole este comando no seu terminal:

bash
Copiar
Editar
git clone https://github.com/oMaike/aspirina.git && cd aspirina && pip install colorama && python3 aspirina.py
📚 Como Usar o ASPIRINA - Guia Completo
🟢 Inicialização
Abra o terminal.

Navegue até a pasta onde salvou o script:

bash
Copiar
Editar
cd caminho/para/pasta
Execute o script:

bash
Copiar
Editar
python3 aspirina.py
💡 No Windows, use python ou py no lugar de python3.

🖥️ Interface do Usuário
Ao executar, você verá:

Um logo ASCII colorido do ASPIRINA

Um prompt para inserir seu texto

🔤 Inserindo o Texto
Digite ou cole o texto que deseja codificar:

bash
Copiar
Editar
Digite o texto/payload: <script>alert('teste')</script>
Pressione Enter para continuar.

🔢 Seleção de Encoding
Será exibido um menu com 6 opções:

less
Copiar
Editar
Escolha o encoding:
1 - Base64
2 - URL Encoding
3 - HTML Entities
4 - UTF-8 (Hex)
5 - Unicode
6 - Hex Encoding

Opção:
Digite o número da opção desejada e pressione Enter.

💾 Resultado
Você verá o texto codificado de acordo com a opção escolhida:

bash
Copiar
Editar
Resultado em Base64: PHNjcmlwdD5hbGVydCgndGVzdGUnKTwvc2NyaXB0Pg==
🔄 Execução Contínua
O script encerra após cada operação.

Para realizar nova codificação, execute novamente:

bash
Copiar
Editar
python3 aspirina.py
💡 Dicas Avançadas
✅ Automatização
Você pode pipear o texto diretamente para o script:

bash
Copiar
Editar
echo "seu texto" | python3 aspirina.py
💻 Exemplo Completo
bash
Copiar
Editar
$ python3 aspirina.py
Digite o texto/payload: <div>teste</div>
Escolha o encoding: 3
Resultado em HTML Entities: &lt;div&gt;teste&lt;/div&gt;
🧰 Dependências
Se encontrar problemas com cores no terminal, instale a biblioteca necessária:

bash
Copiar
Editar
pip install colorama
⚠️ Solução de Problemas
Erros de encoding:

Salve o arquivo como UTF-8

Execute em terminal com suporte UTF-8

No Windows: use chcp 65001 antes de executar

Erro de módulos:

Instale as dependências:

bash
Copiar
Editar
pip install colorama
✨ Recursos
✅ 6 métodos diferentes de encoding

🎨 Interface colorida com ASCII art

🔄 Conversão rápida e eficiente

📋 Fácil de copiar e colar os resultados

🛠️ Tabela de Encodings
Código	Tipo	Exemplo de Saída
1	Base64	VGVzdGUgMTIz
2	URL Encoding	%3Cscript%3E
3	HTML Entities	&lt;script&gt;
4	UTF-8 (Hex)	7465737465
5	Unicode	\u0074\u0065\u0073\u0074
6	Hex Encoding	\x74\x65\x73\x74\x65

⚠️ Aviso Legal
Esta ferramenta é fornecida apenas para fins educacionais e de teste legítimo.
O uso para atividades ilegais é estritamente proibido.

📜 Licença
Distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

📬 Contato
Twitter: @yott4ma1k3

GitHub: github.com/oMaike

🧪 Nota: Para melhor experiência, execute o script em um terminal com suporte a cores.
