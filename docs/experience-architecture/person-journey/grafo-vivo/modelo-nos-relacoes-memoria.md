---
title: Grafo Vivo — Modelo Conceitual de Nós, Relações e Memória Contextual
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: exploratory_non_operational
---

# Grafo Vivo — Modelo Conceitual de Nós, Relações e Memória Contextual

> **Estudo não normativo.** As famílias de nós e tipos de relações abaixo são candidatos de discussão, não taxonomia canônica, esquema Neo4j aprovado, contratos de dados, novos IDs oficiais ou permissão para armazenar dados reais.

## 1. Papel do grafo

O grafo é uma **projeção explicável, temporizada, revisável e filtrada pelo consentimento e pela autoridade** sobre o contexto da Pessoa. Não é fonte de verdade autônoma. Visualização, relatório narrado e conversa devem partir de uma leitura coerente do contexto governado, mas podem ter ritmos de atualização próprios, desde que a versão da análise seja identificável.

O **Momento Atual** é foco narrativo, não uma classificação estática da Pessoa ou pontuação global.

## 2. Famílias candidatas de nós

| Família | Exemplos | Fronteira |
| --- | --- | --- |
| Contexto | Rotina, disponibilidade, condições de deslocamento e circunstâncias declaradas | Não presumir características não relatadas |
| Objetivos | Desejos, metas, horizontes, prioridades explicitadas | Intenção ≠ compromisso assumido ou conclusão |
| Recursos | Tempo, capacidades, ferramentas, suporte e disponibilidade financeira | Informação autodeclarada ≠ comprovação externa |
| Experiências e aprendizados | Cursos iniciados, atividades, aprendizados, experiências verificadas | Curso iniciado ≠ concluído; afirmação ≠ experiência comprovada |
| Lacunas e incertezas | Informações ausentes, interpretações contestadas, contradições | Lacuna ≠ deficiência pessoal ou score |
| Possibilidades | Caminhos hipotéticos, opções de exploração, oportunidades reais elegíveis | Possibilidade hipotética ≠ oportunidade ativa ou garantida |

Essas famílias são **visões de navegação**, não novas entidades de domínio PAS-001. Reutilizar taxonomias e objetos canônicos existentes quando aplicável; não aprovar nomes, cardinalidades ou ontologia aqui.

## 3. Relações candidatas

- `relaciona_se_a`: relação descritiva sem causalidade;
- `pode_contribuir_para`: possibilidade de contribuição, com qualificação e incerteza;
- `depende_de`: condição necessária quando houver suporte explícito;
- `pode_limitar`: restrição contextual, não impossibilidade definitiva;
- `foi_declarado_em`: proveniência de origem;
- `foi_revisado_por`: evento de confirmação/correção, quando autorizado;
- `substitui_versao`: encadeamento temporal de estado;
- `e_hipotese_de`: vínculo de simulação separada;
- `deriva_de`: conexão entre interpretação e evidência identificável.

**Nenhuma relação candidata deve virar aresta canônica por inferência automática de um modelo.** Tipos exatos e responsabilidades dependem de confrontação com PAS-001 e arquitetura de Intelligence.

## 4. Metadados conceituais mínimos

Para cada afirmação e relação candidata, avaliar: identidade opaca da Pessoa proprietária, tipo e referência ao objeto de domínio, conteúdo minimizado, origem/proveniência, classificação (`declarado`, `inferido`, `confirmado`, `contestado`, `desconhecido`, `hipotetico`), instante de registro, validade temporal, versão do contexto, finalidade e decisão de uso/persistência, referência à evidência quando houver, possibilidade de correção/retirada e responsável pela autoridade de domínio.

A listagem não é modelo de tabelas, esquema de grafo ou especificação de retenção. **Dados sensíveis exigem controle específico e minimização.** Não registrar áudio bruto ou transcrição integral no grafo simplesmente porque o mecanismo técnico o permite.

## 5. Evento de atualização: exemplo sintético

Contexto anterior: Pessoa deseja mudar de carreira, dispõe de seis horas semanais, não informou cursos.

Nova conversa: "Comecei um curso de programação há dois meses".

