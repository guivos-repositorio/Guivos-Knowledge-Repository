---
id: RP-002-PILOT-OP-001
title: Liberação Operacional do Piloto e Dry Run Real
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_preflight_pre_real_participant
related:
  - RP-002-PMF-001
  - RP-002-SUP-001
  - RP-002-DAF-001
  - GKR-UX-ORGCOL-SUPPLY-VALUE-001
  - PAS-001-CC-LIFECYCLE-001
  - PAS-001-OA-FOUNDATION-001
---

# Liberação Operacional do Piloto e Dry Run Real

## 1. Finalidade

Este documento transforma a prontidão metodológica do `RP-002-PMF-001` em um **gate operacional executável antes da entrada de qualquer participante real**.

Ele responde à pergunta:

> **O que precisa estar materialmente configurado, revisado e testado para que a Guivos possa iniciar o primeiro Dry Run Real sem confundir prontidão conceitual com autorização operacional?**

O objetivo não é ampliar a teoria do RP-002.

O objetivo é impedir que uma Pessoa real seja recrutada enquanto existirem lacunas de privacidade, segurança, acesso, papéis, ferramentas, benchmark ou governança de dados.

## 2. Estado atual

```text
CONCEPTUAL READINESS
→ PASS

METHODOLOGICAL READINESS
→ PASS

FIELD KIT v0.1
→ MATERIALIZADO

CORRECTION / LIMITATION / DELETION DRILL
→ PASS COM DADOS SINTÉTICOS

OPERATIONAL RELEASE
→ CONDITIONAL

DRY RUN REAL
→ NÃO INICIADO

PARTICIPANT 001
→ HOLD

PMF
→ NOT VALIDATED
```

O `HOLD` não significa falha da tese.

Significa apenas que **nenhuma Pessoa real deve entrar no experimento antes de os blockers operacionais críticos estarem fechados**.

## 3. Fronteira deste documento

Este documento governa:

- pré-condições para recrutamento;
- separação entre identidade e pesquisa;
- minimização de dados;
- papéis e acesso;
- registro de operadores/ferramentas;
- triagem de segurança;
- execução do Dry Run Real;
- benchmark controlado;
- follow-up;
- Evidence Guivos experimental;
- incidentes;
- critérios de liberação do `Participant 001`;
- o que pode ou não retornar ao GKR.

Ele **não**:

- define base legal por conta própria;
- substitui revisão jurídica ou de privacidade;
- autoriza coleta de dados reais;
- cria consentimento genérico para toda a Journey;
- cria diagnóstico;
- cria recomendação clínica, jurídica ou financeira;
- transforma o piloto em produto;
- transforma Research em Canon;
- declara PMF.

## 4. Princípio de liberação

```text
PRONTIDÃO CONCEITUAL
≠ AUTORIZAÇÃO OPERACIONAL

INSTRUMENTO DESENHADO
≠ FERRAMENTA CONFIGURADA

POLÍTICA ESCRITA
≠ CONTROLE DE ACESSO TESTADO

DADOS PSEUDONIMIZADOS
≠ DADOS ANÔNIMOS

PARTICIPANTE RECRUTADO
≠ PARTICIPANTE LIBERADO
```

Regra:

> **O Participant 001 só pode ser liberado quando todos os gates críticos estiverem em `PASS` e houver autorização final de início do Dry Run.**

## 5. Arquitetura operacional de dados

A arquitetura mínima separa dois ambientes.

### 5.1 Identity Vault

Contém somente o necessário para administrar relacionamento operacional com a Pessoa, por exemplo:

- `participant_id` pseudônimo;
- nome;
- canal de contato;
- estado de recrutamento;
- elegibilidade operacional;
- agenda;
- status de follow-up;
- solicitações de direitos;
- retenção/exclusão.

Não deve conter análise rica da Journey quando isso não for necessário para sua função.

### 5.2 Research Base

Usa identificadores como:

```text
PILOT-P-001
EP-P-001-001
OP-P-001-001
```

Pode conter, conforme autorização e necessidade:

- Momento revisado;
- profundidade de captura;
- modo experimental;
- Possibilidades;
- oportunidades;
- gates;
- benchmark;
- ação;
- estados de experiência;
- contribuição;
- Evidence Guivos experimental;
- falhas e aprendizados.

