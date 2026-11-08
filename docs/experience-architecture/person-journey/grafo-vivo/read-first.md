---
title: Grafo Vivo da Jornada — Leia Primeiro
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: exploratory_non_operational
---

# Grafo Vivo da Jornada — Leia Primeiro

> **Estudo conceitual da direção da Guivos. Não é contrato de UX, arquitetura normativa, decisão técnica ou autorização de implementação.**

## Objetivo da seção

Preservar e aprofundar a hipótese de uma experiência contextual, interativa, narrada e conversacional para o dashboard da **Jornada da Pessoa**. Sua possível aplicação a outros participantes fica fora do escopo atual e depende de nova decisão.

## Seção própria do GKR — organização do acervo

**Este é o ponto único de entrada para o Grafo Vivo da Jornada da Pessoa.** Todos os 35 estudos e registros de decisão estão reunidos no diretório `docs/experience-architecture/person-journey/grafo-vivo/`, além deste índice. O menu deve apontar **somente para esta página de entrada**, e não duplicar individualmente os dossiês.

**Natureza da seção:** acervo de concepção e governança em elaboração. A existência desta seção no PR em rascunho **não transforma estudos conceituais em autoridade operacional**, não promove material à Canon e não constitui publicação no GKR principal.

### Visão rápida do estado

| Dimensão | Estado |
| --- | --- |
| Conceito e três modalidades (Explorar, Escutar, Conversar) | Aprovados para aprofundamento conceitual |
| Aprendizado Contextual Contínuo | Modelo candidato, sujeito a regras de dados e validação |
| Instância final de decisão do Grafo Vivo | **Direção da Guivos**, conforme registro AF-10 |
| Posicionamento funcional A/B/C | **Alternativa B aprovada pela Direção** |
| Competência do destino expandido | **Responsabilidade funcional distinta aprovada**; contrato de superfície ainda pendente |
| Revisão técnica UX/Journey AF-01/02/03 | Solicitação documentada no PR #730; sem parecer recebido verificado |
| Replit — Jornada da Pessoa | Futuro destino condicionado, sem auditoria ou execução autorizada |
| Status editorial | PR #730 draft; sem merge ou publicação |

## Biblioteca organizada por assunto

### Fundamentos e experiência

- [Visão conceitual — Grafo Vivo e Contexto Vivo](visao-conceitual.md): proposta, capacidades, princípios e questões abertas.
- [Experiência Conceitual nos Quatro Momentos](experiencia-quatro-momentos.md): primeiro acesso, retorno, atualização por conversa e relatório narrado interativo.
- [Modelo de Nós, Relações e Memória Contextual](modelo-nos-relacoes-memoria.md): famílias e relações candidatas, proveniência, temporalidade, exemplos e limites.
- [Quadro Focal de Fronteiras Funcionais](quadro-focal-fronteiras-funcionais.md): cinco capacidades, gates entre conversa e memória, decisões pendentes e dependências de integração.

### Arquitetura, dados e integrações

- [Arquitetura Conceitual e Integrações Candidatas](arquitetura-conceitual-integracoes.md): camadas, fluxo de dados, provedores candidatos, dependências, riscos e gates.
- [Matriz do Ciclo de Vida da Informação Contextual](matriz-ciclo-vida-informacao-contextual.md): declaração, transcrição, validação, uso temporário, persistência, projeções, narração, correção e revogação.
- [Gatilhos de Revalidação e Impacto Contextual](matriz-gatilhos-revalidacao-impacto-contextual.md): casos de atualização, confirmação proporcional, risco, impacto em análises e revogação.
- [Contrato Conceitual de Sincronização e Versionamento](contrato-conceitual-sincronizacao-versionamento.md): consistência temporal, referências de versão, mudanças concorrentes, falhas e revogações entre contexto, grafo, conversa e narração.
- [Matriz de Estados de Coerência e Recuperação Multimodal](matriz-estados-coerencia-recuperacao-multimodal.md): interrupções, falhas parciais, mudanças de versões, alternativas acessíveis e retomada governada.

### Jornada, superfícies e transições

