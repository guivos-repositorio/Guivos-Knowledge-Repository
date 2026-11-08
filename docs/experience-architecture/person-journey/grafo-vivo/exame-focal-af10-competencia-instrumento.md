---
title: Grafo Vivo — Exame Focal AF-10 de Competência Decisória e Instrumento
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: governance_competence_diagnostic
---

# Grafo Vivo — Exame Focal AF-10 de Competência Decisória e Instrumento

> **Diagnóstico de competência, sem adjudicação.** Identificar o *owner* documental não comprova a titularidade individual de poderes para aprovar uma nova capacidade. Este documento não submete consulta, não emite parecer em nome da Arquitetura da Experiência, não altera os Registries e não autoriza Design, Replit, testes, integrações ou publicação.

## 1. Pergunta restrita

**AF-10:** quais fontes e instâncias podem legitimamente instruir, interpretar e decidir, separadamente, a localização funcional do Grafo Vivo, uma eventual alteração das responsabilidades de PER-008 e a eventual necessidade de novo handoff?

A resposta deve distinguir **(i) produção de conhecimento**, **(ii) parecer de compatibilidade**, **(iii) decisão de competência funcional**, **(iv) reconciliação normativa/documental** e **(v) autorização operacional**. Não atribuir a qualquer etapa o poder das demais.

## 2. Fontes de autoridade efetivamente verificadas

| Fonte vigente | Evidência localizada | Alcance fundamentado | O que não demonstra |
| --- | --- | --- | --- |
| **ADR-001 — GKR como fonte única da verdade** | Decisão aprovada, Markdown e histórico Git | Local institucional para conhecimento aprovado e rastreável | Pessoa/instância de adjudicação de UX |
| **ADR-006 — Guivos Knowledge Architecture** | Aprovada; GKA gere método, evidências, validação e Canon; não substitui arquiteturas especializadas nem cria produto | Autoridade de governança do conhecimento | Poder para aprovar uma superfície ou implementação |
| **A2-METHOD-001 v2.0.0** | `normative: true`; ciclo evidência → hipótese → consolidação → readiness → validação → auditoria → Canon | Método de maturação, reconciliação e promoção do conhecimento | Aprovação tácita do recurso; documentação ≠ operação |
| **GEA-AUDIT-001 v2.0.0** | `normative: true`; auditoria verifica integridade, não decide pelo domínio | Critérios de validação/auditoria e baseline documental | Capacidade da auditoria de criar nova verdade funcional |
| **Orquestração da Jornada da Pessoa v0.4.0** | `owner: Arquitetura da Experiência da Guivos`; `normative: true`; governa continuidade, subordinada às autoridades específicas | Referência competente para o exame de continuidade entre superfícies | Competência individual nomeada para editar Masters/Registries |
| **Surface Registry v0.36.22** | `owner: Arquitetura da Experiência da Guivos`, `normative: false`; inventaria PER-008 e PER-010/011/012 e seus contratos | Fonte documental de responsabilidades e maturidades vigentes | Novo Grafo Vivo já reconhecido; autorização de alteração |
| **Transition Registry v0.29.26** | `owner: Arquitetura da Experiência da Guivos`, `normative: false`; TRN-007 e 008..013 com escopo de validação | Fonte de ligações reconhecidas | Nova transição criada; navegação direta PER-010↔011↔012 |
| **Masters PER-007/008/010/011/012, PAS-001, GPA-006, GIA-COG-001** | Autoridades temáticas que a Orquestração e os Registries preservam | Limites de dados, síntese, domínio, cognição e escolha da Pessoa | Transferência geral de poder à interface do grafo |

**Achado AF-10:** o corpus consultado fornece **responsabilidade arquitetural por área** e **instrumentos de maturação de conhecimento**, mas **não comprova, para esta decisão, a cadeia completa de delegação ou a instância individualmente habilitada a adjudicar em conjunto PER-008, Surface Registry e Transition Registry**. A lacuna precisa ser resolvida por fonte/ato expresso, não por titularidade inferida.

## 3. Mapa de competências por tipo de ato

| Ato possível | Competência funcional a consultar | Evidência exigida para dizer que está autorizado | Estado do exame |
| --- | --- | --- | --- |
| Preparar consulta AF-01/02/03/10 | Equipe de concepção/Journey na branch documental | Escopo, fontes e limites explicitados | **Documentalmente preparado** |
| Emitir parecer de compatibilidade de Hoje | Autoridade de UX/Journey em conjunto com Master PER-008 | Fonte, versão, fundamento e competência do signatário | **Não emitido** |
| Decidir se Grafo Vivo expandido é estado ou responsabilidade distinta | Instância competente de Arquitetura da Experiência, com Registry e fontes de domínio | Ato expresso, alcance e eventuais conflitos resolvidos | **Não adjudicado** |
| Reconhecer eventual handoff/retorno | Competência pela transição, confrontando Orquestração e Transition Registry | Decisão e contrato específicos de entrada, retorno, falha e autoridade | **Não adjudicado** |
| Alterar Master ou Registry | Responsável formal por atualização de autoridades sob pipeline GKR | Identificação do ato autorizador; reconciliação, validação, auditoria e histórico | **Não autorizado** |
| Aprovar uso recorrente de memória/personalização | Dados/Privacidade, PER-007 e autoridades de domínio | Bases, finalidades, escolhas independentes, correção e retenção | **Não autorizado** |
| Aprovar modelos, provedores ou trânsito de dados para voz | GIA, Segurança, Privacidade/Jurídico, Engenharia | Avaliação de riscos, provedor, contrato e dados mínimos | **Não autorizado** |
| Autorizar auditoria de leitura do Replit | Direção/instância com competência sobre workspace e escopo de inspeção | Ordem expressa delimitando acesso, operações permitidas e evidências | **Não autorizado nesta etapa** |
| Autorizar implementação, testes e publicação | Direção e titulares de competência operacional aplicáveis | Ato próprio por ambiente/escopo, posterior aos gates relevantes | **Não autorizado** |

