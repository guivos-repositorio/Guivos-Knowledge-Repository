---
id: RP-002-PILOT-DATA-LAW-001
title: Piloto — Finalidades, Categorias de Dados e Avaliação de Base Legal
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_privacy_assessment_pre_real_participant
related:
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-PRIV-001
  - RP-002-PILOT-CTRL-DEC-001
  - RP-002-PILOT-PRIV-CH-TEST-001
  - RP-002-PMF-001
---

# Piloto — Finalidades, Categorias de Dados e Avaliação de Base Legal

## 1. Finalidade

Este documento materializa a avaliação operacional de `P3 — Finalidades e Categorias de Dados` e `P4 — Base Legal` do Dry Run Real / piloto `RP-002`.

Ele existe para responder, antes de qualquer Pessoa real:

> **Quais dados a Guivos pretende tratar, para quais finalidades, em quais ambientes, com quais limites e sob qual hipótese legal candidata para cada operação?**

Este registro é de **Research e prontidão operacional**.

Ele não substitui revisão jurídica profissional, não constitui parecer jurídico e não autoriza sozinho a entrada de participante real.

## 2. Estado executivo

```text
P3-A — FINALIDADES
→ PASS DOCUMENTAL

P3-B — CATEGORIAS DE DADOS
→ PASS DOCUMENTAL

P3-C — DESTINATÁRIOS / OPERADORES REAIS
→ HOLD

P3-D — PRAZOS EXATOS DE RETENÇÃO
→ HOLD

P3 — FINALIDADES E CATEGORIAS
→ CONDITIONAL

P4-A — MATRIZ DE BASE LEGAL CANDIDATA
→ MATERIALIZADA

P4-B — INSTRUMENTO DE TRANSPARÊNCIA / CONSENTIMENTO
→ DRAFT REQUIRED

P4-C — REVISÃO JURÍDICA / PRIVACIDADE FINAL
→ HOLD

P4 — BASE LEGAL
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 3. Premissas jurídicas verificadas

### 3.1 Guivos Ltda não deve usar a hipótese específica de “órgão de pesquisa” por inferência

A LGPD define `órgão de pesquisa` como órgão/entidade pública ou pessoa jurídica de direito privado **sem fins lucrativos** que cumpra os requisitos legais.

A ANPD esclarece que pessoa jurídica de direito privado com fins lucrativos não pode utilizar, apenas por realizar estudo ou pesquisa, as hipóteses específicas dos arts. `7º, IV` e `11, II, c` destinadas a órgão de pesquisa.

Isso não impede pesquisa por empresa privada. Exige apenas outra hipótese legal aplicável ao caso concreto.

Fontes oficiais:

- LGPD, arts. 5º, XVIII; 7º; 11: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>
- ANPD — Guia sobre tratamento de dados para fins acadêmicos e pesquisas: <https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/web-guia-anpd-tratamento-de-dados-para-fins-academicos.pdf>

### 3.2 Consentimento exige finalidade determinada

A LGPD define consentimento como manifestação livre, informada e inequívoca para finalidade determinada e atribui ao controlador o ônus de demonstrar sua obtenção válida.

Autorizações genéricas são inválidas.

Fonte oficial:

- LGPD, arts. 5º, XII e 8º: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>

### 3.3 Legítimo interesse não é base universal

A ANPD descreve legítimo interesse como hipótese aplicável a dados pessoais **não sensíveis**, vinculada a finalidade legítima, específica e explícita e sujeita à prevalência dos direitos e liberdades fundamentais do titular.

Por isso, o primeiro Dry Run não usa legítimo interesse como justificativa genérica para toda a pesquisa.

Fonte oficial:

- ANPD — Guia de Legítimo Interesse: <https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_hipoteses_legais_tratamento_de_dados_pessoais_legitimo_interesse>

### 3.4 Dados sensíveis têm regime reforçado

A LGPD exige hipóteses específicas para tratamento de dados pessoais sensíveis. Quando consentimento for utilizado, ele deve ser específico e destacado para finalidades específicas.

Fonte oficial:

- LGPD, art. 11: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>

## 4. Princípio operacional do primeiro Dry Run

O piloto é voluntário e experimental.

A arquitetura deve privilegiar:

```text
TRANSPARÊNCIA
+ CONSENTIMENTO ESPECÍFICO PARA O NÚCLEO DA PESQUISA
+ MINIMIZAÇÃO
+ PSEUDONIMIZAÇÃO
+ DIREITO DE SAÍDA
+ NÃO COLETA INTENCIONAL DE DADOS SENSÍVEIS
+ SEPARAÇÃO IDENTITY VAULT × RESEARCH BASE
```

Não usar:

```text
“ACEITOU PARTICIPAR”
→ COMO CONSENTIMENTO GENÉRICO PARA QUALQUER TRATAMENTO
```

## 5. População autorizável para o primeiro Dry Run

Por desenho atual:

- adultos `18+`;
- participação voluntária;
- Momento em famílias de menor risco regulatório previstas no `RP-002-PILOT-OP-001`;
- capacidade de compreender aviso e consentimento;
- possibilidade de interromper a participação sem penalidade.

Fora do escopo inicial:

- crianças e adolescentes;
- emergência ou crise aguda;
- tratamento clínico;
- aconselhamento jurídico;
- decisão financeira de alto risco;
- episódios cujo objetivo exija coleta persistente de dados sensíveis.

## 6. Finalidades do tratamento

### F1 — Recrutamento e elegibilidade operacional

Finalidade:

- convidar a Pessoa;
- verificar faixa etária mínima;
- verificar disponibilidade;
- verificar aderência às famílias permitidas do Dry Run;
- agendar sessão;
- administrar desistência antes da sessão.

Não usar dados de recrutamento para marketing ou advertising.

### F2 — Administração da participação

Finalidade:

- manter `participant_id`;
- conectar a Pessoa à sessão correta;
- administrar agenda;
- controlar estado do ciclo;
- realizar follow-up autorizado;
- executar direitos, correções e exclusões.

### F3 — Compreensão proporcional do Momento

Finalidade:

- compreender apenas o contexto necessário para testar a hipótese do `RP-002`;
- produzir síntese revisável pela Pessoa;
- identificar objetivos, restrições e preferências que materialmente alterem Possibilidades, gates ou oportunidades.

Proibição:

> **não capturar biografia completa quando o episódio exige apenas contexto limitado.**

### F4 — Pesquisa e verificação de oportunidades

Finalidade:

- transformar o Momento revisado em Possibilidades quando útil;
- localizar oportunidades candidatas;
- verificar legitimidade, freshness, acesso, elegibilidade, segurança, restrições e fit contextual;
- registrar por que oportunidades entraram ou foram descartadas.

### F5 — Benchmark experimental

Finalidade:

- comparar Guivos, Search baseline e IA generalista sob snapshot equivalente;
- medir compreensão, utilidade, realizabilidade, ruído e explicabilidade;
- preservar cegamento/randomização quando aplicável.

O benchmark não autoriza uso secundário da identidade.

### F6 — Decisão e ação voluntária

Finalidade:

- registrar se a Pessoa considerou, escolheu, ignorou ou rejeitou uma oportunidade;
- registrar motivo apenas quando necessário e voluntariamente fornecido;
- distinguir intenção de ação de ação efetiva.

### F7 — Follow-up e experiência

Finalidade:

- verificar se a oportunidade foi efetivamente vivida;
- registrar estado de experiência;
- capturar contribuição percebida, efeito negativo, resultado misto ou inconclusivo;
- compreender se o Momento mudou.

### F8 — Aprendizado metodológico e análise agregada

Finalidade:

- testar a hipótese da Guivos;
- medir falhas do método;
- detectar gaps de supply;
- produzir resultados agregados/desidentificados;
- decidir `GO / REVISE / STOP / INCONCLUSIVE`.

### F9 — Governança de privacidade e segurança

Finalidade:

- guardar prova mínima de notice/consentimento;
- atender direitos;
- registrar revogação e exclusão;
- manter logs estritamente necessários de acesso/incidente;
- demonstrar execução de controles.

Não utilizar esta finalidade como justificativa para vigilância desnecessária.

## 7. Categorias de dados — Identity Vault

Permitidas quando necessárias:

| Categoria | Exemplo | Regra |
|---|---|---|
| identificador operacional | `PILOT-P-001` | obrigatório como pseudônimo |
| nome | nome da Pessoa | somente Identity Vault |
| canal de contato | e-mail/telefone escolhido | mínimo necessário |
| faixa etária / confirmação 18+ | `18+` ou faixa | evitar data de nascimento exata por padrão |
| cidade/região | cidade ou área útil ao episódio | somente se alterar supply/acesso |
| idioma | idioma de interação | quando relevante |
| disponibilidade | dias/horários | quando relevante à oportunidade |
| status de recrutamento | convidado/elegível/agendado/desistiu | operacional |
| consent/version record | versão, data, status | prova mínima |
| direitos/status | solicitação, correção, exclusão, fechamento | separado do dossiê de Research |

Não coletar por padrão:

- CPF;
- RG;
- endereço residencial completo;
- documento de identidade;
- data de nascimento completa;
- dados bancários;
- senha;
- credencial de terceiros.

## 8. Categorias de dados — Research Base

Permitidas em forma pseudonimizada e proporcional:

- `participant_id`;
- `episode_id`;
- domínio(s) de evolução relevantes;
- síntese revisada do Momento;
- objetivo/direção declarada;
- Próximo Passo;
- restrições materiais;
- preferências materiais;
- Possibilidades utilizadas no episódio;
- oportunidades candidatas;
- resultado dos gates `G1–G10`;
- fontes e freshness;
- explicação de fit/não-fit;
- resultado do benchmark;
- intenção de ação;
- ação efetiva quando informada;
- estado de experiência;
- contribuição percebida;
- Novo Momento quando aplicável;
- observações metodológicas;
- falhas/incertezas.

## 9. Dados sensíveis — política do primeiro Dry Run

```text
COLETA INTENCIONAL
→ NÃO

