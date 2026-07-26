---
id: UXA-006
title: Wireframe de Baixa Fidelidade da Tela Hoje
status: draft
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-005
related:
  - UXA-002
  - UXA-003
  - UXA-004
  - UXA-009
  - UXA-010
  - UXA-011
  - PAS-001-CV-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
normative: false
---

# Wireframe de Baixa Fidelidade da Tela Hoje (identificador UXA-006)

O identificador técnico `UXA-006` serve somente para rastreabilidade. O nome de leitura desta superfície é **Tela Hoje**.

Esta versão incorpora a **Validação Funcional e Reformulação da Tela Hoje** e o princípio de **Presença Companheira e Coerência de Posicionamento da Guivos**.

## 1. Pergunta da superfície

> **O que mudou, o que merece minha atenção e quais possibilidades podem apoiar meu momento agora?**

A Tela Hoje é a hipótese de porta de entrada pessoal. Ela deverá reduzir esforço de decisão e transmitir continuidade de jornada sem transformar a Guivos em feed, catálogo infinito, painel de produtividade ou voz genérica de recomendação.

## 2. Wireframe reformulado

![Wireframe móvel reformulado da Tela Hoje](../assets/wireframes/uxa-006-hoje-mobile.svg)

[Visualizar o arquivo gráfico vetorial escalável](../assets/wireframes/uxa-006-hoje-mobile.svg)

O wireframe permanece monocromático e estrutural. Ele não define cores, tipografia, iconografia ou componentes finais.

## 3. Hierarquia aprovada

| Ordem | Bloco | Responsabilidade |
|---:|---|---|
| 1 | cabeçalho contextual | indicar a Tela Hoje, o contexto de atuação e o acesso a intervenções |
| 2 | síntese condicional | organizar o momento somente quando a leitura conjunta acrescentar compreensão |
| 3 | atenção principal | apresentar no máximo uma decisão ou ação prioritária, com alternativas legítimas |
| 4 | continuidade da jornada | manter vínculo com o Próximo Passo relevante |
| 5 | possibilidades para o próximo passo | apresentar até dois cartões legíveis em largura integral |
| 6 | experiência próxima em Coletivos | aparecer somente quando houver utilidade temporal |
| 7 | navegação global | permitir acesso a Hoje, Jornada, Explorar, Mapa e Eu |

A ausência de um bloco deverá reorganizar o espaço vertical. A tela não deverá manter áreas vazias apenas para preservar uma composição fixa.

## 4. Presença companheira na Tela Hoje

A superfície deverá permitir que a pessoa perceba:

> A Guivos compreende que minha jornada possui continuidade, organiza o que importa neste momento e me oferece possibilidades, mas a decisão continua sendo minha.

Isso deverá ser demonstrado por:

- reconhecimento do momento, sem intimidade artificial;
- explicação de relevância e prazo;
- conexão entre informação, objetivo e Próximo Passo;
- possibilidade de revisar, adiar, corrigir, recusar ou encerrar;
- linguagem calma e específica;
- ausência de culpa por inatividade;
- intenção comercial claramente identificada;
- estados vazios que preservem serenidade e continuidade.

A tela não deverá utilizar slogans motivacionais, recomendações sem explicação ou frases que poderiam pertencer indistintamente a qualquer aplicativo de tarefas, marketplace ou rede social.

## 5. Cabeçalho contextual

O cabeçalho deverá indicar:

- que a pessoa está na Tela Hoje;
- em qual contexto está atuando;
- acesso à Central de Intervenções;
- modo discreto ou proteção visual, quando aplicável.

A forma preferencial do seletor é:

> Agindo como: Minha jornada

As alternativas poderão representar uma Organização ou um Coletivo. A troca deverá ser explícita e não poderá executar ação institucional como se fosse pessoal.

## 6. Síntese condicional do momento

A síntese deverá reunir somente fatos ou avaliações suficientemente relevantes.

Exemplo alinhado ao posicionamento:

> Seu próximo passo está pronto. Há uma oportunidade com inscrições até sexta e uma atividade amanhã.

A síntese aparecerá quando houver pelo menos dois acontecimentos materiais cuja leitura conjunta reduza esforço de compreensão.

Ela será omitida quando:

- existir somente um item relevante;
- nenhum item material estiver disponível;
- a agregação repetir o bloco principal;
- a fonte estiver incompleta ou incerta;
- o resumo puder expor informação sensível.

Estado sem itens materiais:

> Nada precisa da sua atenção agora. Sua jornada permanece disponível quando fizer sentido continuar.

A síntese não deverá utilizar:

- culpa por ausência;
- comparação com outros participantes;
- contagem de dias consecutivos;
- volume de oportunidades como prova de qualidade;
- mensagens publicitárias disfarçadas.

## 7. Atenção principal

O wireframe reserva a maior hierarquia para um único item.

Critérios de seleção:

1. segurança e direitos;
2. prazo ou risco material;
3. confirmação solicitada;
4. processo já iniciado;
5. dependência ou bloqueio real;
6. prioridade declarada pelo participante.

Quando existirem múltiplos itens críticos:

- o item de maior prioridade ocupará o destaque;
- a tela informará a quantidade de itens adicionais;
- a Central de Intervenções reunirá os demais;
- os itens não disputarão simultaneamente a hierarquia principal.

A mensagem deverá explicar consequência e alternativas sem utilizar culpa. Exemplo:

> Sua vaga continua reservada até sexta. Você pode revisar agora ou deixar para depois.

Ações mínimas:

- ação principal;
- adiar, quando legítimo;
- abrir explicação;
- recusar, encerrar ou silenciar, quando aplicável.

## 8. Continuidade da jornada

O bloco deverá mostrar:

- formulação do Próximo Passo;
- objetivo relacionado;
- estado real;
- bloqueio ou dependência;
- ação possível.

O título preferencial é **Continuando sua jornada**, evitando a aparência de painel genérico de produtividade.

O bloco permanece antes das oportunidades para preservar a continuidade da jornada acima da descoberta comercial.

A ausência de Próximo Passo será válida. A interface não deverá exigir que a pessoa crie um movimento apenas para preencher a tela.

## 9. Possibilidades para o próximo passo

O título preferencial do bloco é **Possibilidades para seu próximo passo**. Os itens continuam sendo oportunidades funcionais, mas sua apresentação deverá explicar a relação legítima com a jornada.

A versão utiliza até dois cartões empilhados e em largura integral.

Conteúdo mínimo:

- tipo;
- título;
- preço ou gratuidade;
- prazo ou disponibilidade;
- localização ou modalidade;
- razão resumida de relevância;
- acesso à explicação.

Regras:

- o recorte deverá ser pequeno;
- nenhuma quantidade mínima será exigida;
- patrocínio não poderá elevar relevância funcional;
- a tela deverá evitar oportunidades repetitivas;
- o catálogo completo pertence a Explorar ou Minhas Oportunidades;
- uma oportunidade poderá ser relevante e ainda assim não aparecer hoje;
- a pessoa deverá poder abrir outras oportunidades sem sobrecarregar a superfície;
- contratar ou participar nunca será apresentado como obrigação de evolução.

## 10. Coletivos e atividades

O título preferencial é **Uma experiência próxima**, quando houver um acontecimento material.

O bloco permanecerá condicional e deverá privilegiar:

- atividade próxima;
- convite ou solicitação pendente;
- alteração material de regra, horário ou local;
- ação de causa ou voluntariado;
- decisão necessária de líder ou moderador;
- recurso com prazo de uso.

Publicações sociais sem finalidade, atualizações genéricas ou simples ausência recente não deverão ocupar a Tela Hoje.

## 11. Navegação global

A navegação permanece:

- Hoje;
- Jornada;
- Explorar;
- Mapa;
- Eu.

`Jornada` reúne contexto, objetivos, Próximos Passos, experiências e evolução. Esta reformulação não altera a nomenclatura consolidada.

## 12. Estados alternativos que ainda exigem wireframe

- nenhuma atenção e nenhuma oportunidade;
- informação sensível em modo discreto;
- múltiplos itens críticos;
- falha ao carregar uma fonte externa;
- oportunidade expirada após apresentação;
- alteração de preço em processo iniciado;
- contexto de Organização;
- contexto de Coletivo;
- acessibilidade com texto ampliado;
- baixa conectividade.

## 13. Decisões humanas aplicadas

1. A síntese do momento foi mantida como bloco condicional.
2. Um único item principal foi preservado.
3. O Próximo Passo permanece antes das oportunidades.
4. As oportunidades utilizam largura integral e empilhamento.
5. O bloco de Coletivos permanece somente com utilidade temporal.
6. O seletor de contexto explica que a pessoa está agindo em determinado papel.
7. A navegação Hoje, Jornada, Explorar, Mapa e Eu foi preservada.
8. A presença companheira e o propósito passam a orientar títulos, explicações, alternativas e estados vazios.

## 14. Perguntas ainda abertas

1. Qual estado alternativo da Tela Hoje deverá ser detalhado primeiro?
2. Como a Central de Intervenções apresentará múltiplos itens críticos?
3. Quais informações deverão permanecer ocultas na tela bloqueada?
4. Como a hierarquia se adapta a texto ampliado e leitores de tela?
5. Qual será o comportamento em baixa conectividade?
6. A presença companheira é percebida sem parecer personagem, amizade simulada ou pressão emocional?

## 15. Critérios de aceite do wireframe

O wireframe poderá avançar quando demonstrar que:

- a finalidade da tela é compreendida sem explicação externa;
- a Guivos é percebida como apoio contínuo à jornada, não como painel genérico;
- o contexto de atuação está explícito;
- a síntese não repete um único item;
- a atenção principal é identificada rapidamente;
- sugestão, decisão e compromisso permanecem distintos;
- preço e prazo aparecem sem pressão comercial;
- oportunidades permanecem legíveis em tela móvel;
- controle de relevância é encontrável;
- ausência de itens não é tratada como falha;
- a linguagem preserva autonomia, calma e possibilidade de pausa;
- a tela conduz a ações reais sem exigir permanência prolongada;
- a leitura não depende do conhecimento do identificador técnico.

## 16. Limites

Esta versão não autoriza protótipo navegável, design visual, testes de usabilidade, componentes técnicos ou desenvolvimento.