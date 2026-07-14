---
id: PAS-001-EV-FOUNDATION-001
title: Fundamentos Iniciais da Capacidade de Eventos de Vida
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
supersedes_status: PAS-001 section 7 capacity 04 row
related:
  - PAS-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-EV-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Eventos de Vida

## 1. Autoridade e vínculo

Este documento é a **primeira extensão normativa da Capacidade 04 — Eventos de Vida** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional da especificação-base `PAS-001 0.5.0`, especialmente das definições de Estado, Evento de Vida e mapa de capacidades, e dos contratos finais do Contexto Vivo e da Capacidade de Objetivos.

Esta extensão substitui normativamente o estado `Planned / concept consolidated` da linha da Capacidade 04 na seção 7 do `PAS-001 0.5.0` e confirma seu estado `In progress`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade normativa desta extensão.

# 885. Fundamentos iniciais da Capacidade 04 — Eventos de Vida

A Capacidade de Eventos de Vida deverá permitir que a Guivos reconheça mudanças relevantes na realidade de uma Pessoa, Organização ou Coletivo e compreenda como essas mudanças podem afetar sua jornada.

Ela deverá conectar:

```text
estado anterior
→ mudança relevante
→ novo estado ou transição
→ impactos possíveis
→ reavaliação da jornada
```

> Um Evento de Vida não deverá ser tratado apenas como algo que aconteceu, mas como uma mudança temporalmente localizada capaz de alterar contexto, objetivos, prioridades, restrições, relações ou decisões.

# 886. Pergunta central

> **Como mudanças relevantes alteram a jornada do participante?**

A capacidade deverá responder:

- o que mudou;
- quando mudou;
- quem foi afetado;
- qual era o estado anterior;
- qual poderá ser o novo estado;
- quais dimensões contextuais foram impactadas;
- quais objetivos poderão precisar de revisão;
- quais decisões dependentes deverão ser reavaliadas;
- quais informações ainda são incertas;
- qual participação humana é necessária.

# 887. Objetivo funcional

O objetivo funcional da Capacidade 04 é:

> **Reconhecer, representar e acompanhar mudanças relevantes da vida real, permitindo que a Guivos atualize sua compreensão e reavalie a jornada de forma proporcional, explicável, segura e controlada pelo participante.**

A capacidade deverá reduzir o risco de a Guivos continuar operando com base em uma realidade que já mudou.

# 888. Valor entregue

A capacidade deverá entregar valor ao:

1. identificar mudanças que tornam o contexto anterior inadequado;
2. evitar recomendações baseadas em estado desatualizado;
3. permitir adaptação rápida da jornada;
4. reorganizar objetivos e prioridades quando necessário;
5. reconhecer novas restrições, capacidades e possibilidades;
6. preservar continuidade histórica;
7. reduzir a necessidade de o participante repetir toda a sua realidade;
8. apoiar momentos de transição;
9. permitir intervenção proporcional;
10. preservar o controle sobre informações sensíveis.

# 889. Singularidade funcional

A singularidade da Capacidade de Eventos de Vida é:

> **Governar mudanças relevantes capazes de alterar a jornada.**

Ela não deverá assumir integralmente a responsabilidade por:

- representar todo o contexto atual;
- governar objetivos;
- definir Próximos Passos;
- selecionar oportunidades;
- executar intervenções;
- registrar toda experiência;
- avaliar evolução humana;
- realizar diagnóstico clínico, jurídico, financeiro ou profissional.

# 890. Definição funcional de Evento de Vida

Evento de Vida é:

> **Uma ocorrência, transição ou mudança relevante, situada no tempo, capaz de alterar ou exigir reavaliação de uma ou mais dimensões do contexto, objetivos, prioridades, restrições, relações ou decisões da jornada.**

Um Evento de Vida poderá ser:

- pontual;
- progressivo;
- previsto;
- inesperado;
- iniciado;
- em andamento;
- concluído;
- interrompido;
- confirmado;
- contestado;
- sensível;
- individual;
- organizacional;
- coletivo.

# 891. Evento de Vida e estado

## Estado

Representa a realidade atual compreendida do participante.

## Evento de Vida

Representa uma mudança capaz de alterar essa realidade.

Exemplo:

```text
Estado anterior:
Empregado em determinada organização

Evento de Vida:
Encerramento do vínculo profissional

Estado possível posterior:
Em transição profissional
```

O evento deverá preservar a ligação entre o estado anterior e a condição posterior sem assumir que todos os efeitos já são conhecidos.

# 892. Unidade funcional

A unidade funcional será o **registro de Evento de Vida**.

Cada registro deverá possuir identidade própria e poderá se relacionar a:

- participante;
- período;
- estado anterior;
- estado resultante;
- dimensões afetadas;
- objetivos;
- outros eventos;
- evidências;
- fontes;
- permissões;
- decisões dependentes;
- experiências;
- organizações;
- relacionamentos.

O registro não deverá ser reduzido a uma simples anotação no perfil.

# 893. Critério de relevância

Uma mudança poderá ser tratada como Evento de Vida quando possuir potencial material para alterar:

- Momento Atual;
- identidade contextual;
- direção;
- objetivo;
- prioridade;
- capacidade;
- restrição;
- preferência relevante;
- relacionamento;
- disponibilidade;
- segurança;
- condição financeira;
- localização;
- vínculo institucional;
- necessidade de apoio;
- decisão futura;
- interpretação da evolução.

A relevância deverá ser contextual, não universal.

# 894. Relevância contextual

A mesma ocorrência poderá possuir impactos diferentes para participantes diferentes.

Exemplo:

```text
Mudança:
Alteração de residência

Participante A:
Mudança operacional de baixo impacto

Participante B:
Mudança de cidade, emprego, rede de apoio e objetivos
```

A Guivos não deverá aplicar impacto padronizado apenas pelo nome do evento.

# 895. Tipos iniciais de Evento de Vida

## 895.1 Profissional

Exemplos:

- contratação;
- desligamento;
- promoção;
- mudança de função;
- aposentadoria;
- início de empreendimento;
- encerramento de negócio;
- afastamento;
- mudança de equipe.

## 895.2 Educacional

Exemplos:

- início de formação;
- conclusão;
- aprovação;
- reprovação;
- abandono;
- mudança de área;
- ingresso em instituição.

## 895.3 Familiar e relacional

Exemplos:

- nascimento;
- casamento;
- separação;
- falecimento;
- mudança na composição familiar;
- início ou encerramento de relacionamento;
- necessidade de cuidado de familiar.

## 895.4 Residencial e geográfico

Exemplos:

- mudança de residência;
- mudança de cidade;
- imigração;
- retorno ao país;
- perda de moradia;
- alteração relevante de deslocamento.

## 895.5 Financeiro

Exemplos:

- mudança significativa de renda;
- endividamento;
- quitação relevante;
- recebimento de patrimônio;
- perda financeira;
- alteração de benefício.

## 895.6 Saúde e acessibilidade

Exemplos:

- diagnóstico informado pelo participante;
- recuperação;
- acidente;
- afastamento;
- nova necessidade de acessibilidade;
- mudança de capacidade funcional.

A Guivos não deverá realizar diagnóstico.

## 895.7 Social e comunitário

Exemplos:

- entrada em coletivo;
- saída de comunidade;
- início de voluntariado;
- mudança de papel social;
- participação em causa;
- rompimento de vínculo comunitário.

## 895.8 Espiritual e existencial

Exemplos:

- mudança de prática espiritual;
- entrada ou saída de comunidade religiosa;
- conversão declarada;
- crise de sentido;
- nova direção existencial.

Esses eventos exigirão proteção reforçada.

## 895.9 Organizacional

Exemplos:

- fusão;
- reestruturação;
- mudança de liderança;
- abertura ou fechamento de unidade;
- alteração estratégica;
- crise institucional;
- mudança regulatória relevante.

## 895.10 Coletivo

Exemplos:

- criação ou dissolução de coletivo;
- mudança de representação;
- mobilização;
- conquista comunitária;
- emergência local;
- alteração de regras internas.

# 896. Classificações não valorativas

Um Evento de Vida poderá ser percebido como:

- favorável;
- desfavorável;
- ambivalente;
- neutro;
- ainda não compreendido.

A classificação deverá representar a percepção contextual, não um julgamento universal da Guivos.

Exemplo:

> Uma promoção poderá representar conquista, sobrecarga, mudança de identidade profissional ou combinação desses efeitos.

# 897. Evento previsto e evento ocorrido

## Evento previsto

Existe expectativa ou planejamento de que determinada mudança aconteça.

Exemplo:

> Mudança de cidade prevista para dezembro.

## Evento ocorrido

A mudança foi reconhecida como efetivamente realizada ou iniciada.

Exemplo:

> Mudança de cidade iniciada em 10 de dezembro.

Planejamento não deverá ser apresentado como fato consumado.

# 898. Evento pontual e evento progressivo

## Pontual

Possui ocorrência temporal relativamente identificável.

Exemplo:

> Assinatura de contrato de trabalho.

## Progressivo

Ocorre ao longo de um período.

Exemplo:

> Transição gradual para assumir cuidados permanentes de um familiar.

