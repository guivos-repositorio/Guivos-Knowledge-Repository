---
id: UXA-093
title: Materialização Controlada da Central de Atualizações
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-090
  - UXA-091
  - UXA-092
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-106
  - GKR-SURF-PER-107
  - GKR-SURF-PER-108
  - GKR-TRN-110
  - GKR-TRN-111
  - GKR-JOURNEY-GAPS-001
  - M7.80
normative: false
---

# Materialização Controlada da Central de Atualizações

## 1. Finalidade

A UXA-093 materializa exclusivamente a referência P0A de `GKR-SURF-PER-107 — Central de Atualizações`, preservando a separação entre a central pessoal de triagem e os canais especializados de comunicação do Coletivo.

A frente responde:

> **Como a Pessoa identifica o que mudou, de qual contexto veio, qual é a natureza e autoridade da atualização, se precisa fazer algo e qual prazo é legítimo, sem transformar a experiência em feed de engajamento?**

A UXA-093 é uma frente de **materialização**, não de validação funcional.

## 2. Autoridades utilizadas

- UXA-058 — contrato funcional de interações, recomendações e conexões;
- UXA-059 — programa de wireframes e prioridade P0A/P0B;
- UXA-091/092 — `Meus Coletivos` e continuidade pós-aprovação;
- registros de superfícies, transições, lacunas e jornadas integradas.

## 3. Decisão de escopo

A UXA-059 define a Central de Atualizações como a sétima referência P0A e prescreve **móvel primeiro** para experiências da Pessoa.

Por isso, esta frente cria **um único SVG móvel primário** para `PER-107`.

Não são materializados nesta UXA:

- Central sem atualização relevante;
- agrupamento por excesso de volume;
- falha de sincronização ou baixa conectividade;
- resumo periódico;
- áreas especializadas de Comunicados, Discussões, Perguntas, Atividades ou Decisões;
- Caixa de contatos e mensagens;
- Recomendações recebidas como superfície própria;
- `PER-108 — Início do Participante`.

Esses estados e superfícies permanecem dívidas P0B/P1/P2 ou dependências posteriores.

## 4. Wireframe principal

![Wireframe móvel da Central de Atualizações](../assets/wireframes/uxa-093-collective-updates-center-mobile.svg)

[Visualizar o arquivo gráfico vetorial escalável](../assets/wireframes/uxa-093-collective-updates-center-mobile.svg)

O wireframe é estrutural e monocromático. Não define identidade visual final, componente técnico, algoritmo implementado, mecanismo real de entrega ou prontidão de produto.

## 5. Hierarquia funcional materializada

A referência principal apresenta:

1. identidade da `Central de Atualizações`;
2. retorno explícito para `Meus Coletivos`;
3. categorias de leitura coerentes com UXA-058;
4. atualização que precisa de ação com origem, natureza, autoridade e prazo;
5. alerta de segurança com autoridade operacional e confirmação de leitura semanticamente limitada;
6. atualização informativa de vínculo sem obrigação de ação;
7. regra explícita de que leitura não equivale a concordância, presença ou decisão;
8. regra de ordenação sem engajamento, popularidade, compra de plano ou publicidade silenciosa;
9. limite explícito de que `Início do Participante` continua superfície própria e ausente.

## 6. Central como triagem, não feed

A Central consolida referências de atualização, mas não transforma objetos distintos em um único fluxo social.

Cada item preserva:

- origem;
- tipo;
- contexto;
- autoridade ou autor relevante;
- data ou última alteração;
- estado de leitura;
- necessidade de ação;
- prazo legítimo quando houver.

Comunicado, alerta, solicitação, discussão, pergunta, decisão, convite, recomendação ou contato continuam objetos funcionalmente distintos.

## 7. Ordenação e atenção

A materialização segue a ordem de atenção autorizada por UXA-058:

1. risco ou segurança material;
2. ação explicitamente exigida por compromisso aceito;
3. alteração de atividade futura confirmada;
4. resposta direta;
5. prazo legítimo;
6. preferência escolhida;
7. recência.

Não são critérios legítimos de ordenação:

- potencial de engajamento;
- volume de reações;
- popularidade do autor;
- quantidade de mensagens;
- compra de plano;
- publicidade;
- interesse comercial não declarado.

## 8. Leitura não é ação ou consentimento

A UXA-093 preserva a regra de que confirmação de leitura não é padrão universal.

Quando apresentada por motivo legítimo de segurança, confirmar leitura significa somente abrir ou reconhecer a informação. Não significa:

- concordar;
- aceitar nova regra;
- confirmar presença;
- concluir tarefa;
- renunciar a direito;
- aumentar reputação ou dedicação.

Ausência de confirmação não gera punição automática.

## 9. Proteção de dados

