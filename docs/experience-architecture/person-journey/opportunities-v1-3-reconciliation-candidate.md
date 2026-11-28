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

## 11. Estado

CANDIDATE / NON-NORMATIVE. Nenhum novo SURF-ID/TRN-ID, nenhuma promoção de maturidade, nenhuma alteração nas autoridades vigentes, nenhuma autorização de execução ou publicação. O dossiê permite revisão rastreável, não representa fechamento integral da reconciliação.