Eventos progressivos deverão permitir:

- início aproximado;
- período;
- marcos;
- evolução;
- estado em andamento;
- incerteza temporal.

# 899. Evento simples e evento composto

## Evento simples

Representa uma mudança funcional principal.

## Evento composto

Agrupa mudanças relacionadas que formam uma transição maior.

Exemplo:

```text
Transição profissional

- desligamento;
- mudança de renda;
- início de busca;
- mudança de rotina;
- revisão de objetivos.
```

Os componentes deverão permanecer identificáveis quando produzirem efeitos próprios.

# 900. Evento primário e efeitos derivados

A capacidade deverá diferenciar:

## Evento primário

A mudança reconhecida.

## Efeito derivado

A consequência contextual ou funcional produzida.

Exemplo:

```text
Evento:
Desligamento profissional

Possíveis efeitos:
- alteração de renda;
- maior disponibilidade;
- mudança de prioridade;
- bloqueio de objetivo;
- criação de objetivo profissional;
- necessidade de apoio.
```

Os efeitos não deverão ser presumidos indiscriminadamente.

# 901. Evento de Vida e atividade

## Atividade

Representa algo realizado.

Exemplos:

- participar de reunião;
- fazer caminhada;
- enviar currículo;
- assistir a uma aula.

## Evento de Vida

Representa uma mudança relevante da realidade ou trajetória.

Exemplos:

- contratação;
- mudança de cidade;
- início de formação;
- encerramento de relacionamento.

Uma atividade não deverá ser transformada automaticamente em Evento de Vida.

# 902. Evento de Vida e experiência

## Experiência

Representa uma vivência efetivamente realizada.

## Evento de Vida

Representa uma mudança relevante que poderá decorrer da experiência ou alterar as experiências futuras.

Exemplo:

```text
Experiência:
Participar de uma ação voluntária

Possível Evento de Vida:
Assumir papel permanente de liderança em uma organização social
```

Nem toda experiência gera Evento de Vida.

# 903. Evento de Vida e mudança contextual

Toda mudança contextual não será necessariamente um Evento de Vida.

Exemplo de mudança contextual de baixa relevância:

- preferência temporária;
- alteração pequena de horário;
- mudança pontual de disponibilidade.

Uma mudança contextual poderá ser promovida a Evento de Vida quando possuir impacto suficiente sobre a jornada.

# 904. Evento de Vida e atualização comum

## Atualização comum

Corrige ou atualiza um elemento contextual sem representar transição relevante.

## Evento de Vida

Explica por que uma mudança significativa ocorreu ou começou a ocorrer.

Exemplo:

```text
Atualização:
Nova cidade de residência

Evento de Vida:
Mudança residencial de Belo Horizonte para Lisboa
```

A atualização poderá existir sem evento, e o evento poderá gerar múltiplas atualizações.

# 905. Evento de Vida e sinal

Um sinal representa informação que poderá indicar mudança.

Exemplos:

- alteração recorrente de localização;
- cancelamento de compromissos;
- mudança de padrão de atividade;
- novo vínculo em integração;
- ausência prolongada.

Sinal não deverá ser tratado automaticamente como Evento de Vida confirmado.

# 906. Evento de Vida e evidência

Evidência é a informação que sustenta o reconhecimento ou interpretação do evento.

Exemplos:

- declaração do participante;
- documento;
- confirmação institucional;
- integração autorizada;
- registro temporal;
- comunicação de representante autorizado.

A evidência não é o próprio evento.

# 907. Evento de Vida e objetivo

Evento de Vida e objetivo são unidades distintas.

```text
Evento:
Nascimento de um filho

Possíveis impactos:
- novo objetivo familiar;
- alteração de prioridade profissional;
- mudança de disponibilidade;
- aumento de restrições financeiras.
```

O evento poderá alterar objetivos, mas não deverá criar objetivo pessoal ativo sem confirmação.

# 908. Evento de Vida e Próximo Passo

Um Evento de Vida poderá gerar necessidade de ação.

Exemplo:

```text
Evento:
Mudança de cidade confirmada

Possível Próximo Passo:
Atualizar documentação de residência
```

A Capacidade de Eventos de Vida deverá informar a necessidade de reavaliação, mas não governar integralmente os Próximos Passos.

# 909. O que não constitui automaticamente Evento de Vida

Não deverão ser classificados automaticamente como Evento de Vida:

- clique;
- pesquisa;
- compra;
- consumo de conteúdo;
- visualização;
- presença isolada;
- atividade rotineira;
- notificação recebida;
- alteração técnica de cadastro;
- inferência comportamental;
- oportunidade apresentada;
- intenção futura não confirmada;
- pequena alteração sem impacto material.

