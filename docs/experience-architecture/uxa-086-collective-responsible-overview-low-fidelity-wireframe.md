---
id: UXA-086
title: Materialização Controlada da Visão Geral do Responsável do Coletivo
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-018
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-080
  - UXA-085
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-COL-002
  - GKR-SURF-COL-003
  - GKR-TRN-112
  - GKR-JOURNEY-GAPS-001
  - M7.73
normative: false
---

# Materialização Controlada da Visão Geral do Responsável do Coletivo

## 1. Finalidade

A UXA-086 materializa exclusivamente a primeira referência de baixa fidelidade de `GKR-SURF-COL-002 — Visão Geral do Responsável`.

A superfície é o ponto inicial protegido para uma pessoa que representa legitimamente um Coletivo e precisa compreender:

> **Em nome de qual Coletivo estou atuando, o que exige responsabilidade agora, quais operações estão disponíveis dentro da minha autoridade e para onde devo seguir?**

A UXA-086 não materializa a gestão completa de solicitações, participantes, comunicação, moderação, relações institucionais ou configurações. Ela cria a superfície de orientação e entrada para essas responsabilidades.

## 2. Canal e cenário

Canal inicial: **computador**.

A escolha segue a UXA-059: gestão densa, comparação de estados e autoridade operacional exigem contexto visual mais amplo antes de qualquer derivação móvel.

O cenário canônico utiliza um Coletivo fictício com:

- propósito confirmado;
- entrada mediante aprovação;
- solicitações pendentes;
- participantes confirmados;
- uma atividade futura;
- comunicação oficial existente;
- uma condição de proteção que exige acompanhamento;
- Organização apoiadora sem autoridade automática;
- responsável autenticado com escopo delimitado.

Nenhum dado real ou sensível é utilizado.

## 3. Wireframe

![Wireframe desktop da Visão Geral do Responsável do Coletivo](../assets/wireframes/uxa-086-collective-responsible-overview-desktop.svg)

[Visualizar o arquivo gráfico vetorial escalável](../assets/wireframes/uxa-086-collective-responsible-overview-desktop.svg)

O wireframe é estrutural e monocromático. Não define identidade visual final, componentes técnicos, comportamento implementado ou prontidão de produto.

## 4. Hierarquia funcional

| Ordem | Bloco | Responsabilidade |
|---:|---|---|
| 1 | contexto e autoridade | identificar Coletivo, papel, escopo e limites da representação |
| 2 | momento operacional | resumir mudanças e responsabilidades materiais sem transformar volume em desempenho |
| 3 | atenção principal | destacar uma responsabilidade legítima e explicar por que requer cuidado |
| 4 | solicitações e vínculos | mostrar síntese por estado e permitir entrada na futura gestão especializada |
| 5 | comunicação e atividades | indicar mudanças operacionais e canais especializados sem reuni-los em feed único |
| 6 | proteção e moderação | tornar riscos e eventos protegidos visíveis somente no limite necessário à função |
| 7 | governança e relações | resumir decisões, papéis, relações e autonomia do Coletivo |
| 8 | navegação de gestão | abrir áreas permitidas conforme autoridade |

## 5. Contexto e autoridade

O cabeçalho deverá mostrar:

- nome do Coletivo;
- propósito resumido;
- papel da pessoa autenticada;
- escopo de autoridade;
- estado de representação;
- acesso a permissões, ajuda e contestação.

Ações fora do escopo deverão aparecer indisponíveis ou ausentes, com explicação quando necessário.

Apoio, patrocínio ou relação com Organização não transfere automaticamente propriedade, moderação ou autoridade sobre o Coletivo.

## 6. Momento operacional

A síntese deverá explicar o que mudou e quais responsabilidades são materiais.

Ela poderá utilizar:

- solicitações aguardando análise;
- alterações em participantes ou papéis;
- atividade futura confirmada ou alterada;
- comunicado oficial relevante;
- decisão ou consulta aberta;
- evento de proteção;
- relação ou recurso que exige revisão.

Não serão utilizados como prova isolada de avanço:

- número de membros;
- quantidade de mensagens;
- frequência de acesso;
- volume de publicações;
- crescimento de participantes;
- reações ou popularidade.

## 7. Atenção principal

A superfície poderá destacar no máximo uma responsabilidade principal quando houver fundamento material.

O bloco deverá declarar:

- o que precisa de cuidado;
- por que isso importa;
- qual autoridade é necessária;
- prazo real, quando existir;
- consequência possível;
- ação disponível;
- alternativa ou adiamento legítimo;
- possibilidade de contestar a prioridade.

Quando não houver responsabilidade urgente:

> **Nenhuma responsabilidade exige ação imediata neste momento.**

## 8. Solicitações e vínculos

A UXA-086 materializa apenas a **síntese de entrada** para a operação de vínculos.

A superfície poderá separar:

- solicitações pendentes;
- aguardando informação da pessoa;
- participantes confirmados;
- convites pendentes;
- participações pausadas;
- suspensões preventivas;
- papéis aceitos;
- moderadores e autoridades.

A ação principal `Revisar solicitações` representa o endpoint documental de `GKR-TRN-112`, mas **não materializa `GKR-SURF-COL-003`** e não valida a transição.

A UXA-086 não permite inferir como aprovar, pedir informação, recusar, expirar, suspender ou remover. Esses fluxos permanecem para pacote posterior.

