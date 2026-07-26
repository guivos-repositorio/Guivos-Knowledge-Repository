---
id: UXA-008
title: Wireframe de Baixa Fidelidade do Cadastro de Oportunidade pela Organização
status: draft
version: 0.1.0
owner: Guivos Experience Architecture
last_updated: 2026-07-26
parent: UXA-005
related:
  - UXA-004
  - UXA-007
  - GPA-004
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
normative: false
---

# UXA-008 — Wireframe de Baixa Fidelidade do Cadastro de Oportunidade pela Organização

## 1. Pergunta da superfície

> **Como uma Organização informa uma oportunidade de forma completa, transparente e corrigível, sem transformar o envio em ativação automática?**

O wireframe representa o fluxo web da Organização e detalha a etapa `Preço e condições`, preservando a visão das onze etapas do cadastro.

## 2. Wireframe

![Wireframe desktop do cadastro de oportunidade](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg)

[Visualizar o SVG isoladamente](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg)

## 3. Estrutura global

A tela possui:

- navegação institucional lateral;
- cabeçalho da oportunidade;
- estado de salvamento;
- pré-visualização;
- indicador das onze etapas;
- formulário principal;
- painel de consistência e transparência;
- ações persistentes de voltar, salvar e continuar.

A Organização deverá visualizar claramente em nome de qual entidade e unidade está realizando o cadastro.

## 4. Etapas do fluxo

| Nº | Etapa | Resultado esperado |
|---:|---|---|
| 1 | Tipo | natureza funcional da oportunidade |
| 2 | Finalidade | valor, público e relação com necessidades ou movimentos |
| 3 | Responsável | Organização, unidade, autoridade e suporte |
| 4 | Disponibilidade | vagas, estoque, janelas, recorrência e validade |
| 5 | Local | modalidade, endereço, cobertura e acessibilidade |
| 6 | Preço | custo, condições, inclusão, cancelamento e validade |
| 7 | Elegibilidade | requisitos necessários e decisor final |
| 8 | Proteção | riscos, sensibilidade, acessibilidade e políticas |
| 9 | Comercial | comissão, patrocínio, exclusividade e relações financeiras |
| 10 | Prévia | apresentação em cartão, detalhe, busca, mapa e modo acessível |
| 11 | Enviar | declaração, revisão e submissão para avaliação |

A navegação entre etapas deverá preservar rascunho e sinalizar campos que afetam outras etapas.

## 5. Etapa representada: preço e condições

### 5.1 Modelo de acesso

Opções iniciais:

- paga;
- gratuita;
- subsidiada;
- benefício.

A seleção altera campos posteriores, mas não deverá apagar informações já fornecidas sem confirmação.

### 5.2 Preço principal e cobrança

Campos:

- moeda;
- preço principal;
- cobrança única ou recorrente;
- número de parcelas ou ciclos;
- periodicidade;
- custo total conhecido ou estimado;
- possibilidade de reajuste.

No locale pt-BR, valores ilustrativos utilizam `R$` e formatação brasileira, como `R$ 79,90`.

### 5.3 Taxas e custos externos

A Organização deverá declarar:

- matrícula;
- material obrigatório;
- emissão de certificado;
- transporte;
- hospedagem;
- equipamentos;
- impostos ou taxas;
- outros custos necessários.

A ausência de taxa deverá ser confirmada, não apenas presumida pelo campo vazio.

### 5.4 Incluído e não incluído

A separação deverá impedir que uma descrição positiva oculte custos ou responsabilidades externas.

Exemplos:

- incluído: aulas, material digital e avaliação;
- não incluído: certificação externa, equipamento e conectividade.

### 5.5 Cancelamento, reembolso e validade

A etapa deverá solicitar:

- forma de cancelamento;
- multa ou ausência de multa;
- prazo de arrependimento;
- regras de reembolso;
- validade do preço;
- política de reajuste;
- efeitos de alteração após inscrição.

## 6. Painel de consistência

O painel lateral deverá:

- indicar campos atendidos;
- apontar omissões materiais;
- explicar por que determinada informação é necessária;
- apresentar como o preço será exibido ao participante;
- detectar contradições, como `gratuito` com taxa obrigatória não declarada;
- permitir abrir pré-visualização completa.

O painel não substitui avaliação humana ou institucional posterior.

## 7. Salvamento e continuidade

O fluxo deverá suportar:

- salvamento automático;
- salvamento manual;
- retorno posterior;
- histórico de alterações;
- autoria por campo material;
- colaboração por papéis;
- bloqueio de envio quando houver informação crítica ausente;
- aviso antes de sair com alterações não sincronizadas.

## 8. Pré-visualização

A Organização deverá visualizar a oportunidade como aparecerá:

- no cartão;
- no detalhe;
- na busca;
- no mapa;
- em comparação;
- na tela `Hoje`;
- em intervenção contextual;
- em modo acessível;
- em modo discreto, quando aplicável.

A prévia deverá distinguir dado fornecido pela Organização de avaliação produzida posteriormente pela Guivos.

## 9. Envio e avaliação

Fluxo esperado:

```text
Rascunho
→ Enviada
→ Em avaliação
→ Ajustes solicitados
→ Aprovada para ativação
→ Ativa
```

Também serão possíveis:

- rejeitada antes da ativação;
- pausada;
- indisponível;
- expirada;
- contestada;
- corrigida;
- encerrada;
- cancelada.

O envio não poderá ser apresentado como publicação imediata.

## 10. Estados alternativos que ainda exigem wireframe

- oportunidade gratuita;
- oportunidade subsidiada por patrocinador;
- benefício corporativo;
- preço sob consulta;
- custo variável por localização;
- múltiplas moedas;
- taxa obrigatória divergente;
- Organização com informação institucional pendente;
- ajustes solicitados pela Guivos;
- cadastro colaborativo por várias pessoas;
- oportunidade recorrente;
- oportunidade com crianças ou adolescentes;
- atividade de Coletivo vinculada a Organização.

## 11. Perguntas para validação humana

1. As onze etapas são compreensíveis ou excessivas?
2. A etapa atual está suficientemente destacada?
3. O painel lateral ajuda ou aumenta a carga cognitiva?
4. O cálculo de custo total deve ser automático e editável?
5. `Incluído` e `não incluído` precisam ser campos estruturados ou texto livre?
6. A pré-visualização deve estar sempre disponível?
7. Quais campos devem bloquear o envio?
8. A Organização compreende que envio, aprovação, ativação e apresentação são estados diferentes?
9. Quais papéis institucionais podem cadastrar, revisar e enviar?

## 12. Critérios de aceite do wireframe

O wireframe poderá avançar quando:

- a Organização compreender a sequência e o estado atual;
- preço e custo total não puderem ser ocultados involuntariamente;
- taxas e condições forem explicitadas;
- rascunho e retorno posterior forem confiáveis;
- pré-visualização mostrar o efeito dos dados fornecidos;
- envio não for confundido com ativação;
- ajustes e recurso forem previstos;
- autoria e responsabilidade institucional permanecerem rastreáveis.
