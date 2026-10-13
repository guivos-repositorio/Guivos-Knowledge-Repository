---
id: GEM-OPPORTUNITIES-POINTS-STATUS-001
title: Oportunidades — Pontos e Incentivos — Decisões e Pendências Econômicas
status: proposed
version: 0.1.1
owner: Guivos
last_updated: 2026-10-13
normative: false
---

# Pontos e incentivos — decisões de produto e pendências econômicas

> **Documento compacto candidato, sem eficácia econômica ou autorização de operação.** Registra decisões de direção de produto e separa parâmetros financeiros, contratos, segurança e homologação ainda não aprovados. Não institui preço oficial, paridade, moeda de pagamento, emissão real, resgate ou integração entre produtos.

## 1. Modelo de produto estabelecido

- **Opcionalidade:** Organizações e Coletivos podem oferecer oportunidades pagas ou gratuitas sem obrigação de conceder pontos. Os pontos são incentivo secundário, não promessa de evolução pessoal.
- **FIN-COMPRA:** em oportunidade paga elegível, o ofertante escolhe percentual entre opções que a Guivos venha a aprovar; o custo dos pontos é deduzido de seu repasse, separadamente de taxa própria da Guivos. O exemplo R$ 200 × 1% = 2 pontos e retenção ilustrativa de R$ 2 **não aprova tabela ou paridade de resgate**.
- **FIN-EVENTO:** participação, classificação e outras premiações elegíveis são suportadas por **orçamento de pontos pré-pago pelo organizador**. Reserva, promessa, crédito disponível e liquidação são estágios distintos.
- **Uma unidade:** pontos de origens distintas devem convergir à mesma unidade de valor da Pessoa; origem de financiamento não cria moedas paralelas.
- **Limites independentes:** limite de pessoas beneficiadas por bônus não limita inscrições gerais no evento.
- **Mall e Travel:** possíveis superfícies de utilização futura, sem aceitação ou liquidação automaticamente habilitadas.

O custo de incentivos é atribuído ao **ofertante de origem**, não a cofinanciamento implícito da Guivos; regras finais de perdas, estornos e cobranças continuam pendentes.

## 2. Matriz econômica P1–P9

| ID | Objeto | Situação correta |
|---|---|---|
| P1 / ROUND | Precisão e arredondamento | **Direção de política aprovada:** HALF_EVEN, precisão 0,01 ponto por fato gerador elegível/ofertante, estorno proporcional acumulado e reversão integral exata; implementação e testes não autorizados |
| P2 / PAR-02 | Valor de utilização do ponto | Paridade dependente de lastro e liquidação; EQ-1 (1 ponto = R$ 1) **somente cenário ilustrativo** |
| P3 / FUND-01 | Preço de aquisição de saldo para eventos | Separar cobertura de eventual tarifa; preço, tributação e devolução em aberto |
| P4 | Percentuais optativos e base elegível | Tabela oficial, descontos, exclusões e vigência não definidos |
| P5 | Taxas e repasse | Rubricas de custo dos pontos, remuneração Guivos, pagamentos e tributos separadas; valores e ordem final pendentes |
| P6 / COVER | Estornos e chargeback | Responsabilidades, recuperação após resgate, disputa e proteção da Pessoa pendentes |
| P7 / LIQ-01 | Mall | Contratos com vendedores, split, cancelamento e conciliação ainda não aprovados |
| P8 / LIQ-02 | Travel | Fornecedores, cotação, reservas, alterações, multas e liquidação ainda não aprovados |
| P9 / LEG-FIN-COVER | Natureza jurídica, contábil e tributária | Enquadramento, cobertura, retenção, saldos não utilizados e direitos pendentes de avaliação especializada |

A tabela registra o **parâmetro ROUND/P1 aprovado por deliberação expressa** e os demais gates ainda pendentes. A decisão específica de P1 não torna a operação de pontos autorizada.

## 3. Critérios de integridade

1. Nenhum crédito sem gatilho elegível e cobertura financeiramente verificável; nenhuma promessa de bônus acima de orçamento reservado.
2. Manter registro individualizado por origem financiadora, evento, transação e contraparte, com reversões idempotentes e conciliação.
3. Não presumir saldo negativo automático, confisco ou cobrança à Pessoa em chargebacks sem fundamento normativo, contratual e proteção adequada.
4. Separar crédito de ponto, preço de aquisição, valor de uso e liquidação de parceiros; não assumir equivalência entre rubricas.
5. A disponibilização em Mall ou Travel exige contratos específicos, paridade ratificada, cobertura, governança, conformidade e testes próprios.

## 4. Fronteiras de maturidade e navegação

**PR #655:** dossiê original candidato, com decisões, análises P1–P9 e 16 casos E2E definidos; **0/16 casos executados** conforme registros disponíveis. Não tratar sucesso de CI como homologação, implementação ou autorização de produto.

Este documento permanece `status: proposed`, `normative: false` e **não integra o MENU como autoridade vigente** por mero merge. Não modifica Home, Masters, registries, contratos ou ambiente Replit. A inclusão editorial e a publicação de política econômica vigente requerem decisão própria.

## 5. Próxima decisão verificável

Consolidar testes e especificação da decisão ROUND/P1, comprovação de lastro, proposta parametrizada PAR/FUND e revisão jurídico-contábil antes de ratificar P2–P3; seguir a P4–P6 (contratos de ofertantes), P7–P8 (parceiros) e P9 (transversal). Registrar autoridade, data, objeto, condições e evidências de cada decisão. A implantação demanda conclusão dos gates técnicos e humanos separados.

**Evidência específica de ROUND/P1:** [deliberação na Issue #661](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/issues/661#issuecomment-6157719752). A atualização do dossiê está na PR #655, v2.8.1 candidata, ainda em DRAFT.

**Fonte histórica:** [PR #655 — Pontos e Incentivos](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/655), documento `docs/economic-model/opportunities-points-and-event-rewards-candidate.md`, v2.8.0 candidata.
