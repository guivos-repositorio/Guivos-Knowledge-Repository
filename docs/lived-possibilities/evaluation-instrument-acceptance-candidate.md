---
id: GKR-LIVED-POSSIBILITIES-INSTRUMENT-ACCEPTANCE-CANDIDATE-001
title: Possibilidades Vividas — G03 Contrato Candidato do Instrumento e Critérios de Aceite
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-22
normative: false
---

# G03 — Instrumento de avaliação e critérios de aceite

Especificação documental candidata, fundada no [instrumento conceitual](evaluation-capture-and-lifecycle.md) e no [G02](authority-and-flow-contract-candidate.md), para posterior protótipo isolado com dados sintéticos. Nenhuma questão, opção, inferência ou permissão aqui constitui alteração automática do canon UXA-057, publicação, implementação ou teste executado.

## 1. Estrutura da experiência de captura

Sequência: contexto autorizado da vivência → significado (dois eixos separados) → expressões universais e texto livre → aprofundamento opcional → resumo para revisão e correção → controles granulares de compartilhamento → confirmação inequívoca do registro privado → eventual publicação somente sob autoridade específica.

O formulário independente não exibe o grafo público, contagens ou percentuais de terceiros durante a captura; isso não impede que a pessoa já tenha visto o grafo na descoberta. A pessoa deve poder interromper, não responder, pular aprofundamentos e recusar divulgação sem penalidade. Não presumir que omissão seja escolha por impacto neutro.

### 1.1 Eixo A — relevância

Pergunta: **Quanto essa experiência representou para você?**

Opções de trabalho (uma resposta, quando declarada):
1. Nada significativo
2. Pouco significativo
3. Moderadamente significativo
4. Muito significativo
5. Extremamente significativo
6. Ainda não sei dizer

A sexta opção é incerteza, não sexto grau de relevância. **Sem resposta** é estado distinto; não preencher implicitamente. Não inferir relevância pelo número de expressões, extensão do relato ou sentimento.

### 1.2 Eixo B — natureza do impacto

Pergunta: **Como essa experiência impactou você?**

Opções de trabalho (uma resposta, quando declarada):
1. Positivamente
2. Negativamente
3. De forma positiva e negativa
4. Não percebi impacto
5. Ainda não sei dizer

Distinguir estado **sem resposta** de ausência de impacto e incerteza. Não derivar B de A, nem supor efeito favorável quando a experiência for muito significativa. Não transformar escala em nota de reputação.

### 1.3 Expressões e texto livre

Pergunta: **O que essa experiência representou para você?** Permitir múltiplas expressões, nenhum item, texto livre opcional e perspectivas distintas ou contraditórias. Preservar a declaração literal, autoria e versão; quaisquer equivalências/agrupamentos são derivados e governados, nunca substituição silenciosa.

Estrutura candidata: dimensão interna → família semântica → expressão universal → expressão contextual, com vínculos múltiplos possíveis. As quatro dimensões são percepção, contribuição, evolução e potencial, não quatro perguntas obrigatórias. Famílias iniciais: Inspiração, Conhecimento, Desenvolvimento, Reflexão, Bem-estar, Superação, Pertencimento, Descoberta, Continuidade, Desconforto, Frustração, Indiferença. A lista inicial não é taxonomia definitiva. Em especial, **indiferença**, **ausência de contribuição**, **não percebi impacto**, **incerteza** e **sem resposta** não são equivalentes; não agrupar automaticamente sem exame semântico.

Não apresentar frequência ou popularidade das expressões durante o preenchimento, evitar indução por ordenação e linguagem; ordem, componentes e tradução final requerem validação. AI pode sugerir agrupamentos a revisar, nunca inventar relato pessoal ou incluir nova família automaticamente.

## 2. Aprofundamento contextual

Inicialmente apresentar até três perguntas opcionais relevantes ao conteúdo declarado, sem repetição e sem obrigar divulgação. A pessoa poderá aprofundar voluntariamente após o conjunto inicial ou encerrar. Exemplos não normativos:
- “Aprendi algo novo” → “O que você aprendeu?”
- “Me motivou” → “O que despertou sua motivação?”
- “Descobri novas possibilidades” → “Quais possibilidades você descobriu?”
- “Me decepcionou” → “O que provocou essa percepção?”

Se a pessoa declarar impacto negativo, misto, neutro ou incerto, não induzir conversão em aprendizado, benefício ou evolução. Não repetir informação já expressa ou impor categoria/área. Perguntas adaptativas devem ter origem rastreável; respostas são sempre da pessoa. A natureza do aprofundamento não altera automaticamente os eixos de relevância/impacto.

