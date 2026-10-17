---
id: GKR-UX-GLOBAL-FOOTER-FTR02-001
title: Rodapé Global — Inventário de Destinos e Links FTR-02
status: proposed
version: 0.1.3
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
scope: footer-link-evidence
depends_on:
  - GKR-UX-GLOBAL-FOOTER-001
  - GKR-UX-GLOBAL-FOOTER-SURFACE-001
  - GKR-UX-GLOBAL-FOOTER-FTR-TRACKER-001
---

# Rodapé Global — Inventário FTR-02 de Destinos e Links

## 1. Objetivo e precedência

Este inventário reúne **os rótulos aprovados no desenho do Rodapé Institucional Global** e seus destinos ainda sujeitos a confirmação. Não é um mapa de rotas implementadas. A [referência visual oficial](global-institutional-footer.md) v1.0.0 prevalece sobre textos, ordem de colunas, assinatura e identidade. A [arquitetura transversal candidata](global-footer-surface-candidate.md) v0.2.8 e o [quadro FTR](global-footer-ftr-control-board.md) v0.1.0 complementam o controle de responsabilidades.

**Regra fundamental:** um documento de produto, URL de protótipo, link do MENU do GKR, conta social homônima, slug sugerido, link no cabeçalho ou screenshot **não comprovam** que um destino público oficial está disponível. A aprovação do rótulo é independente da verificação de `URL + titularidade + conteúdo + publicação + comportamento`.

**Leitura dos estados:**
- `LABEL_APPROVED / DESTINATION_NOT_VERIFIED`: nome consta da referência visual; destino operacional sem evidência de aprovação e teste nesta auditoria.
- `ARCHITECTURE_ACCEPTED / DESTINATION_NOT_DEFINED`: obrigação funcional do link Mapa do Ecossistema e posição aceitas, mas página não definida.
- `CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED`: ícone previsto visualmente, identidade e endereço da conta oficial não comprovados.
- `FEATURE_VISUAL_ONLY`: área ou ação representada visualmente, integração não comprovada.

Nenhum item deste inventário recebe `VERIFIED_FOR_PRODUCTION`.

## 2. Destinos de exploração do ecossistema

| Item e ordem do rodapé | Proveniência do rótulo | URL pública verificada para este destino | Estado FTR-02 |
|---|---|---|---|
| 01. Pessoa e Journey | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 02. Organizações e Coletivos | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 03. Mall | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 04. Travel | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 05. Business | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 06. Media | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 07. Intelligence | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 08. Ads | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| 09. Mapa do Ecossistema | Home Pessoa §31; FTR-01/D1 posicionou-o após os oito destinos | Destino e arquitetura da página ainda não definidos | ARCHITECTURE_ACCEPTED / DESTINATION_NOT_DEFINED |

**Fronteira de implementação:** a inspeção secundária do Replit documentada em FTR-03 identificou rotas internas `/pessoa` e `/organizacoes-coletivos`, mas relatou que os respectivos endereços públicos testados não renderizavam as Homes. Isso **não qualifica** os dois destinos como URLs públicas aprovadas para o rodapé, nem autoriza inventar rotas para as outras seis Homes. O link `Mapa` observado no cabeçalho não substitui o destino `Mapa do Ecossistema`.

## 3. Coluna institucional Guivos

| Item | Evidência de conteúdo | URL pública oficial verificada | Estado FTR-02 |
|---|---|---|---|
| Sobre a Guivos | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| Comunidade | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| Carreiras | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |
| Imprensa | Rodapé oficial §3 | Não verificada | LABEL_APPROVED / DESTINATION_NOT_VERIFIED |

**Nota:** informação institucional nos documentos internos do GKR não equivale a página institucional pública da Guivos. Não encaminhar pessoas ao repositório como substituto presumido de `Sobre a Guivos`.

## 4. Coluna Ajuda e faixa jurídica

| Item | Local previsto | URL oficial verificada | Dependência específica |
|---|---|---|---|
| Central de Ajuda | Ajuda | Não verificada | Serviço/canal real e responsável |
| Fale conosco | Ajuda | Não verificada | Canal oficial, destinatário e disponibilidade |
| Privacidade | Ajuda | Não verificada | Destino e validação Legal/Privacidade |
| Termos de Uso | Ajuda | Não verificada | Destino e validação Legal |
| Acessibilidade | Ajuda | Não verificada | Informação/canal real, revisão de Acessibilidade |
| Política de Privacidade | Faixa inferior | Não verificada | URL, versão publicada e revisão Legal/Privacidade |
| Termos de Uso | Faixa inferior | Não verificada | URL, versão publicada e revisão Legal |