Não deve conter nome, e-mail, telefone ou outro identificador direto por padrão.

### 5.3 Regra de ligação

A chave que relaciona identidade e dossiê de pesquisa deve possuir acesso mais restrito que o dossiê pseudonimizado.

```text
IDENTIDADE
→ acesso mínimo

PESQUISA
→ pseudonimizada

CHAVE DE LIGAÇÃO
→ acesso ainda mais restrito
```

## 6. O que nunca deve ir para o GKR

O Guivos Knowledge Repository preserva conhecimento, não banco de participantes.

Não inserir no GitHub/GKR:

- nome de participante;
- e-mail;
- telefone;
- endereço;
- documento;
- áudio individual;
- transcrição identificável;
- resposta bruta identificável;
- dossiê individual;
- chave de ligação;
- planilha de recrutamento;
- solicitações individuais de direitos;
- logs privados de incidentes.

O GKR pode receber posteriormente:

- protocolo;
- metodologia;
- resultados agregados;
- contraexemplos desidentificados;
- mudanças de hipótese;
- limitações;
- decisões de GO / REVISE / STOP;
- evidência suficiente para promoção de maturidade, quando existir.

## 7. Privacidade — blockers obrigatórios

Antes de qualquer Pessoa real, devem estar explicitamente resolvidos:

### P1 — Controlador formal

Identificar quem toma as decisões essenciais sobre o tratamento de dados do piloto.

A ANPD descreve o controlador como o agente responsável pelas principais decisões do tratamento e pelo atendimento aos direitos dos titulares.

Referência oficial:

<https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1>

**Estado atual:** `TBD / BLOCKER`.

### P2 — Canal de privacidade

Definir um canal verificável pelo qual a Pessoa possa exercer direitos ou pedir esclarecimentos.

**Estado atual:** `TBD / BLOCKER`.

### P3 — Finalidades e categorias de dados

Documentar, antes da coleta:

- finalidade de recrutamento;
- finalidade da entrevista;
- finalidade do benchmark;
- finalidade dos follow-ups;
- categorias de dados;
- destinatários/operadores;
- retenção;
- exclusão;
- compartilhamentos previstos.

O aviso ao participante deve ser claro e proporcional ao piloto.

Referência estrutural útil da ANPD:

<https://www.gov.br/anpd/pt-br/acesso-a-informacao/aviso-de-privacidade>

### P4 — Base legal

A base legal aplicável ao tratamento deve ser **documentada e revisada com os fatos reais da operação**.

Este documento não presume consentimento nem qualquer outra hipótese legal.

Referência oficial:

<https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes/perguntas-frequentes>

**Estado atual:** `TBD / BLOCKER`.

### P5 — Direitos do titular

O processo precisa suportar, quando aplicável:

- informação;
- confirmação/acesso;
- correção;
- bloqueio/eliminação nos casos aplicáveis;
- revogação quando consentimento for a base usada;
- informação sobre compartilhamento;
- demais direitos aplicáveis.

Referência oficial:

<https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares>

### P6 — Retenção

A proposta operacional de Research permanece:

```text
CONTATO OPERACIONAL
→ até o follow-up final + janela operacional definida

ÁUDIO
→ OFF por padrão

DOSSIÊ PSEUDONIMIZADO
→ durante execução, análise e auditoria do ciclo
→ depois passa por revisão explícita de retenção
```

Nenhum prazo deve ser tratado como obrigação legal universal sem revisão do contexto real.

### P7 — Gravação

```text
RECORDING
→ OFF BY DEFAULT
```

Se algum ciclo futuro exigir gravação, isso demanda decisão específica, transparência, necessidade demonstrável e controles adicionais.

### P8 — Minimização

Perguntar ou registrar uma informação somente se ela puder materialmente alterar:

- Possibilidade;
- gate;
- oportunidade;
- segurança;
- explicação;
- decisão metodológica.

## 8. Drill de correção, limitação e exclusão

O fluxo foi testado previamente apenas com registros sintéticos.

Estado:

```text
CREATE SYNTHETIC IDENTITY
→ PASS

LINK PSEUDONYMOUS EPISODE
→ PASS

CORRECT
→ PASS

LIMIT
→ PASS

DELETE
→ PASS

RESIDUAL SCAN
→ 0 MATCHES NO TESTE SINTÉTICO
```

