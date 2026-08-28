---
id: GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
title: Organizações e Coletivos — Mapa Lógico de Superfícies e Estados da Experiência Autenticada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-27
normative: false
maturity: authenticated_surface_state_map_defined_pre_priority_flows
depends_on:
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - UXA-014
  - UXA-019
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-100-A3
  - UXA-100-A4
---

# Organizações e Coletivos — Mapa Lógico de Superfícies e Estados da Experiência Autenticada

## 1. Finalidade

Este documento materializa o **mapa lógico de superfícies, responsabilidades e estados** da futura experiência autenticada de Organização e Coletivo.

Ele parte da Arquitetura da Informação já definida e responde:

> **Quais responsabilidades já possuem IDs no registro global, como elas se agrupam na nova IA, quais estados precisam ser suportados e onde ainda existe lacuna antes de definir fluxos prioritários e wireframes?**

O mapa não cria composição visual.

```text
MAPA DE SUPERFÍCIES
≠ WIREFRAME
≠ LAYOUT
≠ UI
≠ PROTÓTIPO
≠ IMPLEMENTAÇÃO
```

## 2. Decisão de taxonomia

A reconciliação do `GKR-JOURNEY-SURFACE-REGISTRY-001` mostra que as responsabilidades principais necessárias para esta fase já possuem IDs suficientes para organizar o primeiro mapa autenticado.

Portanto:

> **Nenhum novo `GKR-SURF-ORG-*` ou `GKR-SURF-COL-*` é criado neste incremento.**

A regra é reutilizar responsabilidades existentes e somente criar novo ID no futuro quando houver necessidade funcional que não possa ser representada sem ambiguidade por uma responsabilidade atual.

```text
NOVA IA
≠ NOVO ID AUTOMÁTICO

NOVO AGRUPAMENTO
≠ NOVA TELA AUTOMÁTICA

RESPONSABILIDADE EXISTENTE
≠ WIREFRAME VIGENTE
```

## 3. Maturidade não promovida

Este mapa reorganiza a leitura, mas não promove maturidade.

Em especial:

- `GKR-SURF-ORG-001` continua contratado, com wireframe principal pendente;
- `GKR-SURF-COL-002` continua parcial/materialização local e não é baseline final da UX principal;
- `UXA-015..018` permanecem históricos `superseded`;
- fluxos especializados já validados preservam sua validação própria;
- responsabilidades programadas/contratadas continuam sem materialização quando esse for seu estado;
- nenhum SVG histórico é reativado.

## 4. Camadas do mapa

O mapa utiliza quatro tipos de elemento:

### 4.1 Context layer

Informação transversal necessária para interpretar qualquer superfície:

- participante ativo;
- unidade/contexto;
- papel;
- autoridade e limites.

Não recebe novo surface ID nesta fase.

### 4.2 Primary synthesis responsibility

Responsabilidade de entrada que sintetiza Momento, atenção e Próximos Passos sem duplicar a fonte de verdade.

- Organização: `GKR-SURF-ORG-001`;
- Coletivo: `GKR-SURF-COL-002`.

### 4.3 Domain responsibility

Responsabilidade ligada a objetos de trabalho específicos, como oportunidade, participação, relação ou evidência.

### 4.4 Specialized responsibility

Fluxos com autoridade independente, por exemplo Planos e cobrança.

Eles se conectam à experiência principal sem defini-la.

## 5. Mapa macro — Organização

```text
CONTEXTO ATIVO / AUTORIDADE
        ↓
GKR-SURF-ORG-001
Visão Geral da Organização
        ├── OPORTUNIDADES E PROGRAMAS
        │   ├── GKR-SURF-ORG-002 — cadastro de oportunidade
        │   └── GKR-SURF-ORG-003 — oportunidade aprovada/ativa
        │
        ├── RELAÇÕES
        │   ├── GKR-SURF-ORG-004 — proposta de relação
        │   ├── GKR-SURF-ORG-005 — avaliação/negociação bilateral
        │   └── GKR-SURF-ORG-006 — relação ativa/revisão
        │
        ├── RESPONSABILIDADES / EVIDÊNCIAS
        │   └── GKR-SURF-ORG-007 — resultados e evidências institucionais
        │
        └── PLANOS E CAPACIDADE [especializado]
            ├── GKR-SURF-ORG-301
            ├── GKR-SURF-ORG-302
            ├── GKR-SURF-ORG-303
            └── GKR-SURF-ORG-304
```

