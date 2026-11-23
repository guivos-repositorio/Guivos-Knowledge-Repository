---
id: GKR-LIVED-POSSIBILITIES-AUTHORITY-FLOW-CANDIDATE-001
title: Possibilidades Vividas — Contrato Funcional Candidato de Autoridade e Fluxos
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-22
normative: false
---

# G02 — Autoridade dos registros e fluxos

Contrato candidato exclusivamente documental para o futuro protótipo isolado, com dados sintéticos. Preserva UXA-057 e PAS-001; não adjudica esquema físico, API, serviço, nova superfície, cobertura real ou autorização de execução. Identificadores de teste abaixo não são IDs canônicos.

## 1. Objetos e autoridades

| Objeto | Responsabilidade | Limite |
|---|---|---|
| Oportunidade | Identidade, edição, unidade, etapa, período, nome e CAPA | Projeção não altera cadastro |
| Identidade oficial da Pessoa | Titularidade e identificação conforme escopo | Perfil público não autoriza vínculo com vivência |
| Registro de Experiência PAS-001 | Vivido efetivamente situado, contexto e proveniência | Avaliação não cria ou valida automaticamente experiência |
| R1 UXA-057 | Avaliação privada autoritativa, identidade lógica estável, versões, autoria, evidência e histórico material | Formulário, cache, projeção e confirmação visual não são R1 |
| P1 UXA-057 | Objeto público distinto, escopo autorizado, proveniência, estado e versão | Não contém automaticamente dados/evidência privados |
| Grafo de impacto | Projeção contextual autorizada de contribuições elegíveis | Não é autoridade privada ou pública de avaliação, nem trajetória individual |

Relacionar R1 ao objeto/edição/unidade/etapa/período vividos, autoria, papel, evidência e versão dos critérios; referência ao Registro de Experiência quando legitimamente estabelecida, sem exigir exposição da trajetória nem duplicar cadastro. Identidade lógica não depende de nome, foto, CAPA ou existência pública do objeto. Experiências materialmente distintas podem originar avaliações distintas; complemento, correção e mudança de visibilidade da mesma vivência não. A chave física e cardinalidades finais permanecem pendentes de adjudicação. No protótipo, usar referência sintética estável por pessoa e unidade avaliável, com discriminador de vivência quando necessário.

Instrumento de impacto e instrumento operacional são independentes sob autoridade comum; não fundir notas ou substituir critérios operacionais. O protótipo demonstra exclusivamente o módulo de impacto.

## 2. Elegibilidade e evidência

Manter as categorias da autoridade: verificada pela Guivos, confirmada por responsável competente, declarada pela Pessoa, externa identificada, insuficiente/conflitante/revogada. Não tratá-las como equivalentes. Verificar relação suficiente, titularidade e escopo efetivamente vivido antes do envio; antes de projeção pública, revalidar evidência suficiente e autorização específica. Compra, inscrição e interesse não comprovam vivência posterior; etapa parcial e edição distinta são delimitadas. A Jornada pode preservar experiência pessoal ainda não suficientemente comprovada sem inclusão pública. Não usar selo de verificação sem evidência correspondente. Nenhuma categoria é universalmente admitida ou excluída por este contrato. Para testar, usar casos sintéticos explicitamente elegíveis, inelegíveis ou pendentes; não estabelecer política real de suficiência.

## 3. Fluxos lógicos e handoffs

| Origem | Destino funcional | Condição | Falha / retorno |
|---|---|---|---|
| Detalhe da oportunidade | Grafo público de impacto | Escopo contextual e P1/projeção legitimamente autorizados | Estado vazio/indisponível; não expor R1 |
| Solicitação pós-vivência ou acesso à oportunidade encerrada | Formulário R-A | Identificação, elegibilidade e escopo revalidados; participação voluntária | Recusar/adiar e retornar sem bloquear acesso; se inelegível, não submeter |
| Formulário | Revisão consciente | Respostas e contexto preservados; compartilhamento separado | Corrigir, voltar ou sair; sem publicação |
| Revisão | Submissão R1 | Ação inequívoca e revalidação | Falha distinta de confirmação; recuperar estado sem duplicar |
| R1 | Publicação P1 / projeção | Autoridade, escopo, evidência e autorização suficientes | R1 permanece protegido; sem exposição por falha |
| Minhas Avaliações | Continuidade R-B | Titularidade e política aplicável | Consulta independente da página original; indisponibilidade não autoriza acesso de terceiros |
| R-B | Complementação/retificação ou visibilidade | Mesma identidade lógica e versão; revisão e revalidação | Preservar última versão legítima; não sobrescrever silenciosamente |
| R-C/R-D | Resposta, contestação, moderação/recurso | Competência, objeto/edição, independência e proteção | Sem edição da avaliação pelo ofertador; sem revelar identidade protegida |

