---
id: GKR-UX-PER007-MASTER-001
title: Jornada da Pessoa — PER-007 — Compreensão Inicial Revisável — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-023
  - UXA-037
  - UXA-097
related:
  - GKR-UX-PER006-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - PER-006
  - PER-007
  - PER-008
  - TRN-006
  - TRN-007
---

# Jornada da Pessoa — PER-007 — Compreensão Inicial Revisável — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-007 — Compreensão Inicial Revisável` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

A superfície existe para apresentar a compreensão inicial como **hipótese revisável**, permitir que a Pessoa examine sua origem e natureza, corrija ou rejeite o que não representa sua realidade e decida conscientemente, de forma independente, sobre persistência e personalização.

Este documento não cria tela, layout, wireframe, UI, protótipo, sistema visual ou implementação.

```text
PER-006 — PROCESSAMENTO VISÍVEL
→ TRN-006 / LOCALMENTE VALIDADA
→ PER-007 — COMPREENSÃO INICIAL REVISÁVEL
→ TRN-007 / INTEGRALMENTE VALIDADA
→ PER-008 — HOJE
```

## 2. Papel na Jornada

`PER-007` governa o intervalo entre a disponibilidade de uma compreensão inicial e a decisão consciente que pode habilitar a continuidade para `Hoje`.

Ela governa:

- apresentação da compreensão como hipótese, não diagnóstico;
- distinção entre afirmações confirmadas e inferidas;
- origem e natureza das afirmações;
- confiança somente quando houver inferência e sem equivalê-la a certeza;
- lacunas, desconhecidos e base insuficiente sem preenchimento artificial;
- revisão, correção, rejeição, contestação e manutenção em aberto;
- separação entre conteúdo de origem e interpretação derivada;
- decisão sobre persistência;
- decisão independente sobre personalização;
- continuidade legítima sem personalização;
- exclusão da compreensão quando aplicável;
- confirmação explícita antes de `TRN-007`;
- handoff governado para `PER-008 — Hoje`.

Ela não governa:

- processamento material anterior;
- diagnóstico clínico ou classificação da Pessoa;
- inferências sensíveis automáticas;
- nova finalidade de uso;
- política jurídica final de retenção;
- mecanismo técnico de persistência ou personalização;
- arquitetura interna de IA;
- conteúdo especializado de `Hoje`.

## 3. Entrada legítima

A entrada ocorre por `TRN-006 — PER-006 → PER-007`, localmente validada por `UXA-037`.

A compreensão chega como material temporário disponível para revisão. A passagem não significa que:

- a compreensão seja fato;
- a Pessoa tenha confirmado as afirmações;
- uma inferência tenha sido aceita;
- persistência tenha sido autorizada;
- personalização tenha sido autorizada.

```text
COMPREENSÃO DISPONÍVEL
≠ COMPREENSÃO CONFIRMADA
≠ PERSISTÊNCIA
≠ PERSONALIZAÇÃO
```

Este Master não promove `TRN-006`.

## 4. Job da Pessoa

A Pessoa precisa conseguir:

1. compreender que está diante de uma leitura inicial e revisável;
2. reconhecer o que veio de seu conteúdo e o que foi derivado;
3. distinguir afirmações confirmadas de inferidas;
4. compreender confiança e incerteza sem confundi-las com certeza;
5. identificar lacunas e desconhecidos;
6. revisar cada afirmação relevante;
7. confirmar, corrigir, rejeitar, contestar ou manter em aberto quando aplicável;
8. compreender o efeito de retirar ou excluir conteúdo;
9. escolher conscientemente se a compreensão poderá persistir;
10. escolher independentemente se poderá ser usada para personalização;
11. continuar sem personalização quando essa for sua escolha;
12. confirmar conscientemente antes de seguir para `Hoje`.

## 5. Natureza da compreensão

A compreensão inicial deve ser apresentada como **hipótese revisável**.

São incompatíveis com o contrato:

- diagnóstico;
- verdade consolidada sobre a Pessoa;
- linguagem de certeza quando existe inferência;
- conclusão moral sobre escolhas ou comportamento;
- afirmação de que a Guivos “conhece” definitivamente a Pessoa;
- preenchimento artificial de informação ausente.

