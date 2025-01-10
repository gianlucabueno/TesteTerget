import json
import xml.etree.ElementTree as ET

# Função para fazer a análise do faturamento
def analise_faturamento(faturamento_diario):
    menor_faturamento = 0  # Começando com infinito para garantir que qualquer valor será menor
    maior_faturamento = 0 # Começando com -infinito para garantir que qualquer valor será maior
    soma_faturamento = 0
    dias_validos = 0
   
    # Laço para percorrer todos os dias e calcular os valores
    for faturamento in faturamento_diario:
        if faturamento['valor'] > 0:  # Ignorando dias sem faturamento
            # Atualizando menor e maior faturamento
            if menor_faturamento == 0 and maior_faturamento == 0:
                menor_faturamento = faturamento['valor']
                maior_faturamento = faturamento['valor']
            elif faturamento['valor'] < menor_faturamento:
                menor_faturamento = faturamento['valor']
            elif faturamento['valor'] > maior_faturamento:
                maior_faturamento = faturamento['valor']
            
            # Somando os faturamentos válidos
            soma_faturamento += faturamento['valor']
            dias_validos += 1

    # Calculando a média de faturamento
    if dias_validos > 0:
        media_faturamento = soma_faturamento / dias_validos
    else:
        media_faturamento = 0

    # Contando o número de dias com faturamento superior à média
    dias_acima_media = 0
    for faturamento in faturamento_diario:
        if faturamento['valor'] > media_faturamento:
            dias_acima_media += 1
        
    # Exibindo os resultados
    print(f"Menor faturamento: {menor_faturamento:.2f}")
    print(f"Maior faturamento: {maior_faturamento:.2f}")
    print(f"Numero de dias com faturamento superior a media mensal: {dias_acima_media}")

# Função para ler os dados do JSON
def ler_json(arquivo_json):
    with open(arquivo_json, 'r') as file:
        return json.load(file)

# Função para ler os dados do XML
def ler_xml(arquivo_xml):
    # Lê o conteúdo do arquivo XML
    with open(arquivo_xml, 'r') as file:
        xml_data = file.read()

    # Adiciona uma tag raiz temporária (como <dados>) para tornar o XML válido
    xml_data = f'<dados>{xml_data}</dados>'

    # Parseia o XML com a tag raiz temporária
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    faturamento_diario = []
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        faturamento_diario.append({'dia': dia, 'valor': valor})

    return faturamento_diario

# Caminhos para os arquivos JSON e XML
arquivo_json = "C:/Users/GianBueno/Downloads/dados.json"
arquivo_xml = "C:/Users/GianBueno/Downloads/dados (2).xml"

# Leitura dos dados JSON e XML
faturamento_diario_json = ler_json(arquivo_json)
faturamento_diario_xml = ler_xml(arquivo_xml)

# Chama a função para realizar a análise com dados JSON
print("Analise de Faturamento (JSON):")
analise_faturamento(faturamento_diario_json)

# Chama a função para realizar a análise com dados XML
print("\nAnalise de Faturamento (XML):")
analise_faturamento(faturamento_diario_xml)