Limite:

> **o drill prova a lógica do workbook/processo; não prova exclusão nos futuros operadores reais de nuvem.**

Quando ferramentas reais forem escolhidas, o drill deve ser repetido nelas.

## 9. Registro de operadores e ferramentas

Nenhuma ferramenta deve ser usada com dados reais apenas porque é tecnicamente conveniente.

Para cada operador/ferramenta, registrar:

| Campo | Pergunta |
|---|---|
| `tool_or_operator` | qual serviço ou operador? |
| `purpose` | para quê? |
| `data_categories` | que dados receberá? |
| `direct_identifiers_allowed` | identificadores diretos serão permitidos? |
| `sensitive_data_allowed` | dados sensíveis serão permitidos? |
| `international_transfer` | existe transferência internacional? |
| `contract_or_DPA_status` | situação contratual relevante? |
| `approved_by` | quem aprovou? |
| `status` | PENDING / APPROVED / REJECTED |
| `notes` | limitações |

Estado atual mínimo:

```text
FORM / RECRUITMENT TOOL
→ TBD

IDENTITY STORAGE
→ TBD

RESEARCH STORAGE
→ TBD

GENERAL AI TOOL
→ TBD

SEARCH / WEB TOOLS
→ TBD
```

Até a escolha e revisão desses operadores, `Participant 001` permanece `HOLD`.

## 10. Regra para uso de IA

Padrão do piloto:

```text
IDENTIFICADOR DIRETO PARA IA
→ NÃO, por padrão

CONTEXTO PSEUDONIMIZADO / SANITIZADO
→ somente o necessário

DADO SENSÍVEL DESNECESSÁRIO
→ não coletar / não enviar

TRANSCRIÇÃO BRUTA IDENTIFICÁVEL
→ não enviar por padrão
```

A ferramenta de IA não recebe a Journey completa apenas porque uma tarefa isolada precisa de apoio.

## 11. Matriz mínima de papéis

O Dry Run precisa possuir funções explícitas, ainda que uma mesma Pessoa acumule mais de uma função quando não houver conflito material.

| Papel | Função central |
|---|---|
| Pilot Owner | responde pelo ciclo e decisão de liberação |
| Interviewer | conduz captura proporcional e revisão do Momento |
| Moment Reviewer | revisa síntese e evita distorção |
| Supply Researcher | localiza oportunidades candidatas |
| Supply Verifier | verifica fonte, freshness, gates e fatos críticos |
| Benchmark Operator | produz baselines sob o mesmo snapshot |
| Benchmark Blinder | preserva cegamento/randomização quando aplicável |
| Data Steward | governa acesso, retenção, correção e exclusão |
| Safety Owner | decide interrupção/escalonamento de segurança |
| Analyst | consolida resultados pseudonimizados |

### Separação importante

> **Quem produz a solução Guivos não deve controlar sozinho a avaliação cega que decide se a Guivos venceu.**

## 12. Matriz de acesso

Princípio de mínimo privilégio:

```text
INTERVIEWER
→ identidade mínima + episódio designado

SUPPLY RESEARCHER / VERIFIER
→ contexto mínimo necessário, sem identidade direta

BENCHMARK BLINDER
→ chave de cegamento, não identidade rica

ANALYST
→ base pseudonimizada

DATA STEWARD
→ acesso necessário para governança, não autoridade sobre interpretação humana
```

A existência da matriz escrita não substitui configuração real das permissões.

## 13. Safety Gate

O piloto não é serviço de emergência nem substitui profissional habilitado.

### S0 — dentro do escopo

Momento não sensível e compatível com as famílias do piloto.

**Ação:** continuar.

### S1 — sensível, não emergencial

Surge informação sensível que não exige emergência e não precisa ser aprofundada para a tarefa.

**Ação:** minimizar; registrar somente restrição material; evitar aconselhamento fora do escopo.

### S2 — necessidade profissional fora do piloto

O episódio exige orientação clínica, jurídica, financeira de alto risco ou outra atuação especializada.

**Ação:** interromper a hipótese Guivos nesse território e explicar limite; não improvisar aconselhamento.

### S3 — urgência explícita

Há risco imediato, emergência ou crise aguda.

**Ação:** parar o experimento; priorizar segurança; não continuar coleta para fins de pesquisa.

No Brasil, referências públicas de emergência incluem:

