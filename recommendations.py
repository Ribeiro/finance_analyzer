def gerar_recomendacoes(indicadores: dict, selic: float):
    rec = []

    # Endividamento
    eg = indicadores["endividamento_geral"]
    if eg <= 0.6:
        rec.append(f"✅ Endividamento Geral de {eg:.2%} está saudável.")
    else:
        rec.append(f"🔺 Endividamento Geral de {eg:.2%} é alto. Reduza a dependência de dívidas.")

    # Alavancagem
    alav = indicadores["alavancagem"]
    if alav <= 2:
        rec.append(f"✅ Alavancagem de {alav:.2f} indica equilíbrio entre capital próprio e de terceiros.")
    else:
        rec.append(f"❌ Alavancagem de {alav:.2f} é crítica. Avalie aporte de capital próprio.")

    # Cobertura de Juros
    cj = indicadores["cobertura_juros"]
    if cj >= 2:
        rec.append(f"✅ Cobertura de Juros de {cj:.2f} é suficiente.")
    elif 1 <= cj < 2:
        rec.append(f"⚠️ Cobertura de Juros de {cj:.2f} está apertada. Atenção a novos financiamentos.")
    else:
        rec.append(f"❌ Cobertura de Juros de {cj:.2f} indica risco de inadimplência com Selic a {selic:.2f}%.")

    return rec