```text
COMPREENSÃO INICIAL
→ HIPÓTESE REVISÁVEL

HIPÓTESE
≠ DIAGNÓSTICO
≠ VERDADE CONSOLIDADA
```

## 6. Afirmações e natureza

Quando uma compreensão combinar conteúdos de naturezas diferentes, a Pessoa deve conseguir distinguir o que é:

- confirmado por ela;
- inferido;
- desconhecido;
- mantido em aberto;
- rejeitado ou contestado, quando aplicável.

Uma mesma frase não deve receber simultaneamente os rótulos de confirmada e inferida sem separação explícita dos trechos correspondentes.

Confirmação parcial não transforma uma inferência rejeitada em fato.

## 7. Origem e interpretação derivada

A experiência deve preservar a distinção entre:

```text
CONTEÚDO DE ORIGEM
≠ TRANSCRIÇÃO, QUANDO APLICÁVEL
≠ REPRESENTAÇÃO DERIVADA
≠ INTERPRETAÇÃO INFERIDA
```

A Pessoa deve conseguir reconhecer a relação material entre uma afirmação e sua origem sem exposição de raciocínio interno detalhado.

Corrigir ou rejeitar uma interpretação derivada não deve silenciosamente reescrever o conteúdo de origem.

## 8. Confiança, incerteza e lacunas

Confiança somente deve ser apresentada quando houver inferência e quando existir base legítima para comunicá-la.

```text
CONFIANÇA
≠ CERTEZA
```

A experiência deve admitir:

- confiança limitada;
- incerteza;
- evidência insuficiente;
- desconhecido;
- questão em aberto.

Não se deve criar precisão numérica, score humano ou percentual de certeza sem autoridade real.

## 9. Revisão consciente

A revisão não deve possuir resposta preselecionada.

Quando aplicável, a Pessoa deve poder:

- confirmar;
- corrigir;
- rejeitar;
- contestar;
- manter em aberto;
- retirar conteúdo do conjunto aplicável;
- voltar para revisar material anterior dentro das rotas legitimamente contratadas.

Nenhuma ausência de ação deve ser interpretada como confirmação.

## 10. Correção, retirada e exclusão

Correção, retirada e exclusão possuem escopos diferentes e não devem ser tratadas como sinônimos.

A solução deve tornar compreensível, conforme a autoridade aplicável:

- o que está sendo corrigido;
- o que deixa de participar da compreensão;
- o que é excluído;
- o que permanece como conteúdo de origem sob controles anteriores;
- quando a compreensão precisa ser recalculada sem o item afetado.

A implementação técnica e jurídica desses efeitos permanece fora deste Master.

## 11. Persistência

A decisão de persistir a compreensão deve ser consciente e separada das demais decisões.

```text
CONFIRMAR COMPREENSÃO
≠ PERSISTIR COMPREENSÃO
```

A experiência não pode:

- preselecionar persistência;
- inferir persistência pela continuidade;
- tratar persistência como condição moralmente superior;
- transformar persistência em autorização para nova finalidade.

Quando a autoridade corrente oferecer uso somente na sessão, seu efeito deve permanecer distinguível de persistência posterior.

## 12. Personalização

Personalização exige escolha própria e independente.

```text
PERSISTÊNCIA
≠ PERSONALIZAÇÃO

PERSONALIZAÇÃO
≠ NOVA FINALIDADE
```

A experiência não pode:

- preselecionar personalização;
- inferi-la da persistência;
- condicionar toda continuidade à personalização;
- expandir a finalidade originalmente apresentada.

A opção de continuar sem personalização deve permanecer legítima.

## 13. Combinações legítimas de decisão

Persistência e personalização devem ser apresentadas como decisões únicas e independentes dentro de seus respectivos grupos.

A autoridade corrente preserva, entre outras consequências:

- se `Excluir esta compreensão` for escolhido, personalização fica indisponível e a continuidade ocorre sem personalização;
- se `Usar somente nesta sessão` for escolhido, eventual personalização só pode valer para a sessão e finalidade apresentadas;
- continuar sem personalização não representa erro ou experiência inferior.

Nenhuma combinação incompatível deve ser silenciosamente aceita.

## 14. Base insuficiente

