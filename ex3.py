def analise_faturamento(faturamento_diario):
    menor_faturamento = 0 # Começando com infinito para garantir que qualquer valor será menor
    maior_faturamento = 0  # Começando com -infinito para garantir que qualquer valor será maior
    soma_faturamento = 0
    dias_validos = 0   
    # Laço para percorrer todos os dias e calcular os valores
    for faturamento in faturamento_diario:
        if faturamento > 0:  # Ignorando dias sem faturamento
            # Atualizando menor e maior faturamento
            if menor_faturamento == 0:
                menor_faturamento = faturamento
            elif faturamento < menor_faturamento:
                menor_faturamento = faturamento
            elif faturamento > maior_faturamento:
                maior_faturamento = faturamento
            
            # Somando os faturamentos válidos
            soma_faturamento += faturamento
            dias_validos += 1

    # Calculando a média de faturamento
    if dias_validos > 0:
        media_faturamento = soma_faturamento / dias_validos
    else:
        media_faturamento = 0

    # Contando o número de dias com faturamento superior à média
    dias_acima_media = 0
    for faturamento in faturamento_diario:
        if faturamento > 0 and faturamento > media_faturamento:
            dias_acima_media += 1
        
        # Exibindo os resultados
    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Numero de dias com faturamento superior a media mensal: {dias_acima_media}")

#Numeros criados devido não ter o json ou xml disponível 
faturamento_diario = [250, 300, 150, 400, 350, 500, 450, 200, 300, 420, 600, 650]

# Chama a função para realizar a análise
analise_faturamento(faturamento_diario)