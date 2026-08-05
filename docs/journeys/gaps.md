---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.5.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-059
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é **observacional e não promocional**. Ele permanece `active` para registrar ausências verificadas, mas não declara que mapas, transições ou jornadas estejam funcionalmente validados como completos.

Uma lacuna somente muda de estado por pacote governado com autoridade, materialização e validação correspondentes.

## 2. Fila priorizada com rastreabilidade granular

| Prioridade | Lacuna | Participante afetado | IDs relacionados | Maturidade primária | Autoridade existente | Evidência ausente | Gate de fechamento |
|---:|---|---|---|---|---|---|---|
| 1 | Meus Coletivos | Pessoa | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | não iniciado | UXA-059 | superfície, entrada e saída | materialização e validação funcional |
| 2 | Central de Atualizações | Pessoa | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | não iniciado | UXA-059 | superfície e transições | materialização e validação funcional |
| 3 | Início do Participante reformulado | Pessoa em Coletivo | GKR-SURF-PER-108; GKR-TRN-111 | reformulação pendente | UXA-059 | referência reformulada e continuidade | reformulação, materialização e validação |
| 4 | Visão Geral do Responsável | Coletivo | GKR-SURF-COL-002; GKR-TRN-112 | não iniciado | UXA-059 | superfície do responsável | materialização e validação funcional |
| 5 | gestão completa de solicitações pelo responsável | Coletivo | GKR-SURF-COL-003; GKR-TRN-105 a GKR-TRN-109; GKR-TRN-112 | programado | UXA-056; UXA-059 | operação, decisões e retornos na origem | fluxo bilateral materializado e validado |
| 6 | relação Organização–Coletivo | Organização e Coletivo | GKR-SURF-ORG-004 a GKR-SURF-ORG-006; GKR-SURF-COL-008; GKR-TRN-206 a GKR-TRN-209 | contratado | UXA-019 | superfícies e transições bilaterais | materialização e validação bilateral |
| 7 | matriz visual institucional completa | Organização | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | indeterminado | UXA-014 | inventário integrado e continuidades | programa específico e validação |
| 8 | dez estados residuais do Opportunity Boost | camada comercial | GKR-SURF-COM-005; GKR-TRN-305 | materializado | UXA-038; UXA-055 | validação funcional dos estados residuais | pacote de validação correspondente |
| 9 | efeito externo de oportunidades | Pessoa | GKR-SURF-PER-203; GKR-SURF-BND-001; GKR-TRN-205 | indeterminado | UXA-004; UXA-007 | efeito, retorno e resultado no destino externo | contrato e validação específicos quando aplicáveis |
| 10 | reconciliação da Tela Hoje com a compreensão inicial | Pessoa | GKR-SURF-PER-007; GKR-SURF-PER-008; GKR-TRN-007 | validado localmente | UXA-002; UXA-010; UXA-037 | transição integrada entre pacotes | validação da continuidade integrada |
| 11 | integração publicação–descoberta de oportunidades | Organização e Pessoa | GKR-SURF-ORG-003; GKR-SURF-PER-201; GKR-TRN-203 | parcial | UXA-004 | validação conjunta entre ciclo institucional e mapa | revalidação funcional integrada |
| 12 | sincronização integrada entre mapa, lista e detalhe | Pessoa | GKR-SURF-PER-201 a GKR-SURF-PER-203; GKR-TRN-204; GKR-TRN-210; GKR-TRN-211 | validado localmente | UXA-004; UXA-007 | validação do conjunto entre pacotes | revalidação funcional integrada |
| 13 | estados de erro, retorno e interrupção dispersos | todos | registro de transições completo ainda seletivo | parcial | autoridades diversas | matriz integrada de exceções | cobertura e validação por jornada |

## 3. Efeito da UXA-078

A UXA-078 corrige a estrutura documental dos cinco achados da UXA-077:

- endpoints passam a resolver por ID;
- busca de Coletivos e descoberta de oportunidades são separadas;
- publicação institucional e Detalhe de Oportunidade são separados;
- UXA-055 passa a ser a fonte dos dez estados residuais;
- os campos obrigatórios são registrados por superfície.

Essas correções:

- aguardam nova validação funcional;
- não materializam interfaces ausentes;
- não alteram a maturidade primária das referências;
- não encerram as lacunas listadas;
- não comprovam jornada ponta a ponta.

## 4. Fronteira externa

`GKR-SURF-BND-001` estabiliza documentalmente o destino de `GKR-TRN-205`.

Ela não comprova:

- existência de integração técnica;
- conclusão de inscrição, contratação ou compra;
- retorno de dados;
- resultado externo;
- responsabilidade da Guivos por operação de terceiro.

Por isso, a lacuna de efeito externo permanece aberta.

## 5. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver:

1. autoridade documental identificada;
2. maturidade primária registrada;
3. materialização específica quando necessária;
4. transições de entrada e saída;
5. estados alternativos, de retorno e de exceção;
6. proteção de dados e autoridade;
7. validação funcional correspondente;
8. atualização deste registro por pacote governado.

## 6. Restrições

- nenhuma tela genérica fecha uma lacuna;
- uma seta presumida não cria transição;
- proximidade entre artefatos não comprova continuidade;
- inclusão no catálogo não altera maturidade;
- validação de uma superfície não valida automaticamente a jornada;
- atribuição de ID não equivale a materialização;
- correção documental não equivale a aprovação funcional;
- ausência de evidência será registrada como `indeterminado`, `parcial` ou `ausente`.

## 7. Estado vigente

A UXA-074 aprovou este registro como instrumento observacional. A UXA-075 manteve o status `active`.

A UXA-078 melhora a rastreabilidade e corrige a estrutura granular, sem fechar ou reclassificar lacunas de produto. Os registros reformulados permanecem `draft`.
