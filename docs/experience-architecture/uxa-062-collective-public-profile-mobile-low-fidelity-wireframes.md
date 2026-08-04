---
id: UXA-062
title: Wireframes Móveis do Perfil Público do Coletivo
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
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
related:
  - UXA-063
  - M7.64
normative: false
---

# Wireframes Móveis do Perfil Público do Coletivo

## 1. Finalidade

Este documento materializa a terceira referência da espinha dorsal P0A definida pela UXA-059: o Perfil Público móvel do Coletivo.

A família permite que uma pessoa compreenda, antes de qualquer vínculo:

- que Coletivo é este;
- por que e como chegou ao perfil;
- qual é o propósito declarado;
- como o Coletivo funciona;
- quem possui responsabilidade pública;
- qual relação existe com Organizações;
- quais informações e contagens podem ser exibidas;
- que reputação contextual está disponível;
- quais regras e proteções antecedem qualquer participação;
- se a entrada está aberta, depende de aprovação, está temporariamente indisponível ou exige processo protegido.

Os artefatos são wireframes móveis de baixa fidelidade. Não representam design final, protótipo navegável, política jurídica, algoritmo, sistema de reputação implementado ou Engenharia de Produto.

## 2. Posição no programa

A continuidade materializada é:

```text
Explorar Coletivos ou Resultados de Busca
→ Perfil Público ou apresentação protegida
→ compreender propósito, condições e origem
→ acompanhar ou iniciar futura revisão de participação
```

A UXA-062 não cria o fluxo de Solicitação de Participação, a Solicitação Pendente, o ambiente interno do participante ou a gestão do responsável.

## 3. Decisão de agrupamento

A família utiliza quatro SVGs porque os estados alteram materialmente decisão principal, visibilidade, dados exibidos ou proteção:

1. perfil público com entrada aberta;
2. perfil público com entrada mediante aprovação;
3. perfil público com entradas temporariamente indisponíveis;
4. apresentação protegida acessada por convite autorizado.

Reputação com base suficiente e insuficiente aparece dentro dos dois primeiros estados. A experiência completa de avaliações permanece para P2.

## 4. Artefatos

### 4.1 Entrada aberta

