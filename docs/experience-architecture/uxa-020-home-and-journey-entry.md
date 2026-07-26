---
id: UXA-020
title: Página Inicial da Guivos e Início da Jornada
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-003
  - UXA-011
  - UXA-011-A1
related:
  - UXA-002
  - UXA-005
  - UXA-006
  - UXA-009
  - UXA-010
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - GIA-000
normative: true
---

# Página Inicial da Guivos e Início da Jornada (identificador UXA-020)

## 1. Decisão arquitetural

A experiência pessoal da Guivos possuirá uma **Página Inicial da Guivos**, denominada **HOME**, anterior à **Tela Hoje**.

A HOME será a primeira superfície para quem ainda não iniciou sua jornada e também permanecerá acessível para apresentar a Guivos e suas soluções como ecossistema integrado.

A sequência pessoal passa a ser:

```text
HOME da Guivos
→ convite para iniciar a jornada
→ relato voluntário do Momento Atual
→ compreensão inicial produzida pela Guivos
→ revisão, correção e autorização pela pessoa
→ Tela Hoje com síntese, oportunidades e Próximos Passos contextuais
```

A **Tela Hoje** deixa de ser a primeira entrada de uma pessoa sem contexto e passa a ser a principal superfície recorrente depois que a jornada possuir compreensão inicial suficiente e autorizada.

## 2. Pergunta da superfície

> **Como apresentar o impacto e a amplitude da Guivos, permitir que a pessoa conheça o ecossistema e convidá-la a iniciar sua jornada sem presumir seu contexto ou antecipar recomendações personalizadas?**

A HOME deverá permitir que a pessoa compreenda, antes de compartilhar dados:

1. o que é a Guivos;
2. como a Guivos pode apoiar uma jornada;
3. o que acontece quando ela conta seu Momento Atual;
4. quais soluções fazem parte do ecossistema;
5. que iniciar a jornada é voluntário;
6. que nenhuma solução será indicada como pessoalmente relevante antes de existir contexto autorizado suficiente.

## 3. Distinção entre HOME e Tela Hoje

| Superfície | Responsabilidade principal | Momento de uso |
|---|---|---|
| **HOME da Guivos** | apresentar propósito, impacto, início da jornada e soluções do ecossistema | primeira visita, jornada ainda não iniciada ou consulta institucional voluntária |
| **Tela Hoje** | organizar o que mudou, o que merece atenção e quais possibilidades podem apoiar o momento atual | após compreensão inicial confirmada e em retornos recorrentes |

A HOME não deverá assumir responsabilidades da Tela Hoje.

Ela não deverá:

- afirmar que compreende o momento da pessoa antes de receber informações;
- apresentar oportunidades como personalizadas;
- criar um resumo individual sem base autorizada;
- definir Próximo Passo antes da confirmação da compreensão inicial;
- simular relevância por popularidade, patrocínio ou interesse comercial;
- funcionar como catálogo infinito ou feed;
- obrigar a pessoa a iniciar a jornada para conhecer a Guivos.

A Tela Hoje não deverá repetir toda a apresentação institucional da HOME. Ela utilizará a compreensão já confirmada para apoiar continuidade, decisões e possibilidades contextuais.

## 4. Estados de entrada

### 4.1 Visitante sem autenticação

Poderá:

- compreender a proposta da Guivos;
- conhecer as soluções do ecossistema;
- visualizar exemplos claramente identificados como ilustrativos ou gerais;
- iniciar a jornada;
- acessar entrada, criação de conta, privacidade, acessibilidade e ajuda.

Não receberá indicação personalizada.

### 4.2 Pessoa autenticada sem jornada iniciada

Poderá:

- iniciar ou retomar o relato de seu Momento Atual;
- escolher quanto deseja compartilhar;
- conhecer o ecossistema sem personalização;
- salvar um relato incompleto, quando possível;
- adiar o início sem punição ou perda artificial.

### 4.3 Pessoa com relato em análise

Deverá visualizar:

- o que foi recebido;
- quais fontes estão sendo consideradas;
- quais etapas ainda dependem de confirmação;
- controles para interromper, remover ou substituir informações;
- linguagem que não prometa compreensão imediata ou perfeita.

