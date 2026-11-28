---
title: "Jornada da Pessoa — Oportunidades v1.3.0 — Proposta de reconciliação"
status: candidate
version: "1.3.0"
normative: false
last_updated: "2026-11-28"
---

# Oportunidades da Pessoa — proposta de reconciliação v1.3.0

## 1. Escopo e autoridade

Dossiê candidato das decisões de produto e reconciliações conceituais das etapas 18–28. Não substitui a Canon, não cria capacidade ou identificador oficial, não autoriza UXA-108, Design, Product Engineering, publicação, integração com dados reais, emissão de pontos ou concessão de selos. A versão 1.2.0 (80 RF, 18 RNF, oito movimentos) não foi recuperada integralmente para confronto individual; esta consolidação não declara cobertura integral nem substituição definitiva da versão anterior.

Base vigente: [Estado Atual](../../project/current-state-register.md) v3.51.17; [PAS-001](../../product-architecture/pas-001-guivos-journey.md); [Mapa de capacidades](../../product-architecture/pas-001-guivos-journey-mapa-final-capacidades.md); [Roadmap](../../roadmap.md); [PER-201](per-201-opportunity-map-master.md) v0.1.0; [PER-202](per-202-opportunity-list-master.md) v0.1.0; [PER-203](per-203-opportunity-detail-master.md) v0.1.1. O produto permanece em GE-2 Knowledge, M7.88; engenharia pausada/não liberada.

## 2. Descoberta contextual

Materializar a descoberta contextual já prevista na Capacidade 06, não criar nova autoridade. Identificar oportunidades reais, admissíveis e potencialmente relacionadas ao contexto autorizado, momento, trajetória, intenções e condições atuais/futuras. Descobrir além das intenções declaradas sem presumir interesse. Distinguir abertura futura confirmada/condicionada, oportunidade existente ainda inacessível e possibilidade ainda não materializada; a última não entra como oferta real. Reavaliar após mudanças de contexto, disponibilidade, localização autorizada ou oferta; manifestação proativa subordinada à Capacidade 07, inclusive silêncio. Contexto insuficiente permite busca manual e ordenação neutra. Ausência de resultado é legítima. Não ampliar consulta silenciosamente.

Autoridades preservadas, todas v1.0.0: [FOUNDATION](../../product-architecture/pas-001-oportunidades-ativas-fundamentos-iniciais.md) §§2081–2093, 2099–2101; [LIFECYCLE](../../product-architecture/pas-001-oportunidades-ativas-ciclo-de-vida.md) §2161; [VIEW](../../product-architecture/pas-001-oportunidades-ativas-visualizacao-controle.md) §§2255–2267; [EVENT](../../product-architecture/pas-001-oportunidades-ativas-eventos-funcionais.md); [INTEGRATION](../../product-architecture/pas-001-oportunidades-ativas-integracoes-funcionais.md); [CONTRACT](../../product-architecture/pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md) (75 KPIs, 15 famílias, 24 guardrails). Reutilizar contratos; reabrir apenas mediante adjudicação específica.

## 3. Navegação e composição propostas

Entrada única Oportunidades no menu da Jornada da Pessoa; nova aba preserva sessão e estado da origem. Não alterar Jornada existente antes de validação. Preservar PER-101..108, distinção entre atividades de coletivos e vínculo/participação no coletivo; acesso contextual definitivo ainda a definir.

Cards (PER-202) inicialmente; Mapa (PER-201); Detalhes (PER-203), mantendo estrutura superior e rodapé. Consulta compartilhada: busca, filtros, ordenação, seleção, resultados carregados, posição de scroll, região e zoom quando válidos. Revalidar mudanças materiais. Desktop: um card horizontal por linha, 10 iniciais, Ver mais acrescenta 10, sem scroll infinito. Mapa: lista compacta 30%, mapa 70%, rolagem independente da lista, seleção/hover e marcadores sincronizados, clusters, preço/gratuidade quando conhecidos, Buscar nesta região por ação consciente. Consulta geográfica não limitada aos dez cards; preservar identidade e filtros; oportunidades online acessíveis sem coordenadas fictícias. Localização opcional, região manual não equivale a residência, posição ou histórico. Alternativa textual acessível quando mapa indisponível.