![Perfil público móvel com entrada aberta](../assets/wireframes/uxa-062-collective-public-profile-open-entry-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-062-collective-public-profile-open-entry-mobile.svg`

### 4.2 Entrada mediante aprovação

![Perfil público móvel com entrada mediante aprovação](../assets/wireframes/uxa-062-collective-public-profile-approval-entry-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-062-collective-public-profile-approval-entry-mobile.svg`

### 4.3 Entradas temporariamente indisponíveis

![Perfil público móvel com entradas temporariamente indisponíveis](../assets/wireframes/uxa-062-collective-public-profile-closed-entry-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-062-collective-public-profile-closed-entry-mobile.svg`

### 4.4 Apresentação protegida

![Apresentação móvel protegida de Coletivo](../assets/wireframes/uxa-062-collective-public-profile-protected-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-062-collective-public-profile-protected-mobile.svg`

## 5. Canal e dimensões

Todos os artefatos possuem:

- canal inicial: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- fidelidade: baixa;
- navegação recorrente: `Hoje | Jornada | Explorar | Mapa | Eu`;
- item ativo: `Explorar`.

A versão para computador não é criada porque ainda não foi demonstrada mudança material de hierarquia.

## 6. Cenários canônicos

| Estado | Coletivo | Origem | Decisão principal |
|---|---|---|---|
| entrada aberta | Pedal Horizonte | resultado orgânico de busca | acompanhar ou participar |
| aprovação | Ciclistas da Serra | resultado orgânico de busca | acompanhar ou solicitar participação |
| entradas indisponíveis | Pedal Urbano Aberto | publicidade identificada | acompanhar ou compreender o fechamento |
| protegido | Rede de Apoio Reservada | convite autorizado | revisar convite e condições |

Os nomes, datas, contagens e percentuais são fictícios e servem somente à validação estrutural.

## 7. Hierarquia comum

A ordem funcional preservada é:

```text
retorno e ação de compartilhamento permitida
→ origem da navegação
→ identidade, classificação e situação
→ propósito e descrição
→ território, modalidade e acessibilidade
→ forma de acompanhar ou participar
→ regras e condições essenciais
→ participantes em contagem governada
→ responsáveis, moderação e relações institucionais
→ experiência e reputação contextual
→ atividades, proteção, contato e denúncia
```

Estados protegidos podem reduzir ou ocultar blocos quando a própria exposição aumentar risco.

## 8. Origem da navegação

Cada artefato informa a origem antes da decisão de entrada.

As origens demonstradas são:

- resultado orgânico de busca;
- publicidade identificada;
- convite autorizado.

A origem poderá preservar, conforme privacidade e necessidade:

- consulta;
- região;
- posição do resultado;
- natureza orgânica ou comercial;
- pessoa que convidou;
- validade e escopo do acesso.

Retornar deverá preservar o contexto anterior. Visualizar o perfil não entrega a identidade da pessoa ao Coletivo, à Organização apoiadora ou ao anunciante.

## 9. Entrada aberta

O estado apresenta:

- `Entrada aberta` como condição atual;
- `Acompanhar` e `Participar` como ações independentes;
- regras essenciais antes da futura confirmação;
- ausência de acesso interno por simples acompanhamento;
- participantes confirmados em faixa ou número governado;
- lista nominal protegida;
- responsável e moderação identificados;
- relação institucional sem autoridade automática;
- resumo de reputação com base suficiente.

Selecionar `Participar` deverá levar futuramente à revisão de vínculo, dados, regras e confirmações vazias. O perfil não ativa participação por si só.

## 10. Entrada mediante aprovação

O estado apresenta:

- condição `Aprovação necessária`;
- ação `Solicitar participação` distinta de entrada confirmada;
- critérios legítimos;
- dados necessários;
- responsável autorizado pela análise;
- prazo estimado sem garantia;
- possibilidade de cancelamento;
- ausência de acesso interno durante a análise;
- reputação com amostra insuficiente.

O perfil não presume que silêncio, espera ou envio da solicitação equivalem a aprovação.

## 11. Entradas temporariamente indisponíveis

O estado apresenta:

- ação de participação indisponível;
- motivo do fechamento;
- revisão prevista com data estimada;
- ausência de garantia de reabertura;
- acompanhamento opcional sem fila ou prioridade;
- atividades públicas preservadas somente quando seguras;
- reputação separada do estado operacional;
- natureza publicitária da origem preservada.

Publicidade não cria acesso, prioridade, qualidade, legitimidade ou recomendação da Guivos.

## 12. Apresentação protegida

O estado protegido não funciona como perfil público completo.

Ele apresenta somente:

- identidade reduzida permitida;
- propósito público mínimo;
- motivo da limitação;
- origem por convite autorizado;
- informações ocultas por proteção;
- dados e regras que serão revisados antes de continuar;
- possibilidade de recusar ou denunciar o convite;
- ausência de reputação pública quando isso revelar participação sensível.

Território exato, contagem, lista nominal, responsáveis, atividades e contato permanecem ocultos até processo especializado e legítimo.

## 13. Acompanhar e participar

`Acompanhar` poderá permitir atualizações públicas escolhidas e retorno posterior. Não concede:

- participação;
- acesso ao ambiente interno;
- presença em lista;
- papel;
- autoridade;
- contato privado;
- compartilhamento automático de dados.

`Participar` ou `Solicitar participação` inicia um fluxo futuro e consciente. Nenhuma confirmação começa selecionada.

## 14. Regras e condições

O perfil deverá antecipar informação suficiente para evitar uma decisão cega.

Poderão ser mostrados:

- regras essenciais;
- requisitos de segurança;
- custos ou recursos, quando existirem;
- dados necessários;
- acessibilidade;
- modalidade;
- possibilidade de pausa e saída;
- quem analisa solicitações;
- prazo estimado;
- mudanças materiais recentes.

A leitura não equivale a consentimento. Confirmações materiais ocorrerão no fluxo especializado de participação.

## 15. Contagens e pessoas

A família separa:

- participantes confirmados;
- pessoas acompanhando, quando publicamente permitido;
- responsáveis e moderadores;
- participantes de atividades específicas.

Não serão incluídos em contagem pública genérica:

- solicitações pendentes;
- pessoas suspensas;
- convites;
- seguidores;
- presença em atividade;
- dados operacionais internos.

A lista nominal permanece protegida por padrão. Em contexto sensível, até a contagem pode ser ocultada.

## 16. Responsáveis e Organizações relacionadas

O Perfil Público deverá identificar responsabilidades materiais sem criar autoridade implícita.

Uma Organização poderá aparecer como:

- apoiadora logística;
- cedente de espaço;
- financiadora;
- anunciante;
- parceira institucional;
- operadora legítima, quando contratada.

A relação deverá indicar seu limite. Apoio, anúncio ou parceria não concede automaticamente:

- autoridade sobre participantes;
- acesso a solicitações;
- acesso a contatos;
- acesso a avaliações individuais;
- acesso ao conteúdo protegido da Jornada;
- direito de comunicação comercial.

## 17. Reputação contextual

Quando houver base suficiente, o perfil poderá apresentar:

- objeto avaliado;
- quantidade de avaliações verificadas;
- período;
- dimensões selecionadas;
- percentuais com denominador e método acessíveis;
- limitações;
- caminho para distribuição detalhada.

Quando a base for insuficiente, deverá declarar:

> **Ainda não há avaliações verificadas suficientes para apresentar um resumo público.**

A ausência de resumo não representa nota zero, aprovação, reprovação ou inexistência de experiências.

A primeira versão não utiliza estrelas ou nota universal como representação principal.

## 18. Publicidade e relação comercial

Quando a pessoa chega por publicidade, o perfil preserva:

- rótulo comercial;
- anunciante;
- posição após resultado orgânico;
- distinção entre publicidade e recomendação;
- ausência de alteração da ordem orgânica;
- controles de ocultação e denúncia aplicáveis.

A informação comercial não substitui propósito, regras, responsáveis, proteção ou reputação contextual.

## 19. Compartilhamento, recomendação e convite

`Compartilhar` distribui uma referência permitida e não equivale a recomendar.

O perfil não materializa o fluxo completo de recomendação. Convites permanecem distintos e devem informar quem convida, contexto, validade e possibilidade de recusa.

Apresentações protegidas não poderão ser compartilhadas externamente quando isso ampliar acesso ou revelar informação sensível.

## 20. Proteção, contato e denúncia

A família reserva caminhos para:

- política de proteção;
- responsável de contato público;
- denúncia do perfil;
- denúncia de convite;
- denúncia de publicidade;
- privacidade e segurança;
- revisão de regras.

Denunciar não será reduzido a avaliação negativa. Contato público não autoriza mensagem privada ou exposição de telefone e e-mail pessoais.

## 21. Acessibilidade

Os artefatos utilizam:

- títulos e rótulos textuais;
- natureza comercial anterior ao conteúdo;
- estados que não dependem apenas de cor;
- ações nomeadas;
- ordem linear;
- `title` e `desc` em cada SVG;
- textos explícitos para ações indisponíveis;
- explicação textual de amostra insuficiente;
- localização e proteção descritas por linguagem, não apenas ícones.

A materialização não conclui teste com tecnologia assistiva nem conformidade técnica final.

## 22. Matriz de cobertura

| Estado contratual | Artefato | Situação |
|---|---|---|
| perfil público com entrada aberta | entrada aberta | materializado |
| perfil público com aprovação | aprovação | materializado |
| entradas temporariamente fechadas | entradas indisponíveis | materializado |
| Coletivo protegido | apresentação protegida | materializado |
| origem orgânica preservada | entrada aberta; aprovação | materializado |
| origem patrocinada preservada | entradas indisponíveis | materializado |
| convite protegido | apresentação protegida | materializado |
| acompanhar separado de participar | entrada aberta; aprovação; indisponível | materializado |
| contagem governada e lista protegida | entrada aberta; aprovação; indisponível | materializado |
| contagem ocultada por risco | apresentação protegida | materializado |
| Organização relacionada com limite | entrada aberta; aprovação; indisponível | materializado |
| reputação com base suficiente | entrada aberta | materializado |
| reputação com base insuficiente | aprovação | materializado |
| reputação suprimida por proteção | apresentação protegida | materializado |
| denúncia e proteção | quatro artefatos | materializado |
| fluxo completo de participação | não criado | pendente |
| Coletivo encerrado | não criado | pendente P0B posterior |
| perfil não listado por link | coberto parcialmente pelo protegido | decisão posterior |
| reputação detalhada | não criada | pendente P2 |

## 23. Critérios para validação funcional

A UXA-063 deverá verificar:

1. compreensão da origem sem confusão entre orgânico, publicidade e convite;
2. distinção entre acompanhar, participar e solicitar participação;
3. visibilidade do estado de entrada antes da ação;
4. presença de propósito, funcionamento, regras e proteção;
5. contagens sem popularidade ou exposição nominal;
6. autoridade e relação institucional com limites claros;
7. reputação suficiente, insuficiente ou suprimida sem nota universal;
8. publicidade sem influência sobre legitimidade ou reputação;
9. fechamento temporário sem promessa de reabertura;
10. proteção sem revelar identidade, localização ou participação sensível;
11. retorno à busca, ao convite ou à origem com contexto preservado;
12. ausência de antecipação do fluxo de participação.

## 24. Limites do incremento

Não são iniciados:

- Solicitação de Participação;
- Solicitação Pendente;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante;
- gestão do responsável;
- avaliação completa;
- recomendação completa;
- mensagem privada;
- algoritmo de busca ou reputação;
- política jurídica;
- protótipo;
- teste com pessoas;
- identidade visual;
- Engenharia de Produto.

## 25. Estado do incremento

- quatro SVGs materializados;
- zero SVG validado funcionalmente neste incremento;
- validação especializada pendente na UXA-063;
- nenhuma nova decisão de Produto ou Engenharia autorizada;
- contagens do Opportunity Boost preservadas separadamente.