### 4.4 Pessoa com compreensão inicial disponível

Deverá revisar:

- o que a Guivos compreendeu;
- informações confirmadas;
- observações autorizadas;
- inferências e respectivos níveis de confiança;
- informações desconhecidas;
- possíveis inconsistências;
- finalidade de uso;
- controles para corrigir, retirar ou limitar.

Somente após confirmação suficiente poderá avançar para a Tela Hoje com personalização material.

### 4.5 Pessoa com jornada iniciada

Após autenticação, a entrada recorrente preferencial poderá ser a **Tela Hoje**.

A HOME continuará acessível por:

- marca da Guivos;
- opção `Conhecer a Guivos`;
- opção `Ecossistema Guivos`;
- navegação institucional ou menu global.

A HOME não precisa ocupar uma posição permanente na navegação móvel principal `Hoje`, `Jornada`, `Explorar`, `Mapa` e `Eu`.

## 5. Hierarquia funcional da HOME

A ordem preferencial será:

```text
identidade e proposta de impacto
→ convite principal para iniciar a jornada
→ explicação simples de como a Guivos atua
→ formas de contar o Momento Atual
→ confiança, privacidade e controle
→ soluções do ecossistema
→ exemplos gerais e não personalizados
→ acesso institucional, ajuda e entrada
```

A ausência ou simplificação de um bloco deverá reorganizar a página sem criar espaços artificiais.

## 6. Bloco de impacto e início da jornada

O primeiro bloco deverá comunicar que toda jornada começa em um Momento Atual e que a Guivos pode ajudar a compreender possibilidades e próximos movimentos sem decidir pela pessoa.

Formulação de referência, não definitiva:

> **Toda jornada começa no momento em que você está agora.**
>
> Conte à Guivos o que está vivendo, buscando ou tentando transformar. A partir da sua autorização, organizaremos uma compreensão inicial do seu momento e apresentaremos possibilidades que podem apoiar seus próximos passos.

Ação principal preferencial:

> **Iniciar minha jornada**

Ações alternativas:

- `Contar meu momento`;
- `Conhecer o ecossistema`;
- `Entrar na minha conta`;
- `Continuar depois`.

A linguagem não deverá sugerir que compartilhar informações garante transformação, oportunidade, diagnóstico ou resultado.

## 7. Explicação de como a Guivos atua

A HOME deverá explicar um ciclo simples:

```text
você conta seu momento
→ a Guivos organiza uma compreensão inicial
→ você revisa e corrige
→ possibilidades são relacionadas ao contexto autorizado
→ você escolhe seus próximos passos
→ a jornada pode ser atualizada quando a realidade mudar
```

Deverão permanecer explícitos:

- a pessoa controla o que compartilha;
- a compreensão pode estar incompleta;
- inferências são diferentes de fatos confirmados;
- oportunidades são possibilidades, não ordens ou garantias;
- a jornada pode ser pausada, corrigida ou reiniciada;
- produtos, serviços e relações comerciais mantêm origem e intenção visíveis.

## 8. Relato multimodal do Momento Atual

A pessoa poderá contar seu momento por uma ou mais formas, conforme disponibilidade e autorização:

### 8.1 Texto livre

Poderá relatar:

- o que está vivendo;
- o que deseja compreender;
- o que pretende mudar, construir, resolver ou explorar;
- dificuldades, restrições e prioridades;
- acontecimentos recentes;
- o que não deseja receber ou considerar.

### 8.2 Voz

A experiência deverá:

- explicar que a voz poderá ser transcrita;
- permitir ouvir ou revisar a gravação, quando aplicável;
- apresentar a transcrição antes de utilizá-la materialmente;
- permitir corrigir, remover ou regravar;
- distinguir arquivo de áudio original e texto transcrito;
- informar finalidade, retenção e exclusão.

### 8.3 Arquivos

Poderão ser aceitos documentos, imagens ou outros formatos autorizados em evolução posterior.

Antes do uso, a pessoa deverá compreender:

- quais arquivos foram recebidos;
- o que poderá ser extraído;
- qual finalidade justifica a análise;
- se o arquivo contém informações sensíveis ou de terceiros;
- por quanto tempo será mantido;
- como remover o arquivo e os dados derivados;
- quais limitações de leitura existem.

