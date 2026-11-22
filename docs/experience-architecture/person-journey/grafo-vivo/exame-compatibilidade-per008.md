---
title: Grafo Vivo — Exame de Compatibilidade com PER-008 — Hoje
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: diagnostic_non_operational
---

# Grafo Vivo — Exame de Compatibilidade com PER-008 — Hoje

> **Diagnóstico condicionado, sem adjudicação funcional.** Este documento não altera PER-008, PER-007, PER-010/011/012, GPA-006, GIA-COG-001, PAS-001, Surface Registry, Transition Registry ou contratos de planos. Não autoriza nova superfície, fluxo, APIs, protótipos, testes ou implementação.

## 1. Questão examinada

Em que medida a proposta de exploração visual, relatório narrado e conversa com a Intelligence pode ser apresentada a partir de **PER-008 — Hoje** sem converter a superfície de síntese em dashboard de performance humana, absorver responsabilidades especializadas ou introduzir novas transições?

## 2. Premissas documentais verificadas

- `PER-007` apresenta compreensão revisável e preserva **decisões distintas de persistência e personalização**; a chegada a PER-008 é subordinada a `TRN-007`.
- `PER-008` reúne **primeira entrada** e **estado recorrente**; sua finalidade é uma síntese contextual para orientar a escolha da Pessoa, e não um catálogo, feed ou painel de produtividade.
- A primeira entrada pode legitimamente não apresentar histórico, objetivo, passo, oportunidade, evolução ou qualquer conteúdo contextual sofisticado.
- `PER-008` deve manter caminhos específicos para aprofundamentos existentes: `TRN-008/009` para Objetivos (`PER-010`), `TRN-010/011` para Próximos Passos (`PER-011`), `TRN-012/013` para Evolução (`PER-012`), quando aplicáveis.
- Retornar a Hoje **não** salva edição incompleta, confirma sugestão, aceita passo, reconhece evolução ou amplia autorização.
- A ausência de personalização não bloqueia o acesso a Hoje.
- Permissões, conteúdo confirmado, atualidade e finalidade limitam qualquer síntese ou uso de contexto.
- Modelos de grafos, voz e memória contextual permanecem capacidades candidatas, sem contrato técnico.

## 3. Matriz de compatibilidade — diagnóstico

| Comportamento candidato | Compatibilidade inicial | Condições | Lacuna de decisão |
| --- | --- | --- | --- |
| Convite discreto para entender o contexto por outro formato | **Potencialmente compatível** | Conteúdo e affordance condicionados a base e autorização reais; não impor participação | Definir se é estado/ação interna de PER-008 ou acesso a função distinta |
| Exibir miniatura de relações como elemento de síntese | **Potencialmente compatível** | Baixa complexidade, legibilidade, nenhuma inferência apresentada como fato | Autoridade para expansão do grafo, edição e filtros |
| Abrir grafo expandido e navegar por múltiplos nós | **Exige adjudicação** | Não absorver Objetivos, Próximos Passos ou Evolução; não criar handoffs indiretos | Responsabilidade funcional, localização e transições |
| Escutar síntese equivalente ao conteúdo de Hoje | **Potencialmente compatível** | Acessibilidade, consentimento aplicável e versionamento; narração opcional | Serviço/estado de áudio, tratamento de falhas, retenção |
| Escutar relatório completo, histórico ou orientação ampliada | **Exige adjudicação** | Relatório não pode extrapolar limites de PER-008 nem declarar evolução sem autoridade | Fonte da síntese, profundidade e relação com PER-012 |
| Conversar sobre o que aparece em Hoje | **Potencialmente compatível como hipótese** | Explicações da Intelligence sem alterar domínio ou autorizações por simples conversa | Delimitar estado interno versus canal transversal |
| Incorporar novas informações das conversas à memória duradoura | **Não autorizado por PER-008 isoladamente** | Verificar escolhas e competências vigentes de dados, revisão e persistência | Política de contexto contínuo, confirmação, revogação e proveniência |
| Simular "e se..." a partir do contexto atual | **Exige adjudicação** | Cenário separado de fatos e persistência; não criar objetivo ou próximo passo | Limites, duração, armazenamento e apresentação |
| Destaques de mudanças na volta a Hoje | **Potencialmente compatível** | Apenas diferença verdadeira, temporalmente referenciada e autorizada | Regra de baseline/snapshot e dependências com PER-012 |
| Reconhecer evolução pela mudança do grafo | **Incompatível** | Mudança visual não equivale a trajetória reconhecida | Deve permanecer sob PER-012 e PAS-001 |
| Navegar diretamente de Objetivos para Próximos Passos pelo grafo | **Incompatível com os handoffs vigentes** | Preservar rotas registradas | Exigiria adjudicação expressa do Transition Registry |
| Exigir grafo, narração, conversa ou personalização para usar Hoje | **Incompatível** | Uso opcional e equivalência acessível | Nenhuma |
| Exibir contexto privado a terceiros ou provedores sem escopo legítimo | **Incompatível** | Minimização, finalidade e autoridade específica | Avaliação de segurança de cada integração |

**Nota:** “potencialmente compatível” significa apenas que não foi encontrada incompatibilidade frontal de finalidade no exame limitado; **não é aprovação funcional**, nem criação de estado, CTA ou responsabilidade.

## 4. Três alternativas de acomodação a comparar