- Polícia Militar: `190`;
- SAMU: `192`;
- Corpo de Bombeiros: `193`.

Referência oficial de números tridígitos:

<https://www.gov.br/anatel/pt-br/regulado/acompanhamento-e-controle/servicos-de-utilidade-publica-e-de-emergencia-tridigitos>

O SAMU 192 é serviço gratuito de urgência 24/7:

<https://www.gov.br/saude/pt-br/composicao/saes/samu-192>

Para apoio emocional voluntário no Brasil, o CVV informa atendimento gratuito pelo `188`, 24 horas:

<https://cvv.org.br/o-cvv/>

Essas referências não transformam o piloto em serviço de saúde.

## 14. População inicial do Dry Run

Adultos com Momentos reais em famílias de menor risco regulatório:

### Família A — Trabalho / carreira / aprendizagem

Exemplos:

- transição profissional;
- desenvolvimento de competência;
- mentoria;
- formação;
- exploração de área.

### Família B — Descoberta / novas experiências

Exemplos:

- cultura;
- hobbies;
- aprendizagem exploratória;
- atividades presenciais;
- novas experiências de baixo risco.

### Família C — Comunidade / participação / contribuição

Exemplos:

- voluntariado;
- grupos comunitários;
- Coletivos;
- participação local;
- redes de prática.

### Família D — Decisão contextual

Situações com alternativas reais e restrições materiais, sem entrar em território clínico, jurídico ou financeiro crítico.

## 15. Exclusões iniciais

Não incluir no primeiro Dry Run:

- menores de idade;
- emergência ou crise aguda;
- violência ou risco imediato;
- aconselhamento clínico individual;
- diagnóstico;
- decisão jurídica individual complexa;
- recomendação financeira de alto risco;
- imigração complexa com consequência jurídica material;
- inferência religiosa não autorizada;
- qualquer episódio que o Safety Owner considere inadequado ao desenho atual.

## 16. Recrutamento

O recrutamento precisa deixar claro que:

- trata-se de pesquisa/piloto;
- a solução está em validação;
- participar não garante encontrar uma oportunidade;
- a Pessoa pode discordar da interpretação;
- a Pessoa pode não agir;
- a Guivos pode concluir que nenhuma oportunidade encontrada é adequada;
- uma oportunidade pesquisada não implica parceria entre Guivos e provider;
- dados e direitos serão explicados no aviso aplicável antes da coleta.

### Compensação

Quando houver compensação experimental:

> **ela deve ser fixa e independente de feedback positivo, preferência pela Guivos, ação, inscrição, compra ou conclusão de oportunidade.**

Isso reduz pressão para agradar o experimento.

## 17. Tamanho do Dry Run Real

Primeira execução recomendada:

```text
6 EPISÓDIOS REAIS
```

O Dry Run não serve para estimar PMF estatisticamente.

Serve para detectar falhas de operação antes da amostra principal.

Cobertura mínima desejada:

- pelo menos um episódio `Direct`;
- pelo menos dois `Exploratory` ou com baixa direção inicial;
- pelo menos dois `Decisional`;
- um caso em que histórico/continuidade possa ser testado somente se existir legitimamente;
- diversidade entre Famílias A, B e C;
- Família D apenas quando segura e operacionalmente adequada.

O modo pertence ao Episódio, não à Pessoa.

## 18. Dry Run — sequência operacional

```text
0. RELEASE GATE
↓
1. RECRUTAMENTO
↓
2. TRIAGEM
↓
3. AVISO / TRANSPARÊNCIA / AUTORIZAÇÕES APLICÁVEIS
↓
4. PARTICIPANT_ID
↓
5. ENTREVISTA PROPORCIONAL
↓
6. SÍNTESE DO MOMENTO
↓
7. REVISÃO PELA PESSOA
↓
8. ROUTING DE MODO
↓
9. POSSIBILIDADES, SE AGREGAREM VALOR
↓
10. PESQUISA DE SUPPLY
↓
11. VERIFICAÇÃO DE FONTE / FRESHNESS
↓
12. GATES
↓
13. SELEÇÃO POR OBJETIVO DO MODO
↓
14. ENTREGA GUIVOS
↓
15. BASELINES
↓
16. CEGAMENTO / RANDOMIZAÇÃO QUANDO APLICÁVEL
↓
17. AVALIAÇÃO IMEDIATA
↓
18. AÇÃO / NÃO AÇÃO
↓
19. FOLLOW-UP
↓
20. EXPERIÊNCIA / CONTRIBUIÇÃO
↓
21. NOVO MOMENTO, QUANDO HOUVER
↓
22. FECHAMENTO DO EPISÓDIO
```

