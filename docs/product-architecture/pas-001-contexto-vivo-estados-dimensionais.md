---
id: PAS-001-CV-STATE-001
title: Estados Funcionais das Dimensões do Contexto Vivo
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
related:
  - PAS-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-STATE-001 — Estados Funcionais das Dimensões do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`. A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

As seções abaixo mantêm a numeração sequencial originalmente aprovada para a Capacidade 02.

# 46. Estados funcionais das dimensões do Contexto Vivo

As oito dimensões do Contexto Vivo não deverão ser tratadas como campos estáticos ou classificações definitivas da pessoa.

Cada dimensão poderá conter vários elementos simultâneos, com origens, níveis de confiança, temporalidades e permissões diferentes.

Exemplo:

> Na dimensão Identidade, uma pessoa pode ser profissional, estudante, responsável familiar e voluntária ao mesmo tempo. Um desses papéis pode estar ativo, outro emergindo e outro deixando de ser relevante.

Portanto, cada dimensão deverá possuir:

1. um **estado resumido**, utilizado para compreensão e orquestração;
2. os **elementos que compõem esse estado**;
3. a qualidade e atualidade das informações;
4. eventuais conflitos ou necessidades de revisão;
5. os controles definidos pelo participante.

## 46.1 Estrutura comum de estado

Toda dimensão deverá ser analisada por cinco perspectivas.

| Perspectiva | Pergunta respondida |
|---|---|
| Cobertura | A Guivos possui informação suficiente sobre essa dimensão? |
| Confiança | Qual é a força das informações e interpretações disponíveis? |
| Temporalidade | A representação ainda corresponde ao momento atual? |
| Condição funcional | O que está acontecendo nessa dimensão? |
| Necessidade de ação | É necessário confirmar, revisar, limitar ou atualizar algo? |

### Cobertura

- **Não compreendida:** não existem informações suficientes;
- **Parcial:** existem elementos relevantes, mas a compreensão ainda é incompleta;
- **Suficiente:** existem informações suficientes para a finalidade atual;
- **Ampliada:** existem informações detalhadas e evidências adicionais autorizadas.

Cobertura ampliada não representa necessariamente maior qualidade. O objetivo não é acumular dados, mas possuir informação suficiente para gerar valor.

### Confiança

- baixa;
- média;
- alta;
- muito alta;
- contestada.

### Temporalidade

- atual;
- em transição;
- possivelmente envelhecida;
- histórica;
- sem referência temporal suficiente.

### Necessidade de ação

- nenhuma ação necessária;
- observar;
- solicitar confirmação;
- solicitar atualização;
- resolver conflito;
- respeitar limitação;
- deixar de utilizar para determinada finalidade.

# 47. Estados da dimensão Identidade

A dimensão Identidade representa os papéis e formas pelas quais o participante se reconhece no momento.

## Estados funcionais

### Não expressa

O participante ainda não declarou papéis relevantes e não existem evidências suficientes para construir uma representação útil.

### Emergente

Um possível papel começou a aparecer, mas ainda está em formação ou possui baixa confirmação.

Exemplo:

> A pessoa começou a atuar em projetos voluntários, mas ainda não se reconhece como voluntária.

### Ativa

Um papel foi declarado ou confirmado como relevante no momento atual.

### Múltiplas identidades ativas

Dois ou mais papéis coexistem e influenciam a jornada.

Exemplos:

- profissional;
- estudante;
- responsável familiar;
- empreendedor;
- integrante de uma comunidade religiosa.

A Guivos não deverá presumir que um único papel representa toda a pessoa.

### Em transição

Um papel está sendo iniciado, encerrado ou transformado.

Exemplo:

> O participante está deixando de ser empregado para iniciar atuação como empreendedor.

### Contestada

A representação existente foi rejeitada, questionada ou considerada inadequada pelo participante.

### Histórica

O papel foi relevante anteriormente, mas não deve mais orientar a experiência atual, salvo quando seu histórico for necessário.

## Regras específicas

- papéis não deverão ser inferidos apenas por comportamento isolado;
- um papel profissional não deverá substituir a identidade integral da pessoa;
- papéis poderão coexistir, competir por prioridade ou perder relevância;
- o participante deverá poder escolher quais papéis deseja considerar em cada contexto.

# 48. Estados da dimensão Momento

A dimensão Momento representa as condições predominantes da vida atual.

## Estados funcionais

### Não compreendido

Não existem informações suficientes para identificar a situação atual de forma responsável.

### Parcialmente compreendido

Alguns elementos são conhecidos, mas ainda não existe uma síntese contextual suficiente.

### Relativamente estável

As condições relevantes permanecem suficientemente consistentes para orientar a jornada atual.

“Estável” não significa ausência de mudanças, mas inexistência de uma transição relevante identificada naquele momento.

### Em transição

Uma mudança relevante está ocorrendo.

Exemplos:

- mudança profissional;
- mudança de cidade;
- início de estudos;
- reorganização financeira;
- mudança familiar;
- início de nova rotina.

### Em reorganização

O participante está adaptando prioridades, recursos, disponibilidade ou decisões após uma mudança.

### Impactado por Evento de Vida

Um evento recente alterou ou pode alterar significativamente outras dimensões.

### Incerto ou conflitante

As informações disponíveis não permitem compreender com segurança qual condição deve orientar a jornada.

### Necessita revisão

A síntese existente perdeu atualidade ou existem sinais de mudança ainda não confirmados.

## Regras específicas

- o Momento deverá representar condições atuais, não uma classificação permanente;
- um Evento de Vida poderá alterar o Momento sem redefinir toda a pessoa;
- diferentes áreas da vida poderão apresentar condições distintas simultaneamente;
- a Guivos deverá evitar rótulos genéricos ou diagnósticos sobre a situação do participante.

# 49. Estados da dimensão Direção

A dimensão Direção representa objetivos, intenções, prioridades, sonhos e caminhos desejados.

## Estados funcionais

### Não definida

O participante não declarou uma direção ou não deseja defini-la naquele momento.

### Exploratória

A pessoa deseja descobrir possibilidades antes de estabelecer um objetivo específico.

### Declarada

Uma intenção ou objetivo foi expressado, mas ainda não possui prioridade ou estrutura suficiente.

### Ativa

A direção está vigente e pode orientar Próximos Passos e oportunidades.

### Priorizada

A direção foi reconhecida como foco principal ou recebeu prioridade explícita.

### Múltiplas direções ativas

Existem dois ou mais objetivos simultâneos.

Eles poderão ser:

- complementares;
- independentes;
- concorrentes;
- temporalmente sequenciais.

### Conflitante

Duas ou mais direções competem por tempo, recursos ou prioridade e exigem reflexão ou decisão do participante.

### Suspensa

A direção continua relevante, mas não deve orientar ações no momento.

### Concluída

O objetivo foi alcançado conforme o critério definido pelo participante.

### Abandonada ou retirada

O participante decidiu não continuar naquela direção.

### Necessita revisão

A direção permanece registrada, mas não existem evidências suficientes de que continue válida.

## Regras específicas

- ausência de objetivo não deverá ser tratada como falha;
- a Guivos poderá apoiar exploração sem pressionar por decisão imediata;
- conclusão, suspensão ou abandono deverão ser diferenciados;
- um objetivo não deverá permanecer ativo indefinidamente apenas porque não foi formalmente encerrado.

# 50. Estados da dimensão Capacidades

A dimensão Capacidades representa conhecimentos, competências, experiências, recursos e redes disponíveis.

## Estados funcionais

### Não identificada

Não existem informações suficientes sobre determinada capacidade.

### Declarada

O participante informou possuir uma capacidade, sem necessidade de evidência externa para todos os usos.

### Evidenciada

Existem experiências, resultados, certificações ou confirmações autorizadas que apoiam a declaração.

### Em desenvolvimento

A capacidade está sendo aprendida, praticada ou fortalecida.

### Disponível

A capacidade existe e pode ser utilizada no contexto atual.

### Parcialmente disponível

A capacidade existe, mas sua utilização está limitada por tempo, recursos, confiança, atualização ou contexto.

### Indisponível no momento

A capacidade não pode ser utilizada nas condições atuais, ainda que faça parte do histórico do participante.

### Possivelmente desatualizada

A capacidade foi registrada anteriormente, mas poderá exigir revisão.

### Contestada

A declaração, evidência ou interpretação foi questionada.

## Regras específicas

- não possuir certificação não significa não possuir capacidade;
- possuir capacidade não significa disponibilidade para utilizá-la;
- a Guivos não deverá atribuir nível profissional sem evidência ou critério adequado;
- capacidades poderão ser formais, práticas, sociais, relacionais ou adquiridas por experiência.

# 51. Estados da dimensão Restrições

A dimensão Restrições representa limites que podem afetar decisões, oportunidades e experiências.

## Estados funcionais

### Nenhuma restrição declarada

O participante não informou restrições relevantes para a finalidade atual.

Isso não significa que nenhuma restrição exista.

### Potencial

Existe um possível limite, mas seu impacto ainda não foi confirmado.

### Ativa

A restrição influencia atualmente as possibilidades do participante.

### Temporária

A restrição possui duração ou condição previsivelmente limitada.

### Recorrente

A restrição pode reaparecer em determinadas situações ou períodos.

### Condicional

A restrição somente existe sob condições específicas.

Exemplo:

> A pessoa pode participar de atividades presenciais, desde que ocorram aos finais de semana.

### Reduzida

O impacto da restrição diminuiu, mas ainda pode ser relevante.

### Resolvida

A restrição deixou de afetar a jornada atual.

### Incerta ou conflitante

As informações disponíveis são insuficientes ou divergentes.

### Restrita pelo participante

O participante não deseja informar detalhes, mas indica que existe uma condição que deve ser respeitada.

## Regras específicas

- restrições não deverão ser tratadas como deficiências pessoais;
- a Guivos deverá utilizar apenas o nível de detalhe necessário;
- restrições sensíveis poderão ser representadas funcionalmente sem exposição da causa;
- uma restrição resolvida deverá deixar de bloquear oportunidades futuras.

# 52. Estados da dimensão Preferências

A dimensão Preferências representa formas desejadas de participação, interação e experiência.

## Estados funcionais

### Não expressa

Nenhuma preferência relevante foi declarada.

### Tentativa

Existe um sinal inicial, mas ainda não há confirmação suficiente.

### Declarada

O participante informou diretamente uma preferência.

### Confirmada

A preferência foi reiterada ou confirmada em situações coerentes.

### Contextual

A preferência é válida somente para determinada área, situação ou finalidade.

Exemplo:

> A pessoa prefere experiências online para estudos, mas presenciais para atividades esportivas.

### Persistente

A preferência mostrou estabilidade durante período relevante.

### Alterada

O participante indicou uma nova preferência que substitui ou modifica a anterior.

### Conflitante

Existem preferências diferentes para contextos ainda não suficientemente diferenciados.

### Retirada

O participante não deseja mais que determinada preferência seja considerada.

### Necessita revisão

A preferência é antiga ou deixou de apresentar evidências suficientes de atualidade.

## Regras específicas

- comportamento observado não deverá automaticamente se tornar preferência;
- preferências não deverão limitar permanentemente a descoberta de novas possibilidades;
- a pessoa poderá escolher receber alternativas fora de suas preferências usuais;
- preferências contextuais deverão ser priorizadas sobre generalizações amplas.

# 53. Estados da dimensão Relacionamentos

A dimensão Relacionamentos representa Pessoas, Organizações e Coletivos relevantes para a jornada.

## Estados funcionais

### Não identificado

Nenhum relacionamento relevante foi informado para a finalidade atual.

### Identificado

O vínculo foi reconhecido, mas sua relevância ainda não foi plenamente estabelecida.

### Potencial

Existe possibilidade de conexão, apoio ou colaboração, mas o relacionamento ainda não foi formado.

### Relevante

O relacionamento possui importância reconhecida para determinada área ou objetivo.

### Ativo

Existe interação, colaboração, participação ou vínculo atual.

### Enfraquecido ou inativo

O relacionamento permanece no histórico, mas não apresenta atividade ou relevância atual suficiente.

### Encerrado

O vínculo deixou de existir ou não deve mais orientar a jornada.

### Restrito

O participante limitou o uso, exposição ou compartilhamento relacionado ao vínculo.

### Conflitante

O relacionamento produz benefícios e dificuldades simultâneos, ou existem informações divergentes sobre sua condição.

### Necessita revisão

A atualidade ou relevância do vínculo não está suficientemente clara.

## Regras específicas

- relacionamento não significa automaticamente confiança;
- vínculo digital não significa relacionamento relevante;
- a Guivos não deverá expor informações de terceiros sem base adequada;
- relacionamentos deverão ser representados conforme finalidade e autorização.

# 54. Estados da dimensão Evolução

A dimensão Evolução representa mudanças, resultados e evidências acumuladas ao longo do tempo.

## Estados funcionais

### Base não estabelecida

Ainda não existe referência suficiente para comparar mudanças.

### Base estabelecida

Existe um estado inicial ou anterior capaz de permitir comparação futura.

### Mudança observada

Foi identificada diferença entre dois momentos, sem conclusão automática sobre seu significado.

### Progresso evidenciado

Existem evidências autorizadas de avanço em relação a objetivo ou condição definida.

### Progresso autodeclarado

O participante reconhece avanço, ainda que não exista evidência externa.

### Resultado misto

Existem avanços e dificuldades simultâneos.

### Marco alcançado

Um resultado relevante foi concluído ou reconhecido pelo participante.

### Dificuldade ou retrocesso relatado

O participante informou perda, interrupção ou afastamento de uma condição desejada.

Esse estado não deverá ser utilizado como julgamento ou classificação permanente.

### Sem evidência recente

Não existem informações suficientes para afirmar mudança recente.

### Suspensa para avaliação

A interpretação da evolução depende de confirmação, evidências adicionais ou resolução de conflito.

## Regras específicas

- mudança não significa necessariamente progresso;
- atividade não significa resultado;
- conclusão de oportunidade não significa evolução automática;
- evolução deverá ser relacionada a objetivos, condições ou critérios reconhecidos;
- dificuldades e retrocessos fazem parte da jornada e não deverão ser tratados como falha moral;
- a visão histórica deverá preservar avanços, mudanças, pausas e revisões.

# 55. Estado resumido de uma dimensão

Cada dimensão poderá produzir uma síntese como:

```text
Dimensão: Direção
Cobertura: suficiente
Condição funcional: múltiplas direções ativas
Confiança: alta
Temporalidade: atual
Prioridade: saúde
Direção secundária: desenvolvimento profissional
Conflitos: disponibilidade limitada
Revisão necessária: não
Permissão: uso autorizado para Próximos Passos e oportunidades
```

Essa síntese não substitui os elementos internos da dimensão. Ela funciona como uma representação operacional e explicável para a experiência.

# 56. Transições entre estados

As transições deverão ocorrer por evidências autorizadas.

Exemplos:

```text
Direção exploratória
→ direção declarada
→ direção ativa
→ direção priorizada
→ direção concluída
```

```text
Restrição potencial
→ restrição ativa
→ restrição reduzida
→ restrição resolvida
```

```text
Preferência tentativa
→ preferência declarada
→ preferência confirmada
→ preferência alterada
```

Uma transição poderá:

- avançar;
- retroceder;
- ser suspensa;
- ser contestada;
- retornar para revisão;
- manter dois estados contextuais simultâneos.

Não deverá existir uma única sequência obrigatória para todas as pessoas.

# 57. Impactos entre dimensões

Uma alteração poderá propor impactos em outras dimensões, mas não deverá atualizá-las automaticamente sem evidência suficiente.

Exemplo:

> Uma mudança de emprego poderá alterar Momento e Identidade. Ela também poderá afetar Capacidades, Restrições e Direção, mas esses efeitos precisam ser avaliados separadamente.

O fluxo funcional será:

```text
Mudança identificada
→ dimensões possivelmente afetadas
→ avaliação individual
→ confirmação proporcional
→ atualização seletiva
→ novo Contexto Vivo
```

# 58. Regras gerais dos estados dimensionais

1. Nenhum estado deverá ser tratado como identidade definitiva da pessoa.
2. Estados resumidos deverão ser explicáveis.
3. Uma dimensão poderá conter elementos em estados diferentes.
4. Atualizações deverão preservar origem e histórico.
5. Estados sensíveis ou de alto impacto exigirão confirmação proporcional.
6. Ausência de informação não deverá ser interpretada como ausência de condição.
7. Estados históricos não deverão orientar automaticamente experiências atuais.
8. O participante poderá contestar o estado resumido.
9. As dimensões poderão evoluir em ritmos diferentes.
10. Nenhuma dimensão deverá ser utilizada além das finalidades autorizadas.

## 59. Estado do bloco e próximo ponto

Com este documento, ficam definidos:

- a estrutura comum de estado;
- os estados funcionais de Identidade, Momento, Direção, Capacidades, Restrições, Preferências, Relacionamentos e Evolução;
- as transições possíveis;
- os impactos controlados entre dimensões;
- as regras gerais de representação dimensional.

O próximo bloco normativo da Capacidade 02 deverá especificar as **regras detalhadas de atualização e envelhecimento do Contexto Vivo**.