1. Captura sob finalidade autorizada.
2. Identificação de `curso_iniciado` como **declaração da Pessoa** — não comprovação.
3. Detecção da relação candidata com aprendizado e eventual interesse, **sem inferir proficiência ou objetivo de migrar para programação**.
4. Se houver ambiguidade relevante, confirmar; caso contrário, aplicar somente a política de persistência e personalização vigentes.
5. Registrar proveniência e tempo, se autorizado, e gerar projeção atualizada do subgrafo.
6. Se a mudança alterar substancialmente uma análise anterior, sinalizar sua versão e oferecer nova síntese/relatório.
7. Na hipótese "e se eu tivesse dez horas por semana", manter um **cenário temporário distinto**, sem substituir as seis horas declaradas.

## 6. Regras de integridade do contexto

- **Fonte de verdade**: objetos de Jornada, consentimentos e experiências permanecem com suas autoridades; Neo4j, se escolhido, funciona como memória/projeção relacional governada.
- **Atualização governada**: grafo não cria metas, Próximos Passos ou experiências por mera aparição de um nó.
- **Controle da Pessoa**: revisar, corrigir, contestar, solicitar exclusão/retirada e entender consequências conforme contratos aplicáveis.
- **Proveniência**: preservar distinção entre mensagem original, transcrição, representação derivada, inferência e evidência independente.
- **Temporalidade**: não confundir momento antigo com condição atual; indicar informações desatualizadas e conflitos.
- **Simulação isolada**: nunca misturar cenários hipotéticos à memória persistente como fatos.
- **Retirada/erro**: um evento de correção ou revogação deve invalidar projeções, caches e narrativas derivadas quando necessário.
- **Privacidade**: subgrafos individualizados, autenticação e escopo; não revelar a terceiros conexões íntimas por acesso transversal.
- **Experiência inclusiva**: cada explicação essencial do grafo precisa de equivalente em linguagem textual ou falada.

## 7. Organização da experiência

Três perspectivas candidatas, sem criar novas telas por inferência:
1. **Meu contexto** — o que está conhecido, aberto, revisável e relevante agora.
2. **Possibilidades** — como recursos e condições afetam caminhos hipotéticos ou oportunidades reais verificadas.
3. **Minha evolução** — diferenças temporais fundamentadas, sem score de desenvolvimento humano.

Cada perspectiva pode oferecer ação de "por que isso aparece?", exibir a origem e chamar a Intelligence para esclarecer; não confundir explicação com abertura automática de novas permissões.

## 8. Estrutura de integração conceitual

```text
Entrada legítima (texto/voz/anexo)
   → transcrição (quando necessária, passível de revisão)
   → extração de afirmações candidatas
   → validação contextual, finalidade e autoridade de persistência
   → fonte governada / memória com proveniência
   → projeção relacional autorizada
   → subgrafo explicável na interface
   → relato narrado versionado ou conversa orientada
```

A integração com provedores externos de voz deve receber o **mínimo contexto necessário**. O Grok/xAI é candidato a TTS e Speech-to-Speech; não assume automaticamente a governança de memória ou decisões da Intelligence.

## 9. Critérios de avaliação futura

- O usuário compreende o que é fato, inferência ou hipótese?
- O histórico de correção/revogação chega aos nós e relatórios derivados?
- O grafo permanece utilizável com poucos ou muitos nós e no celular?
- A orientação oral transmite a mesma informação importante da exploração visual?
- Um novo dado é contextualizado sem criar objetivos, provas ou obrigações?
- Há controle de autorização, acesso, custo por interação e latência?
- É possível explicar por que uma conexão ou oportunidade aparece?

## 10. Pendências de competência

Resolver com os responsáveis vigentes, antes de qualquer implementação: ponto de entrada e relação com PER-008; modelo lógico e vocabulário sob PAS-001; escopos de persistência/personalização conforme PER-007; fonte de verdade de oportunidades e experiências; eventos de mudança, explicabilidade e versões; regras de áudio; mecanismos de retirada e retenção; e gates de prototipação/engenharia.

**Nenhum novo PER-ID, nova autoridade normativa, seleção de base física ou liberação operacional decorre deste estudo.**
