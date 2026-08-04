---
id: UXA-064
title: Wireframes Móveis da Revisão e Solicitação de Participação em Coletivos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-062
  - UXA-063
related:
  - UXA-065
  - M7.66
normative: false
---

# Wireframes Móveis da Revisão e Solicitação de Participação em Coletivos

## 1. Finalidade

Este documento materializa a quarta referência da espinha dorsal P0A definida pela UXA-059: a revisão e a Solicitação de Participação móvel.

A família permite que uma pessoa, antes de criar ou solicitar vínculo:

- compreenda o significado da participação;
- diferencie entrada aberta, aprovação e convite protegido;
- revise regras e condições materiais;
- veja exatamente quais dados serão enviados;
- compreenda quais dados não serão compartilhados;
- revise visibilidade, notificações e permissões;
- saiba quem possui autoridade para analisar;
- confirme conscientemente, sem opções previamente selecionadas;
- cancele antes do envio;
- compreenda o resultado imediato sem confundi-lo com a futura Solicitação Pendente.

Os artefatos são wireframes móveis de baixa fidelidade. Não representam design final, protótipo, política jurídica, tecnologia de consentimento ou Engenharia de Produto.

## 2. Continuidade materializada

```text
Perfil Público validado
→ revisar significado do vínculo
→ revisar regras, dados e permissões
→ confirmar entrada aberta ou enviar solicitação
→ receber confirmação imediata ou comprovante transitório
→ futura Solicitação Pendente, quando houver aprovação
```

Para convite protegido:

```text
apresentação protegida validada
→ revisar remetente, autoridade, motivo e validade
→ revisar dados mínimos e proteções
→ recusar, denunciar ou enviar para revisão especializada
```

A UXA-064 não materializa o acompanhamento contínuo da solicitação, a decisão do responsável ou a área `Meus Coletivos`.

## 3. Decisão de agrupamento

A família utiliza cinco SVGs porque as seguintes mudanças alteram materialmente decisão, consequência ou proteção:

1. revisão para entrada aberta;
2. confirmação imediata da entrada aberta;
3. revisão de solicitação mediante aprovação;
4. comprovante transitório do envio;
5. revisão de convite protegido.

O comprovante não substitui a superfície `Solicitação Pendente`. Ele registra somente que o envio ocorreu e reserva a continuidade futura.

## 4. Artefatos

### 4.1 Revisão para entrada aberta