### A — Complemento discreto em Hoje

PER-008 permanece como síntese. Um resumo opcional de relações, explicação narrada do conteúdo elegível e perguntas sobre a própria síntese são explorados como **comportamentos candidatos internos**. Não implica que o conjunto completo de grafo, simulação ou diálogo contínuo possa ser absorvido.

**Vantagem:** menor risco de duplicar a finalidade de Hoje. **Risco:** capacidades profundas exigirem escopo não contemplado.

### B — Hoje como entrada, aprofundamento sob autoridade própria

Hoje apresenta apenas acesso conceitual discreto para explorar/escutar/conversar; a experiência expandida exige **delimitação funcional e transições a adjudicar**. Não criar automaticamente um novo `PER-ID`.

**Vantagem:** separa síntese de exploração profunda. **Risco:** complexidade documental e de navegação.

### C — Distribuição por responsabilidades já existentes

Hoje oferece síntese; visualizações e explicações especializadas de objetivos, passos e evolução permanecem dentro de `PER-010/011/012`, conforme seus próprios contratos. O diálogo transversal e a narração ampliada exigiriam exame específico.

**Vantagem:** respeita especialização de domínio. **Risco:** fragmentação da experiência e perda de fluidez multimodal.

**Recomendação para próximo exame: B como hipótese de arquitetura funcional a confrontar, não como escolha aprovada.** Pode combinar A para o resumo e C para aprofundamentos autorizados, desde que a direção de UX e os Registries adjudquem as fronteiras.

## 5. Estados e exemplos a avaliar posteriormente

| Cenário | Tratamento seguro no estudo |
| --- | --- |
| Primeira entrada com compreensão revisada, sem histórico | Síntese neutra, áudio opcional se permitido, nenhum grafo preenchido artificialmente |
| Primeira entrada sem personalização | Continuidade funcional legítima, sem pedir autorização disfarçada |
| Retorno com contexto atualizado | Exibir apenas alterações verificadas e pertinentes, sem pontuar evolução |
| Pessoa diz "comecei um curso" | Informação declarada candidata; persistência exige autoridade vigente, sem reconhecer comprovação |
| Pessoa pergunta "e se eu estudasse 10h?" | Cenário hipotético temporário, separado do contexto atual |
| Grok em falha ou áudio indisponível | Informação textual acessível e possibilidade de continuar sem voz |
| Revogação de autorização após narração anterior | Revisar acesso a snapshots/áudios/caches, observando regras vigentes de retenção e exclusão |
| Pessoa seleciona um objetivo no grafo | Explicação permitida, sem editar, aceitar ou criar navegação não contratada |

## 6. Fronteiras de integração

- **Guivos Intelligence:** compreender e explicar sob GPA-006 e GIA-COG-001; não assumir decisões da Pessoa.
- **Fonte governada da Journey:** objetos, permissões, estados e referências oficiais; não delegar alterações ao desenho do grafo.
- **Grafo/memória relacional:** projeção contextual e relações com origem, versão e incerteza, sujeita a retenção/retirada autorizadas.
- **Grok/xAI (candidato):** TTS e conversação por voz; deve receber apenas contexto estritamente necessário e não consolidar memória autonomamente.
- **Transcrição (Gemini ou alternativa):** representação revisável de entrada, sem equivaler automaticamente à autorização para guardar conteúdo.
- **Superfícies de Objetivos/Passos/Evolução:** mantêm controle de seus objetos e handoffs vigentes.

## 7. Lacunas que bloqueiam formalização

1. **P-01 — Competência:** quem governa exploração expandida e diálogo contínuo, distinguindo interface de responsabilidade de domínio?
2. **P-02 — Localização:** em quais estados/superfícies já reconhecidos caberiam convite discreto, narração e grafo compacto?
3. **P-03 — Navegação:** quais ações exigem novas decisões de Registry, sem inferir link direto entre PER-010/011/012?
4. **P-04 — Dados:** qual permissão cobre uso contextual efêmero versus persistência posterior e personalização?
5. **P-05 — Relatórios:** como a narração versionada se relaciona a síntese Hoje e interpretação de Evolução?
6. **P-06 — Integrações:** que dados mínimos podem ser enviados a Grok e outros serviços, com quais controles?
7. **P-07 — Revogação:** como invalidar versões derivadas e memórias quando houver correção ou retirada?
8. **P-08 — Planos:** quais capacidades são comuns ou sujeitas a limites legítimos? Não criar entitlements.
9. **P-09 — Acessibilidade:** qual experiência equivalente existe sem grafo e sem áudio?

## 8. Parecer

**Conclusão condicionada:** a finalidade de PER-008 comporta o exame de **formas opcionais de explicar sua síntese**, mas não sustenta, isoladamente, a absorção de um ambiente completo de exploração, simulação, narração estendida e memória contínua. Tampouco autoriza novas transições, finalidades de dados ou alterações em objetivos, passos e evolução.

**Próxima atividade sugerida:** quadro focal de fronteiras entre *síntese em Hoje*, *exploração expandida*, *explicação narrada*, *conversa contextual* e *persistência de novas informações*, com consulta aos Registries e às autoridades de dados, para adjudicação posterior pela instância competente.

**Estado:** diagnóstico documental não normativo; nenhuma seleção final de alternativa A/B/C e nenhuma autorização para Design, Replit, APIs, testes, publicação ou IDs oficiais.