A referência a “Direção” não presume que uma aprovação geral elimine os gates especializados. O usuário declarou intenção de **iniciar futuramente** implantação em `https://replit.com/@guivos/Jornada-da-Pessoa` quando houver suficiência; essa intenção não é um ato operacional atual.

## 4. Instrumentos e sequência de eficácia — hipótese subordinada à governança

1. **Minuta de consulta:** documento que pode ser revisado; não é submissão.
2. **Consulta formal a destinatário validado:** evidencia que autoridade competente foi efetivamente provocada, com canal/data/autoria registrados.
3. **Parecer de domínio/compatibilidade:** só tem o alcance explicitado na competência e no conteúdo emitido.
4. **Ato de adjudicação funcional:** seleciona a alternativa A/B/C ou outro enquadramento **somente se** a instância puder decidir e tiver evidência suficiente.
5. **Ato específico de reconciliação:** define quais Masters/Registries precisam ser atualizados, preservando precedência e rastreabilidade.
6. **Readiness, validação e auditoria:** aferem integridade da versão a promover, conforme A2-METHOD-001 e GEA-AUDIT-001.
7. **Autorização técnica/operacional posterior:** separadamente aprova inspeção, Design, teste, integração e implantação, se cabível.

**Sequência indicativa, não rito novo.** O pipeline do GKR não substitui procedimentos especializados de UX, Engenharia ou privacidade.

## 5. Quesitos de competência que restam sem resposta verificável

| Referência local | Quesito de deliberação | Fonte/registro a exigir |
| --- | --- | --- |
| C-01 | Que instância pode confirmar que o Master PER-008 já comporta um estado explicativo leve? | Norma de competência UX/Journey e pronunciamento com fonte |
| C-02 | Quem pode decidir reconhecimento de responsabilidade expandida ou rejeitá-lo? | Regime de autoridade de superfícies e decisão expressa |
| C-03 | Quem aprova a criação/alteração de handoff e a maturidade do contrato? | Governança de transições, ato e evidência funcional |
| C-04 | Qual precedência vale se Orquestração, Master e Registry divergirem sobre uma hipótese? | Fonte de precedência aplicável, sem reinterpretar unilateralmente |
| C-05 | Que instrumento distingue aprovação documental e liberação de Design/Engenharia? | Fonte de governança operacional e limites do ato |
| C-06 | A quem compete validar a destinação de dados a Grok/terceiros? | Instrumento de Segurança/Privacidade/Jurídico/GIA |
| C-07 | Quem deve autorizar inspeção de leitura do Replit e quais limites? | Ato de acesso/auditoria próprio |
| C-08 | Como retirar do menu nav itens conceituais sem comprometer rastreabilidade? | Regra de menu do `mkdocs.yml`, pipeline GKR e decisão editorial competente |

C-xx são marcadores locais do diagnóstico, **não IDs oficiais**.

## 6. Reconciliação do menu — achado herdado

O cabeçalho editorial do `mkdocs.yml` restringe a exibição no MENU de documentos `draft/proposed` a casos declarados por autoridade superior como fonte operacional. Nesta branch, documentos `conceptual_study` do Grafo Vivo constam da navegação.

**Recomendação:** antes do eventual merge/publicação, examinar a compatibilidade e preparar, **mediante autorização editorial competente**, a retirada das entradas de estudos candidatos do MENU, preservando acesso por índice, link e histórico. Não alterar o menu neste exame, pois seu objetivo é exclusivamente AF-10.

## 7. Parecer focal de suficiência

**Suficiente para encaminhamento dirigido de verificação de competência:** a pergunta AF-10 pode ser formulada com as fontes e distinções acima.

**Insuficiente para adjudicação:** o corpus examinado não demonstra uma delegação nominativa/instância específica apta a praticar o ato conjunto de alteração funcional e de transições. Não se deve emitir despacho fictício em nome da Arquitetura da Experiência nem escolher B apenas por ser hipótese prioritária.

**Insuficiente para implantação:** não há ato de liberação para Design, auditoria técnica no Replit, API, integrações, testes ou publicação.

## 8. Próxima ação documental proposta

Preparar **minuta de encaminhamento institucional de AF-10**, formulando pedido de identificação da instância decisória, instrumento válido, fronteiras de precedência e competência para eventual reconciliação de PER-008/Registries. Só registrar como “submetido” após envio real comprovado por canal autorizado.

Em paralelo, o achado de navegação deve ser resolvido **antes de qualquer merge**, sem equiparar menu de documentação candidata a autoridade operacional.

## 9. Estado

- Competência por área: **mapeada**.
- Instância decisória específica: **não identificada de forma conclusiva**.
- Parecer ou despacho emitido: **nenhum**.
- Alternativas funcionais A/B/C: **não selecionadas**; B permanece prioritária apenas para exame.
- Revisão de Masters/Registries/menu: **não executada nesta etapa**.
- Workspace Replit: **não inspecionado, não modificado**.
- PR #730: **rascunho, sem merge ou publicação**.

**Sem novos IDs oficiais, mudanças normativas, implementação, testes, Design operacional, APIs ou alteração de planos.**
