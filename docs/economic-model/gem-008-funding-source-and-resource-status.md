---
id: GEM-008-FUNDING-SOURCE-AND-RESOURCE-STATUS-001
title: Fontes Econômicas e Estados de Recursos
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Fontes Econômicas e Estados de Recursos

## 1. Objetivo

Classificar fontes econômicas e estados de recursos para impedir que expectativa, compromisso, caixa recebido ou recurso vinculado sejam tratados como disponibilidade irrestrita.

## 2. Fontes candidatas

| Código | Fonte | Natureza conceitual |
|---|---|---|
| FS-01 | receita operacional futura | retorno por valor entregue |
| FS-02 | receita vinculada | limitada a finalidade ou obrigação |
| FS-03 | organização financiadora | financia acesso, programa ou benefício |
| FS-04 | patrocínio | recurso vinculado a campanha, conteúdo ou causa |
| FS-05 | contribuição de parceiro | produto, serviço, desconto, capacidade ou infraestrutura |
| FS-06 | fundo social | recurso de finalidade social específica |
| FS-07 | capital | aporte de fundador ou investidor; não é receita |
| FS-08 | dívida ou financiamento | recurso com obrigação de pagamento |
| FS-09 | grant, doação ou subvenção | recurso sujeito a condições e prestação de contas |
| FS-10 | eficiência compartilhada | redução legítima de custo; não é caixa automaticamente realizado |

## 3. Estados

```yaml
resource_status:
  proposed |
  expected |
  committed |
  available |
  restricted |
  reserved |
  allocated |
  consumed |
  exhausted |
  suspended |
  terminated
```

## 4. Regras

- `expected` não sustenta obrigação;
- `committed` não significa disponibilidade imediata;
- `available` não significa irrestrito;
- `restricted` não poderá financiar finalidade incompatível;
- `reserved` não poderá ser tratado como caixa livre;
- `allocated` não significa execução concluída;
- `consumed` deverá possuir finalidade e evidência;
- capital, dívida e aporte não serão registrados como receita operacional;
- economia estimada não será tratada como caixa realizado;
- encerramento da fonte deverá tratar obrigações remanescentes.

## 5. Registro conceitual

```yaml
funding_source_id: string
source_type: string
provider: string | null
purpose: string
status: proposed
restricted: boolean
beneficiaries:
  - string
obligations:
  - string
recurring_validated: false
amount_defined: false
start_condition: string
end_condition: string
termination_treatment: string
```

## 6. Fora do escopo

- valores;
- contratos;
- instrumentos financeiros;
- contas bancárias;
- tributação;
- contabilização;
- captação;
- operação.