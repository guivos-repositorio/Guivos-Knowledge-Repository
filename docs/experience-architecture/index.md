---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.66.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - UXA-038
  - UXA-050
  - UXA-055
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - UXA-065
  - UXA-066
  - UXA-067
  - UXA-068
  - UXA-069
  - UXA-070
  - UXA-071
  - M7.72
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório em experiências compreensíveis para Pessoas, Coletivos e Organizações.

Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design visual ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização visual ou documental
→ validação funcional
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Jornada pessoal — início protegido

| Responsabilidade | Autoridade |
|---|---|
| contrato do início protegido | UXA-020; UXA-023 |
| escolha, rascunho, revisão e autorização | UXA-034; UXA-035 |
| processamento e compreensão inicial | UXA-036; UXA-037 |
| expressão guiada por texto e voz | UXA-068 |
| validação da expressão guiada | UXA-069 |

### 3.1 Cobertura relacionada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Início protegido geral | 4 | 4 | 0 |
| Compreensão inicial | 5 | 5 | 0 |
| Expressão Guiada do Momento Atual | 8 | 8 | 0 |
| **Subtotal relacionado** | **17** | **17** | **0** |

A contagem permanece separada das famílias de Coletivos e Opportunity Boost.

## 4. Expressão Guiada validada

A UXA-068 e a UXA-069 governam oito estados:

1. orientação comum;
2. rascunho por texto;
3. preparação para voz;
4. gravação em andamento;
5. revisão da transcrição;
6. pergunta adaptativa;
7. separação de focos;
8. síntese estruturada.

Foram validados:

- conteúdo de origem separado da ajuda temporária;
- ajuda temporária somente após solicitação consciente;
- texto e voz equivalentes;
- rascunho sem análise ou salvamento implícitos;
- escolha única sobre o áudio, sem padrão;
- gravação e transcrição com finalidade limitada;
- interrupção, descarte e retorno com efeitos conhecidos;
- transcrição automática separada da versão revisada;
- perguntas opcionais com razão explícita e exemplos não recomendatórios;
- assuntos apenas sugeridos e organizados após escolha;
- síntese identificada como item derivado, sem uso automático;
- continuidade possível usando somente conteúdos de origem;
- inventário e autorização da UXA-034 antes do processamento material.

## 5. Autoridades dos Coletivos

| Responsabilidade | Autoridade |
|---|---|
| descoberta, Perfil Público e participação | UXA-056 |
| avaliação e reputação contextual | UXA-057 |
| interação, recomendação, contato e proteção | UXA-058 |
| programa e priorização de wireframes | UXA-059 |
| descoberta e busca móvel | UXA-060; UXA-061 |
| Perfil Público móvel | UXA-062; UXA-063 |
| revisão e solicitação móvel | UXA-064; UXA-065 |
| Solicitação Pendente móvel | UXA-066; UXA-067 |

## 6. Estado visual dos Coletivos

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| descoberta e busca | 5 | 5 | 0 |
| Perfil Público | 4 | 4 | 0 |
| revisão e solicitação | 5 | 5 | 0 |
| Solicitação Pendente | 8 | 8 | 0 |
| **Total de Coletivos** | **22** | **22** | **0** |

`Meus Coletivos`, Central de Atualizações, Início do Participante reformulado e Visão Geral do Responsável permanecem não iniciados.

## 7. Programa do Ambiente de Simulação

A UXA-070 estabelece um ambiente documental para inspecionar jornadas sem duplicar artefatos canônicos.

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

O programa diferencia participante, papel, perspectiva e autoridade. Visitante, solicitante, responsável, representante institucional, especialista e patrocinador são perspectivas ou papéis contextuais, não novos participantes estruturais.

A unidade mínima será um nó de jornada referenciado. Cada ligação será uma transição governada com origem, destino, condição, autoridade, efeito, dados, reversibilidade e evidência.

Estados de maturidade controlados:

- contratado;
- programado;
- materializado;
- validado;
- reformulação pendente;
- não iniciado;
- bloqueado;
- supersedido;
- arquivado;
- indeterminado.

O ambiente deverá exibir lacunas e continuidades ausentes sem criar telas genéricas ou setas presumidas.

## 8. Reutilização canônica

- artefatos serão referenciados por ID, caminho e versão;
- arquivos canônicos permanecerão em modo somente leitura;
- uma mesma referência poderá aparecer em várias perspectivas sem cópia;
- anotações e sobreposições permanecerão fora do artefato de origem;
- nenhuma ligação será criada por proximidade visual ou numeração;
- inclusão no ambiente não altera maturidade, prioridade ou canonicidade;
- Opportunity Boost permanecerá camada comercial identificada, não participante ou autoridade.

## 9. Continuidade governada

### 9.1 Jornada pessoal

```text
Home pública
→ início protegido
→ escolha de modalidade
→ Expressão Guiada do Momento Atual
→ inventário e autorização
→ processamento visível
→ compreensão inicial
```

### 9.2 Coletivos P0A

```text
Explorar Coletivos
→ Resultados de Busca
→ Perfil Público
→ Revisão e Solicitação de Participação
→ Solicitação Pendente
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

As cinco primeiras referências estão materializadas e validadas. As seguintes serão exibidas como lacunas, não como experiências existentes.

### 9.3 Organização e Coletivo

```text
proposta
→ avaliação bilateral
→ aprovação pelas autoridades legítimas
→ relação ativa
→ revisão
→ renovação, ajuste, pausa ou encerramento
```

A relação não transfere propriedade, direção ou dados além do escopo autorizado.

## 10. Decisões estruturais preservadas

- relato livre permanece legítimo;
- compartilhar pouco não é falha;
- digitar não solicita análise automática;
- gravar autoriza somente a operação apresentada;
- transcrição automática não é declaração confirmada;
- ajuda temporária não cria compreensão;
- síntese não substitui fonte;
- desconhecido não é fato;
- pergunta adicional não é obrigação de revelar;
- personalização depende de gates próprios;
- solicitação não é aprovação;
- convite não cria vínculo;
- consultar não altera fila;
- cancelamento, recusa e expiração permanecem distintos;
- publicidade não compra relevância, reputação ou autoridade;
- leitura, rolagem e silêncio não equivalem a confirmação.

## 11. Limites

Não foram iniciados:

- UXA-071;
- materialização do mapa integrado;
- SVG ou tela do ambiente de simulação;
- protótipo navegável;
- aplicação ou motor de simulação;
- modelo de IA ou algoritmo adaptativo;
- gravação, transcrição ou armazenamento reais;
- envio guiado de arquivos;
- protocolo clínico ou emergencial;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- política jurídica;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 12. Próxima transição

**UXA-071 — Materialização Documental do Mapa Integrado de Jornadas e Transições**, mediante autorização separada.

A futura referência permanecerá documental e não corresponderá automaticamente a protótipo ou implementação.
