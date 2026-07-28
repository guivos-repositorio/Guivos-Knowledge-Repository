---
id: GKR-KNOWLEDGE-BOARD-001
title: Painel de Conhecimento
status: active
version: 12.13.0
owner: Guivos
last_updated: 2026-07-28
depends_on:
  - GKR-STATE-001
related:
  - ROADMAP-12.13.0
  - GEM-004
  - GEM-004-A1
  - GEM-004-A2
  - GEM-010
  - GEM-010-A1
  - GEM-COMMERCIAL-BASELINE-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - UXA-000
  - UXA-011-A1
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - M7.39
normative: false
---

# Painel de Conhecimento

## 1. Autoridade

Este painel resume o portfólio arquitetural vigente. O estado oficial é declarado pelo Registro do Estado Atual.

## 2. Estado institucional vigente

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | baseline comercial de planos, benefícios e preços definida | M7.39; GEM-004-A1; GEM-004-A2; GEM-010-A1 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Modelo Econômico | baseline comercial candidata definida; validação pendente | GEM-004 0.2.0; GEM-010 0.2.0 |
| Pessoas | Free, Plus e Pro definidos | GEM-004-A1 |
| Coletivos | Livre, Gestão, Impacto e Enterprise definidos | GEM-004-A1 |
| Organizações | Business Start, Growth e Scale definidos | GEM-004-A1 |
| Oferta e ciclo comercial | documentados; não implementados | GEM-004-A2 |
| Preços | candidatos; sem autorização de cobrança | GEM-010-A1 |
| Home pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Início protegido móvel | funcionalmente validado e reformulado | UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | funcionalmente validada e reformulada em cinco estados | UXA-011-A1; UXA-036; UXA-037 |
| Referência móvel da Home | não iniciada | — |
| Referência desktop do início protegido e compreensão | não iniciada | — |
| Tela Hoje | entrada recorrente após condição explicitamente escolhida | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | estados móveis e referência desktop validados | UXA-024 a UXA-033 |
| Persistência e personalização | governadas; implementação não iniciada | UXA-011-A1; UXA-036; UXA-037 |
| Protótipo, design e testes | não iniciados | — |
| Capacidades Empresariais | não iniciadas | — |
| Engenharia de Produto | pausada | W0-01 |

## 3. Portfólio por situação

### Concluído ou consolidado

- Arquitetura de Fundação congelada;
- Guivos Journey funcionalmente concluído;
- Modelo Econômico documentado inicialmente;
- baseline comercial candidata de planos definida;
- planos e preços para Pessoas, Coletivos e Organizações consolidados;
- regras de oferta, upgrade, downgrade e cancelamento documentadas;
- remediação e validação mecânica concluídas;
- validação externa e 18 decisões humanas concluídas;
- Tela Hoje, Detalhe e Cadastro validados;
- experiências de Organizações e Coletivos estabelecidas;
- Home pública validada e materializada;
- início protegido móvel criado, validado e reformulado;
- compreensão inicial móvel criada, validada e reformulada;
- Mapa principal, estados móveis e referência desktop validados e reformulados.

### Em validação ou calibração pendente

- nove formulações candidatas de Resultados Empresariais;
- utilidade dos limites do Guivos Free;
- disposição a pagar por Plus e Pro;
- cotas e preços de Coletivos;
- bases de cobrança e preços de Organizações;
- custos de servir e margens;
- comissão e política transacional;
- parâmetros de Enterprise e Scale.

### Aguardando autorização

#### Modelo Econômico e Mercado

- pesquisa de utilidade e disposição a pagar;
- validação de planos com Coletivos;
- validação de planos com Organizações;
- unit economics e cenários;
- comissão e política transacional;
- revisões especializadas;
- teste controlado.

#### Arquitetura da Experiência

- página de Planos e Preços;
- estados de limite, comparação, contratação e cancelamento;
- referência móvel da Home;
- validação da transição para a primeira Tela Hoje;
- estados de processamento, pausa, falha e retomada;
- referência do início protegido e da compreensão para computador;
- estados especializados de texto, voz e arquivos;
- referência para tablet.

#### Arquitetura de Negócios