# 910. Categorias de participante

A capacidade deverá operar para:

## Pessoa

Mudanças na realidade individual.

## Organização

Mudanças institucionais, estratégicas, operacionais ou estruturais.

## Coletivo

Mudanças compartilhadas governadas por regras próprias de participação e decisão.

A mesma ocorrência poderá gerar eventos distintos para participantes relacionados.

# 911. Titularidade do evento

O Evento de Vida deverá possuir titular identificado.

A titularidade poderá pertencer a:

- uma Pessoa;
- uma Organização;
- um Coletivo;
- mais de um participante, quando o evento for compartilhado.

Um evento que afeta determinada pessoa não deverá ser automaticamente registrado como evento próprio de todas as pessoas relacionadas.

# 912. Participantes afetados

Além do titular, o evento poderá afetar:

- familiares;
- equipes;
- organizações;
- profissionais;
- coletivos;
- beneficiários;
- dependentes;
- parceiros.

A capacidade deverá diferenciar:

- titular do evento;
- ator que causou ou participou;
- participante afetado;
- fonte da informação;
- representante autorizado.

# 913. Origem do Evento de Vida

Um evento poderá ser:

- declarado pelo participante;
- informado por representante autorizado;
- confirmado por organização;
- recebido por integração;
- observado por uma capacidade;
- sugerido pela Guivos Intelligence;
- derivado de outro evento;
- reconstruído retroativamente;
- identificado durante revisão contextual.

A origem deverá permanecer registrada.

# 914. Autoridade da fonte

Cada fonte poderá afirmar somente fatos sob sua autoridade.

| Fonte | Poderá confirmar | Não poderá confirmar |
|---|---|---|
| Participante | Sua vivência, percepção e mudança pessoal | Estado interno de terceiros |
| Organização | Vínculo, alteração institucional ou ocorrência organizacional | Impacto pessoal integral |
| Instituição de ensino | Matrícula, aprovação, conclusão | Transformação subjetiva |
| Serviço de saúde autorizado | Informação sob o escopo permitido | Objetivos e prioridades pessoais |
| Calendário | Evento planejado | Realização ou significado |
| Aplicativo externo | Ocorrência registrada | Impacto humano completo |
| Guivos Intelligence | Hipótese de mudança | Evento pessoal definitivo |

# 915. Eventos declarados

Quando o participante declarar uma mudança, a capacidade deverá preservar:

- linguagem original;
- data declarada;
- período;
- significado atribuído;
- participantes envolvidos;
- impactos percebidos;
- incertezas;
- sensibilidade;
- permissões.

A declaração poderá possuir autoridade suficiente para muitos eventos pessoais sem exigir documentação.

# 916. Eventos observados

Outra capacidade poderá observar uma ocorrência compatível com Evento de Vida.

O registro deverá permanecer como:

- sinal;
- observação;
- evento proposto;
- evento aguardando confirmação;

até que exista autoridade suficiente para o reconhecimento aplicável.

# 917. Eventos integrados

Uma integração poderá fornecer fatos como:

- contratação registrada;
- matrícula;
- conclusão institucional;
- mudança de endereço;
- nascimento registrado;
- alteração organizacional;
- encerramento de vínculo.

A capacidade deverá validar:

- identidade;
- escopo;
- autoridade;
- temporalidade;
- finalidade;
- consentimento ou outra base legítima;
- sensibilidade.

# 918. Eventos inferidos

Guivos Intelligence poderá inferir que uma mudança talvez tenha ocorrido.

Exemplo:

> Identificamos sinais de que sua situação profissional pode ter mudado. Isso está correto?

A inferência deverá:

- ser identificada como hipótese;
- apresentar base;
- indicar confiança;
- informar limitações;
- solicitar confirmação quando houver impacto relevante;
- não atualizar silenciosamente objetivos ou contexto sensível.

# 919. Confirmação proporcional ao impacto

A necessidade de confirmação deverá considerar:

- sensibilidade;
- intensidade do impacto;
- número de capacidades afetadas;
- reversibilidade;
- autoridade da fonte;
- risco de erro;
- finalidade;
- existência de conflito.

Mudanças de alto impacto deverão exigir confirmação ou autoridade equivalente.

# 920. Eventos sensíveis

Eventos poderão envolver:

- saúde;
- deficiência;
- religião;
- política;
- renda;
- dívida;
- sexualidade;
- família;
- violência;
- vulnerabilidade;
- localização precisa;
- migração;
- situação jurídica;
- segurança.

Esses eventos deverão possuir:

