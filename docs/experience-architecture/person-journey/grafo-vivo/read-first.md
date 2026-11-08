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

## Documentos

- [Visão conceitual — Grafo Vivo e Contexto Vivo](visao-conceitual.md): proposta, capacidades, princípios e questões abertas.
- [Arquitetura Conceitual e Integrações Candidatas](arquitetura-conceitual-integracoes.md): camadas, fluxo de dados, provedores candidatos, dependências, riscos e gates.
- [Modelo de Nós, Relações e Memória Contextual](modelo-nos-relacoes-memoria.md): famílias e relações candidatas, proveniência, temporalidade, exemplos e limites.
- [Experiência Conceitual nos Quatro Momentos](experiencia-quatro-momentos.md): primeiro acesso, retorno, atualização por conversa e relatório narrado interativo.
- [Matriz de Responsabilidades e Fronteiras Funcionais](matriz-responsabilidades-fronteiras.md): confronto com PER-007/008/010/011/012 e Intelligence, eventos, lacunas e limites.
- [Exame de Compatibilidade com PER-008 — Hoje](exame-compatibilidade-per008.md): matriz de compatibilidade, três alternativas de acomodação, lacunas e parecer condicionado.
- [Quadro Focal de Fronteiras Funcionais](quadro-focal-fronteiras-funcionais.md): cinco capacidades, gates entre conversa e memória, decisões pendentes e dependências de integração.
- [Confronto dos Registries e Fluxos de Integração](confronto-registries-integracoes-fluxos.md): confirmação dos estados de superfícies e transições, fluxos de dados, gates, cenários e lacunas.
- [Matriz do Ciclo de Vida da Informação Contextual](matriz-ciclo-vida-informacao-contextual.md): declaração, transcrição, validação, uso temporário, persistência, projeções, narração, correção e revogação.
- [Gatilhos de Revalidação e Impacto Contextual](matriz-gatilhos-revalidacao-impacto-contextual.md): casos de atualização, confirmação proporcional, risco, impacto em análises e revogação.
- [Contrato Conceitual de Sincronização e Versionamento](contrato-conceitual-sincronizacao-versionamento.md): consistência temporal, referências de versão, mudanças concorrentes, falhas e revogações entre contexto, grafo, conversa e narração.
- [Matriz de Estados de Coerência e Recuperação Multimodal](matriz-estados-coerencia-recuperacao-multimodal.md): interrupções, falhas parciais, mudanças de versões, alternativas acessíveis e retomada governada.
- [Quadro Consolidado de Prontidão Conceitual e Pendências de Adjudicação](quadro-consolidado-prontidao-pendencias.md): inventário de evidências, maturidades, gates, riscos e fronteiras para futuras decisões.
- [Dossiê de Competências e Adjudicação de Entrada Funcional](dossie-competencias-adjudicacao-entrada-funcional.md): alternativas A/B/C de localização, efeitos sobre PER-008/Registries e quesitos a decidir sem seleção automática.
- [Exame Focal de Admissibilidade de Competência e Transição](exame-focal-admissibilidade-competencia-transicao.md): admissibilidade das alternativas, testes por comportamento, atos necessários e quesitos para a autoridade competente.
- [Quadro de Respostas Requeridas e Instrumentos de Competência](quadro-respostas-instrumentos-competencia.md): consulta e evidências dos quesitos AF-01..AF-10, dependências e instrumentos possíveis sem adjudicação.
- [Consulta Focal de Competência à Arquitetura UX/Journey](consulta-focal-competencia-ux-journey.md): minuta de consulta sobre AF-01, AF-02, AF-03 e AF-10, sem submissão formal ou parecer presumido.
- [Verificação de Autoridade e Suficiência Documental para Submissão](verificacao-autoridade-suficiencia-submissao.md): confronta ADR-001/006, A2-METHOD-001, GEA-AUDIT-001, registra baseline visual informado pela direção, gates para futura implantação e achado do menu GKR.
- [Exame Focal AF-10 de Competência Decisória e Instrumento](exame-focal-af10-competencia-instrumento.md): identifica competências por área, instrumentos possíveis, lacunas de delegação e critérios para futura consulta formal.
- [Minuta de Encaminhamento Institucional do AF-10](minuta-encaminhamento-institucional-af10.md): texto candidato de solicitação, perguntas à autoridade, anexos e condições para eventual envio formal.
- [Verificação do Destinatário e Canal de Submissão AF-10](validacao-destinatario-canal-af10.md): área temática identificada, sem instância, canal e instrumento decisório comprovados; consulta segue não enviada.
- [Registro de Decisão da Direção — Competência AF-10](decisao-direcao-competencia-af10.md): Direção designada como instância decisória final, consultas técnicas por domínio e GKR/GitHub como registro; sem adjudicar A/B/C ou liberar execução.

## Estado das decisões (07/11/2026)

**Aprovado para aprofundamento conceitual:**
- Alternativa C: Grafo Vivo exploratório com contexto, possibilidades, evolução temporal, simulação e conversa.
- Três maneiras complementares de compreender a Jornada: **explorar visualmente**, **escutar relatório narrado**, **conversar com a Intelligence**.
- Aprendizado Contextual Contínuo: identificar informações novas em conversas, distinguir afirmações de hipóteses e consolidar de modo revisável, com validação proporcional.
- Mesma compreensão contextual fundamentando visualização, escuta e conversação.

**Não aprovado/pendente:** inclusão em telas existentes, novas superfícies/IDs, taxonomia ou esquema de grafo, regras técnicas de persistência, seleção de bibliotecas e provedores de voz, políticas definitivas de retenção, cronograma, preços/planos, aplicação aos demais participantes, testes, execução e publicação operacional.

## Autoridades preservadas

Os documentos vigentes de Jornada da Pessoa, PER-007 (compreensão revisável), PER-008 (Hoje), PER-010 (Objetivos), PER-011 (Próximos Passos), PER-012 (Evolução), Surface/Transition Registries, PAS-001, GIA-COG-001 e regras de privacidade/proveniência **não são substituídos** por este estudo. Novos mecanismos deverão ser confrontados formalmente com essas autoridades antes de qualquer adoção funcional.

**Documentação ≠ implementação ≠ validação ≠ autorização operacional.**