## 3. Revisão, envio, continuidade

Antes da submissão, apresentar resumo fiel e editável dos dois eixos, expressões e relatos. Separar os controles de agregação, exposição da identidade, foto, vínculo à manifestação, acesso ao perfil, relatos públicos e eventual exposição de eixos individuais; não considerar aceitação de uma permissão como autorização de todas. A opção de compartilhar em primeiro lugar e marcada é **preferência de interface solicitada**, sob gate G06: não configura autorização válida automática, não publica por silêncio e não substitui manifestação afirmativa quando consentimento for exigido. Não escolher default operacional de publicação nesta etapa.

Submeter R1 com confirmação inequívoca e idempotência segundo G02; publicação P1 e projeção são eventos/autoridades distintos. Falha não pode parecer sucesso. Revisar a mesma avaliação após semanas, meses ou anos sem recomeçar ou duplicar, distinguindo data da vivência, reconhecimento, registro, retificação e publicação. Resguardar autoria, versões, retirada e retenção conforme autoridade. Convite posterior opcional depende da competência de Intervenções Contextuais, não de disparo autônomo deste instrumento.

## 4. Cenários de aceite documental e futuro teste sintético

| ID local | Cenário | Resultado esperado |
|---|---|---|
| G03-T01 | Relevância “Muito significativo” e impacto negativo | Duas respostas preservadas independentemente; sem inferência favorável |
| G03-T02 | Relevância incerta e natureza mista | Incerteza não vira intensidade; manifestação mista aceita |
| G03-T03 | “Não percebi impacto” | Não converter em “não respondeu” nem em família Indiferença automaticamente |
| G03-T04 | Eixo omitido | Persistir ausência como ausência, sem preencher grau ou natureza |
| G03-T05 | Múltiplas expressões positivas e negativas | Preservar todas sem resolver contradição automaticamente |
| G03-T06 | Texto livre com expressão fora da base | Manter literal original, sem inventar família definitiva |
| G03-T07 | Expressão compatível com múltiplas dimensões | Vínculo interno múltiplo sem pedir à pessoa para classificar áreas |
| G03-T08 | Aprofundamento pertinente | Até três perguntas iniciais opcionais, sem repetir respostas |
| G03-T09 | Sem interesse em aprofundar | Permitir encerrar a avaliação |
| G03-T10 | Impacto negativo ou misto | Pergunta não sugere que a pessoa necessariamente evoluiu |
| G03-T11 | Revisão antes do envio | Resumo editável e correção sem perda de autoria |
| G03-T12 | Compartilhamento recusado | R1 privado preservado; sem publicação ou penalidade |
| G03-T13 | Compartilhamento em primeira posição, inicialmente marcado | Simular prioridade visual, mas não inferir autorização jurídica pela inação; G06 governa decisão |
| G03-T14 | Foto ou perfil não autorizado | Ausência desses campos na projeção, mesmo com agregação autorizada |
| G03-T15 | Atualização voluntária posterior | Mesma identidade R1, versão, datas e manifestação preservadas |
| G03-T16 | Tentativa de envio com falha/duplicação | Não inventar confirmação nem criar segundo registro |
| G03-T17 | Formulário depois de consultar grafo na descoberta | Formulário não mostra contagens ou influência social durante o preenchimento |
| G03-T18 | Sugestão de nova expressão por AI | Sem adoção automática ou atribuição textual à pessoa |
| G03-T19 | Não aplicável, insuficiência de informação, neutralidade | Manter distinções e pertinência por pergunta/critério, sem misturar instrumento operacional |
| G03-T20 | Formulário de qualidade operacional disponível no mesmo ecossistema | Não incorporar seus critérios nem notas ao instrumento/grafo de impacto |

Cenários especificados, não executados. Resultados requerem testes futuros apenas após autorização expressa de Replit.

## 5. Pendências de validação e limites

Requerem validação posterior: compreensão da escala verbal, opção “Nada significativo” frente a “Não percebi impacto”, semântica e neutralidade das doze famílias, estabilidade intercultural e i18n, acessibilidade, número e ordem de opções, não resposta e eventual “não se aplica” por pertinência, critérios definitivos de obrigatoriedade, linguagem de compartilhamento e preferência de pré-marcação sob G06. A proposta não atribui pesos, nota, ranking, score ou diagnóstico à pessoa.

**Estado G03:** especificação documental e 20 cenários disponíveis para aceite humano. Não equivale à aprovação empírica da taxonomia, consentimento, contrato técnico, testes executados ou maturidade para produção. Sem Replit, publicação, merge, alterações do main ou tratamento de dados reais.
