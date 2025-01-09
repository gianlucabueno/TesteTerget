faturamento_estados = [
    {"estado": "SP", "faturamento": 67836.43},
    {"estado": "RJ", "faturamento": 36678.66},
    {"estado": "MG", "faturamento": 29229.88},
    {"estado": "ES", "faturamento": 27165.48},
    {"estado": "Outros", "faturamento": 19849.53}
]



faturamento_total  = 0
percentual = 0 

for item in faturamento_estados:
    print(f"Estado: {item['estado']}, Faturamento: R${item['faturamento']:.2f}")
    faturamento_total  = faturamento_total  + item['faturamento']
print(f"faturamento eh igual a : {faturamento_total}")
for item in faturamento_estados:
    percentual = (item['faturamento'] / faturamento_total ) * 100
    print(f"percentual do estado {item['estado']} eh igual a: {percentual:.2f} ")