---
id: GKR-LIVED-POSSIBILITIES-PRIVACY-ACCEPTANCE-CANDIDATE-001
title: Possibilidades Vividas — G06 Contrato Candidato de Privacidade e Compartilhamento
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-22
normative: false
---

# G06 — Privacidade, compartilhamento e prova de autorização

Especificação **documental candidata** para exame humano, confrontada com [Governança de Dados e Consentimentos](../governance-framework/data-privacy-and-consent-governance.md), [UXA-057](../experience-architecture/evaluation-reputation-authority.md), [G02](authority-and-flow-contract-candidate.md), [G03](evaluation-instrument-acceptance-candidate.md), [G04](graph-projection-and-counting-acceptance-candidate.md) e [G05](identity-media-and-cover-acceptance-candidate.md). Não constitui parecer jurídico nem autorização para publicar, integrar ou implementar.

## 1. Distinções essenciais

**R1 privado** é o registro autoritativo de avaliação; **P1** é publicação distinta condicionada à autoridade suficiente; **grafo** é projeção de manifestações elegíveis e legitimamente divulgáveis, não novo repositório autoritativo. Diferenciar: existência do registro; contribuição para agrupamentos; identificação contextual; fotografia; vínculo Pessoa–manifestação; acesso ao perfil; relato textual; relevância e natureza individuais. Uma escolha não autoriza automaticamente as outras.

Três modalidades aprovadas conceitualmente:
1. **Somente para mim:** avaliação privada; sem contribuição pública.
2. **Contribuir sem identificação pública:** apenas agregação legitimamente autorizada, com tratamento contra reidentificação; não prometer anonimato técnico/jurídico absoluto.
3. **Compartilhar minha participação:** eventual identificação pública da relação com a oportunidade, **somente** dentro de escopos autorizados, com controles independentes para foto, perfil, relato e eixos individuais.

É possível modificar preferências depois, respeitando autoridades, direitos e efeitos legítimos sobre derivados. Não punir recusa, não bloquear acesso a oportunidades ou à própria avaliação e não impor exposição como condição de pertencimento.

## 2. Diretriz de prioridade e conflito de pré-seleção

A Direção solicitou que **“Compartilhar minha participação” seja a primeira opção e venha marcada inicialmente**, deixando alternativa contrária à alteração manual. Preservar a **prioridade visual da primeira opção**, mas distinguir claramente **destaque, seleção de interface e autorização efetiva**.

**Gate jurídico-funcional aberto:** a pré-seleção sem ação afirmativa pode não constituir consentimento livre, informado e inequívoco quando essa for a base jurídica aplicável. Ela não deve ser tomada como permissão de identificação, fotografia, vínculo identificável, relato, perfil ou tratamento que exija consentimento. A mera falta de oposição, desmarcação ou leitura não gera P1 ou autorização de agregação por esta especificação. A base jurídica de cada tratamento deve ser determinada pela autoridade competente; consentimento não é rótulo universal.

**Alternativa candidata para preservar a intenção da Direção:** apresentar “Compartilhar minha participação” sempre em primeiro lugar, com destaque informativo, **sem seleção operante prévia** onde houver consentimento exigível; requerer ação afirmativa específica na etapa de compartilhamento e registrar a decisão. Uma escolha válida previamente feita pela própria Pessoa pode ser reapresentada conforme sua vigência e finalidade, nunca reativada por padrão após retirada. Para protótipo sintético, simular a opção visual prioritária e o fluxo de confirmação, sem atribuir a pré-marcação efeito de publicação.

Não fixar mecanismo operacional definitivo, base jurídica, tipo de controle UI, texto legal ou presunção de validade por esta proposta. A pré-seleção solicitada segue **não aprovada como autorização automática**. Requer adjudicação específica antes de qualquer uso real.

## 3. Matriz de escopos e projeção