Quando não houver base suficiente para uma hipótese pessoal útil:

- não se deve fabricar compreensão;
- não se deve pressionar a Pessoa a compartilhar mais;
- a ausência de hipótese deve ser explícita;
- alternativas legítimas podem incluir revisar, compartilhar algo adicional voluntariamente, continuar sem personalização ou encerrar.

```text
BASE INSUFICIENTE
≠ FALHA DA PESSOA
≠ OBRIGAÇÃO DE EXPOSIÇÃO ADICIONAL
```

## 15. Estados funcionais

O Design deve conseguir acomodar, quando aplicável:

1. compreensão inicial disponível;
2. compreensão em revisão;
3. afirmação confirmada;
4. afirmação inferida;
5. confiança/incerteza aplicável;
6. desconhecido ou questão em aberto;
7. correção;
8. rejeição ou contestação;
9. retirada;
10. necessidade de recalcular hipótese;
11. base insuficiente;
12. escolha de persistência;
13. escolha independente de personalização;
14. exclusão da compreensão;
15. continuidade sem personalização;
16. confirmação final;
17. estado pronto para `TRN-007`.

```text
ESTADOS FUNCIONAIS
≠ TELAS CANÔNICAS
≠ NOVOS PER-IDs
```

## 16. Confirmação e handoff para Hoje

`TRN-007 — PER-007 → PER-008` é **integralmente validada** por `UXA-097`.

A sequência corrente é:

```text
REVISAR COMPREENSÃO
→ ESCOLHER PERSISTÊNCIA
→ ESCOLHER PERSONALIZAÇÃO INDEPENDENTEMENTE
→ CONFIRMAR
→ TRN-007
→ PER-008 — HOJE
```

A confirmação deve usar o estado canônico vigente.

Se compreensão ou permissões mudarem antes da transição, `Hoje` deve receber o estado vigente, não uma cópia desatualizada.

Navegar para `Hoje` não amplia consentimento, não cria nova finalidade e não presume avanço pessoal.

## 17. Primeira entrada em Hoje

A primeira entrada em `Hoje` deve ser neutra diante de ausência legítima de histórico.

`Hoje` pode refletir a compreensão confirmada e oferecer continuidades legítimas, mas `PER-007` não deve fabricar:

- histórico inexistente;
- avanço;
- urgência;
- oportunidade;
- Próximo Passo;
- personalização não escolhida.

A responsabilidade detalhada de `PER-008` pertence ao seu próprio Master futuro.

## 18. Proteções

Devem permanecer verdadeiras:

- autenticação não autoriza processamento, persistência ou personalização;
- compreensão é hipótese, não diagnóstico;
- confirmado e inferido permanecem distinguíveis;
- confiança não equivale a certeza;
- inferência sensível automática não é autorizada por este Master;
- engajamento não equivale a evolução;
- persistência não autoriza personalização;
- personalização não cria nova finalidade;
- publicidade não recebe autorização por consequência;
- continuar sem personalização permanece disponível;
- nenhuma escolha é apresentada como moralmente superior.

## 19. Linguagem

A linguagem deve:

- tratar a compreensão como inicial e revisável;
- distinguir hipótese de fato;
- evitar diagnóstico;
- evitar certeza indevida;
- explicar confiança e incerteza de modo compreensível;
- não culpabilizar rejeição ou correção;
- não pressionar persistência ou personalização;
- deixar claros os efeitos das escolhas;
- tratar base insuficiente de forma neutra.

## 20. Acessibilidade

A futura solução deve considerar:

- operação por teclado;
- foco visível;
- estados não dependentes apenas de cor;
- rótulos de natureza compreensíveis por tecnologia assistiva;
- controles de revisão identificáveis;
- escolhas mutuamente exclusivas corretamente representadas;
- mensagens de consequência compreensíveis;
- zoom e responsividade;
- ausência de movimento obrigatório para compreender conteúdo.

## 21. Conteúdo sintético para Design

Design pode simular:

- afirmações fictícias confirmadas;
- inferências fictícias não sensíveis;
- níveis qualitativos de confiança quando coerentes;
- lacunas e desconhecidos;
- correção, rejeição e manutenção em aberto;
- base insuficiente;
- escolhas de persistência;
- escolhas independentes de personalização;
- continuidade sem personalização;
- handoff simulado para `Hoje`.

