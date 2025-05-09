# 📊 Analisador Financeiro com Recomendação baseada na Taxa Selic

Este projeto em Python realiza **análises financeiras interativas** de uma empresa com base em dados contábeis e na taxa Selic atual, gerando **recomendações estratégicas** conforme a saúde financeira da organização.

---

## 🚀 Funcionalidades

- Entrada interativa de dados financeiros
- Configuração manual da Taxa Selic
- Cálculo de indicadores:
  - Nível de endividamento
  - Grau de alavancagem financeira
  - Custo da dívida
  - Retorno sobre o ativo (ROA)
- Geração de recomendações estratégicas
- Interface por terminal com menu

---

## 🛠️ Estrutura do Projeto

```

finance-analyzer/
├── analyzer.py          # Cálculo dos indicadores financeiros
├── recommendations.py   # Lógica para recomendações baseadas nos indicadores e Selic
├── models.py            # Estrutura de dados da empresa (Financials)
├── main.py              # Interface interativa com o usuário
├── .gitignore
└── README.md

````

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/finance-analyzer.git
cd finance-analyzer
````

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Execute o programa

```bash
python main.py
```

---

## 💡 Exemplo de uso

```
=== Analisador Financeiro ===
1. Inserir taxa Selic
2. Inserir dados da empresa e analisar
3. Sair
Escolha uma opção: 1
Informe a taxa Selic atual (%): 14.75
✅ Taxa Selic configurada: 14.75%

...

📊 Indicadores Financeiros:
Nível De Endividamento: 0.68
Custo Da Dívida (%): 11.00
...

🧾 Recomendações:
- A empresa possui um nível saudável de endividamento.
- O custo da dívida está abaixo da Selic, indicando uso eficiente de capital de terceiros.
```

---

## 📋 Requisitos

* Python 3.8 ou superior

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 🙋‍♂️ Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou enviar PRs.