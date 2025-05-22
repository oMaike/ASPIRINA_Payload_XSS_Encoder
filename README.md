# 🔥 ASPIRINA - Ferramenta de Encoding

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg) 
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## 📌 Visão Geral
Ferramenta completa para conversão de textos em múltiplos formatos de encoding, desenvolvida em Python com interface colorida e intuitiva.

## 📥 Instalação Rápida

```bash
# Copie e cole este comando no seu terminal:
git clone https://github.com/oMaike/aspirina.git && cd aspirina && pip install colorama && python3 aspirina.py

📚 Como Usar o ASPIRINA - Guia Completo
Aqui está um passo a passo detalhado para usar a ferramenta ASPIRINA:

🚀 Inicialização
Abra o terminal (Command Prompt no Windows, Terminal no macOS/Linux)

Navegue até a pasta onde salvou o script:

bash
cd caminho/para/pasta
Execute o script:

bash
python aspirina.py
🖥️ Interface do Usuário
Ao executar, você verá:

Um logo ASCII colorido do ASPIRINA

Informações de contato (Twitter e GitHub)

O prompt para inserir seu texto

🔤 Inserindo o Texto
Digite ou cole o texto que deseja codificar

Digite o texto/payload: <script>alert('teste')</script>
Pressione Enter

🔢 Seleção de Encoding
Você verá um menu com 6 opções:

Escolha o encoding:
1 - Base64
2 - URL Encoding
3 - HTML Entities
4 - UTF-8 (Hex)
5 - Unicode
6 - Hex Encoding
Opção: 
Digite o número correspondente ao formato desejado e pressione Enter.

💾 Resultados
O script mostrará o texto codificado no formato escolhido:

Resultado em Base64: PHNjcmlwdD5hbGVydCgndGVzdGUnKTwvc2NyaXB0Pg==
🔄 Execução Contínua
O script encerra após cada operação (por design)

Para nova codificação, execute novamente:

bash
python aspirina.py
💡 Dicas Avançadas
Para Windows:

Use py ou python no lugar de python3

Se tiver erro de cores, instale o colorama:

cmd
pip install colorama
Automatização:
Você pode pipear o texto diretamente:

bash
echo "seu texto" | python aspirina.py
Exemplo Completo:

bash
$ python aspirina.py
Digite o texto/payload: <div>teste</div>
Escolha o encoding: 3
Resultado em HTML Entities: &lt;div&gt;teste&lt;/div&gt;
⚠️ Solução de Problemas
Se vir erros de encoding, tente:

Salvar o arquivo como UTF-8

Executar em terminal UTF-8

Para Windows: chcp 65001 antes de executar

Erros de módulos: instale as dependências:

bash
pip install colorama


✨ Recursos

✅ 6 métodos de encoding diferentes

🎨 Interface colorida com ASCII art

🔄 Conversão rápida e eficiente

📋 Pronto para copiar e colar resultados

🛠️ Opções de Encoding

Código	Tipo	Exemplo de Saída

1.	Base64	VGVzdGUgMTIz
2.	URL Encoding	%3Cscript%3E
3.	HTML Entities	<script>
4.	UTF-8 (Hex)	7465737465
5.	Unicode	\u0074\u0065\u0073\u0074\u0065
6.	Hex Encoding	\x74\x65\x73\x74\x65
   
⚠️ Aviso Legal
Esta ferramenta é fornecida apenas para fins educacionais e de teste legítimo. O uso para atividades ilegais é estritamente proibído.

📜 Licença
Distribuído sob licença MIT. Consulte o arquivo LICENSE para mais informações.

📬 Contato

Twitter: @yott4ma1k3

GitHub: github.com/oMaike

Nota: Para melhor experiência, execute em terminal com suporte a cores.

Este bloco único contém:
1. Cabeçalho com badges
2. Visão geral com código incorporado
3. Lista completa de recursos
4. Instruções de uso
5. Tabela de referência rápida
6. Informações legais e de contato

Basta copiar todo este conteúdo e colar em seu arquivo README.md!