Cabeçalho inspirado na Home Pessoa; referência Figma node 12136:801, validação visual pendente. Goldplay 400/500/600 conforme direitos; fallback Instrument Sans; fundo branco e Purple 1 #7D55C6 como direção de design aprovada, não baseline normativa universal. Responsividade desktop/tablet/mobile. Não exibir rótulos provisórios nem dados inventados em produção.

## 4. Filtros e ordenação

Rápidos: Domínios de Evolução, Ofertador (Todos/Organização/Coletivo/Profissional), Tipo (Todos/Convencional/Ao vivo), Modalidade (Todos/Presencial/Online/Híbrido). Taxonomia Tipo a reconciliar com classificação funcional vigente; Profissional já origem possível (§2083 FOUNDATION), não quarta categoria estrutural automaticamente.

Domínios canônicos JED-001..009: Saúde e Bem-estar; Trabalho, Carreira e Estudos; Vida Financeira; Empreendedorismo e Projetos; Relacionamentos e Vida Social; Espiritualidade, Propósito e Valores; Viagens, Lazer, Cultura e Novas Experiências; Causas, Voluntariado e Contribuição; Organização e Equilíbrio da Vida. Ainda estou descobrindo é estado transversal, não décimo domínio.

Painel completo (37 grupos propostos):
- Geral: domínios, ofertador, tipo, modalidade, preço/gratuidade, pontos, subsídios/benefícios, origem, patrocínio, relações comerciais/comissão.
- Localização: país, estado/região, cidade, distância, região pesquisada.
- Disponibilidade: período/datas, dias, horários, duração, disponibilidade futura, elegibilidade.
- Preferências: idioma, tradução/legendas, acessibilidade, salvos, riscos/condições, confiança da fonte.
- Meu contexto: momento atual, disponibilidade, condições financeiras, deslocamentos, intenções, trajetória, novas possibilidades, possibilidades futuras, objetivos, Próximos Passos.

Preço: gratuito/pago/faixa; pontos: todas/com incentivo/aceitam pontos quando autorizados. Permitir mostrar/ocultar patrocinadas e filtrar sem comissão; nenhuma informação desconhecida equivale a ausência de comissão. Identificar relações comerciais; não misturar publicidade com ordenação orgânica. Filtros rápidos imediatos, painel completo aplicação conjunta, seleção múltipla quando compatível, remoção individual; limpar filtros não desativa personalização. Controle de contexto independente, busca sensível protegida. Não presumir interesse, renda, residência ou intenção por filtro.

Ordenação inicial contextual explicável se houver base legítima; alternativas propostas: distância, datas, atualização, preço, acessibilidade, confiança da fonte. Avaliações e quantidade de pontos dependem de adjudicação específica, sem alterar relevância orgânica. Nenhum critério comercial, clique ou tempo de tela aumenta relevância. Patrocínio identificado e separado; não preencher ausência com anúncios.

## 5. Contexto, eventos e grafo

INTEGRATION §§2553, 2570–2573, 2591–2597: recortes mínimos de contexto autorizado, sem cópia integral, perfil comercial paralelo ou ciclos de auto-reforço. Guivos Intelligence avalia compatibilidade, Guivos AI apoia trajetórias/possibilidades, grafo representa relações governadas, não autoridade independente. [GIA](../../intelligence-architecture/index.md) é referência conceitual, não autorização de implementação física.

Reutilizar EVENT família 11: OportunidadeVisualizada, OportunidadeSalva, OportunidadeRemovidaDosSalvos, InteresseEmOportunidadeDeclarado, InteresseEmOportunidadeRetirado, OportunidadeDescartada, OportunidadeOcultada, LimitacaoDeOportunidadesSemelhantesRegistrada. Interesse exige manifestação inequívoca. Navegação/hover/mapa/filtro não confirma interesse, localização ou objetivo. Preservar declarada/observada/inferida/predita, evidência, fonte, autoridade, temporalidade, finalidade, permissões, sensibilidade, correlação, idempotência, sincronização, revogação propagada e falha segura. Contexto Vivo decide seus próprios efeitos; Experiências e Evolução Contínua avaliam evidências sob contratos próprios. Não definir schema físico, acesso direto ao Neo4j ou credenciais no navegador.

## 6. Detalhes, avaliações, reconhecimento e economia