- [Matriz de Responsabilidades e Fronteiras Funcionais](matriz-responsabilidades-fronteiras.md): confronto com PER-007/008/010/011/012 e Intelligence, eventos, lacunas e limites.
- [Exame de Compatibilidade com PER-008 — Hoje](exame-compatibilidade-per008.md): matriz de compatibilidade, três alternativas de acomodação, lacunas e parecer condicionado.
- [Confronto dos Registries e Fluxos de Integração](confronto-registries-integracoes-fluxos.md): confirmação dos estados de superfícies e transições, fluxos de dados, gates, cenários e lacunas.
- [Dossiê de Competências e Adjudicação de Entrada Funcional](dossie-competencias-adjudicacao-entrada-funcional.md): alternativas A/B/C de localização, efeitos sobre PER-008/Registries e quesitos a decidir sem seleção automática.
- [Exame Focal de Admissibilidade de Competência e Transição](exame-focal-admissibilidade-competencia-transicao.md): admissibilidade das alternativas, testes por comportamento, atos necessários e quesitos para a autoridade competente.
- [Análise Técnica UX/Journey — AF-01, AF-02 e AF-03](analise-tecnica-ux-journey-af01-af02-af03.md): confronto do Master de Hoje, Orquestração e Registries, com achados e perguntas para parecer especializado, sem resposta presumida.

### Governança, decisões e implantação condicionada

- [Quadro Consolidado de Prontidão Conceitual e Pendências de Adjudicação](quadro-consolidado-prontidao-pendencias.md): inventário de evidências, maturidades, gates, riscos e fronteiras para futuras decisões.
- [Quadro de Respostas Requeridas e Instrumentos de Competência](quadro-respostas-instrumentos-competencia.md): consulta e evidências dos quesitos AF-01..AF-10, dependências e instrumentos possíveis sem adjudicação.
- [Consulta Focal de Competência à Arquitetura UX/Journey](consulta-focal-competencia-ux-journey.md): minuta de consulta sobre AF-01, AF-02, AF-03 e AF-10, sem submissão formal ou parecer presumido.
- [Verificação de Autoridade e Suficiência Documental para Submissão](verificacao-autoridade-suficiencia-submissao.md): confronta ADR-001/006, A2-METHOD-001, GEA-AUDIT-001, registra baseline visual informado pela direção, gates para futura implantação e achado do menu GKR.
- [Exame Focal AF-10 de Competência Decisória e Instrumento](exame-focal-af10-competencia-instrumento.md): identifica competências por área, instrumentos possíveis, lacunas de delegação e critérios para futura consulta formal.
- [Minuta de Encaminhamento Institucional do AF-10](minuta-encaminhamento-institucional-af10.md): texto candidato de solicitação, perguntas à autoridade, anexos e condições para eventual envio formal.
- [Verificação do Destinatário e Canal de Submissão AF-10](validacao-destinatario-canal-af10.md): área temática identificada, sem instância, canal e instrumento decisório comprovados; consulta segue não enviada.
- [Registro de Decisão da Direção — Competência AF-10](decisao-direcao-competencia-af10.md): Direção designada como instância decisória final, consultas técnicas por domínio e GKR/GitHub como registro; sem adjudicar A/B/C ou liberar execução.
- [Decisão da Direção — Alternativa B](decisao-direcao-alternativa-b.md): Hoje como entrada para experiência expandida; seleciona B sem criar nova superfície, TRN, integração ou autorização operacional.
- [Especificação Funcional Candidata da Experiência Expandida — Alternativa B](especificacao-funcional-experiencia-expandida-b.md): entrada voluntária, três modalidades, alternância, retorno, estados, recuperação, limites de dados e decisões de competência pendentes.
- [Decisão da Direção — Responsabilidade Funcional Distinta](decisao-direcao-responsabilidade-distinta.md): reconhecimento expresso da responsabilidade expandida, separada de Hoje e dos domínios, sem criar IDs ou autorizar implementação.
- [Decisão da Direção — Entrada, Retorno e Modalidades](decisao-direcao-entrada-retorno-modalidades.md): entrada voluntária, retorno explícito neutro e três modos internos aprovados conceitualmente, sem criação de IDs ou alteração dos Registries.
- [Decisão da Direção — Elegibilidade no Primeiro Hoje](decisao-direcao-primeiro-hoje.md): acesso opcional na primeira entrada quando existe contexto legítimo suficiente, sem exigir histórico e sem consentimento implícito.
- [Contrato Funcional Candidato — Passagem e Retorno Hoje ↔ Grafo Vivo](contrato-funcional-candidato-passagem-retorno.md): pré-condições, envelope lógico mínimo, estados, versões, retorno neutro, recuperação e quesitos CT-01/02 para adjudicação.
- [Decisão da Direção — CT-01 e CT-02](decisao-direcao-ct01-ct02.md): aprovação conceitual do planejamento de reconhecimento no Surface Registry e da necessidade de contratos formais próprios de entrada e retorno, sem criar IDs ou alterar Registries.
- [Matriz Focal de Reconciliação dos Registries — CT-01/02](matriz-reconciliacao-registries-ct01-ct02.md): compara R1/R2/R3, recomenda R2 para deliberação, especifica requisitos de suficiência dos dois contratos, gaps e impactos sobre autoridades vigentes.
- [Decisão da Direção — R2](decisao-direcao-r2.md): representação da responsabilidade funcional distinta aprovada como diretriz, sem criação de superfície ou ID oficial.
- [Duas Minutas Candidatas de Transição — Entrada e Retorno](minutas-contratos-transicao-entrada-retorno.md): contratos separados de passagem Hoje → Grafo Vivo e retorno Grafo Vivo → Hoje, ainda não normativos nem validados.
- [Decisão da Direção — Minutas como Base Documental](decisao-direcao-minutas-base.md): adoção expressa das duas minutas como base de reconciliação, sem contratos normativos, novos IDs ou implementação.
- [Quadro Único de Formalização Funcional e Dados Mínimos — v0.9.1, C1 e consultas B01/B02](quadro-unico-formalizacao-funcional-dados.md): consolida decisões vigentes, dados mínimos e **duas propostas de diff não aplicadas** para Surface Registry e Transition Registry; placeholders não são IDs e nenhum Registry foi alterado.