## 9. Comunicação e atividades

A visão geral poderá apresentar somente síntese de:

- comunicado oficial recente;
- atividade próxima;
- pergunta sem resposta oficial;
- consulta ou decisão aberta.

Comunicado, discussão, pergunta, atividade, consulta e decisão permanecem objetos distintos conforme UXA-058. A visão geral não os transforma em feed ou chat único.

## 10. Proteção e moderação

Eventos protegidos serão apresentados somente quando a pessoa autenticada possuir autoridade e necessidade legítimas.

A síntese poderá indicar:

- evento aguardando triagem;
- proteção temporária ativa;
- conteúdo em revisão;
- decisão de moderação pendente de registro;
- recurso ou contestação existente.

Dados pessoais, relatos sensíveis e evidências completas não serão expostos na visão geral quando uma indicação agregada ou mínima for suficiente.

## 11. Governança, relações e autonomia

A superfície poderá resumir:

- decisões e consultas abertas;
- papéis e autoridades vigentes;
- Organização apoiadora;
- recursos ou dependências materiais;
- relação comercial ou patrocínio identificado;
- necessidade de revisão ou contestação.

Relações institucionais completas permanecem fora do escopo e não materializam `GKR-SURF-COL-008`.

## 12. Navegação mínima do responsável

```text
Visão Geral
├── Solicitações e participantes
├── Comunicação
├── Perguntas e respostas
├── Atividades
├── Decisões e governança
├── Perfil público e descoberta
├── Avaliações e reputação
├── Moderação e proteção
├── Pessoas, papéis e autoridades
├── Relações e recursos
└── Configurações
```

Somente a Visão Geral é materializada pela UXA-086. Os demais itens são destinos documentais previstos e poderão permanecer indisponíveis, parciais ou ausentes.

## 13. Dados exibidos e proibidos

### 13.1 Exibidos no limite necessário

- identidade do Coletivo;
- papel e autoridade da pessoa autenticada;
- contagens operacionais por estado quando legítimas;
- responsabilidades e prazos materiais;
- atividades e comunicações relevantes;
- indicadores agregados de proteção;
- relações e recursos materiais em síntese.

### 13.2 Proibidos por inferência

A visão geral não concede acesso automático a:

- conteúdo protegido da jornada pessoal;
- outros Coletivos da pessoa solicitante ou participante;
- contatos pessoais não necessários;
- histórico externo de avaliações, recusas ou denúncias;
- dados sensíveis sem finalidade e autoridade;
- listas nominais públicas por padrão;
- ranking de participação ou dedicação.

## 14. Estados incluídos e excluídos

### Incluído

- responsável com autoridade válida;
- operação regular com responsabilidades materiais;
- sínteses das principais áreas;
- entrada para solicitações;
- ausência de responsabilidade urgente como comportamento previsto no mesmo contrato estrutural.

### Excluído

- autoridade insuficiente como wireframe separado;
- fila completa de solicitações;
- detalhe de participante e vínculo;
- criação de comunicado;
- moderação completa;
- configuração de visibilidade;
- relação bilateral Organização–Coletivo;
- responsividade móvel;
- estados de erro e baixa conectividade.

Esses estados permanecem para pacotes posteriores quando alterarem materialmente hierarquia, decisão, autoridade ou recuperação.

## 15. Matriz de rastreabilidade

| Campo | UXA-086 |
|---|---|
| contrato de origem | UXA-014; UXA-056; UXA-058; UXA-059 |
| família funcional | gestão do Coletivo |
| superfície granular | GKR-SURF-COL-002 |
| transição relacionada | GKR-TRN-112 |
| público | responsável, moderador ou autoridade legítima conforme papel |
| autoridade | representação válida e escopo concedido |
| canal | computador |
| entrada | acesso protegido ao contexto de gestão do Coletivo |
| saída principal | futura gestão de solicitações e demais áreas autorizadas |
| risco dominante | excesso de autoridade, exposição de dados e coerção operacional |
| materialização | 1 SVG desktop |
| validação funcional | não executada nesta UXA |

## 16. Efeito sobre os registros

Após integração da UXA-086:

- `GKR-SURF-COL-002` deixa de estar visualmente ausente e passa a possuir uma referência materializada;
- sua maturidade continua limitada pela ausência de validação funcional específica;
- `GKR-TRN-112` continua não validada como transição;
- `GKR-SURF-COL-003` continua sem materialização operacional própria;
- a jornada do Coletivo continua `draft`;
- a lacuna não é declarada encerrada nesta etapa.

## 17. Limites

A UXA-086 não:

- valida funcionalmente o wireframe;
- fecha automaticamente a lacuna `GKR-SURF-COL-002`;
- materializa `GKR-SURF-COL-003`;
- materializa Meus Coletivos, Central de Atualizações ou Início do Participante;
- cria protótipo navegável;
- define design visual final;
- cria componentes técnicos;
- executa teste com pessoas;
- altera Modelo Econômico ou Resultados Empresariais;
- inicia Engenharia de Produto.

## 18. Próximo ato possível

Após integração e autorização separada, o próximo ato recomendado é:

> **UXA-087 — Validação Funcional da Visão Geral do Responsável do Coletivo.**

A UXA-087 não é iniciada por este pacote.