Detalhes e fluxos visuais compartilhados pelo Card-Oportunidades: galeria, roteiro, condições, preço, ofertador, responsável/anfitrião, perfis, perguntas/respostas, avaliações, relatos, Possibilidades Vividas, serviços adicionais, cupom, subtotal/taxas/descontos/total. Não duplicar interfaces. Reconciliar oportunidade principal, edição/etapa, histórico e perfis com [PR #735](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/735), candidata, sem importar como Canon. Moderação Guivos, não aprovação obrigatória pelo ofertador/anfitrião, conforme proposta daquela PR; política e cobertura pendentes.

[Autoridade de Avaliação e Reputação](../evaluation-reputation-authority.md) v1.1.0 e [adjudicação de superfícies](../evaluation-reputation-surface-responsibility-adjudication.md) v1.0.0: R1 privado distinto de P1 público autorizado; R-A..R-D não atribuídas por analogia. PER-203 necessita extensão expressa para exibição pública; experiência/edição/etapa delimitada, elegibilidade, amostra, denominador, período, versão, verificação, privacidade e limites. Sem nota universal ou transferência automática entre edições/identidades. [Experiências](../../product-architecture/pas-001-experiencias-fundamentos-iniciais.md) §3425: expectativa, qualidade percebida, atendimento, segurança, utilidade, acessibilidade, adequação, resultado quando aplicáveis. [Evolução Contínua](../../product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md) §§3964–3968: satisfação, percepção, resultado e mudança sustentada distintos.

Possibilidades Vividas: percepções naturais, aprendizados, sentimentos e impactos relatados, inclusive negativos/neutros/ambivalentes/insuficientes; grafo e alternativa gráfica, fotos e links de perfis apenas com permissões específicas; não criar relações entre participantes sem autoridade; sem garantia de causalidade. Não confundir avaliação comercial, contribuição percebida e evolução reconhecida. [Selos — Reconhecimento e Reputação](../../economic-model/selos-guia-consulta.md): Verificado e Contribuição Reconhecida são direções de produto para Coletivos, concessão/exibição não autorizadas; [PR #654](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/654) preservada. PV pode futuramente subsidiar evidências, não conceder selos. Extensão a outros atores exige autoridade própria.

Preço principal, custo total, adicionais, condições, validade, moeda, cancelamento, risco e responsável pela cobrança verificáveis. Gratuito significa sem cobrança necessária ao acesso principal. PER-203 → TRN-212 → PER-204 somente processo interno legítimo; TRN-212..216 contratadas. PER-203 → TRN-205 → BND-001 mediante revisão consciente, finalidade, destino, dados, revalidação e cancelamento; BND-001 é fronteira, não tela. Não presumir conclusão externa. Carrinho/checkout são interfaces, não autoridade financeira; pagamento, inscrição, elegibilidade, participação, experiência e evolução distintos.

[Pontos — autoridade econômica](../../economic-model/points-economic-authority.md) v1.0.0: benefício não monetário, saldo unificado e lotes rastreáveis; não transferível/conversível/comprável por padrão; sem taxa Pontos↔BRL. FIN-COMPRA/FIN-EVENTO, PCT/FIX/RANK/CUSTOM, pagamento misto e destinos Mall/Travel são direções/propostas sujeitas aos contratos; [PR #655](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/655). Sem emissão, resgate, liquidação, preço ou percentual inventado. Incentivo opcional, sem compra de relevância. Operações reais bloqueadas.

## 7. Componentes e estado observado

Oportunidades: shell, consulta, mapa, seleção e navegação; Jornada: sessão/contexto; Card-Oportunidades: cards horizontal/compacto/geográfico, detalhes e fluxos visuais; Possibilidade-Vivida via Card; Footer-Rodape e Menu-Ecossistema compartilhados; Intelligence/AI/grafo: capacidades governadas. Fonte única de manutenção por componente; versões compatíveis propagadas sem reconstrução manual; atualização segura, sem ampliar autorização, com recuperação de falha. Não compartilhar credenciais/contexto sensível na URL.

Auditoria somente leitura relatada pelo agente Replit nesta demanda: Oportunidades, 9 testes estruturais e typecheck aprovados; não E2E. Consumidor espera Card 1.10.0 mountList/mountJourney, versão pública anterior sem recursos comprovados, allowlist vazia. Footer público 1.0.0 preview, integração ausente; PV via Card não comprovado; Menu ausente; autenticação/contexto, catálogo e mapa não operacionais. Auditoria relatou deployment público ativo não previsto na autorização histórica, origem/autoria e data desconhecidas; tratar como incidente de governança a verificar, não lançamento oficial. Não reproduzir endereço temporário nem dados de infraestrutura desnecessários neste repositório público. Nenhuma alteração operacional ou autorização de origem nesta proposta.

## 8. Matriz de reconciliação e gates

| ID | Escopo | Tratamento |
|---|---|---|
| RC-01 | Descoberta contextual | PAS-001 já contempla; ampliar PER-201/202 após gate |
| RC-02 | Online e futuro | Fundamentos existentes; representação proposta |
| RC-03 | Domínios | Nove confirmados; aplicação pendente |
| RC-04 | Profissional | Papel previsto; categoria estrutural e contratos dependem de frente transversal |
| RC-05 | Coletivos | PER-101..108 preservados; acesso a definir |
| RC-06 | Filtros | Estrutura proposta; controles e critérios a validar |
| RC-07 | Grafo | Reusar EVENT/INTEGRATION; contratos técnicos pendentes |
| RC-08 | PV/reputação | Extensão expressa de PER-203, PR #735/#654, cobertura real pendente |
| RC-09 | Comércio | Fronteiras preservadas; checkout/pontos bloqueados |
| RC-10 | Compartilhamento | Contratos técnicos/segurança/homologação pendentes |
| RC-11 | Rota | Reconciliar navegação sem alterar IDs |

INT-01 regularizar deployment; INT-02 contrato Card; INT-03 origens exatas; INT-04 cadeia PV; INT-05 Footer; INT-06 Menu; INT-07 sessão/contexto; INT-08 catálogo; INT-09 mapa; INT-10 inteligência/grafo; INT-11 atualização compatível; INT-12 E2E/responsividade. Todos pendentes de homologação; não autorizar publicação por inferência.

## 9. Alterações futuras, não executadas neste dossiê

- PER-201 §§1–6,9–10,12,15,18,20,27–29: consulta contextual e dimensão geográfica.
- PER-202 §§1–9,11,13–14,18–19,25–27: descoberta contextual e Cards.
- PER-203 §§2–4,6,8,11,14,17–24,29–31: exibição contextual, continuidade, limites de autoridade.
- [Flow Map](flow-map.md) §§4–5,8–10; [Surface Registry](../../journeys/surface-registry.md); [Transition Registry](../../journeys/transition-registry.md): preservar IDs, reexaminar TRN-203/210 se escopo material mudar; não promover maturidade.
- GIA e contratos especializados: referenciar autoridade em vez de duplicar.
- Estado Atual, README, Roadmap e referências: sincronizar somente após adjudicação; não alterar menu para candidato sem autorização.
- Auditar integralmente v1.2.0, dependências de PR #735 e demais frentes, decidir acesso a coletivos, cobertura de avaliações, critérios de ordenação e gates de implementação. Validar Figma, licença tipográfica e integração ponta a ponta. Nenhum merge automático.

## 10. Auditoria cruzada com a PR #735 — interfaces de responsabilidade

Exame documental focal dos quatro arquivos candidatos da [PR #735](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/735), não adjudicação ou homologação. A #735 mantém o detalhamento de ciclo de vida, perfis e conteúdo; a #736 delimita descoberta, consumo e continuidade. As seguintes condições de consumo referenciam aquelas propostas, sem criar autoridade concorrente.

| Achado | Condição de consumo / encaminhamento |
|---|---|
| CR-01 | Identidade estável da oportunidade principal e unidade/edição/período/etapa efetivamente ofertada; preservar versão, responsável, condições e proveniência. Recorrência não inferida por título. |
| CR-02 | Realizações encerradas ou sem disponibilidade de participação saem da descoberta ativa, recomendação, mapa e inscrição conforme estado; histórico autorizado permanece consultável. Não confundir encerramento de edição com encerramento da oportunidade principal; futuro condicionado não é disponibilidade presente. Cancelamento não comprova realização. |
| CR-03 | Preservar card oficial de descoberta; card histórico distinto, resumido, sem mapa, preço atual, checkout ou inscrição; ação Consultar experiência. Consumo compartilhado a validar, não duplicar componente. |
| CR-04 | Inédita sem avaliações/relatos próprios: omitir seções vazias, não gerar nota zero. Recorrente: histórico de edições comparáveis identificado como anterior, separado da edição futura. Histórico: apenas dados próprios da realização; base insuficiente explicitada quando pertinente. |
| CR-05 | Perfis públicos de ofertador e anfitrião distintos, retorno contextual, competência e identidade verificadas. Anfitrião é papel da Pessoa, não nova conta nem necessariamente Profissional. PER-103 não estendido por analogia. |
| CR-06 | Link do anfitrião ao próprio Perfil Público de Experiências facultativo, desativado por padrão na proposta, titular ativa/revoga conscientemente, destino público revalidado, sem link inverso ou exposição da Journey. |
| CR-07 | Referenciar quatro dimensões candidatas da #735 (correspondência com proposta, qualidade, contribuição percebida, continuidade/novas possibilidades) e dois momentos voluntários (logo após e posteriormente se pertinente). As dimensões PAS-001 §3425 são referência, não instrumento concorrente; escalas e metodologia pendentes. |
| CR-08 | Avaliações, perguntas públicas e experiências compartilhadas passam por exame Guivos antes da exibição, sem aprovação obrigatória de ofertador/anfitrião; AI auxiliar sob política ratificada. Pré-moderação de respostas/FAQ ainda proposta complementar; dúvida privada não vira pública. |
| CR-09 | Moderação global, autorização de publicação e visibilidade por superfície são distintas. Ocultação editorial de experiência compartilhada no próprio perfil não altera fonte, outra superfície, indicadores ou reputação; não permite ocultar avaliações/perguntas por interesse comercial. Revogação prevalece. |
| CR-10 | Fonte única de relatos por autoria/papel/edição; referências autorizadas por superfície, inclusive Media. Retirar seção redundante Outros relatos, preservando conteúdo e finalidade sem publicação automática por migração. |
| CR-11 | FAQ e dúvidas anteriores à participação; respostas de responsável competente, revalidadas na recorrência. Encerradas não recebem novas dúvidas de inscrição; histórico autorizado opcional. |
| CR-12 | Reputação não controla recomendação; não ativar ordenação por avaliações ou pontos sem adjudicação, base comparável e controles. Não alterar card oficial para indicadores de reputação por inferência. |
| CR-13 | Preservar Goldplay legítima, escala, paleta oficial de 30 tokens, componentes e responsividade; fallback apenas degradação declarada, não conformidade visual. Demonstração sintética isolada, identificação no shell de teste quando necessária, nunca rótulos/dados provisórios em superfície pública de produção. |
| CR-14 | Preservar gates G1–G6 da #735, R1/P1 e R-A..R-D, IDs/maturidade, proibição de publicação e engenharia operacional. Nenhum gate encerrado. |

Fontes específicas da #735: [ciclo de vida e perfis](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/735/head/docs/experience-architecture/opportunity-lifecycle-public-profiles-candidate.md), [moderação e visibilidade](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/735/head/docs/experience-architecture/opportunity-content-moderation-visibility-candidate.md), [conexão facultativa de perfis](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/735/head/docs/experience-architecture/opportunity-host-person-public-profile-link-candidate.md), [exame de protótipo](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/735/head/docs/experience-architecture/opportunity-lifecycle-prototype-reconciliation.md). Em caso de alteração futura dessas propostas, reexaminar dependências. Nenhuma ratificação de metodologia, esquema de dados, permissão, rota ou cobertura inicial por esta auditoria.

## 11. Auditoria cruzada com a PR #730 — integração governada

Exame focal de seis documentos da PR #730, especialmente Quadro Único v1.0.0 §§18.5–18.25, modelo de nós/relações, arquitetura de integrações, sincronização/versionamento, gatilhos/revalidação e responsabilidades. O resumo da PR não substitui o estado mais detalhado do Quadro Único. A #730 permanece candidata; a #736 não adjudica seus contratos.

| Achado | Condição de consumo pela experiência Oportunidades |
|---|---|
| GV-01 | Grafo Vivo é projeção explicável e revisável, não fonte autônoma. Intercâmbio bidirecional por capacidades e fontes competentes, não gravação direta da interface no grafo. |
| GV-02 | Preservar B, R2, I-A, C1 e Explorar/Escutar/Conversar; entrada voluntária por PER-008 e retorno neutro. Nenhum atalho Grafo → Oportunidades, ID ou handoff oficial por inferência. CT-01/02 candidatos não são transições registradas. |
| GV-03 | B01: fonte canônica da compreensão, emissor de versão, precedência e atualização pós-PER-007 ainda não adjudicados. Não presumir Neo4j, modelo de IA, cache ou projeção como registro competente. |
| GV-04 | B02: categoria × finalidade × modalidade × destinatário ainda depende de Dados/Privacidade. Compreender, persistir, personalizar e compartilhar são decisões distintas; abrir tela não autoriza transferência. |
| GV-05 | B03–B05 prioritárias, pendentes; B06–B12 condicionadas. Sem integração real, persistência ou autorização de terceiros por este registro. |
| GV-06 | Catálogo e fontes competentes confirmam existência, disponibilidade, condições e elegibilidade no próprio escopo; hipótese não é oportunidade ativa. Simulação isolada, sem alterar recursos ou contexto real. |
| GV-07 | Preservar origem, declaração/interpretação/inferência/confirmação/correção, temporalidade, validade e versão; classificações candidatas da #730 não constituem taxonomia canônica nem equivalência automática com categorias existentes. |
| GV-08 | Mudança contextual legitimamente admitida pode solicitar reavaliação de pertinência e condições; conflito, dado sensível e revogação exigem tratamento pela competência apropriada. Nunca cancelar objetivo ou criar interesse por inferência. |
| GV-09 | Consulta e motivos de correspondência devem referenciar versão elegível quando formalizada; em atualização material, sinalizar desatualização, revalidar e não apresentar recomendação antiga como atual. Preservar estado de navegação apenas enquanto válido. |
| GV-10 | Correção/revogação prevalecem sobre snapshots e caches; interromper usos incompatíveis, invalidar derivados conforme política competente. Concorrência/retry não podem duplicar efeitos ou sobrescrever silenciosamente conflitos. Falha parcial não equivale a êxito. |
| GV-11 | Nós e arestas são candidatos visuais, não schema físico; não criar relações, objetivos, passos, participação ou evolução por desenho. Oferecer explicabilidade e alternativa textual acessível. |
| GV-12 | Fase 1 da #730 tem autorização específica de prévia sintética; §18.25 relata 64/64 testes locais e 15/15 verificações Chromium, não repetidos na auditoria relatada, sem integração real. Não transferir esse aceite à #736. Fase 2 bloqueada; nenhuma seleção técnica ou liberação de produção. |

Fontes: [Quadro Único](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/730/head/docs/experience-architecture/person-journey/grafo-vivo/quadro-unico-formalizacao-funcional-dados.md), [modelo de nós](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/730/head/docs/experience-architecture/person-journey/grafo-vivo/modelo-nos-relacoes-memoria.md), [arquitetura](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/730/head/docs/experience-architecture/person-journey/grafo-vivo/arquitetura-conceitual-integracoes.md), [sincronização](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/730/head/docs/experience-architecture/person-journey/grafo-vivo/contrato-conceitual-sincronizacao-versionamento.md), [revalidação](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/730/head/docs/experience-architecture/person-journey/grafo-vivo/matriz-gatilhos-revalidacao-impacto-contextual.md), [responsabilidades](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/730/head/docs/experience-architecture/person-journey/grafo-vivo/matriz-responsabilidades-fronteiras.md).

Gate de RC-07/INT-10: adjudicar B01/B02, demais dependências pertinentes, contratos de fonte/catalogação e eventos PAS-001, finalidade e permissões; definir procedimento e autorização próprios de integração e testar correção, revogação, conflitos e falha segura. Não modificar #730 nem reabrir decisões aprovadas; nenhuma integração real autorizada.

## 12. Auditoria cruzada com as PRs #654 e #655 — reconhecimento e incentivos

Exame focal dos cinco documentos da #654 (política consolidada v0.9.1, auditoria de prontidão, ato de competências, handoff e dossiê dos dois selos) e da proposta transversal #655 v3.0.0, com leitura dirigida das seções 36–40. Não constitui ratificação econômica, jurídica, estatística ou operacional. As duas frentes são independentes e não transferem autoridade para a #736.

| Achado | Condição de consumo / encaminhamento |
|---|---|
| SI-01 | Verificado e Contribuição Reconhecida são direções aprovadas para Coletivos; Contribuição Reconhecida pressupõe Verificado vigente na direção qualitativa. Não estender automaticamente a Organização, Profissional ou Pessoa. |
| SI-02 | G0/B-01: poderes específicos e representação competente a comprovar; minuta sem assinatura/eficácia. 36/36 exames DEC/RSP, 0/36 ratificações individualizadas comprovadas; não confundir com ausência de aprovação conceitual. |
| SI-03 | OP-01..07 qualitativos aprovados; critérios de prova, elegibilidade, amostra, denominadores, cobertura, atribuição, janela, vigência, recurso, privacidade e antifraude aguardam ratificação. PV fornece apenas evidências autorizadas; não concede selo nem comprova causalidade. |
| SI-04 | Cards/Mapa/Detalhes/perfis somente exibem reconhecimento vigente efetivamente concedido quando superfície autorizada; PER-103 e demais projeções exigem homologação. Ausência neutra, sem ranking, boost, filtro discriminatório ou venda. Sem emissão/exibição produtiva. |
| SI-05 | FIN-COMPRA: incentivo opcional financiado pelo ofertante, direção de retenção do custo no repasse; FIN-EVENTO: orçamento pré-financiado próprio. Não confundir com assinatura Business, taxa Guivos ou receita. |
| SI-06 | A seção 40 da #655 (17/10/2026) supera a proposta anterior de cinco percentuais fixos: um incentivo por compra elegível com pontos nominais, percentual livre e régua potencialmente sincronizados; sem acumular três incentivos. Sem paridade, percentual e régua podem sincronizar entre si em rascunho, pontos ficam a definir; pontos fixos manuais são alternativa de rascunho sem percentual equivalente. Nenhuma conversão inventada. |
| SI-07 | Base é o preço efetivamente cobrado e elegível da própria oportunidade, nunca mensalidade/plano. Custo econômico em BRL do incentivo não pode ultrapassar base elegível em BRL; quantidade nominal de pontos não é comparável a reais. Teto matemático percentual de 100% não é máximo comercial aprovado; range/passo, base final, taxas e cobertura pendentes. |
| SI-08 | Compra paga sem adesão não gera incentivo por compra; oportunidade gratuita não gera retorno percentual sobre base zero, podendo futuramente ter campanha financiada FIX/RANK/CUSTOM. Coletivo Livre não publica oportunidade paga segundo recorte #655; não generalizar elegibilidade a outros atores sem contrato. |
| SI-09 | Esgotamento da cota de incentivo não encerra inscrições/vagas da oportunidade. Benefício prometido ou reservado não é saldo disponível; inscrição/pagamento/participação/classificação são gatilhos distintos, exigem evidências e regras próprias. Não reabrir cota automaticamente por desistência. |
| SI-10 | ROUND/P1: HALF_EVEN, precisão 0,01 ponto por fato gerador elegível/ofertante, aritmética decimal exata, quantização única, reversão parcial cumulativa e integral exata; direção de política aprovada, implementação não autorizada. |
| SI-11 | PAR-02/P2, FUND-01/P3, P4–P9, COVER e LIQ-01/02 pendentes; sem taxa Pontos↔BRL, emissão, resgate Mall/Travel, liquidação ou checkout operacional. 16 E2E especificados, 0 executados segundo dossiê. Não presumir dívida da Pessoa por chargeback posterior. |
| SI-12 | Filtro de incentivo/aceitação de pontos e eventual ordenação somente quando informação e operação autorizadas; valor desconhecido não equivale a zero. Pontos, reputação, reconhecimento, relevância, mérito e evolução não são equivalentes. Não apresentar promessas ou dados de teste como oferta real. |

Fontes: [política consolidada de Selos](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/654/head/docs/experience-architecture/collective-recognition-operational-policy-candidate.md), [auditoria de prontidão](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/654/head/docs/experience-architecture/collective-recognition-pr654-readiness-audit.md), [ato de competências](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/654/head/docs/experience-architecture/collective-recognition-policy-responsibility-and-authority-act-proposal.md), [handoff](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/654/head/docs/experience-architecture/collective-recognition-approval-and-formalization-handoff.md), [dossiê dos dois selos](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/654/head/docs/experience-architecture/collective-recognition-two-badges-candidate.md), [Pontos e premiações v3.0.0](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/blob/refs/pull/655/head/docs/economic-model/opportunities-points-and-event-rewards-candidate.md).

A referência histórica a percentuais predefinidos no guia de consulta não deve ser usada para reintroduzir os cinco presets no protótipo: a decisão posterior da #655 prevalece no recorte candidato de UX, sem alterar a autoridade econômica normativa. Registrar eventual atualização editorial do guia em frente própria. Não criar nova política, conceder selos, emitir pontos, autorizar superfícies ou mudar #654/#655. RC-08/RC-09 continuam condicionados aos gates de cada frente.

## 13. Nomenclatura e parecer de prontidão documental — 28/11/2026

**Decisão expressa da Direção:** denominar o benefício exclusivamente **Pontos**, sem complemento de marca, nas interfaces, comunicações, filtros, cards, documentos e produtos. Exemplos: Saldo de Pontos, Incentivo em Pontos, Ganhar Pontos, Utilizar Pontos. Preservar identificadores técnicos, URLs e referências históricas rastreáveis; eventual atualização de títulos e textos normativos vigentes exige reconciliação própria, sem modificar a natureza econômica, autoridade, permissões ou gates. A decisão não autoriza implementação ou publicação. Este documento candidato usa Pontos; demais frentes devem ser inventariadas antes de alteração transversal.

### Parecer focal

- Consistência: 38 achados CR/GV/SI registrados, sem promoção normativa. Os 37 grupos de filtros somam 10+5+6+6+10. Os nove domínios permanecem referência canônica; Tipo/ordenação/cobertura de avaliações precisam de adjudicação. A ordenação contextual não pode ser determinada por incentivos ou reputação.
- Referências: PAS-001 v1.0.0, mapa de capacidades v1.0.1, Surface Registry v0.36.22 e entrada Profissional v0.1.1 confirmados na main. A verificação exaustiva automatizada de links não foi concluída; referências das auditorias focais consultadas, sem declarar validação integral de todos os links.
- Profissional: GKR-PARTICIPANT-PROFESSIONAL-ENTRY-001 v0.1.1, conceptual_direction_record, normative:false. Reconhece categoria funcional de oferta e identidade própria; não autoriza publicação, venda, pagamentos ou mudança estrutural por inferência. GKR-STATE-001 v3.51.17 ainda enumera Pessoa, Organização e Coletivo como participantes estruturais. RC-04 permanece aberto.
- Cobertura v1.2.0: tentativa de recuperar o texto integral dos 80 RF, 18 RNF e oito movimentos não obteve a matriz original. Não fabricar IDs, conteúdo ou percentual de cobertura. Gate documental aberto; obter a fonte e confrontar cada item antes de declarar substituição da v1.2.0.
- CI no commit anterior 3aa86276ea43acc93e1ea62b07317f06c997b643: Semantic State Validation success; Mechanical Validation in_progress na consulta. Novo commit exige verificação própria. Mergeabilidade técnica observada não equivale a autorização.
- Bloqueios: RC-04/05/07/08/09/10/11 e demais adjudicações específicas, B01/B02, cobertura real, contratos econômicos, fonte e versão dos componentes, origem autorizada, regularização do deployment reportado, catálogo, sessão, mapa, homologação visual e E2E. Engenharia permanece pausada/não liberada; não iniciar execução operacional por esta revisão.

**Parecer: HOLD para promoção canônica e engenharia; apto somente a revisão documental candidata.** Nenhuma alteração em main, PRs de dependência ou projetos Replit. Não declarar auditoria integral concluída.

## 14. Estado

CANDIDATE / NON-NORMATIVE. Nenhum novo SURF-ID/TRN-ID, nenhuma promoção de maturidade, nenhuma alteração nas autoridades vigentes, nenhuma autorização de execução ou publicação. O dossiê permite revisão rastreável, não representa fechamento integral da reconciliação.
