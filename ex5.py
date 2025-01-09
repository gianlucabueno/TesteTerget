def inverter_string(texto):

    palavra = list(texto)  
    inicio = 0
    fim = len(palavra) - 1
    
    while inicio < fim:  
        temp = palavra[inicio]
        palavra[inicio] = palavra[fim]
        palavra[fim] = temp
        
        inicio += 1
        fim -= 1
        

    return ''.join(palavra) 



texto = input("Digite uma string para inverter: ")


print(f"String invertida: {inverter_string(texto)}")
