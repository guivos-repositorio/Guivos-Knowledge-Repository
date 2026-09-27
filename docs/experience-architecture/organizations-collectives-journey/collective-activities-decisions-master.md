---
id: GKR-UX-COL-ACTIVITIES-DECISIONS-MASTER-001
title: Jornada de Organizações e Coletivos — Coletivo — Atividades, Consultas e Decisões — Documento Mestre de Superfície
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-ORGCOL-JOURNEY-READ-FIRST-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-058
related:
  - GKR-SURF-COL-005
  - GKR-SURF-COL-006
  - GKR-SURF-COL-007
  - GKR-JOURNEY-COLLECTIVE-001
---

# Coletivo — Atividades, Consultas e Decisões — Documento Mestre de Superfície

## 1. Responsabilidade

Este Documento Mestre governa a responsabilidade funcional de `GKR-SURF-COL-006` — Atividades, Consultas e Decisões.

`COL-006` concentra trabalho legitimamente relacionado a atividades do Coletivo, consultas estruturadas e decisões registradas dentro da autoridade aplicável.

```text
ATIVIDADE
≠ CONSULTA
≠ DECISÃO
≠ COMUNICAÇÃO OFICIAL
≠ PROTEÇÃO / MODERAÇÃO
```

A mesma superfície pode materializar essas naturezas funcionais sem fundi-las.

## 2. Oportunidades e fluxos especializados

O domínio lógico é denominado **Atividades e Oportunidades**, mas o crosswalk vigente identifica `COL-006` para atividades, consultas e decisões.

Este Master não cria um novo ID apenas para “oportunidades”. Quando uma oportunidade utilizar fluxo especializado existente, esse fluxo preserva sua própria identidade, autoridade, estados e transições.

```text
RELAÇÃO COM OPORTUNIDADE
≠ NOVA SUPERFÍCIE POR INFERÊNCIA
≠ NOVA TRANSIÇÃO POR SIMETRIA
```

## 3. Fronteiras

- `COL-005` governa comunicação oficial material.
- `COL-006` governa atividade, consulta e decisão no recorte próprio.
- `COL-007` governa proteção e moderação especializada.
- `COL-004` governa participantes e vínculos.

Uma decisão pode exigir comunicação oficial posterior, mas registrar a decisão não equivale a comunicá-la. Uma atividade pode exigir proteção, mas `COL-006` não absorve a decisão especializada de moderação.

## 4. Autoridade

Acesso ao contexto do Coletivo não concede autoridade universal para criar, alterar, decidir, encerrar ou publicar objetos.

Cada ação material deve respeitar:

- contexto correto;
- papel e representação vigentes;
- autoridade específica para o objeto;
- finalidade;
- público afetado;
- proteção;
- regras de governança aplicáveis.

Volume de participação, reação ou mensagem não substitui autoridade legítima.

## 5. Matriz operacional integrada

| Natureza | Job funcional | Autoridade mínima | Estado/resultado esperado | Não implica |
|---|---|---|---|---|
| atividade | compreender e operar uma atividade legítima do Coletivo | responsabilidade sobre a atividade e escopo concedido | estado operacional compreensível e continuidade legítima | impacto, pertencimento permanente ou resultado positivo |
| atualização de atividade | registrar mudança operacional material | responsabilidade sobre a atividade | alteração identificável, com proveniência e efeito compreensíveis | comunicação oficial universal |
| conversa de atividade | tratar comunicação contextual da atividade | participação/autoridade compatível com o canal | contexto preservado e arquivamento quando aplicável | participação permanente no Coletivo |
| consulta | coletar contribuição estruturada antes de decisão | autoridade de governança para abrir a consulta | contribuições recebidas no prazo e forma definidos | votação vinculante ou decisão automática |
| decisão | registrar autoridade, fundamento e efeito | instância legítima de decisão | decisão registrada, executável/revisável conforme regra | consenso, unanimidade ou comunicação já realizada |
| oportunidade especializada | encaminhar para responsabilidade própria quando existente | autoridade do fluxo especializado | continuidade no fluxo que possui autoridade própria | absorção do fluxo por COL-006 |

## 6. Atividades

Uma atividade deve permitir compreender, no recorte aplicável:

- identidade e finalidade;
- responsável;
- contexto do Coletivo;
- condição/estado;
- referência temporal quando material;
- requisitos legitimamente aplicáveis;
- alterações materiais;
- acessibilidade e segurança quando pertinentes;
- recursos e informações necessários;
- público/participantes visíveis somente no limite autorizado;
- registros autorizados após encerramento.

