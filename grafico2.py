# Código para obter mais leituras de luminosidade em um intervalo de tempo.
import requests
import matplotlib.pyplot as plt

# Função para obter os dados de luminosidade a partir da API
def obter_dados_luminosidade(dispositivo, dateFrom, dateTo, lastN):
    endereco_url = "46.17.108.113"
    url = f"http://{endereco_url}:8666/STH/v1/contextEntities/type/Lamp/id/{dispositivo}/attributes/luminosity?dateFrom={dateFrom}&dateTo={dateTo}&lastN={lastN}"
    headers = {
        'fiware-service': 'smart',
        'fiware-servicepath': '/'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        luminosity_data = data['contextResponses'][0]['contextElement']['attributes'][0]['values']
        return luminosity_data
    else:
        print(f"Erro ao obter dados: {response.status_code}")
        return []

# Função para criar e exibir o gráfico
def plotar_grafico(luminosity_data):
    if not luminosity_data:
        print("Nenhum dado disponível para plotar.")
        return
    luminosidade = [entry['attrValue'] for entry in luminosity_data]
    tempos = [entry['recvTime'] for entry in luminosity_data]
    plt.figure(figsize=(12, 6))
    plt.plot(tempos, luminosidade, marker='o', linestyle='-', color='r')
    plt.title('Gráfico de Luminosidade em Função do Tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Luminosidade')
    plt.xticks(rotation=80)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Inicializa uma lista vazia para armazenar os dados
dados_completos = []

# Número total de registros que você deseja recuperar
total_registros_desejados = 81

# Define o tamanho do lote para cada chamada (o limite da API)
tamanho_lote = 100

# Faz chamadas sequenciais até obter o número desejado de registros
while len(dados_completos) < total_registros_desejados:
    # Calcula o valor de lastN para esta chamada
    lastN = min(tamanho_lote, total_registros_desejados - len(dados_completos))

    # Obtém os dados e adicione-os à lista de dados completos
    luminosity_data = obter_dados_luminosidade("urn:ngsi-ld:Lamp:001","2023-09-19T18:32:37.257Z", "2023-09-19T18:47:17.257Z",lastN)
    dados_completos.extend(luminosity_data)

    # Atualiza o total de registros recuperados
    total_registros_recuperados = len(dados_completos)

    print(f"Registros recuperados: {total_registros_recuperados}/{total_registros_desejados}")

# Obtém os dados de luminosidade completos e plote o gráfico
luminosity_data.sort(key=lambda x: x['recvTime'])
plotar_grafico(dados_completos)