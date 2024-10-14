import json


def calcular_faturamento():
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    faturamento_diario = dados['faturamento_diario']
    
    valores = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

    if not valores:  
        print("Não há dados de faturamento disponíveis.")
        return

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

calcular_faturamento()