- finalidade específica;
- minimização;
- acesso restrito;
- proteção visual;
- compartilhamento seletivo;
- retenção proporcional;
- explicabilidade;
- possibilidade de contestação;
- ausência de exploração comercial.

# 921. Responsabilidades da Capacidade de Eventos de Vida

A capacidade deverá:

1. receber possíveis eventos;
2. distinguir sinal, atividade, experiência e evento;
3. preservar origem e temporalidade;
4. avaliar relevância;
5. representar o evento;
6. identificar titular e participantes afetados;
7. avaliar confiança;
8. solicitar confirmação proporcional;
9. identificar dimensões contextuais possivelmente afetadas;
10. identificar objetivos potencialmente impactados;
11. produzir propostas de atualização;
12. propagar recortes mínimos;
13. preservar histórico;
14. permitir correção e contestação;
15. acompanhar eventos em andamento;
16. tratar relações entre eventos;
17. proteger sensibilidade;
18. explicar impactos;
19. operar com falha segura;
20. manter o participante no controle.

# 922. Limites da capacidade

A capacidade não deverá:

1. considerar toda mudança como Evento de Vida;
2. criar evento definitivo apenas por inferência;
3. diagnosticar;
4. definir o significado emocional da mudança;
5. impor prioridade;
6. criar objetivo pessoal ativo;
7. concluir objetivo automaticamente;
8. gerar todos os Próximos Passos;
9. selecionar diretamente oportunidades;
10. notificar a cada mudança;
11. compartilhar conteúdo sensível sem finalidade;
12. criar perfil de terceiros;
13. presumir impacto uniforme;
14. apagar estado anterior;
15. reescrever o histórico;
16. classificar a mudança como sucesso ou fracasso universal;
17. utilizar vulnerabilidade comercialmente;
18. substituir o Contexto Vivo;
19. substituir a Capacidade de Objetivos;
20. decidir pela pessoa como deverá reagir.

# 923. Entradas iniciais

A capacidade poderá receber:

- declaração livre;
- correção;
- contestação;
- mudança registrada no Contexto Vivo;
- Evento de Vida planejado;
- fato institucional;
- informação organizacional;
- experiência realizada;
- sinal comportamental;
- evidência;
- documento;
- integração autorizada;
- comunicação de terceiro autorizado;
- hipótese da Guivos Intelligence;
- evento relacionado;
- solicitação de capacidade consumidora.

# 924. Requisitos mínimos de admissão

Uma entrada deverá possuir, conforme seu impacto:

- participante relacionado;
- origem;
- conteúdo mínimo;
- temporalidade;
- finalidade;
- autoridade;
- confiança;
- sensibilidade;
- permissões;
- possibilidade de confirmação;
- possibilidade de contestação.

Informações insuficientes deverão permanecer como sinal ou hipótese.

# 925. Estrutura funcional inicial do Evento de Vida

Cada evento poderá possuir:

| Atributo | Finalidade |
|---|---|
| Identificador | Distinguir o evento |
| Titular | Informar a quem pertence |
| Categoria do participante | Pessoa, Organização ou Coletivo |
| Tipo | Classificar funcionalmente |
| Descrição | Representar a mudança |
| Expressão original | Preservar a linguagem recebida |
| Origem | Identificar a fonte |
| Autoridade | Limitar o significado |
| Estado | Informar a condição atual |
| Data ou período | Situar temporalmente |
| Data de conhecimento | Informar quando a Guivos soube |
| Confiança | Representar certeza |
| Relevância | Informar impacto potencial |
| Dimensões afetadas | Relacionar ao Contexto Vivo |
| Objetivos afetados | Relacionar à direção |
| Participantes relacionados | Identificar envolvidos |
| Evidências | Sustentar reconhecimento |
| Sensibilidade | Aplicar proteção |
| Permissões | Limitar uso |
| Relações | Conectar outros eventos |
| Histórico | Preservar evolução |
| Impactos | Registrar efeitos confirmados ou propostos |

Nem todos os atributos serão obrigatórios para todo evento.

# 926. Temporalidade

A capacidade deverá distinguir:

- data do fato;
- início;
- término;
- duração;
- data estimada;
- data de conhecimento;
- data de confirmação;
- data de aplicação dos efeitos;
- período de impacto;
- revisão prevista.

A Guivos não deverá apresentar conhecimento retroativo como se estivesse disponível anteriormente.

# 927. Estados iniciais do Evento de Vida

Um evento poderá estar:

- Sinalizado;
- Proposto;
- Planejado;
- Confirmado;
- Iniciado;
- Em andamento;
- Concluído;
- Interrompido;
- Cancelado;
- Contestado;
- Corrigido;
- Arquivado.

O estado do evento não deverá ser confundido com o estado do participante.

