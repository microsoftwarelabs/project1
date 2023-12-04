/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 


import subprocess
import webview
import webview

# cria e chama scripts css, html e javascript 
# de dentro do código Python @@

# Variável Python
mensagem_python = "Olá do Python!"

# Função JavaScript que recebe uma mensagem e a exibe
javascript_code = """
function exibirMensagem(mensagem) {
    document.getElementById('mensagem').innerText = mensagem;
}
"""

# Conteúdo HTML com integração de variáveis e JavaScript
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        h1 {{
            color: #007bff;
        }}
    </style>
    <script>
        {javascript_code}
    </script>
</head>
<body>
    <h1>Integração Python/JavaScript/HTML/CSS</h1>
    <p id="mensagem"></p>
    <button onclick="exibirMensagem('{mensagem_python}')">Clique para exibir mensagem do Python</button>
</body>
</html>
"""

# Criando e exibindo a janela com o conteúdo HTML
webview.create_window("Integração Python/JavaScript/HTML/CSS", html=html_content, width=400, height=300)
webview.start()




# chama scripts css, html e javascript de 
# arquivos separados do código Python @@

# Variável
 <link category="PROGRAMMING">Python</link>
mensagem_python = "Olá do Python!"

# Lendo o conteúdo dos arquivos
<link category="WEBPAGE">JavaScript</link>, <link category="WEBPAGE">HTML</link> e <link category="WEBPAGE">CSS</link>
with open('script.js', 'r') as file:
    javascript_code = file.read()

with open('style.css', 'r') as file:
    css_code = file.read()

with open('index.html', 'r') as file:
    html_content = file.read()

# Criando e exibindo a janela com o conteúdo <link category="WEBPAGE">HTML</link>, <link category="WEBPAGE">JavaScript</link> e <link category="WEBPAGE">CSS</link>
webview.create_window("Integração Python/JavaScript/HTML/CSS", html=html_content, js=javascript_code, css=css_code, width=400, height=300)
webview.start()




# Chamar o código javascript Node.js @@

<link category="WEBPAGE">JavaScript</link> usando <link category="WEBPAGE">Node.js</link>
resultado = subprocess.check_output(['node', 'seu_codigo_javascript.js'])

# Decodificar o resultado para obter uma string legível
resultado_decodificado = resultado.decode('utf-8')

# Imprimir o resultado
print(resultado_decodificado)