`Organização e Autoridade`, definido na IA, permanece como **context layer transversal** e como responsabilidade informacional dentro do contexto institucional, sem novo surface ID neste momento.

## 6. Organização — GKR-SURF-ORG-001

### Responsabilidade vigente

`Visão Geral da Organização`.

### Papel no novo mapa

Torna-se a responsabilidade semântica de síntese da IA autenticada.

Ela deve futuramente permitir compreender:

- contexto institucional ativo;
- Momento institucional;
- atenção material;
- objetos em movimento;
- riscos/prazos relevantes;
- relações que exigem decisão;
- evidência/resultado reconhecido quando sustentado;
- Próximos Passos justificados.

### Estado preservado

```text
GKR-SURF-ORG-001
→ contracted responsibility
→ main authenticated wireframe pending
→ UXA-015 historical/superseded
→ UXA-017 historical/superseded
```

O mapa não reutiliza o antigo SVG como baseline.

## 7. Organização — estados lógicos de ORG-001

Os estados abaixo são perfis da mesma responsabilidade e **não criam novas superfícies por padrão**:

- `ORG-OV-NORMAL` — contexto compreensível, sem atenção material prioritária;
- `ORG-OV-ATTENTION` — existe atenção material com motivo identificável;
- `ORG-OV-INCOMPLETE` — informação material ausente ou incompleta;
- `ORG-OV-AUTHORITY` — ação relevante depende de autoridade adicional;
- `ORG-OV-CONTESTED` — informação, evidência ou interpretação relevante está contestada;
- `ORG-OV-BLOCKED` — proteção, privacidade, risco ou dependência impede avanço;
- `ORG-OV-NO-EVIDENCE` — atividade existe, mas não há evidência suficiente para afirmar avanço/resultado;
- `ORG-OV-CAPACITY` — capacidade/limite comercial exige decisão contextual sem converter a tela em upsell.

Os códigos acima são IDs internos deste mapa e não entram no registro global como `GKR-SURF-*`.

## 8. Organização — Oportunidades e Programas

### GKR-SURF-ORG-002

Responsabilidade: cadastro de oportunidade.

Estado atual: **validado** no fluxo especializado.

No novo mapa:

- permanece ponto legítimo de criação/edição aplicável;
- não vira tela genérica para todo tipo de programa por inferência;
- futura necessidade de programa com comportamento materialmente distinto deverá ser examinada antes de criar novo ID.

### GKR-SURF-ORG-003

Responsabilidade: oportunidade aprovada/ativa.

Estado atual: **validado**.

No novo mapa, concentra a responsabilidade sobre o estado operacional da oportunidade após admissão/ativação no escopo já governado.

```text
ORG-002 / ORG-003 VALIDATED
≠ ORG-001 VALIDATED
```

## 9. Organização — Relações

A IA de Relações é coberta por três responsabilidades existentes:

| ID | Responsabilidade | Maturidade preservada |
|---|---|---|
| `GKR-SURF-ORG-004` | proposta de relação com Coletivo | contratado |
| `GKR-SURF-ORG-005` | avaliação e negociação bilateral | contratado |
| `GKR-SURF-ORG-006` | relação ativa e revisão | contratado |

Esses IDs podem materializar estados distintos de um mesmo objeto relacional ou superfícies distintas no futuro. Este mapa **não decide essa composição visual**.

O que permanece obrigatório é o ciclo lógico:

```text
proposta
→ avaliação bilateral
→ negociação quando necessária
→ aprovação legítima
→ ativa
→ revisão
→ ajuste / renovação / pausa / encerramento
```

## 10. Organização — estados relacionais obrigatórios

Sem criar novas superfícies, o domínio precisa suportar:

- rascunho;
- proposta;
- aguardando avaliação;
- autoridade insuficiente;
- divergência entre as partes;
- negociação;
- aguardando aprovação;
- aprovada;
- ativa;
- em revisão;
- alteração material pendente;
- contestada;
- bloqueada por proteção/privacidade;
- suspensa preventivamente;
- renovação pendente;
- encerramento solicitado;
- encerrada;
- encerrada com obrigações remanescentes.

O estado relacional deve continuar pertencendo ao objeto Relação, não à síntese ORG-001.

## 11. Organização — Responsabilidades e Evidências

`GKR-SURF-ORG-007` já existe como responsabilidade de **resultados e evidências institucionais** e permanece `indeterminado`.

A nova IA não cria outro ID apenas para a palavra “Responsabilidades”.

A divisão lógica fica:

```text
RESPONSABILIDADE / COMPROMISSO
→ permanece vinculada ao objeto que a gerou
  (oportunidade, programa, relação ou contexto institucional)

EVIDÊNCIA / RESULTADO
→ pode ser aprofundada em ORG-007
→ pode ser sintetizada em ORG-001
→ não duplica a fonte de verdade
```

Antes de wireframing, os fluxos prioritários deverão verificar se `ORG-007` é suficiente como superfície/responsabilidade de aprofundamento ou se existe uma lacuna funcional real.

Nenhuma nova superfície é criada antecipadamente.

## 12. Organização — contexto e autoridade

A IA `Organização e Autoridade` não recebe surface ID dedicado nesta fase.

O mapa decide que, primeiro, essa informação deve funcionar como camada transversal:

```text
Organização ativa
→ unidade/contexto
→ papel da pessoa
→ autoridade e limites
```

E como detalhe contextual acessível a partir da experiência institucional.

Novo ID somente será justificável se os fluxos prioritários mostrarem que administrar esse contexto exige uma responsabilidade própria que não possa coexistir legitimamente com ORG-001 ou outros objetos.

## 13. Organização — Planos e Capacidade

Preservados sem alteração:

| ID | Responsabilidade | Estado |
|---|---|---|
| `GKR-SURF-ORG-301` | Planos e comparação — Conecta · Eleva · Transforma | validado no fluxo especializado |
| `GKR-SURF-ORG-302` | revisão de contratação | validado |
| `GKR-SURF-ORG-303` | downgrade/cancelamento | validado |
| `GKR-SURF-ORG-304` | resultado/recuperação | validado |

A conexão futura com ORG-001 deve preservar `UXA-100-A4`: entrada/retorno não constituem contratação automática nem validam ORG-001.

## 14. Mapa macro — Coletivo

`GKR-SURF-COL-001` permanece ligado à presença pública/entrada coletiva e não é promovido a tela principal autenticada.

A experiência autenticada do responsável é lida assim:

```text
CONTEXTO ATIVO / AUTORIDADE
        ↓
GKR-SURF-COL-002
Início / Visão Geral do Responsável
        ├── PARTICIPAÇÃO
        │   ├── GKR-SURF-COL-003 — gestão de solicitações
        │   └── GKR-SURF-COL-004 — participantes e vínculos
        │
        ├── ATIVIDADES / GOVERNANÇA / PROTEÇÃO
        │   ├── GKR-SURF-COL-005 — comunicação oficial
        │   ├── GKR-SURF-COL-006 — atividades, consultas e decisões
        │   └── GKR-SURF-COL-007 — proteção e moderação
        │
        ├── RELAÇÕES
        │   └── GKR-SURF-COL-008 — relações institucionais
        │
        └── PLANOS E CAPACIDADE [especializado]
            ├── GKR-SURF-COL-301
            ├── GKR-SURF-COL-302
            ├── GKR-SURF-COL-303
            └── GKR-SURF-COL-304
```

`Aprendizados e Evidências` e `Coletivo e Autoridade` permanecem preocupações de IA transversais sem novo ID nesta fase.

## 15. Coletivo — GKR-SURF-COL-002

### Responsabilidade vigente

`Visão Geral do Responsável`.

### Papel no novo mapa

Permanece o ID lógico de entrada da futura experiência autenticada principal do responsável pelo Coletivo.

A terminologia final da interface poderá convergir para `Início` sem criar novo ID, porque a mudança é de rótulo/IA e não de responsabilidade fundamental.

### Estado preservado

```text
GKR-SURF-COL-002
→ partial / local materialization
→ UXA-086/087 evidence remains local
→ NOT final main authenticated wireframe baseline
```

O mapa não promove a materialização administrativa histórica a wireframe principal.

## 16. Coletivo — estados lógicos de COL-002

Perfis da mesma responsabilidade:

- `COL-HOME-NORMAL` — propósito/momento compreensíveis, sem atenção material prioritária;
- `COL-HOME-ATTENTION` — necessidade, decisão ou risco exige atenção;
- `COL-HOME-INCOMPLETE` — informação material ausente;
- `COL-HOME-AUTHORITY` — ação depende de decisão/governança adicional;
- `COL-HOME-PARTICIPATION` — solicitação, papel ou vínculo exige ação legítima;
- `COL-HOME-GOVERNANCE` — decisão, consulta ou moderação exige atenção;
- `COL-HOME-RELATION` — relação externa exige avaliação/revisão;
- `COL-HOME-CONTESTED` — decisão, informação ou evidência contestada;
- `COL-HOME-BLOCKED` — proteção/privacidade/risco bloqueia avanço;
- `COL-HOME-NO-EVIDENCE` — atividade ocorreu sem evidência suficiente de avanço;
- `COL-HOME-CAPACITY` — limite/capacidade exige decisão contextual.

