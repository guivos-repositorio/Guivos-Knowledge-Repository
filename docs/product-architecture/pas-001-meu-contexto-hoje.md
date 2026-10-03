---
id: PAS-001-CV-VIEW-001
title: Comportamentos Funcionais de Meu Contexto Hoje
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-CV-STATE-001
  - PAS-001-CV-UPDATE-001
  - PAS-001-CV-CONFLICT-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-VIEW-001 — Comportamentos Funcionais de Meu Contexto Hoje

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`, das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0`, das seções 60 a 83 do `PAS-001-CV-UPDATE-001 1.0.0` e das seções 84 a 113 do `PAS-001-CV-CONFLICT-001 1.0.0`.

A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

# 114. Comportamentos funcionais da interface `Meu Contexto Hoje`

`Meu Contexto Hoje` é a principal superfície de transparência, compreensão e controle do Contexto Vivo pelo participante.

Ela deverá permitir que a pessoa compreenda:

- o que a Guivos entende sobre seu momento;
- quais informações estão orientando sua experiência;
- de onde essas informações vieram;
- quais elementos são confirmados, inferidos, incertos ou históricos;
- o que mudou recentemente;
- quais informações precisam de revisão;
- quais conflitos permanecem abertos;
- como corrigir, limitar, ocultar ou remover informações.

> `Meu Contexto Hoje` não é um perfil estático, currículo, diagnóstico pessoal ou classificação definitiva da pessoa.

# 115. Objetivos funcionais

A interface deverá cumprir seis objetivos principais:

1. **Transparência:** mostrar como a Guivos compreende o contexto atual.
2. **Controle:** permitir que o participante altere informações e autorizações.
3. **Explicabilidade:** demonstrar origem, evidência e uso das informações.
4. **Atualização:** facilitar confirmações, correções e mudanças.
5. **Prevenção de erros:** tornar incertezas e conflitos visíveis.
6. **Continuidade:** permitir que a jornada evolua sem exigir reconstrução completa do contexto.

# 116. Princípios da interface

## 116.1 Linguagem humana

A interface deverá apresentar compreensões em linguagem acessível.

Em vez de:

```text
Direção.status = ACTIVE
confidence = 0.84
```

deverá apresentar:

> Seu objetivo de melhorar a saúde está ativo e foi confirmado recentemente.

Os atributos técnicos poderão existir internamente, mas não deverão ser a única forma de comunicação.

## 116.2 Representação humilde

A Guivos deverá utilizar formulações como:

- “Você informou que...”
- “Entendemos que...”
- “Esta informação pode ter mudado.”
- “Ainda não temos certeza sobre...”
- “Isso foi identificado a partir de...”
- “Gostaríamos de confirmar...”

A interface não deverá declarar inferências como verdades absolutas.

## 116.3 Controle proporcional

O participante deverá conseguir controlar uma informação sem precisar compreender toda a arquitetura de dados da plataforma.

## 116.4 Informação suficiente, não excessiva

A visão principal deverá apresentar o necessário para compreensão e ação.

Detalhes de origem, histórico, permissões e evidências deverão estar disponíveis progressivamente.

## 116.5 Não julgamento

Estados como abandono, restrição, dificuldade, conflito ou ausência de objetivo não deverão utilizar linguagem moralizante.

## 116.6 Reversibilidade

Sempre que aplicável, uma alteração deverá poder ser:

- revista;
- corrigida;
- desfeita;
- contestada;
- limitada;
- reaberta.

# 117. Estrutura funcional da visão principal

A visão principal deverá conter cinco áreas funcionais.

## 117.1 Síntese do momento atual

Uma explicação breve sobre o que parece mais relevante no momento.

Exemplo:

> Neste momento, sua prioridade principal é melhorar sua saúde. Você também está explorando possibilidades de desenvolvimento profissional. Sua disponibilidade está concentrada nos finais de semana.

Essa síntese deverá indicar quando contém interpretações ainda não confirmadas.

## 117.2 Dimensões do Contexto Vivo

As oito dimensões deverão estar disponíveis:

- Identidade;
- Momento;
- Direção;
- Capacidades;
- Restrições;
- Preferências;
- Relacionamentos;
- Evolução.