# 928. Evento planejado

Um evento planejado poderá orientar preparação proporcional.

Exemplo:

> Mudança de residência prevista para o próximo semestre.

A capacidade poderá:

- registrar previsão;
- apoiar planejamento;
- solicitar revisão próxima;
- relacionar objetivos;
- preparar capacidades consumidoras autorizadas.

Ela não deverá aplicar todos os efeitos como se o evento já tivesse ocorrido.

# 929. Evento em andamento

Eventos progressivos poderão permanecer ativos durante determinado período.

A capacidade deverá permitir:

- atualizações;
- marcos;
- impactos parciais;
- mudanças de previsão;
- interrupção;
- conclusão;
- contestação.

# 930. Evento cancelado ou não realizado

Quando um evento planejado não ocorrer, a capacidade deverá:

- preservar o planejamento no histórico;
- registrar cancelamento;
- reverter apenas efeitos preparatórios aplicáveis;
- reavaliar decisões dependentes;
- não tratar como falha pessoal;
- distinguir cancelamento de adiamento.

# 931. Relações entre Eventos de Vida

Eventos poderão:

- causar;
- preceder;
- decorrer de;
- agravar;
- reduzir;
- substituir;
- compor;
- interromper;
- reverter;
- estar correlacionados sem causalidade confirmada.

A causalidade não deverá ser presumida apenas pela proximidade temporal.

# 932. Eventos simultâneos

Um participante poderá vivenciar diversos eventos no mesmo período.

A capacidade deverá:

- preservar cada evento;
- identificar interações;
- evitar sobrecarga de perguntas;
- priorizar impactos críticos;
- agrupar revisões compatíveis;
- permitir que efeitos permaneçam incertos;
- não reduzir a situação a um único evento dominante.

# 933. Impacto funcional

O impacto poderá ser:

- inexistente;
- baixo;
- moderado;
- alto;
- crítico;
- ainda indeterminado.

A classificação deverá considerar:

- quantidade de dimensões afetadas;
- objetivos impactados;
- duração;
- reversibilidade;
- urgência;
- sensibilidade;
- risco;
- percepção do participante;
- decisões dependentes.

# 934. Impacto confirmado e impacto proposto

## Impacto confirmado

Existe base suficiente para considerar que determinada dimensão ou objetivo foi afetado.

## Impacto proposto

A Guivos identifica possível efeito que ainda depende de avaliação.

Exemplo:

> Esta mudança poderá alterar sua disponibilidade para o objetivo profissional. Deseja revisar essa informação?

Possibilidade não deverá ser apresentada como fato.

# 935. Saídas iniciais

A capacidade poderá produzir:

- Evento de Vida registrado;
- evento proposto;
- evento confirmado;
- mudança contextual proposta;
- revisão de objetivo solicitada;
- conflito identificado;
- atualização de prioridade sugerida;
- bloqueio possível;
- nova possibilidade de objetivo;
- recorte para capacidade consumidora;
- necessidade de intervenção;
- evidência histórica;
- explicação;
- alerta de inconsistência;
- solicitação de confirmação.

# 936. Relação com o Contexto Vivo

O Contexto Vivo representa o estado autorizado do participante.

A Capacidade de Eventos de Vida deverá informar:

- o que mudou;
- quando;
- por qual origem;
- quais dimensões poderão ser afetadas;
- qual confiança existe;
- quais atualizações estão confirmadas;
- quais permanecem propostas.

O Contexto Vivo deverá governar a incorporação dessas mudanças ao estado atual.

# 937. Atualizações possíveis do Contexto Vivo

Um Evento de Vida poderá afetar:

- Identidade;
- Momento;
- Direção;
- Capacidades;
- Restrições;
- Preferências;
- Relacionamentos;
- Evolução.

O impacto deverá ser avaliado por dimensão.

Exemplo:

```text
Evento:
Mudança profissional

Possíveis impactos:
- Momento: transição;
- Capacidades: nova experiência;
- Restrições: disponibilidade reduzida;
- Direção: objetivo profissional revisado;
- Relacionamentos: nova organização.
```

# 938. Separação de responsabilidades com o Contexto Vivo

## Eventos de Vida

Governam a mudança e sua temporalidade.

## Contexto Vivo

Governa o estado contextual resultante.

```text
Evento de Vida:
explica a transição

Contexto Vivo:
representa a condição atual
```

Nenhuma das capacidades deverá absorver integralmente a responsabilidade da outra.

# 939. Relação com a Capacidade de Objetivos

Um Evento de Vida poderá:

- originar manifestação de direção;
- tornar objetivo inviável;
- alterar prioridade;
- produzir urgência;
- bloquear;
- desbloquear;
- modificar horizonte;
- criar conflito;
- exigir revisão;
- tornar critério inadequado;
- apoiar progresso;
- apoiar conclusão;
- motivar retirada;
- gerar novo ciclo.

# 940. Limites sobre Objetivos

A Capacidade de Eventos de Vida não deverá:

- criar objetivo pessoal confirmado;
- ativar objetivo;
- impor prioridade;
- concluir objetivo qualitativo;
- retirar objetivo;
- alterar critério pessoal definitivamente;
- presumir significado da mudança.

Ela deverá produzir evento, evidência ou proposta para a Capacidade de Objetivos.

# 941. Fluxo inicial com Objetivos

```text
Evento de Vida confirmado
→ objetivos potencialmente afetados identificados
→ impacto avaliado individualmente
→ revisões ou alterações propostas
→ participante confirma mudanças relevantes
→ Capacidade de Objetivos aplica seus contratos
→ capacidades consumidoras reavaliam decisões
```

# 942. Ausência de objetivo relacionado

Um Evento de Vida poderá existir sem objetivo relacionado.

Nessa situação, ele poderá:

- atualizar o Contexto Vivo;
- permanecer apenas no histórico;
- iniciar exploração;
- produzir necessidade de apoio;
- gerar oportunidade de reflexão;
- não produzir nenhuma ação imediata.

A capacidade não deverá criar objetivo apenas para preencher uma relação.

# 943. Relação com Captura de Contexto

A Captura de Contexto poderá identificar:

- mudança recente;
- evento planejado;
- evento em andamento;
- impacto percebido;
- correção;
- evento sensível.

Ela deverá preservar a expressão original e encaminhar a informação para avaliação da Capacidade 04.

# 944. Relação inicial com Próximos Passos

Eventos de Vida poderão gerar:

- necessidade de ação;
- suspensão de ação;
- preparação;
- espera;
- revisão;
- decisão urgente;
- cancelamento de caminho anterior.

A Capacidade 05 deverá governar as ações resultantes.

# 945. Relação inicial com Oportunidades Ativas

Um Evento de Vida poderá:

- tornar oportunidades relevantes;
- tornar oportunidades inadequadas;
- alterar localização;
- alterar disponibilidade;
- criar urgência;
- modificar restrições;
- abrir ou encerrar janelas temporais.

A mudança não deverá ser utilizada para exploração comercial.

# 946. Relação inicial com Intervenções Contextuais

A Capacidade 07 poderá decidir:

- agir;
- perguntar;
- orientar;
- lembrar;
- observar;
- esperar;
- silenciar.

Eventos sensíveis ou de baixa confiança não deverão gerar notificações invasivas.

# 947. Relação inicial com Experiências

Uma experiência poderá:

- produzir Evento de Vida;
- ser afetada por Evento de Vida;
- fornecer evidência;
- permanecer sem mudança relevante.

Experiência e Evento de Vida deverão manter registros distintos.

# 948. Relação inicial com Evolução Contínua

Eventos de Vida poderão constituir marcos relevantes da trajetória.

A Evolução Contínua poderá utilizá-los para compreender:

- transições;
- ciclos;
- mudanças sustentadas;
- respostas contextuais;
- novas capacidades;
- restrições superadas ou surgidas.

A ocorrência de evento não deverá ser tratada automaticamente como evolução positiva ou negativa.

# 949. Papel da Guivos Intelligence

Guivos Intelligence poderá:

- identificar sinais;
- sugerir classificação;
- detectar eventos relacionados;
- propor impactos;
- identificar objetivos possivelmente afetados;
- sugerir revisão;
- resumir mudanças;
- detectar inconsistências;
- produzir explicações.

Ela não deverá:

- confirmar unilateralmente evento pessoal sensível;
- definir significado emocional;
- ativar objetivo;
- impor prioridade;
- produzir diagnóstico;
- compartilhar o evento;
- tratar hipótese como fato.

# 950. Papel da Platform Layer

A Platform Layer poderá apoiar:

- identidade;
- autenticação;
- autorização;
- armazenamento;
- temporalidade;
- versionamento;
- eventos técnicos;
- grafo;
- APIs;
- integrações;
- auditoria;
- segurança;
- notificações;
- observabilidade.

Ela não deverá redefinir o significado funcional do Evento de Vida.

# 951. Controle do participante

O participante deverá poder:

- declarar;
- confirmar;
- corrigir;
- complementar;
- contestar;
- limitar;
- ocultar;
- remover de usos ativos;
- restringir compartilhamento;
- definir significado pessoal;
- informar impactos;
- adiar revisão;
- impedir notificações;
- consultar histórico.