| Finalidade/contexto | Autoridade/controle distinto | Sem autorização ou sem base suficiente |
|---|---|---|
| Avaliação privada | R1 e tratamento legítimo para registro/continuidade | Não atribuir publicação |
| Agregação sem identificação pública | Base jurídica/finalidade, escolha aplicável, evidência e proteção | Não incluir na projeção agregada |
| Identificação da Pessoa | Escopo público contextual, titularidade e revalidação | Não divulgar nome, identificação ou vínculo dedutível |
| Fotografia no grafo | Direito de imagem e permissão/contexto de exposição próprios | Exibir alternativa neutra somente quando adequada e não reidentificável |
| Aresta Pessoa–manifestação | Autorização específica do vínculo contextual | Não criar ligação pública identificável |
| Navegação ao perfil | Perfil público acessível **e** autorização para ligação ao contexto | Omitir/desabilitar acesso, sem inferir contato permitido |
| Relato e aprofundamento | Escopo próprio do conteúdo, proteção de terceiros | Não publicar texto ou detalhamento |
| Relevância/impacto individuais | Divulgação específica de eixos | Não mostrar eixos individuais, mesmo com agregado autorizado |
| Consumo por Analytics/Business/AI | Finalidade e base próprias, minimização e contrato de consumidor | Nenhum consumo irrestrito por analogia |

Mudança para perfil privado invalida navegação pública, não determina sem exame o estado de permissões independentes. Retirada da fotografia invalida somente esse ativo, salvo dependências materiais; retirada da identificação exige remover também links, etiquetas e arestas reidentificáveis. Retirada de agregação afeta conjuntos e denominadores do G04, sem ressurgimento por caches.

## 4. Proteção contra reidentificação, contextos sensíveis e terceiros

Uma “contribuição anônima” na UX pode permanecer dado pessoal sob LGPD quando houver identificador interno ou possibilidade de associação; preferir, na especificação operacional, expressão **“sem identificação pública”** e evitar promessa absoluta de anonimato. Testar reidentificação por grupo pequeno, manifestação rara, coocorrências, edições, períodos, fotografias, relato livre, ligações a perfis, consultas sucessivas e comparação antes/depois de retirada. Suprimir, generalizar ou impedir detalhamento conforme critérios que a autoridade de proteção estabelecer; **não fixar números mágicos** e não mostrar ausência falsamente como zero.

Não tornar públicos dados de terceiros citados em relatos, participação em contextos especialmente sensíveis, dados de crianças/adolescentes, atributos inferidos, localização precisa, situação financeira ou religião sem exame especializado de necessidade/base/risco. Não usar avaliações para direcionamento comercial nem acesso de ofertador à identidade protegida por analogia. Salvaguardas específicas para menores, moderação e direitos permanecem pendentes de adjudicação.

## 5. Evidência, versionamento, direitos e retenção

Uma eventual autorização válida precisa poder ser auditada pelo escopo e pela finalidade: identidade do titular na medida necessária, versão da informação apresentada, contexto/objeto/edição, data/hora, ação afirmativa quando exigida, meio, prova, estado, revisão/retirada, finalidade e efeitos nos derivados. **Registro de preferência ≠ consentimento juridicamente necessário ≠ publicação efetuada.** Separar gestão de consentimento, requisitos de contrato e escolha de exibição.

O registro privado e seus dados derivados não têm retenção indefinida; finalidade, período, minimização, exclusão, restrição, versionamento, segurança e transferências deverão ser examinados no inventário de atividades de tratamento. A retirada de um elemento público não pode ser silenciosamente revertida por backup, replay, cache, reindexação ou mudança de versão. Resposta/contestação/moderação preservam a identidade e não permitem retaliação.

## 6. Cenários de aceite documental e futuro teste sintético

