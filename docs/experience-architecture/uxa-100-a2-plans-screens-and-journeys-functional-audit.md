---
id: UXA-100-A2
title: Auditoria Funcional das Telas, Fluxos e Jornadas de Planos
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
depends_on:
  - UXA-100-A1
  - GEM-004-A1
  - GEM-004-A2
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-UPGRADE-DOWNGRADE-CANCELLATION-POLICY-001
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
normative: false
---

# Auditoria Funcional das Telas, Fluxos e Jornadas de Planos

## 1. Finalidade

A UXA-100-A2 registra a auditoria funcional dos **nove SVGs** da frente de Planos e a sincronização taxonômica posterior autorizada para Pessoa, Coletivo e Organização.

A atualização de 2026-08-08 não cria oferta, checkout, gateway, entitlement, superfície, transição, SVG ou promoção de jornada.

## 2. Autoridades examinadas

A auditoria usa GEM-004-A1/A2, políticas de paywall/ciclo de vida, matriz pagador–beneficiário, UXA-100/A1 e jornadas atuais.

A taxonomia vigente é:

- Pessoa: Free · Plus · Pro;
- Coletivo: Livre · Mobiliza · Impacta · Rede;
- Organização: Conecta · Eleva · Transforma.

Guivos Business Start/Growth/Scale/Enterprise permanece produto separado e não recebe materialização adicional.

## 3. Veredito preservado

> **9/9 SVGs funcionalmente aprovados no escopo da UXA-100; sincronização taxonômica não altera estados, decisões, IDs ou maturidade.**

Resultado preservado:

- 9 SVGs auditados;
- 6 haviam sido reformulados controladamente;
- 3 haviam sido aprovados sem reforma funcional;
- 0 removidos;
- 0 novos IDs;
- 0 novas transições;
- 0 jornadas promovidas.

A alteração atual substitui nomenclatura conflitante e explicita leitura conceitual. Não altera a lógica funcional anteriormente validada.

## 4. Equivalência de rastreabilidade

| Nomenclatura auditada anteriormente | Nomenclatura vigente | Efeito funcional |
|---|---|---|
| Coletivo Gestão | Coletivo Mobiliza | nenhum; capacidades/preço preservados |
| Coletivo Impacto | Coletivo Impacta | nenhum; capacidades/preço preservados |
| Coletivo Enterprise | Coletivo Rede | nenhum; capacidade contratada preservada |
| Business Start na tela Organização | Organização Conecta | nenhum; baseline organizacional preservada |
| Business Growth na tela Organização | Organização Eleva | nenhum; baseline organizacional preservada |
| Business Scale na tela Organização | Organização Transforma | nenhum; baseline organizacional preservada |

Essa equivalência não autoriza correspondência entre planos da Organização e Guivos Business.

## 5. Pessoa

A validação permanece: Free preserva catálogo público; Plus usa formulação sem cota semanal fixa sujeita a uso justo; Pro amplia análise/integrações. Revisão de contratação explicita preço, periodicidade, recorrência, início, pagador/beneficiário, consentimento e separação transacional.

## 6. Coletivo

Os mesmos estados e limites permanecem válidos sob `Livre → Mobiliza → Impacta → Rede`.

- Livre preserva utilidade gratuita;
- Mobiliza preserva capacidades antes atribuídas a Gestão;
- Impacta preserva capacidades antes atribuídas a Impacto;
- Rede preserva capacidade dimensionada antes atribuída a Enterprise.

A leitura conceitual impede interpretar maior plano como maior legitimidade ou impacto. Downgrade continua exigindo tratamento de publicações, administradores, núcleos/unidades, compromissos e exportação.

## 7. Organização

Os mesmos estados e limites permanecem válidos sob `Conecta → Eleva → Transforma`.

- Conecta preserva a baseline antes exibida como Start;
- Eleva preserva a baseline antes exibida como Growth;
- Transforma preserva a baseline antes exibida como Scale.

A Organização continua selecionando unidades, administradores, publicações, Coletivos relacionados, integrações e dados no downgrade. `Transforma` não garante impacto e não é `Guivos Business Enterprise`.

## 8. BND-002

O antigo texto “Enterprise/Scale” é substituído pela função genérica **contratação/dimensionamento assistido**. A mudança corrige semântica sem promover maturidade.

`TRN-416` e `TRN-426` permanecem parciais porque o processo posterior à fronteira continua não materializado como conjunto.

## 9. Critérios preservados

A auditoria continua confirmando, no escopo dos nove SVGs:

1. alternativa gratuita/operacional permanece visível;
2. oportunidade pública não é ocultada;
3. plano atual, limite e consumo são compreensíveis;
4. entrada voluntária e contextual permanecem legítimas;
5. matriz, comparação incremental e delta direto são coerentes;
6. nenhuma opção paga é pré-selecionada;
7. preço/periodicidade/recorrência/início são exigidos quando aplicáveis;
8. pagador e beneficiário são distintos;
9. falha preserva estado anterior/direitos;
10. downgrade/cancelamento explicitam consequências;
11. contratação assistida não simula checkout autônomo;
12. pagamento não promete relevância, confiança, impacto ou evolução;
13. repetição da mesma intenção não duplica cobrança/ativação;
14. jornada documentada não equivale a implementação.

## 10. Estado após sincronização

- 9 SVGs preservados;
- 9/9 com validação funcional vigente no mesmo escopo;
- 0 novos IDs;
- 0 novas transições;
- contagens canônicas permanecem as promovidas pela UXA-100-A3;
- Pessoa, Coletivo e Organização continuam `draft`;
- Guivos Business não é incorporado como quarta jornada;
- Engenharia de Produto continua pausada antes de W0-01.