- reaplicação dos quatro testes;
- ajuste do AQS-O01;
- consolidação dos catálogos canônicos;
- matriz de sustentação entre Resultados;
- preparação das Capacidades Empresariais.

### Pausado ou não iniciado

- Engenharia de Produto;
- checkout, gateway e cobrança;
- oferta pública;
- protótipo navegável e design visual;
- testes de usabilidade;
- autenticação, armazenamento, gravação, transcrição, upload e processamento real;
- persistência e personalização implementadas;
- integrações e produção.

## 4. Baseline de planos

### Pessoas

| Plano | Preço candidato | Valor principal |
|---|---:|---|
| Guivos Free | R$ 0,00 | catálogo público e 2 correspondências personalizadas por semana |
| Guivos Plus | R$ 24,90/mês | correspondências, filtros, alertas e histórico ampliados |
| Guivos Pro | R$ 49,90/mês | análises, integrações e relatórios avançados |

### Coletivos

| Plano | Preço candidato | Limite principal |
|---|---:|---|
| Coletivo Livre | R$ 0,00 | 1 atividade e 1 oportunidade gratuitas/mês; 2 ativas |
| Coletivo Gestão | R$ 89,90/mês | 4 atividades, 4 oportunidades e 6 ativas |
| Coletivo Impacto | R$ 249,90/mês | 15 atividades, 15 oportunidades e 20 ativas |
| Coletivo Enterprise | sob consulta | capacidade contratada; categorias personalizáveis |

### Organizações

| Plano | Preço candidato | Limite principal |
|---|---:|---|
| Business Start | R$ 299,00/mês | 10 novos programas ou oportunidades/mês; 15 ativos |
| Business Growth | R$ 799,00/mês | 50 novos/mês; 75 ativos; até 5 unidades |
| Business Scale | a partir de R$ 1.990,00/mês | capacidade e integrações contratadas |

## 5. Sequência pessoal vigente

```text
Página Inicial pública
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ processamento temporário visível e interrompível
→ hipótese inicial
→ revisão por afirmação
→ decisões independentes sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

Oferta de plano não interrompe essa sequência protegida.

## 6. Regras comerciais preservadas

- catálogo público permanece acessível no Guivos Free;
- limite recai sobre correspondências personalizadas;
- alternativa gratuita permanece visível;
- Coletivo Livre publica somente ofertas gratuitas;
- publicação paga exige Gestão ou superior;
- pessoa gratuita pode comprar atividade paga;
- assinatura e transação são objetos distintos;
- cota não reduz visibilidade de publicação existente;
- Enterprise e Scale utilizam capacidade contratada e uso justo;
- plano pago não altera ranking, relevância, impacto ou evidência;
- preços são candidatos para validação;
- nenhuma cobrança foi autorizada.

## 7. Proteções da experiência preservadas

- a Home não coleta relato pessoal;
- iniciar a jornada é voluntário;
- nenhum relato antecede a explicação;
- dados de acesso são tratados separadamente;
- autenticação não autoriza processamento;
- interromper não mantém tarefa oculta;
- compreensão é hipótese corrigível;
- afirmação aberta não equivale a fato;
- relato e interpretação permanecem separados;
- persistência e personalização exigem decisões próprias;
- exploração sem personalização permanece disponível;
- localização é opcional;
- publicidade e pagamento não aumentam relevância;
- wireframes e validações não equivalem a design ou implementação.

## 8. Distribuição dos candidatos de Resultados

| Estado | Quantidade | Interpretação |
|---|---:|---|
| Em validação | 9 | formulações revisadas aguardando avaliação |
| Fundidos | 3 | conteúdos incorporados com rastreabilidade |
| Rejeitados | 6 | retirados do catálogo futuro |
| Aprovados | 0 | nenhuma aprovação ocorreu |

## 9. Próximo movimento

Após integração, nenhum movimento é automático. A próxima ação poderá ser escolhida entre validação dos planos e preços, modelagem de unit economics, política transacional, página de Planos e Preços, referência móvel da Home, transição para a primeira Tela Hoje ou retomada independente dos testes dos Resultados Empresariais.