| ID local | Cenário | Resultado esperado |
|---|---|---|
| G06-T01 | Avaliação concluída sem decisão pública válida | R1 protegido; P1 não criado automaticamente |
| G06-T02 | “Compartilhar” apresentado em primeiro lugar e destacado | Ordem preservada; não confundir destaque com autorização válida |
| G06-T03 | Opção vem pré-marcada e Pessoa não age | Nenhum consentimento inferido por inação; sem publicação dependente dele |
| G06-T04 | Pessoa confirma autorização específica válida após informação adequada | Registrar prova contextual e limitar projeção ao escopo confirmado |
| G06-T05 | Pessoa opta por “Somente para mim” | Sem projeção pública; acesso legítimo à própria avaliação permanece |
| G06-T06 | Pessoa permite apenas contribuição sem identificação pública | Agregação protegida sem pessoa, foto ou vínculo identificável |
| G06-T07 | Pessoa autoriza identificação mas não foto | Exibir apenas campos identificáveis legitimamente permitidos |
| G06-T08 | Pessoa permite foto mas não navegação ao perfil | Sem link ao perfil; foto depende de autorização própria e demais controles |
| G06-T09 | Pessoa permite perfil mas não vínculo contextual | Não inferir que o perfil público autoriza revelar a vivência |
| G06-T10 | Pessoa autoriza relato mas não eixos individuais | Relato permitido conforme escopo, eixos individuais ocultos |
| G06-T11 | Pessoa revisa escolhas já manifestadas | Preservar escolhas atuais válidas, sem restabelecer defaults anteriores |
| G06-T12 | Pessoa retira identificação, mantém agregado | Remover nome, foto e vínculos reidentificáveis; recalcular exposição |
| G06-T13 | Pessoa retira autorização de agregação | Atualizar nós, contagens, derivados e impedir ressurgimento |
| G06-T14 | Grupo pequeno ou relato único permite inferência | Suprimir/agrupamento conforme política sem falsa contagem zero |
| G06-T15 | Sucessivas consultas revelariam identidade protegida | Impedir inferência por combinação, versão ou comparação |
| G06-T16 | Perfil torna-se privado | Desabilitar navegação; revalidar autorizações dependentes |
| G06-T17 | Conteúdo menciona terceiro identificável | Não publicar dados de terceiro sem base/autorização aplicável |
| G06-T18 | Oportunidade envolve menores ou contexto sensível | Exigir tratamento especializado; sem exposição automática |
| G06-T19 | Oferta comercial/Analytics solicita dados individuais | Negar acesso por analogia; somente contrato e base próprios |
| G06-T20 | Operador restaura cache após retirada | Não ressuscitar informação pública revogada |
| G06-T21 | Pessoa recusa publicação | Não bloquear a avaliação ou a navegação normal |
| G06-T22 | Protótipo isolado usa identidades sintéticas | Sem dados pessoais reais, integrações reais ou publicação |
| G06-T23 | Base jurídica de tratamento não é consentimento | Não rotular genericamente como consentimento; documentar finalidade e hipótese competente |
| G06-T24 | Alteração da versão do texto de autorização | Preservar proveniência; revalidar decisões quando necessário |

Os 24 cenários foram **especificados, não executados**.

## 7. Bloqueios, decisão proposta e limites

**G06 pode receber aceite documental somente como contrato candidato com ressalva expressa**: a ordem e a prioridade visual de compartilhar são aprovadas como direção; a pré-marcação com efeito de opt-out ou autorização automática não é permitida por inferência. O comportamento de publicação real requer definição jurídica por atividade de tratamento, base aplicável, evidência de ação afirmativa quando necessária, dependências entre permissões, limiares de proteção e autorizações competentes. Nenhum controle foi implementado.

Recomendação para próxima deliberação: aprovar que **compartilhar continue sendo a primeira opção, sem transformar marcação inicial ou silêncio em autorização**, mantendo a seleção operacional subordinada à ação válida e aos requisitos da base jurídica. A Direção poderá revisar a preferência visual após observar o futuro protótipo sintético, mas isso não elimina o gate de legalidade. Se a Direção exigir que o controle já esteja selecionado, isso poderá ser representado em simulação sem efeito de publicação; não pode validar juridicamente um opt-out por simples ausência de oposição.

**Estado G06:** contrato documental candidato e 24 cenários disponíveis para aceite humano; autorização real, privacidade operacional, análise jurídica específica, limiares, políticas e implementação permanecem pendentes. Proibição explícita de avançar ao Replit sem autorização posterior.