O mesmo assunto em `Ajuda` e na faixa inferior **pode** compartilhar destino após decisão competente, mas a duplicidade editorial não deve ser removida nem convertida automaticamente em links funcionais. Dados e menções jurídicos da referência devem ser validados por seu responsável para uso em produção (FTR-04).

## 5. Redes e canais exibidos

| Ícone da referência visual, na ordem | URL e titularidade oficial comprovadas nesta auditoria | Estado |
|---|---|---|
| Instagram | Não | CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED |
| YouTube | Não | CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED |
| LinkedIn | Não | CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED |
| X | Não | CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED |
| TikTok | Não | CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED |
| Spotify | Não | CHANNEL_SHOWN / OFFICIAL_ACCOUNT_NOT_VERIFIED |

Identidade de conta não pode ser atribuída apenas por semelhança com o nome `Guivos`; confirmar controle/titularidade, conteúdo, localização pretendida e comportamento de abertura antes de incluir href.

## 6. Controles que não são simples destinos

| Área | Aparência validada / decisão de referência | Evidência de integração real | Estado |
|---|---|---|---|
| Receba novidades — campo de e-mail e botão | Bloco visual e copy aprovados | Captura, consentimento, persistência, feedback e cancelamento não verificados | FEATURE_VISUAL_ONLY — FTR-04/06/07 |
| Obter o app — botões das lojas | Iteração visual posterior mencionada, não comprovada neste registro como atualização da referência normativa de 14/10 | URLs oficiais das lojas não verificadas | CANDIDATE_LATER_VISUAL — NOT_VERIFIED |
| Obter o app — QR Code | Exige fonte oficial; um QR ilustrativo não comprova destino | URL/app oficial, conteúdo decodificado e teste não verificados | CANDIDATE_LATER_VISUAL — NOT_VERIFIED |
| Idioma/região | Só quando suportado pela aplicação e mercado | Controles e localização reais não comprovados | NOT_AUTHORIZED_AS_WORKING |

Esses controles não devem ser publicados como funcionais em virtude de sua mera representação na referência visual ou em protótipo.

## 7. Evidência necessária para promover cada destino

Antes de autorizar cada link, registrar **uma linha por destino**, com: (1) rótulo e grupo; (2) URL exata canônica; (3) tipo de destino — próprio, externo, serviço de suporte ou jurídico; (4) responsável funcional pelo conteúdo e sua aprovação; (5) titularidade para canais sociais; (6) escopo/mercado/idioma; (7) teste de abertura e retorno sem redirecionamento enganoso, datado e com evidência; (8) situação de disponibilidade e tratamento se indisponível; (9) revisão jurídica e privacidade quando pertinente; (10) decisão e versão de publicação.

Para o **Mapa do Ecossistema** há condição adicional: ratificação da arquitetura/conteúdo da página, endereço real e decisão de apresentação do rótulo antes da liberação do destino. A posição editorial definida em FTR-01/D1 **não encerra FTR-02**.

### Regra para ausência de destino

**Na documentação/protótipo:** pode haver rótulo claramente informativo ou representação de demonstração, **sem** link falso (`#`, URL vazia, página de erro) e sem indicação de funcionalidade ativa.

**Na produção:** não publicar link clicável sem destino legítimo verificado. A decisão de manter item informativo sem link, adiar sua exibição ou encontrar alternativa legítima exige aprovação da arquitetura/navegação e verificação de compatibilidade com a referência oficial. Não inventar páginas ou mensagens de disponibilidade.

## 8. Estado de conclusão

**Inventário editorial levantado:**
- 9 itens do grupo `Explore o ecossistema` (8 destinos da imagem + `Mapa do Ecossistema` contratado na arquitetura);
- 4 itens institucionais;
- 5 itens na coluna `Ajuda`;
- 2 ocorrências jurídicas na faixa inferior;
- 6 ícones sociais;
- controles de novidades e eventual acesso ao app tratados separadamente.

