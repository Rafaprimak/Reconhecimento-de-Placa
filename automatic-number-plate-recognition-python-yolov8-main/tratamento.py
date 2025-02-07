import csv
import json
import os

# Função para ler dados do arquivo CSV
def ler_dados_csv(arquivo_entrada):
    dados = []
    with open(arquivo_entrada, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                car_id = row['car_id'].strip()
                license_number = row['license_number'].strip()
                dados.append((car_id, license_number))
            except ValueError:
                continue
    return dados

# Função para remover duplicatas e manter o último license_number para cada car_id
def remover_duplicatas(dados):
    dados_dict = {}
    for car_id, license_number in dados:
        dados_dict[car_id] = license_number
    return dados_dict

# Função para salvar os dados únicos em um arquivo JSON
def salvar_dados_json(dados, arquivo_saida):
    os.makedirs(os.path.dirname(arquivo_saida), exist_ok=True)
    with open(arquivo_saida, 'w') as file:
        json.dump(dados, file, indent=4)

# Caminhos dos arquivos
arquivo_entrada = './CSV/test_interpolated.csv'
arquivo_saida = 'Dados Tratados/output_tratado.txt'

# Atualizando o processo de leitura, tratamento e salvamento dos dados
dados_com_scores = ler_dados_csv(arquivo_entrada)
dados_unicos = remover_duplicatas(dados_com_scores)
salvar_dados_json(dados_unicos, arquivo_saida)

print(f"Dados únicos salvos em {arquivo_saida}")