# 952. Informações de terceiros

Quando um Evento de Vida envolver terceiro, a capacidade deverá:

- minimizar dados;
- evitar criar perfil;
- não atribuir estado interno;
- limitar finalidade;
- proteger identidade;
- permitir representação genérica;
- separar o evento do participante do evento do terceiro.

Exemplo:

> “Passei a cuidar de um familiar” não autoriza criar um perfil clínico do familiar.

# 953. Explicabilidade

O participante deverá conseguir compreender:

- por que a ocorrência foi tratada como possível Evento de Vida;
- qual foi a origem;
- se está confirmada;
- qual confiança existe;
- quais dimensões podem ser afetadas;
- quais objetivos podem precisar de revisão;
- quais capacidades receberam informação;
- quais ações permanecem pendentes;
- como corrigir ou contestar.

# 954. Eventos funcionais iniciais

A capacidade poderá produzir:

- `PossivelEventoDeVidaIdentificado`;
- `EventoDeVidaProposto`;
- `EventoDeVidaDeclarado`;
- `EventoDeVidaConfirmado`;
- `EventoDeVidaIniciado`;
- `EventoDeVidaAtualizado`;
- `EventoDeVidaConcluido`;
- `EventoDeVidaInterrompido`;
- `EventoDeVidaCancelado`;
- `EventoDeVidaContestado`;
- `EventoDeVidaCorrigido`;
- `EventoDeVidaRelacionado`;
- `ImpactoDeEventoDeVidaProposto`;
- `ImpactoDeEventoDeVidaConfirmado`;
- `DimensaoContextualImpactada`;
- `ObjetivoPotencialmenteImpactado`;
- `RevisaoPorEventoDeVidaSolicitada`;
- `RecorteDeEventoDeVidaProduzido`.

Os contratos detalhados serão definidos posteriormente.

# 955. Critérios funcionais de aceite

Este bloco será considerado adequado quando permitir:

1. definir Evento de Vida como mudança relevante;
2. separar evento e estado;
3. diferenciar evento, atividade, experiência e atualização contextual;
4. reconhecer eventos pontuais e progressivos;
5. representar eventos planejados e ocorridos;
6. preservar titularidade;
7. limitar autoridade das fontes;
8. manter inferências como hipóteses;
9. aplicar confirmação proporcional;
10. proteger eventos sensíveis;
11. identificar impactos sem aplicá-los indiscriminadamente;
12. preservar temporalidade;
13. relacionar múltiplos eventos;
14. atualizar Contexto Vivo por contratos próprios;
15. revisar Objetivos sem alterá-los unilateralmente;
16. produzir recortes mínimos;
17. preservar controle do participante;
18. explicar origem, confiança, impacto e uso;
19. tratar Pessoa, Organização e Coletivo;
20. impedir exploração comercial da vulnerabilidade.

# 956. Regras fundamentais

1. Evento de Vida representa mudança relevante, não qualquer ocorrência.
2. Evento de Vida e estado são conceitos distintos.
3. Atividade não equivale automaticamente a Evento de Vida.
4. Experiência não equivale automaticamente a Evento de Vida.
5. Atualização contextual não precisa possuir um Evento de Vida.
6. Evento planejado não equivale a evento ocorrido.
7. Evento progressivo poderá possuir duração e marcos.
8. Relevância depende do contexto.
9. O mesmo evento poderá produzir impactos diferentes.
10. Evento primário e efeitos derivados deverão permanecer distintos.
11. Sinal não equivale a evento confirmado.
12. Evidência não equivale ao evento.
13. Fonte somente poderá afirmar fatos sob sua autoridade.
14. Inferência relevante deverá ser confirmada.
15. Evento não cria objetivo pessoal ativo.
16. Evento não impõe prioridade.
17. Impactos deverão ser avaliados por dimensão e objetivo.
18. Contexto Vivo governa o estado resultante.
19. Objetivos governa alterações na direção.
20. Eventos sensíveis exigem proteção reforçada.
21. Informações de terceiros deverão ser minimizadas.
22. A Guivos não deverá definir unilateralmente o significado emocional da mudança.
23. Receita não deverá influenciar a classificação ou o tratamento do evento.
24. Histórico deverá preservar estado anterior, mudança e efeitos.
25. O participante deverá permanecer no controle.

Com isso, ficam definidos os **fundamentos iniciais da Capacidade 04 — Eventos de Vida**.

O próximo bloco deverá detalhar:

> **o ciclo de vida dos Eventos de Vida, incluindo identificação, proposição, confirmação, estados, temporalidade, relevância, impacto, relações, correção, contestação, encerramento e propagação.**
