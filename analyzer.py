from models import Financials

def calcular_indicadores(financials: 'Financials'):
    divida_total = financials.passivo_circulante + financials.passivo_nao_circulante

    return {
        "endividamento_geral": divida_total / financials.ativo_total,
        "alavancagem": divida_total / financials.patrimonio_liquido,
        "cobertura_juros": financials.ebit / financials.despesas_financeiras if financials.despesas_financeiras else float('inf')
    }