Cada dimensão deverá apresentar apenas seus elementos mais relevantes na visão inicial.

## 117.3 Mudanças recentes

Área destinada a informar:

- elementos confirmados;
- correções;
- novas informações;
- mudanças de estado;
- restrições encerradas;
- objetivos alterados;
- permissões modificadas;
- conflitos resolvidos.

## 117.4 Itens que precisam de atenção

Poderão ser apresentados:

- confirmações necessárias;
- informações envelhecidas;
- conflitos abertos;
- autorizações próximas de expirar;
- elementos incompletos que afetam uma ação atual.

## 117.5 Controles de informação

A interface deverá permitir acesso a:

- permissões;
- integrações;
- compartilhamentos;
- histórico;
- informações ocultadas;
- solicitações de exclusão;
- preferências de revisão.

# 118. Comportamento das dimensões

Cada dimensão deverá apresentar uma síntese funcional.

Exemplo:

```text
Direção

Objetivo principal:
Melhorar a saúde

Estado:
Ativo

Atualidade:
Confirmado recentemente

Uso:
Encontrar próximos passos, atividades e oportunidades

Ações:
Ver detalhes | Atualizar | Pausar | Corrigir
```

A síntese deverá considerar:

- estado funcional;
- cobertura;
- confiança;
- atualidade;
- necessidade de revisão;
- permissões;
- conflitos;
- elementos ativos.

# 119. Estados visuais e linguísticos

A interface deverá diferenciar claramente as condições da informação.

| Condição | Forma de apresentação |
|---|---|
| Confirmada | “Confirmado por você” |
| Declarada | “Informado por você” |
| Observada | “Identificado a partir de uma atividade” |
| Inferida | “Possível compreensão da Guivos” |
| Incerta | “Ainda não confirmado” |
| Contestada | “Você indicou que isso está incorreto” |
| Envelhecida | “Esta informação pode não representar mais seu momento” |
| Histórica | “Fez parte de um momento anterior” |
| Restrita | “Uso limitado por você” |
| Conflitante | “Existem informações diferentes sobre este ponto” |

Cor, ícone ou posição não deverão ser os únicos meios de diferenciação.

# 120. Níveis de detalhamento

A interface deverá utilizar divulgação progressiva.

## Nível 1 — Síntese

Apresenta a compreensão principal.

## Nível 2 — Elementos

Apresenta os elementos que compõem a dimensão.

## Nível 3 — Explicação

Apresenta:

- origem;
- data;
- tipo de informação;
- evidências;
- confiança;
- finalidade;
- permissões;
- histórico;
- conflitos relacionados.

O participante não deverá ser obrigado a navegar pelo nível técnico para executar ações básicas.

# 121. Explicação de uma informação

Cada elemento deverá responder, quando aplicável:

1. O que a Guivos entende?
2. Por que entende isso?
3. De onde veio a informação?
4. Quando foi obtida?
5. Ela foi confirmada?
6. Qual é sua atualidade?
7. Para que está sendo utilizada?
8. Com quais capacidades foi compartilhada?
9. Como afeta a experiência?
10. Como corrigir ou limitar seu uso?

Exemplo:

> Entendemos que você prefere atividades em grupo porque essa preferência foi informada durante a configuração da sua jornada em 10/07/2026. Ela está sendo utilizada para selecionar experiências de saúde e esporte. Você pode alterar ou limitar esse uso.

# 122. Ações disponíveis sobre um elemento

Conforme sua natureza, o participante poderá:

- confirmar;
- corrigir;
- complementar;
- atualizar;
- pausar;
- marcar como encerrado;
- contestar;
- ocultar;
- limitar a finalidade;
- impedir compartilhamento;
- remover;
- solicitar explicação;
- visualizar histórico.

Nem todas as ações deverão aparecer para todos os elementos.

# 123. Confirmação

A confirmação deverá ser simples e contextual.

Exemplo:

> Este objetivo continua sendo importante para você?

Ações:

- Sim, continua.
- Continua, mas mudou.
- Quero pausá-lo.
- Não faz mais sentido.
- Revisar depois.

A confirmação deverá atualizar:

- data;
- confiança;
- atualidade;
- horizonte de revisão;
- histórico.

# 124. Correção

Quando o participante corrigir uma informação, deverá poder indicar:

- qual é a informação correta;
- se a anterior sempre esteve errada;
- se ocorreu uma mudança real;
- desde quando a mudança vale;
- quais usos devem ser interrompidos.

A interface deverá distinguir:

```text
Corrigir informação anterior
```

de:

```text
Registrar uma mudança no meu contexto
```

Essa distinção deverá ser apresentada em linguagem compreensível.

# 125. Contestação

A ação `Isso não está correto` deverá estar disponível para interpretações e informações que possam afetar a experiência.

Após a contestação, a interface poderá oferecer:

- corrigir;
- explicar melhor;
- impedir o uso;
- remover;
- manter somente no histórico;
- informar que a situação mudou.

Uma contestação não deverá exigir que o participante prove que a Guivos está errada.

# 126. Informações inferidas

Inferências deverão ser claramente diferenciadas.

Exemplo:

> Percebemos que você pode estar explorando oportunidades de empreendedorismo.

Ações:

- Isso faz sentido.
- Estou apenas explorando.
- Não representa meu objetivo.
- Não utilizar essa interpretação.
- Explicar por que a Guivos entendeu isso.

Uma inferência não confirmada não deverá ser apresentada junto a declarações confirmadas sem diferenciação.

# 127. Comportamento diante de conflitos

Quando existir conflito relevante, a interface deverá:

- indicar que existem informações diferentes;
- evitar apresentar uma delas como verdade definitiva;
- explicar as origens;
- mostrar o impacto;
- permitir contextualização;
- suspender ações críticas quando necessário.

Exemplo:

> Existem duas informações diferentes sobre sua disponibilidade aos sábados.

```text
Informação anterior:
Disponível pela manhã

Informação recente:
Indisponível aos sábados
```

Ações:

- A situação mudou.
- As duas são válidas em contextos diferentes.
- Uma das informações está incorreta.
- Revisar depois.

# 128. Informações envelhecidas

A interface deverá diferenciar informação envelhecida de informação incorreta.

Exemplo:

> Você informou esta disponibilidade há oito meses. Ela ainda representa seu momento atual?

Ações:

- Sim.
- Atualizar.
- Não utilizar por enquanto.
- Revisar depois.

Informação envelhecida de baixo impacto poderá permanecer visível sem bloquear a experiência.

# 129. Informações sensíveis

Informações sensíveis deverão possuir apresentação e controles reforçados.

A interface deverá informar:

- por que a informação foi solicitada;
- para que está sendo utilizada;
- quais capacidades podem acessá-la;
- se foi inferida ou declarada;
- como limitar ou revogar o uso;
- consequências funcionais da revogação.

Informações sensíveis não deverão aparecer de forma exposta em resumos gerais quando isso não for necessário.

# 130. Permissões por finalidade

O participante deverá conseguir visualizar e controlar permissões por uso.

Exemplo:

```text
Localização aproximada

Encontrar eventos próximos: autorizado
Recomendar serviços: autorizado
Personalizar publicidade: não autorizado
Compartilhar com organizações: não autorizado
```

A alteração de uma finalidade não deverá modificar automaticamente as demais.

# 131. Integrações

A interface deverá apresentar as integrações que contribuem para o Contexto Vivo.

Para cada integração:

- nome da fonte;
- dados autorizados;
- finalidade;
- última atualização;
- duração da autorização;
- elementos produzidos;
- possibilidade de pausar;
- possibilidade de revogar;
- impacto da revogação.

Revogar uma integração não deverá necessariamente apagar fatos legítimos já registrados, mas deverá interromper novas coletas e usos não autorizados.

# 132. Histórico

O participante deverá poder visualizar mudanças relevantes em ordem temporal.

Exemplo:

```text
10/07 — Objetivo “melhorar a saúde” confirmado
15/06 — Disponibilidade alterada para sábado pela manhã
02/05 — Restrição temporária registrada
18/04 — Preferência por atividades coletivas informada
```

O histórico deverá diferenciar:

- fato ocorrido;
- data de registro;
- correção;
- mudança real;
- inferência;
- confirmação;
- alteração de permissão.

# 133. Evolução

A interface poderá mostrar evidências de evolução, desde que não transforme atividade em progresso automaticamente.

Exemplo:

```text
Objetivo: melhorar a saúde

Experiências realizadas:
- grupo de caminhada;
- avaliação profissional;
- desafio de 30 dias.

Evidências registradas:
- aumento da frequência de atividade;
- hábito confirmado pelo participante.

Compreensão atual:
Progresso autodeclarado.
```

O participante deverá poder contestar ou contextualizar a interpretação de evolução.

# 134. Estado sem informações suficientes

Quando uma dimensão possuir pouca informação, a interface não deverá simular compreensão.

Exemplo:

> Ainda não temos informações suficientes sobre as capacidades que você deseja utilizar nesta jornada.

Ações possíveis:

- adicionar informação;
- conversar sobre isso;
- importar de fonte autorizada;
- deixar para depois.

Ausência de informação não deverá ser apresentada como deficiência.

# 135. Dimensões não utilizadas

O participante poderá escolher não desenvolver determinada dimensão naquele momento.

Exemplo:

> Você decidiu não utilizar informações de relacionamentos nesta jornada.

A dimensão poderá permanecer:

- não configurada;
- limitada;
- temporariamente desativada;
- disponível para ativação futura.

A não utilização de uma dimensão não deverá impedir automaticamente o uso da Guivos.

# 136. Priorização de atenção

A interface não deverá apresentar todas as pendências com a mesma prioridade.

## Prioridade crítica

- conflito que afeta decisão imediata;
- informação sensível contestada;
- permissão revogada ainda em propagação;
- elemento crítico envelhecido;
- risco de oportunidade incompatível.

## Prioridade relevante

- objetivo que precisa de revisão;
- restrição temporária possivelmente encerrada;
- disponibilidade desatualizada;
- integração próxima de expirar.

## Prioridade opcional

- complementação de detalhe;
- dimensão ainda pouco compreendida;
- preferência antiga sem impacto atual;
- informação histórica incompleta.

# 137. Prevenção de sobrecarga

`Meu Contexto Hoje` não deverá se transformar em uma lista permanente de tarefas administrativas.

Para isso:

1. apenas itens relevantes deverão ganhar destaque;
2. revisões relacionadas poderão ser agrupadas;
3. ações poderão ser adiadas;
4. perguntas sem impacto atual deverão permanecer secundárias;
5. a pessoa poderá concluir ações progressivamente;
6. a Guivos deverá evitar solicitar novamente informações já disponíveis;
7. a interface deverá explicar quando nenhuma ação é necessária.

# 138. Relação com oportunidades e decisões

Quando uma informação afetar uma recomendação, o participante deverá poder acessar a explicação.

Exemplo:

> Esta atividade foi recomendada porque está relacionada ao seu objetivo de melhorar a saúde, ocorre aos sábados e corresponde à sua preferência por experiências coletivas.

A partir dessa explicação, o participante poderá:

- corrigir o contexto;
- ajustar uma preferência;
- indicar que a recomendação não faz sentido;
- limitar o uso de um elemento;
- solicitar alternativas.

# 139. Consequências das alterações

Antes de uma alteração relevante, a interface deverá informar seus efeitos previsíveis.

Exemplo:

> Ao pausar este objetivo, a Guivos deixará de utilizá-lo para sugerir próximos passos e oportunidades. Seu histórico será preservado.

Outro exemplo:

> Ao revogar o uso da localização, eventos próximos poderão deixar de ser priorizados.

A interface não deverá utilizar consequências como mecanismo de pressão.

# 140. Confirmação de alterações críticas

Alterações críticas poderão exigir confirmação adicional.

Exemplos:

- exclusão de informação;
- revogação ampla;
- encerramento de objetivo principal;
- remoção de restrição sensível;
- compartilhamento com organização;
- exclusão de histórico relevante.

A confirmação deverá explicar a ação, e não apenas solicitar um aceite genérico.

# 141. Recuperação e desfazimento

Quando aplicável, a interface deverá permitir:

