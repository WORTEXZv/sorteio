import os
from flask import Flask, render_template, request, jsonify

# Flask é uma biblioteca oficial do Python para criar sites
app = Flask(__name__)

ARQUIVO_NOMES = 'nomes.txt'

# Função para ler os nomes salvos no arquivo de texto
def ler_nomes():
    if not os.path.exists(ARQUIVO_NOMES):
        return []
    with open(ARQUIVO_NOMES, 'r', encoding='utf-8') as arquivo:
        # Lê as linhas e remove espaços em branco
        return [linha.strip() for linha in arquivo.readlines() if linha.strip()]

# Função para registrar um novo nome no arquivo
def salvar_nome(nome):
    with open(ARQUIVO_NOMES, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome}\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/nomes', methods=['GET', 'POST'])
def gerenciar_nomes():
    if request.method == 'POST':
        dados = request.get_json()
        nome = dados.get('nome')
        
        if nome and nome.strip():
            salvar_nome(nome.strip()) # Salva no .txt
            
        return jsonify({'status': 'sucesso'})
    
    # Se for GET, devolve a lista de nomes do .txt
    return jsonify(ler_nomes())

if __name__ == '__main__':
    # O host '0.0.0.0' permite que outras pessoas na mesma rede Wi-Fi acessem
    app.run(host='0.0.0.0', port=5000, debug=True)