PERSISTÊNCIA POR PADRÃO
→ NÃO

INFERÊNCIA
→ NÃO
```

Se dado sensível surgir espontaneamente:

1. não aprofundar por curiosidade;
2. verificar se a informação é realmente necessária para a tarefa;
3. quando desnecessária, não persistir no dossiê;
4. quando indicar `S2/S3`, aplicar Safety Gate e interromper/desviar o experimento conforme o protocolo;
5. se algum futuro episódio realmente exigir persistência de dado sensível, **não usar este documento como autorização**;
6. pausar a coleta e exigir avaliação específica, finalidade específica e hipótese legal adequada — inclusive consentimento específico e destacado quando essa for a base utilizada.

## 10. Áudio, vídeo e transcrição

```text
GRAVAÇÃO DE ÁUDIO
→ OFF BY DEFAULT

GRAVAÇÃO DE VÍDEO
→ OFF BY DEFAULT

TRANSCRIÇÃO BRUTA IDENTIFICÁVEL
→ NÃO PERSISTIR POR PADRÃO
```

Qualquer mudança exige decisão separada.

## 11. Matriz de base legal candidata

Esta matriz é uma **avaliação operacional candidata**, não parecer jurídico final.

| Operação | Dado | Base candidata | Estado |
|---|---|---|---|
| recrutamento voluntário | dados pessoais comuns | consentimento — art. 7º, I | `PROPOSED` |
| administração do episódio voluntário | dados pessoais comuns | consentimento — art. 7º, I | `PROPOSED` |
| entrevista / compreensão do Momento | dados pessoais comuns necessários | consentimento — art. 7º, I | `PROPOSED` |
| benchmark | respostas e avaliações pseudonimizadas | consentimento — art. 7º, I | `PROPOSED` |
| follow-up / experiência | dados pessoais comuns pseudonimizados | consentimento — art. 7º, I | `PROPOSED` |
| prova do consentimento / atendimento de direitos | registros mínimos necessários | cumprimento de obrigação legal/regulatória — art. 7º, II, quando aplicável | `REVIEW REQUIRED` |
| segurança e auditoria mínima | dados comuns / logs mínimos | legítimo interesse — art. 7º, IX, somente se necessário e após teste de balanceamento; ou outra base aplicável | `HOLD` |
| dado sensível não necessário | dado sensível | **não tratar/persistir** | `REJECTED BY DESIGN` |
| dado sensível necessário em futuro episódio | dado sensível | avaliação específica; consentimento específico/destacado — art. 11, I, quando aplicável | `NOT AUTHORIZED` |
| emergência explícita | dado necessário à proteção da vida/incolumidade | arts. 7º, VII e/ou 11, II, e, conforme caso | `CONTINGENCY ONLY` |

## 12. Por que consentimento é a base candidata para o núcleo do Dry Run

O primeiro Dry Run foi desenhado para ser:

- voluntário;
- de pequena escala;
- não contratual;
- não necessário para prestação de serviço essencial;
- interrompível sem penalidade;
- baseado em finalidades experimentais específicas e explicáveis.

Essas características tornam o consentimento uma hipótese operacional candidata mais transparente para o **núcleo da participação**, desde que sua validade seja materialmente assegurada.

Isso exige:

- linguagem clara;
- ausência de coerção;
- finalidade determinada;
- granularidade suficiente;
- prova de manifestação;
- revogação facilitada;
- não condicionar benefício essencial inexistente à autorização;
- não usar autorização genérica.

## 13. Por que legítimo interesse não será usado como base geral do primeiro piloto

Embora a ANPD reconheça legítimo interesse como hipótese possível para dados não sensíveis em situações concretas, o piloto não precisa começar sob uma base mais complexa e menos intuitiva quando a participação pode ser voluntária e transparente.

Portanto:

```text
LEGÍTIMO INTERESSE PARA O NÚCLEO DA PESQUISA
→ NÃO ADOTADO POR PADRÃO
```

Pode permanecer candidato apenas para operações auxiliares específicas — por exemplo segurança mínima — e somente após:

- finalidade legítima explícita;
- necessidade;
- legítima expectativa;
- teste de balanceamento;
- salvaguardas;
- transparência;
- confirmação de que os dados não são sensíveis.

## 14. Direitos e revogação

Quando consentimento sustentar uma operação do piloto, o processo deve permitir:

- informação;
- confirmação/acesso;
- correção;
- revogação;
- eliminação quando aplicável;
- informação sobre compartilhamentos;
- demais direitos aplicáveis.

A ANPD informa que a revogação do consentimento deve ser facilitada e que tratamentos baseados em consentimento possuem direito de eliminação, ressalvadas hipóteses legais de conservação.

Fonte oficial:

<https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares>

## 15. Compartilhamento e operadores

Nenhum operador real é aprovado por este documento.

Antes do Participant 001, deve existir registro real para cada ferramenta que receber dados pessoais, conforme a matriz do `RP-002-PILOT-OP-001`.

Até lá:

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

Consequência:

> **P3-C continua HOLD.**

## 16. Transferência internacional

Não presumir ausência nem presença de transferência internacional.

Para cada operador real, registrar:

- país/região de armazenamento quando conhecido;
- subprocessadores relevantes;
- mecanismo contratual aplicável;
- necessidade de transferência;
- dado que efetivamente será enviado;
- controles de minimização/pseudonimização.

Até o operador ser escolhido:

```text
INTERNATIONAL TRANSFER STATUS
→ TBD PER OPERATOR
```

## 17. Retenção — classes definidas, prazos ainda não promovidos

As classes de retenção ficam definidas:

### R1 — contato e administração

Até o encerramento operacional + janela de direitos/follow-up definida.

### R2 — prova de consentimento e governança

Reter somente o mínimo necessário para demonstrar decisão, versão e status, pelo prazo juridicamente revisado.

### R3 — Research Base pseudonimizada

Durante execução, análise e auditoria metodológica do ciclo; depois submeter a revisão explícita de retenção/anonimização/exclusão.

### R4 — dados sensíveis incidentais não necessários

Não reter.

### R5 — logs técnicos

Reter apenas o período proporcional à finalidade de segurança/auditoria definida.

Os **prazos exatos** ainda dependem de operadores, necessidade operacional e revisão jurídica.

Consequência:

> **P3-D continua HOLD.**

## 18. Notice e instrumento de consentimento — requisitos mínimos

Antes de Participant 001, deve existir documento/instrumento que informe ao menos:

- controlador;
- canal de privacidade;
- natureza experimental do Dry Run;
- finalidades F1–F9 aplicáveis;
- categorias relevantes;
- voluntariedade;
- o que é opcional;
- gravação OFF por padrão;
- operadores/destinatários efetivamente usados;
- transferências relevantes;
- retenção;
- direitos;
- forma de revogação;
- consequências da revogação sobre continuidade no piloto;
- ausência de promessa de transformação;
- limites do Safety Gate;
- versão/data do instrumento.

## 19. Regra para revogação

```text
REVOGAÇÃO DO CONSENTIMENTO
→ interrompe novas operações sustentadas por consentimento
→ não deve gerar penalidade
→ aciona revisão de eliminação/anonimização
→ preserva somente o que possuir outra base legal válida e necessidade demonstrável
```

Nunca reinterpretar uma revogação como mero “desinteresse do usuário”.

## 20. Regra de não expansão de finalidade

Dados coletados no Dry Run não podem ser automaticamente reutilizados para:

- marketing;
- Ads;
- prospecção comercial;
- treinamento genérico de modelos;
- perfil comercial;
- venda de audiência;
- recomendação patrocinada;
- construção pública de caso individual.

Nova finalidade material exige avaliação própria de compatibilidade e base legal.

## 21. Critérios para promoção de P3

`P3` só pode chegar a `PASS` quando:

- [x] finalidades documentadas;
- [x] categorias documentadas;
- [x] política de dados sensíveis definida;
- [x] gravação definida;
- [ ] operadores/destinatários reais registrados;
- [ ] transferências internacionais reais registradas;
- [ ] prazos exatos de retenção aprovados;
- [ ] notice refletir o stack real.

Estado:

```text
P3
→ CONDITIONAL
```

## 22. Critérios para promoção de P4

`P4` só pode chegar a `PASS` quando:

- [x] hipóteses legais candidatas mapeadas;
- [x] base específica de órgão de pesquisa rejeitada para uso automático;
- [x] consentimento definido como candidato para o núcleo voluntário;
- [x] dados sensíveis excluídos do escopo normal;
- [ ] instrumento de notice/consentimento materializado;
- [ ] operadores reais refletidos no instrumento;
- [ ] retenção refletida;
- [ ] revisão jurídica/privacidade final realizada;
- [ ] versão autorizada congelada antes do primeiro participante.

Estado:

```text
P4
→ HOLD
```

## 23. Relação com P2C

O teste `P2C-SYN-001` permanece independente desta avaliação.

```text
P2B — CANAL
→ PASS

P2C — PROCESSO DE DIREITOS
→ HOLD ATÉ EVIDÊNCIA END-TO-END DO CASO SINTÉTICO
```

A existência do canal não prova o processo de direitos.

## 24. Próximos blockers

Ordem recomendada:

```text
1. fechar P2C-SYN-001
2. materializar notice + consentimento v0.1
3. definir stack real de ferramentas
4. registrar operadores / transferências / permissões
5. definir retenção exata por classe
6. revisar matriz P4 com operação real
7. executar revisão jurídica/privacidade final
8. repetir correction / limitation / deletion drill nos operadores reais
9. somente então avaliar liberação do Participant 001
```

## 25. Decisão

O piloto passa a possuir uma matriz explícita de finalidades, categorias e bases legais candidatas.

Isso reduz incerteza documental, mas **não libera coleta real**.

Checkpoint:

```text
P3
→ CONDITIONAL

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

A próxima autoridade jurídica deve derivar do stack real, do instrumento de transparência/consentimento e de revisão profissional aplicável — não de inferência documental.