Pré-visualizações devem conter apenas o mínimo necessário para a pessoa identificar origem, natureza, contexto e necessidade de ação.

A Central não deve expor silenciosamente:

- conteúdo protegido da Jornada pessoal;
- diagnóstico, condição de saúde ou acessibilidade sem finalidade legítima;
- conteúdo privado de terceiros;
- dados de contato não autorizados;
- conteúdo integral de canais especializados quando um resumo seguro for suficiente.

## 10. Continuidade com superfícies existentes

O wireframe utiliza exemplos que podem ser compreendidos sem inventar destinos ainda ausentes:

- pedido de informação adicional pode retornar à solicitação em `PER-105`;
- vínculo confirmado pode retornar a `PER-106 — Meus Coletivos`;
- alerta de segurança pode ser compreendido e, quando legitimamente necessário, ter leitura confirmada na própria referência.

A UXA-093 não simula áreas P1 ainda não materializadas.

## 11. Efeito em `GKR-SURF-PER-107`

Após eventual integração:

- `PER-107` passa de `ausente` para **`materializado`**;
- seu canal inicial é móvel;
- sua decisão principal é identificar atualização, compreender origem/natureza/autoridade e decidir se deve agir ou apenas seguir;
- sua entrada esperada inclui `PER-106` e acessos pessoais legitimamente configurados;
- sua saída para `PER-108` continua bloqueada porque `PER-108` não foi materializado;
- a validação funcional de `PER-107` permanece pendente.

## 12. Efeito em `GKR-TRN-110`

`GKR-TRN-110 — Meus Coletivos → Central de Atualizações` passa a ter **ambos os endpoints materializados**, mas continua `parcial`.

A materialização não valida por inferência:

- o gatilho exato na origem;
- preservação de contexto entre origem e destino;
- comportamento de retorno;
- concorrência entre leitura, mudança de estado e atualização recebida;
- idempotência de ações;
- relação entre estado `lido` e estado substantivo do objeto.

Esses pontos devem ser avaliados em uma frente funcional própria.

## 13. Efeito em `GKR-TRN-111`

`GKR-TRN-111 — Central de Atualizações → Início do Participante` permanece **`ausente`** porque `PER-108` continua sem materialização vigente.

A UXA-093 não usa um CTA fictício para mascarar essa ausência.

## 14. Rastreabilidade

| Campo | UXA-093 |
|---|---|
| família funcional | continuidade pessoal e controle de atenção em Coletivos |
| superfície principal | GKR-SURF-PER-107 |
| canal | móvel |
| entrada principal | Meus Coletivos ou atualização pessoal legitimamente recebida |
| decisão principal | compreender o que mudou e se exige ação |
| saída atual segura | PER-105/PER-106 quando o objeto já possui destino materializado; retorno livre |
| saída futura | PER-108 e áreas especializadas quando materializadas e validadas |
| transições relacionadas | GKR-TRN-110; GKR-TRN-111 |
| risco dominante | transformar atenção em engajamento, misturar naturezas ou prometer destinos ausentes |
| novo ativo | 1 SVG móvel |
| validação funcional | não executada nesta UXA |

## 15. Efeito quantitativo proposto

Após eventual integração:

- SVGs: 107;
- associações individuais: 107;
- perfis de rastreabilidade: 27;
- SVGs com validação funcional vigente: 96;
- pendentes de validação específica: 11;
- IDs granulares com referência visual: 29 de 40;
- responsabilidades sem SVG dedicado: 10;
- superfícies registradas: 40;
- transições registradas: 37.

Os 11 pendentes serão:

- 10 estados residuais da UXA-055;
- `uxa-093-collective-updates-center-mobile.svg`, ainda não validado.

## 16. Efeito sobre maturidade

Após eventual integração:

- `GKR-SURF-PER-107` → `materializado`;
- `GKR-TRN-110` → permanece `parcial`, agora com os dois endpoints materializados;
- `GKR-TRN-111` → permanece `ausente` por `PER-108` não materializado;
- `GKR-SURF-PER-108` → continua com reformulação pendente;
- Jornadas da Pessoa e do Coletivo → permanecem `draft`;
- Engenharia de Produto → permanece pausada antes de W0-01.

## 17. Limites

A UXA-093 não:

- valida funcionalmente `PER-107`;
- valida `TRN-110` ponta a ponta;
- materializa `PER-108`;
- materializa estados P0B da Central;
- cria áreas P1 de comunicação;
- cria novos IDs de superfície ou transição;
- define API, fila, push, banco, sincronização, algoritmo ou persistência;
- promove Jornada da Pessoa ou do Coletivo;
- altera Resultados Empresariais;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-094.

## 18. Próxima transição possível

Após eventual integração e autorização separada:

> **UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`.**

A UXA-094 não é iniciada por esta materialização.
