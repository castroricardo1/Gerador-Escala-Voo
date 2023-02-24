import re
import json

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO PARA TIRAR O ESPAÇO INICIAL

with open('tam.txt', 'r', encoding='utf-8') as f:
    conteudo = f.readlines()

conteudo_modificado = [linha.lstrip() for linha in conteudo]

with open('arquivo_modificado.txt', 'w') as f:
    f.writelines(conteudo_modificado)

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO PARA FILTRAR SOMENTE POR NUMEROS

with open('arquivo_modificado.txt', 'r', encoding='ISO-8859-1') as f_origem:
    linhas_com_numero = [linha.strip() for linha in f_origem.readlines() if re.match(r'^\d', linha)]


with open('arquivo_destino.txt', 'w', encoding='utf-8') as f_destino:
    for linha in linhas_com_numero:
        f_destino.write(linha + '\n')

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO PARA RETIRAR O EQPT

with open('arquivo_destino.txt', 'r', encoding='utf-8') as f_origem, open('arquivo_sem_eqpt.txt', 'w', encoding='utf-8') as f_destino:
    for linha in f_origem:
        linha_modificada = linha.replace('EQPT/SDE2FGHIM1RWXYZ/C', '')
        f_destino.write(linha_modificada)

#-------------------------------------------------------------------------------------------------------
#TRCHO DE CODIGO QUE RETIRA AS 2 PRIMEIRAS COLUNAS

with open('arquivo_sem_eqpt.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

linhas_modificadas = []

for linha2 in linhas:
    colunas = linha2.split()
    nova_linha = ' '.join(colunas[2:]) + '\n'
    linhas_modificadas.append(nova_linha)

with open('arquivo_sem_coluna.txt', 'w', encoding='utf-8') as f:
    f.writelines(linhas_modificadas)

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO QUE SEPARA O DESTINO DO TEMPO DE VOO

with open('arquivo_sem_coluna.txt', 'r') as f:
    linhas = f.readlines()

# iterar sobre as linhas e aplicar a expressão regular
with open('separando.txt', 'w') as f:
    for linha in linhas:
        match = re.findall(r'([A-Z]{3})(\d{4})$', linha)
        codigo = match[0][0] if match else ''
        numero = match[0][1] if match else ''
        linha_formatada = linha.replace(match[0][0]+match[0][1], codigo+' '+numero)
        f.write(linha_formatada)

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO QUE RETIRA A ROTA DE VOO

# Lê o arquivo de texto e armazena cada linha em uma lista
with open('separando.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i in range(len(linhas)):
    linha = linhas[i]
    match = re.search(r'\d+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(.*?)\s+(?=SB)', linha)
    if match:
        linha_formatada = re.sub(match.group(1), '', linha)
        linhas[i] = linha_formatada

with open('arquivo_formatado.txt', 'w') as arquivo:
    arquivo.writelines(linhas)

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO QUE RETIRA O NIVEL DE VOO E VELOCIDADE

with open('arquivo_formatado.txt', 'r') as file:
    lines = file.readlines()
    new_lines = []
    for line in lines:
        columns = line.split()
        new_line = ' '.join(columns[:4] + columns[6:]) + '\n'
        new_lines.append(new_line)

with open('retirar_nivel_voo.txt', 'w') as new_file:
    new_file.writelines(new_lines)

#-------------------------------------------------------------------------------------------------------
#TRECHO DE CODIGO QUE SEPARA A HORA DA ORIGEM

import re

with open('retirar_nivel_voo.txt', 'r') as f:
    linhas = f.readlines()

# iterar sobre as linhas e separar a quarta coluna
with open('testando.txt', 'w') as f:
    for linha in linhas:
        match = re.match(r'^(.*?)\s+(\S{4})(\d{4})\s+(.*?)$', linha)
        if match:
            coluna_1 = match.group(1)
            coluna_2 = match.group(2)
            coluna_3 = match.group(3)
            coluna_4 = match.group(4)
            nova_linha = f"{coluna_1} {coluna_2} {coluna_3} {coluna_4}\n"
            f.write(nova_linha)
        else:
            f.write(linha)

#-------------------------------------------------------------------------------------------------------
#GERANDO JSON

import json

with open('testando.txt', 'r', encoding='utf-8') as f:
    conteudo = f.readlines()

dados = []

for linha in conteudo:
    colunas = linha.split() # Separar as colunas
    dados.append({
        'dia': colunas[0],
        'numero': colunas[1],
        'aviao': colunas[2],
        'origem': colunas[3],
        'horaorigem': colunas[4],
        'destino': colunas[5],
        'tempo de voo': colunas[6]
    })

# Transformar os dados em JSON
dados_json = json.dumps(dados)

# Salvar o JSON em um novo arquivo
with open('arquivo.json', 'w') as f:
    f.write(dados_json)


