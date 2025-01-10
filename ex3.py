import json
import xml.etree.ElementTree as ET


def analise_faturamento(faturamento_diario):
    menor_faturamento = 0 
    maior_faturamento = 0 
    soma_faturamento = 0
    dias_validos = 0
   
    
    for faturamento in faturamento_diario:
        if faturamento['valor'] > 0:  
            
            if menor_faturamento == 0 and maior_faturamento == 0:
                menor_faturamento = faturamento['valor']
                maior_faturamento = faturamento['valor']
            elif faturamento['valor'] < menor_faturamento:
                menor_faturamento = faturamento['valor']
            elif faturamento['valor'] > maior_faturamento:
                maior_faturamento = faturamento['valor']
            
          
            soma_faturamento += faturamento['valor']
            dias_validos += 1

   
    if dias_validos > 0:
        media_faturamento = soma_faturamento / dias_validos
    else:
        media_faturamento = 0

    
    dias_acima_media = 0
    for faturamento in faturamento_diario:
        if faturamento['valor'] > media_faturamento:
            dias_acima_media += 1
        
    
    print(f"Menor faturamento: {menor_faturamento:.2f}")
    print(f"Maior faturamento: {maior_faturamento:.2f}")
    print(f"Numero de dias com faturamento superior a media mensal: {dias_acima_media}")


def ler_json(arquivo_json):
    with open(arquivo_json, 'r') as file:
        return json.load(file)


def ler_xml(arquivo_xml):
 
    with open(arquivo_xml, 'r') as file:
        xml_data = file.read()


    xml_data = f'<dados>{xml_data}</dados>'

   
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    faturamento_diario = []
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        faturamento_diario.append({'dia': dia, 'valor': valor})

    return faturamento_diario


arquivo_json = "C:/Users/GianBueno/Downloads/dados.json"
arquivo_xml = "C:/Users/GianBueno/Downloads/dados (2).xml"


faturamento_diario_json = ler_json(arquivo_json)
faturamento_diario_xml = ler_xml(arquivo_xml)


print("Analise de Faturamento (JSON):")
analise_faturamento(faturamento_diario_json)


print("\nAnalise de Faturamento (XML):")
analise_faturamento(faturamento_diario_xml)