Participar de uma atividade não cria automaticamente participação permanente no Coletivo.

```text
ATIVIDADE REALIZADA
≠ RESULTADO COMPROVADO
≠ IMPACTO COMPROVADO
```

## 7. Conversa contextual da atividade

UXA-058 autoriza comunicação própria por atividade, separada do Coletivo permanente.

Ela pode reunir, quando aplicável, comunicados da atividade, ponto de encontro, horário, alterações, requisitos, segurança, acessibilidade, dúvidas, materiais e participantes visíveis conforme consentimento.

Após encerramento, a conversa pode ser arquivada preservando informação material e controles de privacidade.

Este Master não transforma conversa de atividade em chat irrestrito.

## 8. Consultas

Consulta é pedido estruturado de contribuição antes de decisão.

A consulta deve informar, conforme UXA-058:

- assunto;
- quem pode participar;
- prazo;
- forma de contribuição;
- quem decidirá;
- como as contribuições serão consideradas;
- conflitos conhecidos;
- resultado e registro posterior.

```text
CONSULTA
≠ DECISÃO

CONTRIBUIÇÃO
≠ VOTO VINCULANTE POR PADRÃO

REAÇÃO
≠ REGRA DE GOVERNANÇA
```

Este Master não inventa quórum, peso, maioria, unanimidade ou método de votação quando a autoridade específica não os definir.

## 9. Decisões

Decisão é registro de autoridade e fundamento.

A decisão deve informar, conforme UXA-058:

- autoridade;
- fundamento;
- alternativas consideradas;
- contribuições recebidas;
- efeito;
- responsável pela execução;
- revisão ou contestação.

A experiência não pode apresentar opinião, popularidade ou volume de mensagens como decisão formal.

## 10. Estados funcionais

A materialização deve distinguir, quando aplicáveis:

### 10.1 Atividade

- inexistente/vazia;
- em preparação;
- aguardando condição ou autoridade;
- programada;
- ativa/em curso;
- alterada materialmente;
- pausada;
- encerrada;
- arquivada;
- bloqueada;
- falha recuperável;
- estado indeterminado.

### 10.2 Consulta

- em preparação;
- aguardando autoridade;
- aberta;
- encerrada para contribuições;
- em consolidação/análise;
- concluída com registro posterior;
- cancelada legitimamente;
- contestada;
- bloqueada;
- estado indeterminado.

### 10.3 Decisão

- pendente;
- autoridade adicional necessária;
- registrada;
- em execução quando aplicável;
- contestada;
- em revisão;
- substituída/corrigida quando legitimamente suportado;
- encerrada com responsabilidades remanescentes.

Estados técnicos mais específicos não são inventados por este Master.

## 11. Ação consciente e efeitos

Criar rascunho, navegar, abrir objeto ou consultar informação não produz decisão nem altera atividade automaticamente.

Ações materiais devem possuir confirmação proporcional quando puderem:

- alterar condição da atividade;
- abrir/encerrar consulta;
- registrar decisão;
- afetar público legitimamente participante;
- produzir efeito difícil de reverter.

Processamento não deve ser representado como sucesso.

## 12. Concorrência, versão e proveniência

Alteração concorrente material exige revalidação antes do efeito.

A experiência deve preservar, quando necessário:

- versão/estado corrente;
- responsável;
- referência temporal;
- origem;
- mudança material;
- relação com versão anterior;
- resultado confirmado, falha ou indeterminação.

Editar decisão ou atividade não deve apagar silenciosamente informação material anterior quando a proveniência for necessária.

## 13. Erro, vazio e recuperação

Devem existir tratamentos proporcionais para:

- nenhuma atividade;
- nenhuma consulta aplicável;
- nenhuma decisão registrada;
- autoridade insuficiente;
- condição externa pendente;
- conteúdo protegido;
- dependência indisponível;
- conflito de governança;
- falha recuperável;
- estado indeterminado;
- objeto alterado por outra Pessoa autorizada.

Ausência de atividade ou contribuição não deve ser convertida em julgamento sobre uma Pessoa.

## 14. Comunicação oficial — COL-005

Quando uma atividade, consulta ou decisão exigir comunicação oficial material, `COL-005` permanece a responsabilidade própria para essa comunicação.

Este Master não declara uma nova `GKR-TRN-*` entre `COL-006` e `COL-005`, porque a arquitetura vigente não comprova ID estável para esse handoff.

```text
DECISÃO REGISTRADA
≠ DECISÃO COMUNICADA

RELAÇÃO FUNCIONAL
≠ TRANSIÇÃO REGISTRADA
```