## Navegação e fontes de autoridade

- **Índice canônico desta seção no ramo de estudo:** este `read-first.md`. Não se duplicam documentos ou conclusões em novas cópias.
- **Fonte de verdade das autoridades vigentes:** Masters da Jornada, Orquestração, Surface/Transition Registries, PAS-001, GPA-006/GIA-COG-001 e políticas de dados em seus locais originais. Os links e análises desta seção **referenciam**, mas não substituem essas autoridades.
- **Histórico de alterações e revisão:** [PR #730](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/730). Documentos anteriores de AF-10 podem preservar estados históricos, com notas de reconciliação para a decisão posterior da Direção.
- **Canal das autorizações da Direção:** esta conversa, com solicitações e decisões expressas; GKR/GitHub consolida e registra. **Não há exigência de revisor GitHub para a Direção deliberar.** Ver [decisão AF-10 e esclarecimento posterior](decisao-direcao-competencia-af10.md).
- **Regra de publicação:** seção preparada na branch; a exposição de material `conceptual_study` no menu principal e eventual merge deverão respeitar a governança editorial e ter autorização própria.

## Estado das decisões (07–08/11/2026)

**Aprovado para aprofundamento conceitual:**
- Alternativa C: Grafo Vivo exploratório com contexto, possibilidades, evolução temporal, simulação e conversa.
- Três maneiras complementares de compreender a Jornada: **explorar visualmente**, **escutar relatório narrado**, **conversar com a Intelligence**.
- Aprendizado Contextual Contínuo: identificar informações novas em conversas, distinguir afirmações de hipóteses e consolidar de modo revisável, com validação proporcional.
- Mesma compreensão contextual fundamentando visualização, escuta e conversação.

**Posicionamento e competência aprovados em 08/11/2026:** Alternativa B — Hoje como porta de entrada contextual para experiência expandida, **com responsabilidade funcional distinta**, sem alteração automática dos Masters ou Registries. Ver [registro de decisão](decisao-direcao-alternativa-b.md).

**Entrada/retorno e modos aprovados em 08/11/2026:** entrada explícita e voluntária a partir de Hoje, retorno neutro, alternância interna Explorar/Escutar/Conversar, sem criação de IDs ou alteração de contratos vigentes. Ver [decisão](decisao-direcao-entrada-retorno-modalidades.md).

**Elegibilidade no Primeiro Hoje aprovada em 08/11/2026:** acesso voluntário quando houver contexto suficiente e autorizado, sem exigir histórico prévio ou fabricar evolução; sem tornar o convite obrigatório. Ver [decisão](decisao-direcao-primeiro-hoje.md).

**CT-01 e CT-02 aprovados conceitualmente em 08/11/2026:** planejar registro da competência distinta no Surface Registry e contratos formais próprios de ida/volta no Transition Registry; nenhum ID ou contrato oficial criado. Ver [decisão CT-01/02](decisao-direcao-ct01-ct02.md).

**Diretriz R2 aprovada em 08/11/2026:** responsabilidade distinta representável na arquitetura de superfícies, sem exigir nova tela visual nem criar ID/registro oficial. Duas minutas próprias de entrada e retorno foram preparadas para exame posterior. Ver [decisão R2](decisao-direcao-r2.md) e [minutas](minutas-contratos-transicao-entrada-retorno.md).

**Minutas de entrada e retorno aprovadas como base documental em 08/11/2026:** a aprovação não valida contratos ou transições oficiais. Ver [decisão](decisao-direcao-minutas-base.md).

**Quadro único v0.2.0 aprovado como baseline documental de instrução em 08/11/2026:** a Direção autorizou o aprofundamento conjunto de R2 (representação funcional) e dados mínimos, sem conversão em política, contrato normativo ou autorização operacional. Ver [quadro único atualizado](quadro-unico-formalizacao-funcional-dados.md).

**Diffs candidatos preparados em 08/11/2026:** quadros de adição propostos para Surface e Transition Registries, restritos à revisão, sem aplicação, IDs, validação normativa ou alteração das contagens oficiais. Ver [quadro único v0.3.0](quadro-unico-formalizacao-funcional-dados.md).

**Diferenças normativas A/B aprovadas como referências documentais em 08/11/2026:** diffs do Surface Registry e Transition Registry adotados para revisão futura, **não aplicados** e sem identificação/validação automática. Ver [quadro único v0.3.1](quadro-unico-formalizacao-funcional-dados.md).

**Aprofundamento conjunto de identidade, maturidade e dados preparado em 08/11/2026:** incluído no [quadro único v0.4.0](quadro-unico-formalizacao-funcional-dados.md), com dois pedidos decisórios futuros delimitados. Foi identificada a necessidade de reconciliar também o detalhamento de superfícies da Pessoa. Nenhum ID, política de dados ou Registry foi alterado.

**Proposta coordenada A+B preparada em 08/11/2026:** o [quadro único v0.5.0](quadro-unico-formalizacao-funcional-dados.md) apresenta uma futura representação compatível com o inventário de superfícies e o detalhamento obrigatório da Pessoa, além de contrato documental candidato de contexto e dados (B01–B12), sem criação de IDs, alteração normativa ou aprovação de provedores.

**Parecer focal de prontidão elaborado em 08/11/2026:** [Quadro Único v0.6.0](quadro-unico-formalizacao-funcional-dados.md) conclui pela **prontidão apenas documental e parcial**: as minutas podem ser aprofundadas, mas a inclusão nos Registries depende da identificação/owner do destino e da reconciliação de dados e privacidade. Sem parecer externo presumido ou autorização normativa.

**Alternativa P1 instruída em 08/11/2026:** [Quadro Único v0.7.0](quadro-unico-formalizacao-funcional-dados.md) confronta alternativas I-A/I-B de identificação funcional, mantém owner/maturidade/IDs sob decisão específica e apresenta matriz de consulta por autoridade para B01–B12. Trata-se de reconciliação documental, não parecer especializado recebido nem autorização normativa.

**I-A aprovada como diretriz e B01–B05 priorizados em 08/11/2026:** o [Quadro Único v0.8.0](quadro-unico-formalizacao-funcional-dados.md) registra a escolha da unidade funcional própria, sem ID/owner oficial, e uma matriz focal de fonte canônica, finalidade, suficiência, versão e proveniência ainda sujeita à autoridade de dados/privacidade.

**Exame focal de competência e B01/B02 concluído em 08/11/2026:** o [Quadro Único v0.9.0](quadro-unico-formalizacao-funcional-dados.md) apresenta Arquitetura da Experiência como owner documental candidato da unidade I-A, preserva a competência decisória da Direção e confronta fontes canônicas e finalidades de dados como matrizes candidatas para consulta. Não há validação externa, atribuição de ID ou edição de Registry.

**C1 aprovada e matrizes B01/B02 adotadas para consulta em 08/11/2026:** a [versão 0.9.1 do Quadro Único](quadro-unico-formalizacao-funcional-dados.md) registra a Arquitetura da Experiência como owner documental da futura unidade I-A e as matrizes de fonte/finalidade como instrumentos de consulta, sem IDs oficiais, política de dados, validação de terceiros ou alterações normativas.

**Não aprovado/pendente:** formalização da responsabilidade no Registry, contrato oficial de entrada/retorno, critérios operacionais de elegibilidade, materialização em telas existentes, novas superfícies/IDs, taxonomia ou esquema de grafo, regras técnicas de persistência, seleção de bibliotecas e provedores de voz, políticas definitivas de retenção, cronograma, preços/planos, aplicação aos demais participantes, testes, execução e publicação operacional.

## Autoridades preservadas

Os documentos vigentes de Jornada da Pessoa, PER-007 (compreensão revisável), PER-008 (Hoje), PER-010 (Objetivos), PER-011 (Próximos Passos), PER-012 (Evolução), Surface/Transition Registries, PAS-001, GIA-COG-001 e regras de privacidade/proveniência **não são substituídos** por este estudo. Novos mecanismos deverão ser confrontados formalmente com essas autoridades antes de qualquer adoção funcional.

**Documentação ≠ implementação ≠ validação ≠ autorização operacional.**
