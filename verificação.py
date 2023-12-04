import difflib

# Duas strings de códigos para comparação
codigo1 = '''
def soma(a, b):
    return a + b
'''

codigo2 = '''
def soma(a, b):
    return a + b
'''

# Converte as strings em listas de linhas
linhas_codigo1 = codigo1.splitlines()
linhas_codigo2 = codigo2.splitlines()

# Cria um objeto Differ
d = difflib.Differ()

# Compara as listas de linhas
diff = list(d.compare(linhas_codigo1, linhas_codigo2))

# Exibe as diferenças
for linha in diff:
    print(linha)