Não pode apresentar como real:

- diagnóstico;
- dado pessoal real;
- inferência sensível real;
- score humano;
- precisão inventada;
- persistência técnica real;
- personalização técnica real;
- autorização adicional.

## 22. Liberdade de Design

A designer pode decidir:

- quantidade de frames;
- composição;
- componentes;
- hierarquia;
- tipografia;
- paleta;
- iconografia;
- densidade;
- motion;
- microinterações;
- representação visual de origem, natureza, confiança e revisão;
- responsividade;
- forma visual das decisões de persistência e personalização.

O GKR não define baseline visual obrigatório para `PER-007`.

Referências visuais anteriores não são autoridade estética corrente.

## 23. Uso por IA

Quando IA for usada para explorar `PER-007`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. Surface Registry e detalhamento da Pessoa;
5. Transition Registry;
6. `UXA-023`;
7. `UXA-037`;
8. `UXA-097`;
9. `GKR-UX-PER006-MASTER-001` para a fronteira de entrada.

A IA não pode:

- transformar hipótese em fato;
- criar diagnóstico;
- inventar confiança ou precisão;
- preencher lacuna artificialmente;
- confirmar em nome da Pessoa;
- preselecionar persistência;
- preselecionar personalização;
- expandir finalidade;
- inventar inferência sensível;
- promover `TRN-006`;
- alterar `TRN-007`;
- criar novo `PER-ID`;
- iniciar Product Engineering.

## 24. Critérios de Aceite Funcional

Uma futura solução visual de `PER-007` é aceitável quando:

1. apresenta a compreensão como hipótese revisável;
2. não apresenta diagnóstico ou verdade consolidada;
3. distingue confirmado de inferido;
4. preserva origem e interpretação derivada;
5. confiança aparece somente quando aplicável e não equivale a certeza;
6. lacunas e desconhecidos não são preenchidos artificialmente;
7. revisão não possui resposta preselecionada;
8. correção, rejeição, contestação e manutenção em aberto são acomodadas quando aplicáveis;
9. confirmação parcial não transforma inferência rejeitada em fato;
10. persistência é escolha consciente;
11. personalização é escolha independente;
12. persistência não autoriza personalização;
13. personalização não cria nova finalidade;
14. continuidade sem personalização é legítima;
15. base insuficiente não pressiona exposição adicional;
16. `TRN-006` permanece localmente validada;
17. `TRN-007` permanece integralmente validada;
18. navegar para `Hoje` não amplia consentimento;
19. nenhuma nova superfície é criada;
20. Product Engineering permanece não liberado.

## 25. Limites

Este Documento Mestre não:

- cria tela final;
- cria Figma;
- cria protótipo;
- define modelo ou fornecedor de IA;
- define política jurídica final;
- implementa processamento;
- implementa persistência;
- implementa personalização;
- implementa armazenamento ou retenção;
- autoriza inferências sensíveis;
- cria diagnóstico;
- define conteúdo completo de `Hoje`;
- executa testes com usuários;
- altera `TRN-006`;
- altera `TRN-007`;
- cria `PER-008`;
- inicia Product Engineering.

## 26. Estado Corrente

```text
PER-007 MASTER
→ CURRENT DESIGN DEFINITION

ENTRY
→ TRN-006 / LOCALLY VALIDATED

JOB
→ REVIEW INITIAL UNDERSTANDING AS HYPOTHESIS
→ DISTINGUISH CONFIRMED / INFERRED / UNKNOWN
→ DECIDE PERSISTENCE
→ DECIDE PERSONALIZATION INDEPENDENTLY

UNDERSTANDING
→ REVISABLE HYPOTHESIS
→ NOT DIAGNOSIS

PERSISTENCE
→ CONSCIOUS CHOICE

PERSONALIZATION
→ INDEPENDENT CONSCIOUS CHOICE

CONTINUE WITHOUT PERSONALIZATION
→ LEGITIMATE

TRN-007
→ INTEGRALLY VALIDATED / UNCHANGED

NEXT DOCUMENTATION TARGET
→ PER-008 — HOJE

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