São IDs internos do mapa, não novos `GKR-SURF-*`.

## 17. Coletivo — Participação

### GKR-SURF-COL-003

Gestão de solicitações.

Estado: **validado no fluxo especializado**.

Preserva handoffs com superfícies da Pessoa sem ser absorvido por elas.

### GKR-SURF-COL-004

Participantes e vínculos.

Estado: **programado**.

Deve futuramente suportar distinções entre:

- pertencimento;
- papel aceito;
- responsabilidade atribuída;
- pausa;
- saída;
- vínculo legítimo.

```text
PERTENCIMENTO
≠ PAPEL
≠ AUTORIDADE
```

## 18. Coletivo — Atividades, Governança e Proteção

A IA separa conceitualmente `Atividades e Oportunidades` de `Governança e Proteção`, mas o registro atual já possui responsabilidades que podem acomodar a primeira materialização sem novos IDs.

### GKR-SURF-COL-005 — comunicação oficial

Estado: **programado**.

Deve permanecer comunicação com função clara, não feed genérico.

### GKR-SURF-COL-006 — atividades, consultas e decisões

Estado: **programado**, com materializações parciais/dispersas históricas conforme registro.

Pode servir como responsabilidade principal para:

- atividades;
- ações;
- consultas;
- decisões;
- oportunidades do Coletivo quando legitimamente operadas.

O mapa de fluxos deverá verificar se a densidade funcional exige futura decomposição. Esta decisão não é antecipada agora.

### GKR-SURF-COL-007 — proteção e moderação

Estado: **contratado**.

Concentra responsabilidade por proteção/moderação, sem transformar toda governança em moderação.

## 19. Coletivo — relações

`GKR-SURF-COL-008` permanece a responsabilidade de **relações institucionais**.

Estado: contratado.

A assimetria atual com `ORG-004..006` é aceitável no mapa porque um ID pode representar uma responsabilidade com múltiplos estados.

COL-008 precisa suportar a perspectiva do Coletivo sobre o mesmo objeto bilateral que, do lado da Organização, pode aparecer nos estados/responsabilidades ORG-004/005/006.

```text
MESMA RELAÇÃO LÓGICA
→ núcleo factual compartilhado
→ perspectiva Organização
→ perspectiva Coletivo
→ ações dependentes da autoridade de cada lado
```

Não devem existir duas fontes independentes de verdade para a mesma relação.

## 20. Coletivo — Aprendizados e Evidências

A IA criou `Aprendizados e Evidências` como domínio informacional, mas o registro atual não possui responsabilidade granular exclusiva para isso.

Decisão deste mapa:

> **não criar novo ID ainda.**

Primeira alocação lógica:

- síntese relevante pode aparecer em `GKR-SURF-COL-002`;
- evidência ligada a atividade/decisão pode permanecer no objeto de `GKR-SURF-COL-006`;
- evidência ligada a relação permanece em `GKR-SURF-COL-008`;
- o futuro fluxo prioritário de acompanhamento deve testar se essa distribuição é compreensível ou se uma superfície própria é necessária.

Novo ID somente será criado com lacuna funcional demonstrada.

## 21. Coletivo — contexto e autoridade

`Coletivo e Autoridade` permanece context layer transversal.

Deve tornar compreensível:

```text
Coletivo ativo
→ propósito/contexto
→ papel da pessoa
→ regra de governança aplicável
→ autoridade e limites
```

A experiência não cria uma superfície administrativa de usuários apenas porque essa informação existe.

## 22. Coletivo — Planos e Capacidade

Preservados:

| ID | Responsabilidade | Estado |
|---|---|---|
| `GKR-SURF-COL-301` | Planos e comparação — Livre · Mobiliza · Impacta · Rede | validado no fluxo especializado |
| `GKR-SURF-COL-302` | revisão de contratação | validado |
| `GKR-SURF-COL-303` | downgrade/cancelamento | validado |
| `GKR-SURF-COL-304` | resultado/recuperação | validado |

A origem/retorno associados semanticamente a COL-002 preservam maturidade própria sem validar a superfície principal final.

## 23. Superfícies da Pessoa participante permanecem separadas

A experiência do responsável pelo Coletivo não absorve:

- `GKR-SURF-PER-106 — Meus Coletivos`;
- `GKR-SURF-PER-107 — Central de Atualizações`;
- `GKR-SURF-PER-108 — Início do Participante`;
- demais superfícies públicas/solicitação da Pessoa.

Essas superfícies preservam suas maturidades próprias.

```text
RESPONSÁVEL PELO COLETIVO
≠ PESSOA PARTICIPANTE
```

Uma mesma pessoa física pode exercer ambos os papéis, mas o contexto e a autoridade não se fundem.

## 24. Matriz IA → responsabilidades existentes

### Organização

| Domínio de IA | Responsabilidade(s) no mapa | Situação |
|---|---|---|
| Visão Geral | ORG-001 | responsabilidade suficiente; wireframe pendente |
| Oportunidades e Programas | ORG-002/003 | fluxos de oportunidade preservados; programas sem novo ID automático |
| Relações | ORG-004/005/006 | contrato existente; materialização principal pendente |
| Responsabilidades e Evidências | ORG-007 + objetos de origem + síntese ORG-001 | sem novo ID por ora |
| Organização e Autoridade | context layer + detalhe contextual | sem novo ID por ora |
| Planos e Capacidade | ORG-301..304 | especializado e validado no escopo próprio |

### Coletivo

| Domínio de IA | Responsabilidade(s) no mapa | Situação |
|---|---|---|
| Início | COL-002 | responsabilidade suficiente; baseline visual principal pendente |
| Atividades e Oportunidades | COL-006 | verificar decomposição somente nos fluxos |
| Participação | COL-003/004 | solicitação validada; participantes programado |
| Governança e Proteção | COL-005/006/007 | responsabilidades suficientes para mapear; materialização parcial/pendente |
| Relações | COL-008 | contratado; materialização bilateral pendente |
| Aprendizados e Evidências | COL-002 + COL-006 + COL-008 | sem novo ID por ora |
| Coletivo e Autoridade | context layer + COL-002/006/007 conforme objeto | sem novo ID por ora |
| Planos e Capacidade | COL-301..304 | especializado e validado no escopo próprio |

## 25. Regra de não duplicação

Uma síntese pode mostrar fragmentos ou estados de múltiplos objetos, mas não os duplica como registros independentes.

Exemplos:

```text
ORG-001 mostra “relação precisa de revisão”
→ fonte = Relação
→ ação entra no contexto ORG-006
```

```text
COL-002 mostra “solicitações aguardando análise”
→ fonte = gestão de solicitações
→ ação entra em COL-003
```

```text
COL-002 mostra “atividade sem responsável necessário”
→ fonte = atividade / COL-006
```

## 26. Estados transversais do mapa

Toda responsabilidade futura deve ser capaz de representar, quando aplicável:

- normal / sem atenção material;
- vazio legítimo;
- informação incompleta;
- aguardando informação;
- aguardando autoridade;
- aguardando contraparte;
- ação não permitida naquele contexto;
- informação contestada;
- risco/proteção;
- bloqueio de privacidade;
- suspensão;
- encerramento;
- erro recuperável;
- mudança material;
- capacidade atingida;
- informação sensível protegida;
- baixa conectividade quando materialmente necessária.

A presença desses estados no mapa **não decide quais exigem tela própria**.

## 27. Vazio legítimo

A futura experiência deve diferenciar:

```text
NÃO EXISTE OBJETO
≠ ERRO
≠ PENDÊNCIA
≠ FALHA DE ENGAJAMENTO
```

Exemplos:

- Organização sem relação ativa com Coletivo;
- Coletivo sem solicitação pendente;
- período sem evidência nova;
- nenhuma atenção material atual.

Vazio não deve gerar pressão artificial para publicar, criar atividade, comprar plano ou aumentar volume.

## 28. Atenção e estado crítico

Atenção continua sendo vista derivada.

O mapa exige que toda atenção possua:

- objeto de origem;
- motivo;
- severidade ou materialidade quando necessária;
- autoridade necessária;
- ação ou alternativa legítima;
- estado de resolução.

A síntese não inventa atenção para aumentar uso.

## 29. Handoffs lógicos permitidos — Organização

Sem definir ainda transições formais, o mapa reconhece adjacências legítimas:

```text
ORG-001
→ ORG-002 / ORG-003
→ ORG-004 / ORG-005 / ORG-006
→ ORG-007
→ ORG-301
```

E dentro de famílias já governadas:

```text
ORG-002 → ORG-003
ORG-004 → ORG-005 → ORG-006
ORG-301 ↔ ORG-302/303/304 conforme contratos existentes
```

A próxima etapa deverá transformar somente as adjacências prioritárias em fluxos explícitos.

## 30. Handoffs lógicos permitidos — Coletivo

```text
COL-002
→ COL-003 / COL-004
→ COL-005 / COL-006 / COL-007
→ COL-008
→ COL-301
```

Preservações especializadas:

```text
COL-003 ↔ superfícies da Pessoa conforme transições já validadas
COL-301 ↔ COL-302/303/304 conforme contratos existentes
```

O mapa não cria conexão automática entre todas as responsabilidades.

## 31. Handoff bilateral Organização ↔ Coletivo

A futura navegação de uma relação precisa preservar:

```text
ORGANIZAÇÃO
ORG-004 / ORG-005 / ORG-006
        ↕
MESMO OBJETO RELAÇÃO
        ↕
COLETIVO
COL-008 + estados aplicáveis
```

A troca entre perspectivas não significa que uma parte possa navegar dentro da área privada da outra.

Ela significa apenas que ambas operam sobre fatos compartilhados com ações autorizadas próprias.

## 32. Context switch

Quando uma mesma pessoa puder representar múltiplos participantes ou unidades, a troca de contexto deverá ocorrer fora da semântica do objeto de trabalho.

O mapa exige que a futura experiência evite:

- editar um objeto como Organização e concluir como Coletivo sem troca explícita;
- transportar filtros ou dados protegidos silenciosamente;
- manter autoridade de aprovação após troca de papel;
- confundir Pessoa participante com responsável pelo Coletivo.

O mecanismo visual e técnico permanece adiado.

## 33. Relação com Produtos Especializados

Nenhum Produto Especializado ganha surface ID dentro desta família por estar acessível a partir da experiência.

Handoffs futuros podem levar a:

- Guivos Business;
- Guivos Ads / Opportunity Boost;
- Guivos Intelligence;
- Mall;
- Travel;
- Media;
- Journey.

Mas:

```text
HANDOFF PARA PRODUTO
≠ PRODUTO ABSORVIDO PELA IA DO PARTICIPANTE
```

## 34. Critério para criar novo surface ID

Novo `GKR-SURF-ORG-*` ou `GKR-SURF-COL-*` somente deverá ser criado quando houver cumulativamente:

1. responsabilidade funcional distinta;
2. objeto ou decisão que não possa coexistir com clareza em responsabilidade atual;
3. ator/contexto identificável;
4. estado principal justificável;
5. entradas e saídas necessárias;
6. benefício de separação superior ao custo de fragmentação;
7. ausência de duplicação com fluxo especializado vigente;
8. decisão documental explícita.

Preferir composição responsável a proliferação de telas.

## 35. O que este mapa não decide

- layout;
- menu visual final;
- sidebar/topbar;
- cards;
- tabela ou lista;
- desktop/mobile;
- responsive states;
- copy final de botão;
- número de cliques;
- modal/drawer/página;
- IDs de componentes;
- permissões técnicas;
- implementação;
- protótipo.

## 36. Gate para fluxos prioritários

A etapa de fluxos prioritários pode iniciar quando estiver claro que:

- ORG-001 e COL-002 são as responsabilidades de síntese sem baseline visual vigente;
- as responsabilidades especializadas existentes estão preservadas;
- IA e registro global não entram em conflito;
- relações bilaterais usam um objeto lógico compartilhado;
- estados críticos podem ser representados sem novos IDs automáticos;
- não existe necessidade comprovada de novo surface ID neste ponto;
- nenhum wireframe foi inferido.

Com este documento:

```text
AUTHENTICATED INFORMATION ARCHITECTURE
→ DEFINED

SURFACE / STATE MAP
→ DEFINED LOGICALLY

NEW GLOBAL SURFACE IDs
→ 0

PRIORITY MAIN FLOWS
→ NOT YET DEFINED

MAIN AUTHENTICATED WIREFRAMES
→ NOT YET DEFINED

UXA-102 / V5
→ NOT STARTED

PRODUCT ENGINEERING
→ PAUSED
```

## 37. Próximo ato documental permitido

Após validação deste mapa, o próximo ato permitido nesta frente é:

> **definir os fluxos prioritários da experiência autenticada principal de Organização e Coletivo, selecionando somente os caminhos necessários para sustentar os futuros wireframes iniciais e preservando transições especializadas já validadas.**

Ainda não é permitido produzir wireframe ou UI.