O envio de um arquivo não autoriza uso irrestrito, compartilhamento externo ou interpretação de todas as informações nele contidas.

### 8.4 Escolhas rápidas e perguntas progressivas

A Guivos poderá oferecer perguntas curtas para reduzir esforço, sem transformar a jornada em formulário obrigatório.

As perguntas deverão ser adaptativas, adiáveis e justificadas. A pessoa poderá responder `não sei`, `prefiro não informar`, `isso não se aplica` ou utilizar texto livre.

### 8.5 Fontes externas autorizadas

Integrações futuras poderão contribuir com contexto somente quando:

- a fonte estiver identificada;
- a finalidade estiver clara;
- o escopo for limitado;
- o consentimento for revogável;
- os dados utilizados forem visíveis e corrigíveis;
- ausência de sincronização ou conflito for declarado.

## 9. Princípio de compartilhamento mínimo

A pessoa não precisará relatar toda a sua vida para iniciar uma jornada.

A experiência deverá buscar o mínimo suficiente para uma compreensão inicial legítima, considerando:

- intenção atual;
- mudança, necessidade ou possibilidade principal;
- restrições relevantes;
- preferências e limites;
- horizonte temporal, quando conhecido;
- autorização para utilização das informações.

Informações adicionais deverão ser solicitadas progressivamente quando possuírem utilidade compreensível.

## 10. Compreensão inicial apresentada pela Guivos

A Guivos deverá apresentar uma síntese revisável antes de utilizar o contexto para recomendações materiais.

A estrutura preferencial será:

### 10.1 O que você nos contou

Informações declaradas diretamente pela pessoa.

### 10.2 O que compreendemos até agora

Síntese produzida pela Guivos com linguagem condicional e específica.

### 10.3 O que pode estar relacionado

Inferências, relações ou hipóteses claramente identificadas.

### 10.4 O que ainda não sabemos

Lacunas que limitam a segurança da compreensão.

### 10.5 Como isso poderá ser utilizado

Finalidades autorizadas, como:

- organizar a Jornada;
- explicar possibilidades;
- relacionar oportunidades;
- apoiar a construção de Próximos Passos;
- reduzir repetição de perguntas;
- reconhecer mudanças posteriores.

### 10.6 Seus controles

Ações mínimas:

- `Está correto`;
- `Faz sentido parcialmente`;
- `Quero corrigir`;
- `Remover esta informação`;
- `Não usar para personalização`;
- `Contar mais`;
- `Prefiro continuar sem recomendações`;
- `Apagar e recomeçar`.

## 11. Gate de compreensão e personalização

A personalização material somente poderá começar quando existirem:

1. informação suficiente para justificar uma leitura inicial;
2. origem e finalidade identificadas;
3. distinção entre confirmado, observado, externo autorizado, inferido e desconhecido;
4. oportunidade real de revisão e correção;
5. autorização compatível com o uso;
6. ausência de conflito material não resolvido;
7. linguagem que preserve incerteza e autonomia.

Quando a base for insuficiente, a Guivos deverá declarar:

> **Ainda não compreendemos seu momento com segurança suficiente para indicar possibilidades pessoais.**

A pessoa poderá:

- compartilhar mais informações;
- revisar o que já informou;
- conhecer soluções e conteúdos gerais;
- explorar oportunidades sem personalização;
- sair e retornar depois.

A interface não deverá preencher lacunas com popularidade, publicidade, perfil demográfico genérico ou inferências sensíveis não autorizadas.

## 12. Acesso às soluções do ecossistema

A HOME deverá apresentar as soluções da Guivos com identidade, finalidade e público compreensíveis.

| Solução | Apresentação na HOME |
|---|---|
| **Guivos Journey** | organiza Momento Atual, objetivos, Próximos Passos, experiências e evolução |
| **Guivos Mall** | reúne produtos e serviços com condições comerciais transparentes |
| **Guivos Travel** | reúne viagens, destinos e experiências |
| **Guivos Business** | conecta Organizações, programas, públicos e oportunidades responsáveis |
| **Guivos Media** | reúne conteúdos, histórias e narrativas relacionadas à evolução humana e ao ecossistema |
| **Guivos Intelligence** | explica relações, contexto, possibilidades, fontes e incertezas |
| **Guivos Ads** | solução institucional de publicidade e patrocínio explicitamente identificados |