## 15. Proteção e moderação — COL-007

Condição de segurança, privacidade, integridade ou moderação pode exigir continuidade para `COL-007`.

Essa relação não autoriza `COL-006` a aplicar punição, restrição ou medida especializada por inferência.

Nenhuma nova transição é criada neste Master.

## 16. Participação e Pessoa

Participar de consulta ou atividade não concede:

- administração do Coletivo;
- representação;
- acesso ao perfil completo de participantes;
- mensagem privada irrestrita;
- autoridade de decisão;
- participação permanente por inferência.

A perspectiva da Pessoa permanece separada e minimizada.

## 17. Aprendizados, evidências e impacto

Atividade e decisão podem produzir registros que posteriormente contribuam para aprendizados ou evidências, mas `COL-006` não transforma automaticamente execução em resultado ou impacto.

```text
ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO

CORRELAÇÃO
≠ CAUSALIDADE
```

A ausência atual de superfície exclusiva para Aprendizados e Evidências do Coletivo permanece uma lacuna explícita; este Master não a absorve silenciosamente.

## 18. Planos e capacidade comercial

Plano não altera autoridade, legitimidade da decisão, peso de contribuição ou proteção.

Este Master não inventa:

- número máximo de atividades;
- número máximo de consultas;
- poder de voto por plano;
- prioridade de decisão;
- alcance garantido;
- métricas de engajamento;
- automação comercial.

Capacidades documentadas de plano, quando aplicáveis, devem permanecer separadas da governança.

## 19. Acessibilidade

Prazo, estado, autoridade, requisito, efeito, proteção e resultado não podem depender exclusivamente de cor, ícone, posição, animação ou densidade visual.

Contribuição e decisão devem ser compreensíveis sem exigir interpretação de sinais puramente visuais.

## 20. Design — liberdade e limites

Design mantém liberdade criativa sobre composição, componentes, hierarquia, densidade, visualização e motion.

Design não pode:

- fundir atividade, consulta e decisão;
- apresentar popularidade como governança;
- transformar reação em voto;
- transformar atividade em impacto;
- absorver `COL-005` ou `COL-007`;
- criar nova superfície de oportunidade por conveniência;
- inventar transições;
- inventar métricas;
- usar low-fidelity como baseline visual canônica.

## 21. IA e prototipação — source lock

IA pode explorar materialização, mas não pode inventar:

- quórum;
- pesos;
- votação;
- critérios de decisão;
- papéis;
- autoridade;
- campos obrigatórios além dos contratos vigentes;
- estados técnicos;
- automações;
- métricas;
- transições.

```text
LACUNA
→ SINALIZAR
→ NÃO INVENTAR
```

## 22. Critérios de aceite

Este Master é funcionalmente suficiente quando a materialização:

1. preserva `COL-006` como responsabilidade de atividades, consultas e decisões;
2. mantém as três naturezas distinguíveis;
3. preserva oportunidades especializadas em suas autoridades próprias;
4. exige autoridade contextual para ações materiais;
5. implementa o contrato de consulta de UXA-058 sem inventar votação;
6. implementa o contrato de decisão de UXA-058 sem substituir governança por popularidade;
7. distingue atividade, resultado e impacto;
8. preserva comunicação oficial em `COL-005`;
9. preserva proteção/moderação em `COL-007`;
10. trata erro, concorrência, revisão e indeterminação;
11. não amplia dados pessoais por participação;
12. não cria transição sem evidência.

## 23. Lacunas preservadas

Permanecem abertas:

- cadeia estável completa de transições de `COL-006`;
- handoffs dedicados `COL-006 ↔ COL-005` e `COL-006 ↔ COL-007`;
- regras específicas de governança de cada Coletivo;
- infraestrutura técnica;
- notificações/canais técnicos;
- analytics/KPIs;
- superfície exclusiva de Aprendizados e Evidências;
- validação dedicada ponta a ponta de `COL-006`;
- implementação.

## 24. Estado de fechamento documental

```text
SURFACE GOVERNED
→ GKR-SURF-COL-006

FUNCTIONAL NATURES
→ ACTIVITY
→ CONSULTATION
→ DECISION

DEDICATED OPPORTUNITY SURFACE
→ NONE BY INFERENCE

KNOWN STABLE TRANSITION CHAIN
→ INCOMPLETE / PRESERVED GAP

NEW TRANSITION ID
→ NONE

NEW SURFACE ID
→ NONE

TECHNICAL DELIVERY
→ NOT CLAIMED

END-TO-END VALIDATION
→ NOT CLAIMED
```