**O inventário não corresponde a links já implementados.** Nesta revisão, `VERIFIED_FOR_PRODUCTION = 0` no escopo dos destinos acima; isto significa **nenhuma evidência suficiente reunida para aprovação de produção**, e não ausência universal de sites, páginas, perfis ou serviços da Guivos.

`FTR-02 = INVENTORY_DOCUMENTED / DESTINATIONS_NOT_VERIFIED / GATE_OPEN`. FTR-04 continua independente para dados legais, avisos e consentimento. FTR-06..08 não podem ser presumidos a partir deste levantamento.

## 9. Evidências públicas adicionais encontradas em 16/10/2026 — domínios candidatos

**Natureza da evidência:** resultados de indexação web pública, não comprovação de titularidade técnica/registral, ambiente de produção atual, disponibilidade por acesso externo direto ou aderência à arquitetura corrente das oito Homes. A tentativa de acesso direto pelo mecanismo de consulta retornou falha (502), portanto **não ocorreu teste HTTP bem-sucedido dessas páginas nesta revisão**.

| Endereço observado na indexação | Conteúdo público indexado e correlação | O que ainda falta | Estado |
|---|---|---|---|
| [https://www.guivos.com/](https://www.guivos.com/) | Uso da marca Guivos, navegação para viagens/compras, bloco de app/comunidade e identificação jurídica reproduzida na referência institucional do rodapé | Confirmar titularidade, domínio canônico pretendido, versão atual do conteúdo, rotas públicas do ecossistema corrente e testes de acesso; não presumir que a experiência indexada representa a HOME Pessoa aprovada | `PUBLIC_DOMAIN_CANDIDATE / NOT_APPROVED_FOR_FOOTER` |
| [https://guivos.us/](https://guivos.us/) | Uso da marca, serviços e informação institucional semelhantes aos encontrados no domínio anterior | Verificar controle do domínio, mercado/idioma, conteúdo vigente, relação oficial com o domínio principal, URLs individuais e aprovação de navegação | `PUBLIC_DOMAIN_CANDIDATE / NOT_APPROVED_FOR_FOOTER` |
| [https://guivos.us/dashboard/guivos_empresas](https://guivos.us/dashboard/guivos_empresas) | Página empresarial indexada com discurso de programa de recompensas e plataforma white-label | Validar atualização e autoridade do conteúdo perante os Masters do GKR, domínio e finalidade pública; **não** mapear automaticamente para a Home Guivos Business aprovada | `LEGACY_OR_CURRENT_UNDETERMINED / NOT_APPROVED_FOR_FOOTER` |

**Risco de divergência temporal:** a experiência indexada menciona pontos, catálogo e ofertas que podem não refletir a arquitetura/produtos e decisões documentais atuais. A correspondência da marca e de identificações textuais **não equivale a homologar o conteúdo**, assumir operação real de ofertas, legitimar URL de `Pessoa e Journey`, `Business`, `Mall`, `Travel` ou afirmar aplicativos disponíveis. Não remover nem alterar contratos econômicos, de pontos ou de produtos no GKR a partir dessa indexação.

**FTR-02 após nova pesquisa:** `PUBLIC_DOMAIN_CANDIDATES_IDENTIFIED = 2` (e uma rota empresarial indexada); `VERIFIED_FOR_PRODUCTION = 0`. O gate permanece `INVENTORY_DOCUMENTED / DESTINATIONS_NOT_VERIFIED / GATE_OPEN` até confirmação de domínio canônico, titularidade, publicação e mapeamento individual aprovado para os itens do rodapé.

**Próxima evidência exigida:** confirmação institucional dos domínios e da relação entre o site legado/indexado e as oito Homes; prova de URL e resposta atual por destino, com revisão de Produto, Brand e Legal nos pontos competentes. Nenhuma alteração no Replit ou em links de produto ocorreu nesta atualização.

## 10. Deliberação institucional — papel dos domínios (16/10/2026)

**Origem da decisão:** o fundador confirmou expressamente nesta conversa a proposta de estabelecer `guivos.com` como domínio global principal da nova Guivos e conservar `guivos.us` como opção de operação por país. A deliberação estabelece **papel arquitetural pretendido**, não comprovação de propriedade registral, disponibilidade de hospedagem, migração realizada, configuração de DNS, caminhos das oito Homes nem lançamento de operações territoriais.

| Domínio | Papel arquitetural aceito | Estado e limite |
|---|---|---|
| `guivos.com` | **Domínio global principal pretendido** para a nova arquitetura Guivos | `PRIMARY_GLOBAL_DOMAIN_ARCHITECTURE_ACCEPTED`; vínculo de titularidade, DNS, HTTPS, ambiente, conteúdo e links por Home ainda `NOT_VERIFIED` |
| `guivos.us` | **Domínio potencial de operação por país**, sujeito a decisão posterior de lançamento/mercado | `COUNTRY_DOMAIN_OPTION_ACCEPTED`; **não** equivale a operação ativa nos Estados Unidos, URL canônica alternativa já configurada ou redirecionamento autorizado |

**Decisão limitada FTR-02/D1 — DOMAIN_ROLE_ACCEPTED_SCOPED:** aprova a prioridade nominal e a posição arquitetural dos domínios. Não aprova caminhos como `/pessoa`, `/business`, `/mapa`, redirecionamentos, subdomínios, lojas de aplicativos ou qualquer href. A estratégia de domínios nacionais adicionais dependerá de decisão por país e não é instituída automaticamente neste registro.

**Implicações para o rodapé:** nenhum dos destinos editoriais recebe `VERIFIED_FOR_PRODUCTION` com esta deliberação. A implementação futura somente poderá vincular links a URLs reais após prova de titularidade/controle, versão atualizada do site, disponibilidade pública, mapeamento individual de rotas e aprovações funcionais (e jurídicas quando aplicáveis). Separar ambientes indexados legados da nova experiência, sem presumir que conteúdos antigos definem os Masters.

**Estado resultante:** `FTR-02/D1 = DOMAIN_ROLE_ACCEPTED_SCOPED`; `FTR-02 = DOMAIN_ROLE_DECIDED / DESTINATIONS_NOT_VERIFIED / GATE_OPEN`; `VERIFIED_FOR_PRODUCTION = 0` no conjunto inventariado. Nenhuma mudança técnica de domínio ou Replit foi executada.

## 11. Confirmação do fundador — registro dos domínios Guivos (16/10/2026)

**Fonte primária declaratória:** nesta conversa, o fundador confirmou expressamente: **“Os registros guivos.com e guivos.us, acima estão registrado conosco. Temos o registro já”.** Esta declaração passa a ser a fonte institucional para reconhecer o **registro dos dois domínios pela Guivos**, sem exigir nova pergunta sobre se os registros existem.

| Domínio | Registro — informação declarada pelo fundador | Papel arquitetural já decidido | Ainda sem comprovação técnica nesta revisão |
|---|---|---|---|
| `guivos.com` | `REGISTRATION_CONFIRMED_BY_FOUNDER` | Principal global da nova Guivos | Registrador, titular formal em RDAP, nameservers, DNS, certificado HTTPS, apontamento, ambiente, estado HTTP e rotas das Homes |
| `guivos.us` | `REGISTRATION_CONFIRMED_BY_FOUNDER` | Potencial domínio para operação por país | Registrador, titular formal em RDAP, nameservers, DNS, certificado HTTPS, apontamento, ambiente e decisão de lançamento por mercado |

**Distinção necessária:** a palavra do fundador constitui confirmação institucional de registro sob controle da Guivos para fins desta governança, **não** é documento registral externo, não prova configuração de DNS, hospedagem ou que os dois sites já exibem a versão nova. O GKR não deve continuar perguntando se os domínios foram registrados; quando necessário para um trabalho técnico específico, o comprovante registral, painel do provedor ou dados de zona DNS serão requisitados apenas para a respectiva finalidade.

**FTR-02/D2 — DOMAIN_REGISTRATION_CONFIRMED_BY_FOUNDER.** Mantém-se `FTR-02/D1 = DOMAIN_ROLE_ACCEPTED_SCOPED`. A confirmação atualiza o requisito de registro, mas **não** promove os destinos individuais do rodapé: `VERIFIED_FOR_PRODUCTION = 0` na matriz de links; `FTR-02 = DOMAIN_ROLE_AND_REGISTRATION_CONFIRMED / DESTINATIONS_NOT_VERIFIED / GATE_OPEN`.

Nenhum DNS, redirecionamento, URL de Home, QR, app, site ou Replit foi alterado por este registro.