## 19. Pré-sessão — checklist do episódio

Antes da entrevista:

- participante passou triagem;
- aviso aplicável entregue;
- permissões e acessos testados;
- episódio pseudônimo criado;
- operador de entrevista sabe o escopo;
- Safety Owner está definido;
- template de incidente está disponível;
- nenhum dado real foi colocado em GitHub/GKR;
- remuneração, se houver, não depende do resultado;
- baseline e Guivos não compartilharão informação além do snapshot autorizado.

## 20. Entrevista e revisão do Momento

Perguntas-base permanecem no `RP-002-PMF-001`.

A entrevista deve capturar somente o necessário.

Depois, a síntese volta para a Pessoa com classificação metodológica:

```text
A — precisa
B — suficientemente precisa
C — correção material
D — falha de compreensão
```

`C` ou `D` bloqueia pesquisa de supply até correção.

## 21. Routing experimental

Após revisão do Momento:

```text
DIRECT
→ direção clara

EXPLORATORY
→ descoberta/experimentação

DECISIONAL
→ alternativas e trade-offs

LONGITUDINAL
→ histórico anterior muda materialmente a decisão
```

O routing é hipótese metodológica.

Não deve virar rótulo de identidade da Pessoa.

## 22. Supply Research

Para cada oportunidade candidata, registrar no mínimo:

- provider/agente;
- oportunidade;
- fonte;
- timestamp;
- modalidade;
- território;
- período;
- custo;
- elegibilidade;
- disponibilidade;
- carga;
- idioma;
- restrições;
- mecanismos;
- Possibilidade, quando usada;
- evidência externa;
- relação comercial;
- incertezas.

A pesquisa pode descobrir oportunidade de agente não parceiro.

```text
DISCOVERY
≠ ADMISSION
≠ PARTNERSHIP
≠ RECOMMENDATION
≠ SPONSORSHIP
```

## 23. Supply Verification

O verifier revisa separadamente fatos críticos.

Checklist:

```text
G1 — existe?
G2 — responsável identificável?
G3 — fonte/legitimidade suficiente?
G4 — disponível no período relevante?
G5 — elegibilidade compatível?
G6 — acesso viável?
G7 — risco/restrições aceitáveis?
G8 — materializa caminho legítimo?
G9 — relação comercial transparente?
G10 — informação suficiente para explicação honesta?
```

`UNKNOWN` material permanece visível e pode impedir apresentação.

## 24. Seleção

### Direct

Priorizar:

- compatibilidade;
- qualidade factual;
- acesso;
- conveniência.

### Exploratory

Priorizar:

- diversidade relevante;
- baixo risco;
- baixo compromisso proporcional;
- valor informacional;
- possibilidade de aprender preferência.

### Decisional

Priorizar:

- fit;
- gates;
- trade-offs;
- evidência;
- explicabilidade.

### Longitudinal

Usar histórico somente se ele alterar materialmente a nova orientação.

## 25. Papéis contextuais da oportunidade

Durante o Dry Run, oportunidades podem ser classificadas como:

- `Principal`;
- `Alternative`;
- `Complementary`;
- `Sequential`;
- `Enabling`;
- `Exploratory`.

Esses papéis não são ranking universal.

## 26. Entrega Guivos

A entrega deve explicar:

1. o que foi compreendido;
2. qual caminho pode fazer sentido, quando a camada de Possibilidade agrega valor;
3. oportunidade(s) concreta(s);
4. por que podem fazer sentido;
5. condições e gates;
6. custos e restrições conhecidos;
7. incertezas;
8. evidência externa e seus limites;
9. alternativas legitimamente descartadas quando isso aumentar confiança;
10. próximo ato possível sem pressão para agir.

Regra:

> **não-fit explicado também é valor.**

## 27. Benchmark controlado

Usar o mesmo snapshot de contexto autorizado para:

- baseline de Search;
- IA generalista;
- Guivos.

Sempre que operacionalmente possível:

- normalizar formato;
- remover marca identificável;
- randomizar ordem;
- separar operador de produção do blinder;
- preservar a opção `Nenhum`.

Perguntas de comparação:

- qual compreendeu melhor?
- qual mostrou caminhos mais úteis?
- qual trouxe oportunidades mais realizáveis?
- qual produziu menos ruído?
- qual explicou melhor?
- qual usaria hoje?
- qual manteria se pudesse escolher apenas uma solução?

## 28. Benchmark ecológico

Registrar como a Pessoa resolveria naturalmente sem a Guivos:

- Google;
- ChatGPT ou outra IA;
- LinkedIn;
- Instagram;
- marketplace;
- amigo;
- especialista;
- comunidade;
- nenhum recurso.

O objetivo é medir valor líquido, incluindo fricção real.

## 29. Ação

Estados comportamentais:

```text
NENHUMA AÇÃO
→ PESQUISA ADICIONAL
→ ABRIU FONTE
→ SALVOU
→ CONVERSOU COM ALGUÉM
→ ENTROU EM CONTATO
→ AGENDOU
→ INSCREVEU
→ COMPROU
→ COMEÇOU
```

`clicou` isoladamente não é automaticamente ação material.

## 30. Follow-up

Checkpoints iniciais:

- T+72h;
- T+14d;
- T+30d quando material.

Estados da experiência:

```text
CONSIDERADA
→ AÇÃO INICIAL
→ COMPROMISSO
→ PRIMEIRO CONTATO
→ PARTICIPAÇÃO INICIAL
→ EM ANDAMENTO
→ CONCLUÍDA / INTERROMPIDA
→ REFLETIDA
```

Interrupção não deve ser tratada automaticamente como falha humana.

## 31. Pós-experiência

Pergunta principal:

> **Essa experiência contribuiu para o seu Momento Atual?**

Depois:

> **De que forma?**

E:

> **O que aconteceu que faz você responder dessa forma?**

Resultados legítimos incluem:

- contribuição forte;
- contribuição parcial;
- nenhuma contribuição percebida;
- ainda inconclusivo;
- efeito negativo;
- efeito misto;
- descoberta de preferência;
- descarte legítimo de um caminho.

## 32. Evidence Guivos experimental

```text
EG-0 — experiência não confirmada
EG-1 — experiência declarada
EG-2 — contribuição declarada
EG-3 — consequência observável descrita
EG-4 — artefato relacionado
EG-5 — confirmação externa compatível
```

Mesmo `EG-5` não equivale automaticamente a evolução comprovada ou causalidade isolada.

## 33. Incidentes e falhas

Manter log separado para:

- incidente de privacidade;
- quebra de acesso;
- erro de pseudonimização;
- gate crítico escapado;
- oportunidade inexistente/desatualizada;
- interpretação materialmente errada;
- falha de cegamento;
- risco/safety;
- pressão indevida sobre participante;
- conflito econômico;
- outros desvios metodológicos.

Um incidente não deve ser escondido para proteger métrica do experimento.

## 34. Stop Rules do Dry Run

Interromper e revisar antes de continuar quando houver, entre outros:

- falha crítica de privacidade;
- acesso indevido;
- safety incident;
- oportunidade apresentada com incompatibilidade grave omitida;
- repetição de compreensão `C/D`;
- cegamento comprometido de forma estrutural;
- participante percebe captura como invasiva;
- ferramenta não suporta correção/exclusão como planejado;
- Researcher/Verifier não consegue estabelecer freshness suficiente;
- processo operacional exige mais contexto sensível do que o benefício justifica.

## 35. Métricas do Dry Run

O Dry Run não valida thresholds estatisticamente.

Ele verifica se é possível medir de forma confiável:

- `Understanding A+B`;
- `Opportunity Precision`;
- `Gate Escape Rate`;
- `Context Cost`;
- `Exploration Learning`;
- oportunidade seriamente considerada;
- benchmark first/tied;
- Action Rate;
- Reflection Return;
- experiência iniciada;
- contribuição;
- Longitudinal Lift, quando aplicável.

## 36. Participant 001 — Release Gate

Estado inicial deste documento:

| Gate | Estado | Evidência necessária |
|---|---|---|
| controlador formal identificado | **HOLD** | identidade formal documentada |
| canal de privacidade definido | **HOLD** | canal operacional testado |
| base legal revisada/documentada | **HOLD** | registro de revisão aplicável |
| notice/transparência final | **HOLD** | versão aprovada para uso |
| operadores/ferramentas aprovados | **HOLD** | registry sem `PENDING` crítico |
| transferência internacional avaliada | **HOLD** | avaliação por operador aplicável |
| permissões reais configuradas | **HOLD** | teste de mínimo privilégio |
| correction/deletion drill em workbook | **PASS** | teste sintético anterior |
| correction/deletion drill nos operadores reais | **HOLD** | repetição em stack real |
| Safety Owner atribuído | **HOLD** | nome/função operacional |
| Supply Researcher atribuído | **HOLD** | nome/função operacional |
| Supply Verifier atribuído | **HOLD** | nome/função operacional |
| Benchmark Blinder atribuído | **HOLD** | nome/função operacional |
| script de recrutamento aprovado | **HOLD** | versão final |
| Participant 001 recrutado e elegível | **HOLD** | triagem aprovada |
| autorização final de início | **HOLD** | release explícito |

Conclusão:

```text
PARTICIPANT 001
→ HOLD
```

Nenhuma linha `HOLD` deve ser convertida para `PASS` por inferência.

## 37. Critério para liberar o Dry Run

O estado muda para:

```text
DRY RUN REAL
→ RELEASED
```

somente quando:

1. todos os blockers críticos do `Participant 001` estiverem `PASS`;
2. os critérios de medição estiverem congelados na versão do ciclo;
3. instrumentos e operadores reais tiverem sido testados;
4. existir responsável por interrupção de segurança;
5. nenhum dado identificável estiver sendo direcionado ao GKR;
6. houver autorização final de execução.

## 38. Congelamento metodológico

Antes do primeiro participante:

```text
FREEZE
→ perguntas centrais
→ critérios A/B/C/D
→ gates G1–G10
→ modos
→ papéis de oportunidade
→ benchmark
→ follow-ups
→ métricas
→ stop rules
```

Mudanças durante o Dry Run precisam:

- ser versionadas;
- registrar motivo;
- indicar episódios afetados;
- impedir comparação enganosa entre versões.

## 39. Saída do Dry Run

Após seis episódios, produzir um relatório desidentificado contendo:

### Operação

- o processo funcionou?
- que etapa quebrou?
- que etapa custou contexto demais?
- houve falha de supply/freshness?
- houve incidente?

### Pessoa

- compreensão do Momento;
- clareza;
- relevância percebida;
- oportunidade seriamente considerada;
- comportamento;
- experiência, quando ocorreu;
- contribuição, quando ocorreu.

### Benchmark

- onde Guivos venceu;
- onde empatou;
- onde perdeu;
- por quê;
- que vantagem reivindicada não apareceu.

### Tese

Classificar:

```text
GO
REVISE
STOP
INCONCLUSIVE
```

## 40. Promoção de evidência para o GKR

O GKR só deve receber resultados depois de consolidação e desidentificação.

O futuro registro precisa distinguir explicitamente:

```text
PARTICIPANTE DISSE
≠ PARTICIPANTE FEZ

PARTICIPANTE FEZ
≠ EXPERIÊNCIA VIVIDA

EXPERIÊNCIA VIVIDA
≠ CONTRIBUIÇÃO

CONTRIBUIÇÃO
≠ CAUSALIDADE

PREFERÊNCIA
≠ PMF
```

## 41. Próximo ato legítimo

Com este protocolo materializado, o próximo ato não é aprofundar mais a teoria.

É fechar operacionalmente os gates do `Participant 001`.

A ordem recomendada é:

```text
1. CONTROLADOR + PRIVACY CONTACT
↓
2. BASE LEGAL / NOTICE REVIEW
↓
3. STACK + OPERATOR REGISTRY
↓
4. ACCESS MATRIX CONFIGURADA
↓
5. OPERATOR-SPECIFIC DELETION DRILL
↓
6. ROLE ASSIGNMENTS
↓
7. RECRUITMENT SCRIPT FINAL
↓
8. PARTICIPANT 001 TRIAGE
↓
9. FINAL RELEASE
↓
10. DRY RUN REAL 001
```

Até o item 9:

> **nenhum participante real deve entrar na base de pesquisa.**