![Revisão de participação com entrada aberta](../assets/wireframes/uxa-064-collective-participation-open-entry-review-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-064-collective-participation-open-entry-review-mobile.svg`

### 4.2 Entrada aberta confirmada

![Participação confirmada por entrada aberta](../assets/wireframes/uxa-064-collective-participation-open-entry-confirmed-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-064-collective-participation-open-entry-confirmed-mobile.svg`

### 4.3 Revisão de solicitação mediante aprovação

![Revisão da solicitação mediante aprovação](../assets/wireframes/uxa-064-collective-participation-approval-request-review-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-064-collective-participation-approval-request-review-mobile.svg`

### 4.4 Comprovante de solicitação enviada

![Comprovante transitório de solicitação enviada](../assets/wireframes/uxa-064-collective-participation-approval-request-receipt-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-064-collective-participation-approval-request-receipt-mobile.svg`

### 4.5 Revisão protegida de convite

![Revisão protegida de convite](../assets/wireframes/uxa-064-collective-participation-protected-invite-review-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-064-collective-participation-protected-invite-review-mobile.svg`

## 5. Canal e dimensões

Todos os artefatos possuem:

- canal inicial: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- fidelidade: baixa;
- decisões textuais que não dependem apenas de cor;
- `title` e `desc` próprios.

A experiência para computador não foi criada porque não existe mudança demonstrada de hierarquia ou autoridade.

## 6. Cenários canônicos

| Estado | Coletivo | Modelo | Resultado principal |
|---|---|---|---|
| revisão aberta | Pedal Horizonte | entrada aberta | revisar e confirmar participação |
| confirmação aberta | Pedal Horizonte | entrada aberta | compreender efeitos e abrir o Coletivo |
| revisão por aprovação | Ciclistas da Serra | aprovação | revisar e enviar solicitação |
| comprovante | Ciclistas da Serra | aprovação | confirmar envio sem criar vínculo |
| convite protegido | Rede de Apoio Reservada | convite autorizado | revisar proteção e enviar para análise |

Nomes, datas, horários, contagens e identificadores são fictícios e servem somente à validação estrutural.

## 7. Hierarquia da revisão

A ordem funcional comum é:

```text
retorno ou cancelamento
→ Coletivo e modelo de entrada
→ significado do vínculo ou da solicitação
→ dados que serão enviados
→ dados que permanecerão protegidos
→ autoridade, prazo e consequência
→ visibilidade, notificações e contato
→ confirmações inicialmente vazias
→ ação principal condicionada
→ cancelamento sem envio
```

Estados protegidos acrescentam remetente, autoridade, motivo, validade, confidencialidade e possibilidade de denúncia.

## 8. Entrada aberta

A entrada aberta exige confirmação consciente mesmo quando não depende de análise do responsável.

A revisão informa que a participação:

- cria vínculo de participante confirmado;
- permite acesso interno conforme permissões;
- não cria função;
- não concede autoridade;
- não impõe presença;
- não autoriza contato privado;
- não concede consentimento comercial;
- permite pausa e saída conforme regras.

A ação `Confirmar participação` permanece indisponível enquanto as confirmações necessárias estiverem vazias.

## 9. Confirmação da entrada aberta

A confirmação imediata demonstra:

- vínculo ativo;
- data e horário do registro;
- acesso ao ambiente interno;
- visibilidade atual da pessoa;
- notificações não ativadas automaticamente;
- contato privado não autorizado;
- ausência de papel e autoridade automáticos;
- possibilidade de revisar, pausar ou sair;
- exigência de nova revisão diante de mudança material de regra.

`Abrir Coletivo` utiliza o ambiente interno existente como continuidade. A UXA-064 não reformula o Início do Participante.

## 10. Entrada mediante aprovação

A revisão de solicitação informa antes do envio:

- ausência de vínculo durante a análise;
- critérios legítimos;
- dados necessários;
- responsável com autoridade identificada;
- prazo estimado sem garantia;
- possibilidade de cancelar;
- possibilidade de informação adicional;
- ausência de compartilhamento automático com Organização apoiadora.

A ação `Enviar solicitação` não equivale a aprovação, acesso interno ou presença em lista de participantes.

## 11. Comprovante transitório

O comprovante demonstra somente que:

- a solicitação foi recebida;
- nenhum vínculo foi criado;
- os dados enviados podem ser revisados;
- o responsável e o prazo estimado permanecem identificados;
- aprovação, recusa, informação adicional ou cancelamento são eventos possíveis;
- a continuidade futura ficará em `Solicitações`.

O comprovante não materializa:

- fila de análise;
- estado atualizado continuamente;
- histórico de eventos;
- pedido de informação adicional;
- decisão;
- contestação;
- cancelamento operacional.

Essas responsabilidades pertencem à futura superfície `Solicitação Pendente` e seus estados críticos.

## 12. Convite protegido

A revisão protegida apresenta:

- remetente identificado;
- autoridade do remetente;
- motivo;
- validade;
- acesso individual e não encaminhável;
- dados mínimos necessários;
- informações que permanecerão ocultas;
- confidencialidade;
- ausência de vínculo automático;
- possibilidade de recusar, ignorar ou denunciar sem penalidade.

A ação `Enviar para revisão protegida` inicia análise especializada e não ativa participação, contato privado ou visibilidade pública.

## 13. Dados permitidos

Conforme o cenário e a necessidade legítima, poderão ser enviados:

- nome de exibição;
- identificador interno da solicitação ou participação;
- confirmações registradas;
- data e horário;
- experiência declarada relevante;
- disponibilidade informada;
- respostas necessárias a processo protegido;
- escolha de visibilidade da participação.

A UXA-064 não define o esquema técnico, retenção definitiva ou base jurídica de produção.

## 14. Dados proibidos por padrão

Não serão enviados automaticamente:

- telefone;
- e-mail pessoal;
- endereço;
- localização exata;
- conteúdo protegido da Jornada;
- outros Coletivos da pessoa;
- avaliações externas;
- denúncias ou recusas anteriores;
- contatos pessoais;
- informações sensíveis não relacionadas;
- histórico comercial;
- inferências não autorizadas.

Dados adicionais exigirão finalidade, necessidade, explicação e nova revisão.

## 15. Permissões separadas

A participação não concede automaticamente:

- aparição pública na lista nominal;
- exibição da participação no perfil pessoal;
- recebimento de todas as notificações;
- mensagem privada;
- compartilhamento de telefone ou e-mail;
- comunicação comercial;
- papel ou função;
- disponibilidade universal;
- autoridade de decisão;
- consentimento para Organização apoiadora.

Cada permissão deverá possuir controle e consequência próprios.

## 16. Confirmações inicialmente vazias

Os wireframes demonstram caixas de confirmação sem seleção inicial.

As confirmações cobrem, conforme o estado:

- regras essenciais;
- requisitos de segurança;
- significado do vínculo;
- possibilidade de pausa e saída;
- dados que serão enviados;
- critérios e condições de análise;
- proteção e confidencialidade do convite.

Leitura, rolagem, silêncio, acompanhamento ou abertura do perfil não equivalem a consentimento.

## 17. Cancelamento

Antes do envio, a pessoa poderá:

- voltar ao Perfil Público;
- fechar a revisão;
- cancelar sem enviar dados;
- recusar convite;
- denunciar convite protegido.

O cancelamento de uma solicitação já enviada pertence à futura Solicitação Pendente, embora o comprovante reserve esse direito.

## 18. Autoridade e Organizações

A revisão mediante aprovação identifica quem analisa e qual papel autoriza a ação.

Uma Organização apoiadora, anunciante, cedente de espaço ou parceira não recebe automaticamente:

- solicitação;
- respostas;
- identidade;
- contatos;
- conteúdo protegido;
- autoridade de aprovação.

A relação institucional somente poderá participar do processo quando existir papel operacional legítimo, finalidade e comunicação explícitas.

## 19. Notificações e comunicação

Nenhuma categoria de notificação é ativada pela simples participação.

A pessoa poderá escolher posteriormente, em superfície própria:

- comunicados importantes;
- atividades;
- perguntas e respostas;
- decisões e consultas;
- convites;
- resumo periódico.

Marketing e publicidade permanecem fora dos canais internos e dependem de consentimento separado quando aplicável.

## 20. Acessibilidade

Os artefatos utilizam:

- títulos e descrições acessíveis;
- ações nomeadas;
- estados textuais;
- caixas vazias visíveis;
- linguagem explícita para consequência e proteção;
- ordem linear;
- botões indisponíveis identificados por texto e contraste estrutural;
- ausência de significado dependente apenas de cor.

A materialização não conclui teste com tecnologia assistiva nem conformidade técnica final.

## 21. Matriz de cobertura

| Estado contratual | Artefato | Situação |
|---|---|---|
| revisão de regras e dados | revisão aberta; revisão por aprovação; convite | materializado |
| entrada aberta consciente | revisão aberta | materializado |
| entrada confirmada | confirmação aberta | materializado |
| solicitação mediante aprovação | revisão por aprovação | materializado |
| envio sem criação de vínculo | comprovante | materializado |
| convite protegido | revisão protegida | materializado |
| confirmações inicialmente vazias | três revisões | materializado |
| dados permitidos e proibidos | três revisões | materializado |
| cancelamento antes do envio | três revisões | materializado |
| autoridade da análise | revisão por aprovação; convite | materializado |
| permissões separadas | revisão aberta; confirmação; aprovação | materializado |
| Organização sem acesso automático | revisão por aprovação | materializado |
| Solicitação Pendente | não criada | próxima referência P0A |
| informação adicional solicitada | não criada | P0B posterior |
| solicitação recusada ou expirada | não criada | P0B posterior |
| cancelamento após envio | não criado | Solicitação Pendente |
| decisão do responsável | não criada | gestão posterior |

## 22. Critérios para validação funcional

A UXA-065 deverá verificar:

1. compreensão do significado do vínculo antes da ação;
2. diferença entre entrada aberta, aprovação e convite;
3. dados enviados e proibidos compreensíveis;
4. permissões separadas da participação;
5. confirmações realmente vazias e não coercitivas;
6. cancelamento visível antes do envio;
7. autoridade e prazo sem promessa indevida;
8. entrada confirmada sem função automática;
9. comprovante sem substituir Solicitação Pendente;
10. convite protegido sem exposição ou compartilhamento;
11. ausência de marketing e contato privado implícitos;
12. continuidade para Perfil Público, ambiente interno e futura pendência.

## 23. Cobertura após materialização

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Coletivos — revisão e solicitação | 5 | 0 | 5 |
| Opportunity Boost | 46 | 36 | 10 |

As famílias permanecem contabilizadas e validadas separadamente.

## 24. Limites

Não são iniciados:

- Solicitação Pendente como superfície contínua;
- informação adicional solicitada;
- recusa, expiração ou contestação;
- gestão de solicitações pelo responsável;
- `Meus Coletivos`;
- Central de Atualizações;
- reformulação do Início do Participante;
- gestão do responsável;
- protótipo;
- teste com pessoas;
- identidade visual;
- tecnologia de consentimento;
- Engenharia de Produto.

## 25. Estado do incremento

- cinco SVGs materializados;
- zero SVG validado funcionalmente neste incremento;
- cinco SVGs pendentes de validação na UXA-065;
- nenhuma nova decisão canônica de Produto ou Engenharia;
- nenhuma alteração em Resultados Empresariais ou baseline comercial;
- contagens do Opportunity Boost preservadas separadamente.

## 26. Próxima transição recomendada

**UXA-065 — Validação Funcional e Reformulação da Revisão e Solicitação de Participação Móvel em Coletivos.**

A UXA-065 deverá validar os cinco SVGs como um percurso único antes de iniciar a superfície Solicitação Pendente.

Nenhuma etapa posterior é iniciada automaticamente.
