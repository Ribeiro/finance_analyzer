from dataclasses import dataclass

@dataclass
class Financials:
    ativo_total: float
    passivo_circulante: float
    passivo_nao_circulante: float
    patrimonio_liquido: float
    receita_liquida: float
    ebit: float
    despesas_financeiras: float