- desfazer atualização;
- restaurar elemento histórico;
- reabrir objetivo;
- reativar preferência;
- revisar permissão;
- reabrir conflito;
- restaurar integração.

A recuperação deverá respeitar temporalidade e autorização atuais.

# 142. Comportamento em falhas

Quando uma atualização não puder ser concluída, a interface deverá informar:

- qual ação falhou;
- o que permaneceu inalterado;
- se algum uso foi suspenso preventivamente;
- como tentar novamente;
- como solicitar suporte.

A interface não deverá apresentar uma alteração como concluída antes de sua confirmação funcional.

# 143. Consistência entre canais

`Meu Contexto Hoje` poderá ser acessado por diferentes canais, mas deverá preservar o mesmo significado funcional.

Canais futuros poderão incluir:

- aplicação web;
- aplicativo móvel;
- conversa com a Guivos;
- voz;
- assistentes;
- canais organizacionais autorizados.

Uma alteração feita por conversa deverá ficar visível na interface principal.

# 144. Acessibilidade e compreensão

A interface deverá considerar:

- linguagem simples;
- navegação por teclado;
- leitores de tela;
- contraste adequado;
- diferenciação não dependente apenas de cor;
- explicações curtas com possibilidade de aprofundamento;
- adaptação a diferentes níveis de familiaridade digital;
- suporte a idiomas e contextos culturais.

# 145. Privacidade visual

A interface deverá permitir proteção contra exposição acidental.

Poderão existir:

- ocultação de detalhes sensíveis;
- visualização resumida;
- confirmação antes de revelar conteúdo;
- bloqueio por sessão;
- preferência de privacidade em dispositivos compartilhados.

# 146. Eventos funcionais relacionados

A interface poderá produzir:

- `ContextoVisualizado`;
- `DimensaoVisualizada`;
- `ExplicacaoSolicitada`;
- `InformacaoConfirmada`;
- `InformacaoCorrigida`;
- `MudancaContextualDeclarada`;
- `InformacaoContestada`;
- `InformacaoOcultada`;
- `UsoLimitado`;
- `PermissaoAlterada`;
- `RevisaoAdiada`;
- `ConflitoContextualizado`;
- `ObjetivoPausado`;
- `ElementoEncerrado`;
- `HistoricoConsultado`;
- `IntegracaoRevogada`;
- `AlteracaoDesfeita`.

Os eventos permanecem funcionais e não determinam implementação técnica.

# 147. Critérios funcionais de aceitação

`Meu Contexto Hoje` será considerado funcionalmente adequado quando permitir que o participante:

1. compreenda a síntese do contexto atual;
2. visualize as oito dimensões;
3. diferencie declaração, inferência, observação e histórico;
4. identifique informações incertas ou envelhecidas;
5. compreenda conflitos relevantes;
6. confirme, corrija ou conteste informações;
7. controle permissões por finalidade;
8. visualize origem e utilização;
9. consulte mudanças relevantes;
10. compreenda impactos de alterações;
11. revogue integrações e usos;
12. adie revisões não críticas;
13. desfaça ações quando aplicável;
14. compreenda por que uma oportunidade ou ação foi apresentada;
15. utilize a experiência sem preencher todas as dimensões.

# 148. Regras fundamentais de `Meu Contexto Hoje`

1. A interface representa uma compreensão atual, não uma definição permanente da pessoa.
2. A Guivos deverá mostrar incerteza quando existir incerteza.
3. Inferências deverão ser identificadas.
4. Informações históricas não deverão parecer atuais.
5. O participante deverá conseguir corrigir a Guivos.
6. Controle não deverá exigir conhecimento técnico.
7. Permissões deverão ser apresentadas por finalidade.
8. Informações sensíveis exigirão proteção reforçada.
9. Pendências deverão ser priorizadas por impacto.
10. A interface não deverá provocar fadiga de atualização.
11. Alterações relevantes deverão ser explicáveis.
12. O participante deverá continuar no controle da própria jornada.

Com isso, ficam definidos os **comportamentos funcionais da interface `Meu Contexto Hoje`**.

O próximo bloco da Capacidade 02 é a definição dos **contratos detalhados dos eventos funcionais do Contexto Vivo**.