PER-203 e PER-103 são candidatos à exibição contextual somente mediante extensão expressa; PER-009 não recebe R-A/R-B por analogia. Não adjudicar SURF/TRN. Preservar canais autorizados de convite e autoridade da Capacidade 07 — Intervenções Contextuais. No protótipo, simular entrada, retorno e eventos, sem envio real.

## 4. Estados e consistência

Separar três dimensões, sem reduzir a um status único:
- Captura privada: rascunho (se autorizado), em revisão pela autora, submissão pendente, confirmação, falha, atualização. Rascunho e tentativa não equivalem a R1 submetido.
- Publicação: não publicada, autorizada pendente, publicada, limitada, retirada/encerrada; estados candidatos de teste, não enumeração canônica.
- Governança: sem caso, contestada, em revisão, decisão/medida, recurso conforme autoridade. Contestação não implica retirada automática.

Enviar uma vez por intenção confirmada; repetição após timeout deve preservar a mesma identidade lógica e resultado quando já confirmado. Revalidar autoria, elegibilidade, escopo, versão e autorização antes de commit e projeção. Em conflito de versões, impedir sobrescrita silenciosa e permitir revisão. Confirmar separadamente registro privado e publicação; ausência de publicação não invalida avaliação privada. Atualização substitui projeção vigente autorizada sem contar duas vezes; retirada limita/remove derivados, preservando histórico apenas conforme finalidade e política. Cache, replay e restore não ressuscitam estado retirado. Falha de revalidação de publicação impede exposição do conteúdo afetado. Retenção/exclusão e evidência reais continuam sob autoridade competente.

## 5. Cenários de aceite documental e futuro teste

| ID local | Cenário sintético | Resultado esperado |
|---|---|---|
| G02-T01 | Pessoa apenas inscrita tenta avaliar vivência posterior | Não elegível para essa vivência; sem R1 de impacto submetido ou P1 |
| G02-T02 | Participação elegível e avaliação privada | R1 confirmado, nenhum P1 ou contribuição pública |
| G02-T03 | Publicação autorizada de conteúdo delimitado | P1/projeção contém somente campos permitidos; R1 não exposto |
| G02-T04 | Duas entradas para a mesma vivência, envio repetido após timeout | Uma identidade lógica, confirmação consistente |
| G02-T05 | Falha antes da confirmação | Não apresentar sucesso; permitir recuperação segura |
| G02-T06 | Complementação meses depois | Mesma identidade lógica, nova versão, sem duplicidade |
| G02-T07 | Outra edição ou vivência materialmente distinta | Registro distinto quando elegível, escopo não misturado |
| G02-T08 | Oportunidade retirada do público | Autora consulta avaliação legítima conforme política; sem republicação |
| G02-T09 | Revogação da publicação ou evidência insuficiente/revogada | Revalidar e retirar/limitar projeção afetada; sem ressurreição |
| G02-T10 | Pessoa recusa convite | Acesso à oportunidade não bloqueado; não publicar |
| G02-T11 | Ofertador contesta crítica | Encaminhar R-C/R-D, sem editar avaliação ou descobrir identidade protegida |
| G02-T12 | Edição concorrente ou autorização alterada durante envio | Detectar conflito, revisar/revalidar; sem sobrescrita ou exposição indevida |
| G02-T13 | Visitante acessa grafo ou URL contextual | Somente projeção autorizada; sem R1 ou trajetória privada |
| G02-T14 | Alteração de nome/CAPA | Não altera identidade lógica, vivência ou histórico |
| G02-T15 | Dados de qualidade operacional disponíveis | Não entram em nós, métricas ou significados do grafo de impacto |

Cenários descritos, não executados. G03–G07 detalharão conteúdo, cálculo, identidade, privacidade e interação. G08 delimitará aplicação independente e integração compartilhada, com autorização expressa anterior à execução. Não escolher backend, tecnologia de integração ou armazenamento real.

## 6. Evidências documentais e limites

Fontes confrontadas na branch candidata: [autoridade UXA-057](../experience-architecture/evaluation-reputation-authority.md) v1.1.0 SHA c5bc6f159ce2dc37fe0a8765221e7adf5805aa31; [adjudicação R-A..R-D](../experience-architecture/evaluation-reputation-surface-responsibility-adjudication.md) v1.0.0 SHA ca682d54b0afdb12f75b341d568c30742014f716; [PAS-001 Experiências](../product-architecture/pas-001-experiencias-fundamentos-iniciais.md) v1.0.0 SHA 97e4a0bedf259cd7ae6a5451e5aeac3207bbda39; [Captura](evaluation-capture-and-lifecycle.md), [Mestre](index.md) e [Prontidão](replit-prototype-readiness.md). Exame focal, não validação jurídica, técnica ou exaustiva. Pendências de produção explícitas: cobertura real, categorias por objeto, esquema/cardinalidade, superfícies e transições, contratos de acesso, segurança, retenção, publicação, integração e governança. Aceite humano do contrato candidato ainda necessário. Nenhuma execução Replit.
