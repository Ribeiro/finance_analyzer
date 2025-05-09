from models import Financials
from analyzer import calcular_indicadores
from recommendations import gerar_recomendacoes

def obter_float_input(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def exibir_menu():
    print("\n=== Analisador Financeiro ===")
    print("1. Inserir taxa Selic")
    print("2. Inserir dados da empresa e analisar")
    print("3. Sair")

def coletar_dados_financeiros():
    print("\nInforme os dados financeiros da empresa:")
    ativo_total = obter_float_input("Ativo Total (R$): ")
    passivo_circulante = obter_float_input("Passivo Circulante (R$): ")
    passivo_nao_circulante = obter_float_input("Passivo Não Circulante (R$): ")
    patrimonio_liquido = obter_float_input("Patrimônio Líquido (R$): ")
    receita_liquida = obter_float_input("Receita Líquida (R$): ")
    ebit = obter_float_input("EBIT (Lucro antes de juros e impostos) (R$): ")
    despesas_financeiras = obter_float_input("Despesas Financeiras (R$): ")

    return Financials(
        ativo_total=ativo_total,
        passivo_circulante=passivo_circulante,
        passivo_nao_circulante=passivo_nao_circulante,
        patrimonio_liquido=patrimonio_liquido,
        receita_liquida=receita_liquida,
        ebit=ebit,
        despesas_financeiras=despesas_financeiras
    )

def main():
    selic = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            selic = obter_float_input("Informe a taxa Selic atual (%): ")
            print(f"✅ Taxa Selic configurada: {selic:.2f}%")

        elif opcao == "2":
            if selic is None:
                print("⚠️ Por favor, configure a taxa Selic antes de continuar.")
                continue

            empresa = coletar_dados_financeiros()
            indicadores = calcular_indicadores(empresa)
            recomendacoes = gerar_recomendacoes(indicadores, selic)

            print("\n📊 Indicadores Financeiros:")
            for k, v in indicadores.items():
                print(f"{k.replace('_', ' ').title()}: {v:.2f}")

            print("\n🧾 Recomendações:")
            for rec in recomendacoes:
                print("-", rec)

        elif opcao == "3":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
