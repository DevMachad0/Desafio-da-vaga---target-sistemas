# Lê um arquivo JSON contendo o faturamento diário e realiza cálculos para encontrar:
# - Menor e maior valor de faturamento
# - Dias com faturamento acima da média mensal
import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)


valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(valores)  
maior_valor = max(valores)  
media_mensal = sum(valores) / len(valores)  
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")