A HOME poderá permitir acesso e conhecimento de cada solução antes do início da jornada.

Antes do gate de personalização:

- os itens serão gerais, editoriais, institucionais ou resultantes de busca explícita;
- a interface não utilizará `para você`, `relevante para seu momento` ou equivalente;
- exemplos deverão ser identificados como exemplos;
- publicidade deverá ser identificada;
- posição comercial não será apresentada como relevância pessoal.

Depois do gate de personalização, as soluções poderão contribuir com possibilidades contextuais, mantendo sua origem visível.

## 13. Exploração sem iniciar a jornada

A pessoa poderá conhecer o ecossistema sem compartilhar seu Momento Atual.

Esse modo deverá preservar:

- busca e exploração geral;
- informações institucionais;
- categorias e exemplos;
- preços e condições, quando aplicáveis;
- origem de cada solução;
- ausência explícita de personalização;
- convite não coercivo para iniciar a jornada quando desejar.

A ausência de jornada iniciada não deverá resultar em punição, mensagens insistentes, redução artificial de conteúdo institucional ou criação de falsa urgência.

## 14. Transição para a Tela Hoje

Após a pessoa confirmar uma compreensão inicial suficiente, a transição deverá explicar o que acontecerá.

Exemplo de referência:

> **Sua jornada pode começar por aqui.**
>
> Organizamos uma compreensão inicial do que você compartilhou. Na Tela Hoje, você poderá revisar essa leitura, acompanhar o que merece atenção e considerar possibilidades relacionadas ao seu momento. Você continuará podendo corrigir ou limitar essas informações.

Ações possíveis:

- `Ir para a Tela Hoje`;
- `Revisar minha compreensão`;
- `Ajustar privacidade`;
- `Continuar contando meu momento`;
- `Sair e continuar depois`.

A Tela Hoje poderá inicialmente apresentar:

- síntese confirmada do Momento Atual;
- informações que ainda exigem revisão;
- um Próximo Passo proposto ou em construção;
- até duas oportunidades com razão explícita de relevância;
- alternativas de exploração geral;
- controles para corrigir a compreensão.

Nenhum bloco precisará ser preenchido artificialmente.

## 15. Wireframe textual de baixa fidelidade

```text
┌──────────────────────────────────────────────┐
│ GUIVOS                         Entrar  Ajuda  │
├──────────────────────────────────────────────┤
│ Toda jornada começa no momento em que você  │
│ está agora.                                  │
│                                              │
│ Conte o que está vivendo, buscando ou        │
│ tentando transformar.                        │
│                                              │
│ [ Iniciar minha jornada ]                    │
│ [ Conhecer o ecossistema ]                   │
├──────────────────────────────────────────────┤
│ COMO A GUIVOS PODE APOIAR                    │
│ Você conta → revisamos juntos → possibilidades│
│ aparecem com explicação → você decide.       │
├──────────────────────────────────────────────┤
│ CONTE SEU MOMENTO DO SEU JEITO               │
│ [ Escrever ] [ Falar ] [ Enviar arquivo ]    │
│ [ Responder perguntas rápidas ]              │
│ Você escolhe o que compartilhar.             │
├──────────────────────────────────────────────┤
│ PRIVACIDADE E CONTROLE                       │
│ Fontes, inferências, finalidade, correção e  │
│ exclusão permanecem acessíveis.              │
├──────────────────────────────────────────────┤
│ CONHEÇA O ECOSSISTEMA GUIVOS                 │
│ Journey | Mall | Travel | Business           │
│ Media | Intelligence | Ads                   │
│ Conteúdo geral — ainda não personalizado.    │
├──────────────────────────────────────────────┤
│ Propósito | Segurança | Acessibilidade       │
│ Privacidade | Termos | Contato               │
└──────────────────────────────────────────────┘
```

O wireframe é estrutural. Não define identidade visual, ilustrações, tipografia, cores, componentes ou responsividade final.

## 16. Estados alternativos obrigatórios

Deverão ser detalhados posteriormente:

- visitante que deseja apenas explorar;
- pessoa autenticada sem jornada;
- relato salvo incompleto;
- gravação interrompida;
- transcrição com baixa confiança;
- arquivo não suportado ou ilegível;
- arquivo com possível informação de terceiros;
- compreensão insuficiente;
- inferências contestadas;
- informação sensível em modo discreto;
- baixa conectividade;
- acessibilidade com texto ampliado ou navegação assistiva;
- pedido de exclusão durante a análise;
- jornada já iniciada com acesso voluntário à HOME;
- operação em outro idioma ou contexto cultural.

## 17. Privacidade, proteção e segurança

A HOME e o início da jornada deverão:

- solicitar somente informações justificáveis;
- evitar exposição de conteúdo sensível em telas compartilhadas;
- permitir pausa antes do envio;
- apresentar finalidade antes da coleta;
- permitir retirada e exclusão compatíveis com obrigações legítimas;
- distinguir dado original e interpretação derivada;
- impedir que arquivos de terceiros sejam tratados como autorização dessas pessoas;
- não realizar diagnóstico médico, psicológico, jurídico, financeiro ou espiritual;
- indicar ajuda humana ou profissional quando o contexto exigir;
- preservar acessibilidade e alternativas ao uso de voz, texto ou arquivo;
- impedir que recusa de uma modalidade bloqueie todas as demais.

## 18. Presença companheira na primeira entrada

A presença companheira deverá ser demonstrada sem afirmar conhecimento inexistente.

Antes do relato, a formulação correta é:

> **Podemos começar pelo que você considera importante contar.**

Não deverão ser utilizadas formulações como:

- `Já sabemos o que você precisa`;
- `Encontramos as melhores oportunidades para você`;
- `Complete seu perfil para desbloquear sua evolução`;
- `Conte tudo para receber resultados melhores`;
- `Você precisa iniciar agora`;
- `A Guivos conhece seu potencial`.

Depois da compreensão inicial, a linguagem continuará condicional, verificável e corrigível.

## 19. Critérios de aceite

A superfície poderá avançar quando demonstrar que:

1. a diferença entre HOME e Tela Hoje é compreendida;
2. a proposta de impacto da Guivos aparece antes das soluções comerciais;
3. iniciar a jornada é voluntário;
4. explorar o ecossistema sem personalização é possível;
5. texto, voz, arquivos e perguntas progressivas possuem controles equivalentes;
6. a pessoa compreende o que acontecerá com suas informações;
7. a Guivos não afirma compreensão antes de apresentar sua base;
8. a compreensão inicial pode ser corrigida, limitada ou rejeitada;
9. recomendações pessoais permanecem bloqueadas antes do gate;
10. soluções do ecossistema mantêm identidade e intenção comercial visíveis;
11. a transição para a Tela Hoje explica continuidade e controles;
12. estados de insuficiência não são preenchidos artificialmente;
13. acessibilidade, baixa conectividade e privacidade possuem alternativas;
14. a leitura independe do identificador técnico;
15. nenhum comportamento exige design visual ou implementação para ser compreendido.

## 20. Limites

Este documento não:

- define textos finais de marketing ou interface;
- aprova identidade visual da HOME;
- cria ilustrações, vídeo, animação ou fotografia;
- define formatos técnicos definitivos de arquivos;
- define reconhecimento de voz ou modelo de inteligência artificial;
- autoriza análise de dados sensíveis sem governança especializada;
- cria protótipo navegável;
- executa testes de usabilidade;
- define componentes técnicos ou APIs;
- inicia Engenharia de Produto ou desenvolvimento;
- altera as responsabilidades de Organização e Coletivo;
- transforma a HOME em canal obrigatório para cada retorno.

## 21. Próximo ponto de decisão

Após integração deste incremento, o próximo ato deverá ser autorizado separadamente e poderá escolher entre:

1. validar funcionalmente a HOME com cenários de primeira entrada;
2. criar o arquivo gráfico vetorial do wireframe de baixa fidelidade;
3. detalhar os estados de captura por texto, voz e arquivo;
4. detalhar a revisão da compreensão inicial;
5. validar a transição entre HOME e Tela Hoje.

Nenhuma dessas etapas é iniciada automaticamente.