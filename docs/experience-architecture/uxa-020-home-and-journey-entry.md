---
id: UXA-020
title: Página Inicial da Guivos e Início da Jornada
status: active
version: 0.2.0
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

A HOME será uma superfície pública e institucional. Ela apresentará a Guivos, seu propósito, o ecossistema e o convite voluntário para iniciar uma jornada. Ela não será o ambiente em que texto, voz ou arquivos pessoais serão coletados ou processados.

O relato do Momento Atual acontecerá em um **fluxo protegido de início da jornada**, separado da HOME por uma transição consciente.

A sequência pessoal será:

```text
Página Inicial da Guivos
→ apresentação do propósito e do ecossistema
→ decisão voluntária de iniciar a jornada
→ autenticação e explicação de privacidade, quando necessárias
→ fluxo protegido de relato do Momento Atual
→ compreensão inicial produzida pela Guivos
→ revisão, correção, limitação e autorização pela pessoa
→ Tela Hoje com síntese, oportunidades e Próximos Passos contextuais
```

A **Tela Hoje** deixa de ser a primeira entrada de uma pessoa sem contexto e passa a ser a principal superfície recorrente depois que a jornada possuir compreensão inicial suficiente, revisável e autorizada.

## 2. Pergunta da superfície

> **Como apresentar o impacto e a amplitude da Guivos, permitir que a pessoa conheça o ecossistema e convidá-la a iniciar sua jornada sem presumir seu contexto, coletar informações indevidamente ou antecipar recomendações personalizadas?**

A HOME deverá permitir que a pessoa compreenda, antes de compartilhar dados:

1. o que é a Guivos;
2. como a Guivos pode apoiar uma jornada;
3. o que acontecerá caso ela decida contar seu Momento Atual;
4. quais soluções fazem parte do ecossistema;
5. que iniciar a jornada é voluntário;
6. que explorar a Guivos não exige iniciar a jornada;
7. que nenhuma solução será indicada como pessoalmente relevante antes de existir contexto autorizado suficiente.

## 3. Superfícies distintas

| Superfície | Responsabilidade principal | Momento de uso |
|---|---|---|
| **Página Inicial da Guivos** | apresentar propósito, impacto, soluções e caminhos de entrada | primeira visita, consulta institucional ou retorno voluntário à apresentação da Guivos |
| **Início protegido da jornada** | receber o relato, governar consentimento, autenticação, privacidade e compreensão inicial | depois da escolha consciente de iniciar ou retomar a jornada |
| **Tela Hoje** | organizar o que mudou, o que merece atenção e quais possibilidades podem apoiar o momento | depois da compreensão inicial confirmada e nos retornos recorrentes |

A HOME não deverá assumir responsabilidades do início protegido da jornada ou da Tela Hoje.

Ela não deverá:

- afirmar que compreende o momento da pessoa antes de receber informações;
- apresentar oportunidades como personalizadas;
- criar resumo individual sem base autorizada;
- definir Próximo Passo antes da confirmação da compreensão inicial;
- simular relevância por popularidade, patrocínio ou interesse comercial;
- funcionar como catálogo infinito ou feed;
- obrigar a pessoa a iniciar a jornada para conhecer a Guivos;
- coletar texto livre, voz, documentos, imagens ou outras informações pessoais diretamente na superfície pública;
- iniciar gravação, leitura de arquivo ou processamento sem transição consciente e finalidade explicada.

A Tela Hoje não deverá repetir toda a apresentação institucional da HOME. Ela utilizará a compreensão confirmada para apoiar continuidade, decisões e possibilidades contextuais.

## 4. Roteamento por estado

### 4.1 Visitante sem autenticação

Poderá:

- compreender a proposta da Guivos;
- conhecer as soluções do ecossistema;
- visualizar exemplos claramente identificados como gerais ou ilustrativos;
- pesquisar e explorar conteúdo geral;
- escolher iniciar a jornada;
- acessar entrada, criação de conta, privacidade, acessibilidade e ajuda.

Não receberá indicação personalizada e não terá relato pessoal processado na HOME.

### 4.2 Pessoa autenticada sem jornada iniciada

Poderá:

- iniciar o fluxo protegido da jornada;
- conhecer o ecossistema sem personalização;
- adiar o início sem punição ou perda artificial;
- compreender o que será solicitado antes de compartilhar informações.

### 4.3 Pessoa com relato salvo ou em andamento

Será direcionada ao ambiente protegido e poderá:

- retomar o relato;
- revisar o que já informou;
- substituir ou remover informações;
- interromper o processo;
- excluir o relato, conforme as regras aplicáveis;
- voltar à exploração geral sem concluir a jornada.

### 4.4 Pessoa com relato em análise

Deverá visualizar:

- o que foi recebido;
- quais fontes estão sendo consideradas;
- quais etapas ainda dependem de confirmação;
- controles para interromper, remover ou substituir informações;
- linguagem que não prometa compreensão imediata ou perfeita.

### 4.5 Pessoa com compreensão inicial disponível

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

### 4.6 Pessoa com jornada iniciada

Após autenticação, a entrada recorrente preferencial será a **Tela Hoje**.

A HOME continuará acessível por:

- marca da Guivos;
- opção `Conhecer a Guivos`;
- opção `Ecossistema Guivos`;
- navegação institucional ou menu global.

A HOME não precisa ocupar uma posição permanente na navegação móvel principal `Hoje`, `Jornada`, `Explorar`, `Mapa` e `Eu`.

## 5. Hierarquia funcional da HOME pública

A ordem preferencial será:

```text
identidade e proposta de impacto
→ convite principal para iniciar a jornada
→ explicação simples de como a Guivos atua
→ confiança, privacidade e controle
→ soluções do ecossistema
→ exemplos gerais e não personalizados
→ acesso institucional, ajuda e entrada
```

A HOME poderá explicar que texto, voz, arquivos e perguntas progressivas estarão disponíveis depois do início consciente da jornada, mas não deverá exibir controles ativos de coleta na página pública.

A ausência ou simplificação de um bloco deverá reorganizar a página sem criar espaços artificiais.

## 6. Bloco de impacto e início da jornada

O primeiro bloco deverá comunicar que toda jornada começa em um Momento Atual e que a Guivos pode ajudar a compreender possibilidades e próximos movimentos sem decidir pela pessoa.

Formulação de referência, não definitiva:

> **Toda jornada começa no momento em que você está agora.**
>
> Conheça a Guivos e, quando desejar, inicie sua jornada. Em um ambiente protegido, você poderá contar o que está vivendo, buscando ou tentando transformar, revisar o que compreendemos e decidir como essas informações poderão apoiar seus próximos passos.

Ação principal preferencial:

> **Iniciar minha jornada**

Ações alternativas:

- `Conhecer o ecossistema`;
- `Entrar na minha conta`;
- `Continuar depois`.

A opção `Contar meu momento` poderá existir somente quando conduzir claramente ao fluxo protegido, sem iniciar coleta imediata na HOME.

A linguagem não deverá sugerir que compartilhar informações garante transformação, oportunidade, diagnóstico ou resultado.

## 7. Explicação de como a Guivos atua

A HOME deverá explicar um ciclo simples:

```text
você decide iniciar
→ entra em um ambiente protegido
→ conta seu momento do modo que escolher
→ a Guivos organiza uma compreensão inicial
→ você revisa, corrige e limita
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
- produtos, serviços e relações comerciais mantêm origem e intenção visíveis;
- a HOME pública não processa relatos pessoais.

## 8. Fronteira de autenticação e consentimento

A pessoa poderá conhecer a Guivos e explorar conteúdo geral sem autenticação.

Autenticação e autorização explícita serão necessárias antes de:

- salvar permanentemente um relato;
- gravar, enviar ou processar voz;
- enviar, armazenar ou analisar arquivos;
- conectar fontes externas;
- produzir compreensão persistente associada a uma pessoa;
- iniciar personalização material;
- utilizar informações em oportunidades, Próximos Passos ou outras indicações pessoais.

Antes da autenticação, a interface poderá explicar as modalidades disponíveis, mas não deverá manter conteúdo pessoal identificável além do estritamente necessário para uma transição segura e explicitamente informada.

O consentimento deverá ser específico, compreensível, revogável quando aplicável e compatível com a finalidade apresentada.

## 9. Relato multimodal no ambiente protegido

A pessoa poderá contar seu Momento Atual por uma ou mais formas, conforme disponibilidade e autorização.

### 9.1 Texto livre

Poderá relatar:

- o que está vivendo;
- o que deseja compreender;
- o que pretende mudar, construir, resolver ou explorar;
- dificuldades, restrições e prioridades;
- acontecimentos recentes;
- o que não deseja receber ou considerar.

### 9.2 Voz

A experiência deverá:

- explicar que a voz poderá ser transcrita;
- permitir ouvir ou revisar a gravação, quando aplicável;
- apresentar a transcrição antes de utilizá-la materialmente;
- permitir corrigir, remover ou regravar;
- distinguir arquivo de áudio original e texto transcrito;
- informar finalidade, retenção e exclusão.

### 9.3 Arquivos

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

### 9.4 Escolhas rápidas e perguntas progressivas

A Guivos poderá oferecer perguntas curtas para reduzir esforço, sem transformar a jornada em formulário obrigatório.

As perguntas deverão ser adaptativas, adiáveis e justificadas. A pessoa poderá responder `não sei`, `prefiro não informar`, `isso não se aplica` ou utilizar texto livre.

### 9.5 Fontes externas autorizadas

Integrações futuras poderão contribuir com contexto somente quando:

- a fonte estiver identificada;
- a finalidade estiver clara;
- o escopo for limitado;
- o consentimento for revogável;
- os dados utilizados forem visíveis e corrigíveis;
- ausência de sincronização ou conflito for declarado.

## 10. Princípio de compartilhamento mínimo

A pessoa não precisará relatar toda a sua vida para iniciar uma jornada.

A experiência deverá buscar o mínimo suficiente para uma compreensão inicial legítima, considerando:

- intenção atual;
- mudança, necessidade ou possibilidade principal;
- restrições relevantes;
- preferências e limites;
- horizonte temporal, quando conhecido;
- autorização para utilização das informações.

Informações adicionais deverão ser solicitadas progressivamente quando possuírem utilidade compreensível.

## 11. Compreensão inicial apresentada pela Guivos

A Guivos deverá apresentar uma síntese revisável antes de utilizar o contexto para recomendações materiais.

A estrutura preferencial será:

### 11.1 O que você nos contou

Informações declaradas diretamente pela pessoa.

### 11.2 O que compreendemos até agora

Síntese produzida pela Guivos com linguagem condicional e específica.

### 11.3 O que pode estar relacionado

Inferências, relações ou hipóteses claramente identificadas.

### 11.4 O que ainda não sabemos

Lacunas que limitam a segurança da compreensão.

### 11.5 Como isso poderá ser utilizado

Finalidades autorizadas, como:

- organizar a Jornada;
- explicar possibilidades;
- relacionar oportunidades;
- apoiar a construção de Próximos Passos;
- reduzir repetição de perguntas;
- reconhecer mudanças posteriores.

### 11.6 Seus controles

Ações mínimas:

- `Está correto`;
- `Faz sentido parcialmente`;
- `Quero corrigir`;
- `Remover esta informação`;
- `Não usar para personalização`;
- `Contar mais`;
- `Prefiro continuar sem recomendações`;
- `Apagar e recomeçar`.

## 12. Gate de compreensão e personalização

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

## 13. Nomenclatura oficial e soluções do ecossistema

A HOME deverá apresentar as soluções da Guivos com identidade, finalidade e público compreensíveis.

| Solução oficial | Apresentação na HOME |
|---|---|
| **Guivos Journey** | organiza Momento Atual, objetivos, Próximos Passos, experiências e evolução |
| **Guivos Mall** | shopping do ecossistema, reunindo produtos e serviços com condições comerciais transparentes |
| **Guivos Travel** | reúne viagens, destinos e experiências |
| **Guivos Business** | conecta Organizações, programas, públicos e oportunidades responsáveis |
| **Guivos Media** | reúne conteúdos, histórias e narrativas relacionadas à evolução humana e ao ecossistema |
| **Guivos Intelligence** | explica relações, contexto, possibilidades, fontes e incertezas |
| **Guivos Ads** | solução de anúncios, publicidade e patrocínios explicitamente identificados |

**Shopping Guivos** é uma descrição em linguagem comum do Guivos Mall e não constitui produto separado.

**Anúncios da Guivos** é uma descrição em linguagem comum do Guivos Ads e não constitui produto separado.

A HOME poderá permitir acesso e conhecimento de cada solução antes do início da jornada.

Antes do gate de personalização:

- os itens serão gerais, editoriais, institucionais ou resultantes de busca explícita;
- a interface não utilizará `para você`, `relevante para seu momento` ou equivalente;
- exemplos deverão ser identificados como exemplos;
- publicidade deverá ser identificada;
- posição comercial não será apresentada como relevância pessoal.

Depois do gate de personalização, as soluções poderão contribuir com possibilidades contextuais, mantendo sua origem visível.

## 14. Exploração sem iniciar a jornada

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

## 15. Transição para a Tela Hoje

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

## 16. Wireframes textuais de baixa fidelidade

### 16.1 Página Inicial pública

```text
┌──────────────────────────────────────────────┐
│ GUIVOS                         Entrar  Ajuda  │
├──────────────────────────────────────────────┤
│ Toda jornada começa no momento em que você  │
│ está agora.                                  │
│                                              │
│ Conheça a Guivos e inicie sua jornada        │
│ quando desejar.                              │
│                                              │
│ [ Iniciar minha jornada ]                    │
│ [ Conhecer o ecossistema ]                   │
├──────────────────────────────────────────────┤
│ COMO A GUIVOS PODE APOIAR                    │
│ Você decide iniciar → conta seu momento em   │
│ ambiente protegido → revisa → você decide.   │
├──────────────────────────────────────────────┤
│ PRIVACIDADE E CONTROLE                       │
│ A HOME não coleta relatos pessoais.          │
│ Finalidade, correção e exclusão serão        │
│ explicadas antes do compartilhamento.        │
├──────────────────────────────────────────────┤
│ CONHEÇA O ECOSSISTEMA GUIVOS                 │
│ Guivos Journey | Guivos Mall | Guivos Travel │
│ Guivos Business | Guivos Media               │
│ Guivos Intelligence | Guivos Ads             │
│ Conteúdo geral — ainda não personalizado.    │
├──────────────────────────────────────────────┤
│ Propósito | Segurança | Acessibilidade       │
│ Privacidade | Termos | Contato               │
└──────────────────────────────────────────────┘
```

### 16.2 Entrada do fluxo protegido

```text
┌──────────────────────────────────────────────┐
│ INICIAR MINHA JORNADA                        │
├──────────────────────────────────────────────┤
│ Conte seu momento do seu jeito.              │
│ Você controla o que compartilha.             │
│                                              │
│ [ Escrever ] [ Falar ]                       │
│ [ Enviar arquivo ]                           │
│ [ Responder perguntas progressivas ]         │
├──────────────────────────────────────────────┤
│ Antes de continuar, veja finalidade, uso,    │
│ retenção, correção e exclusão.                │
│                                              │
│ [ Revisar privacidade ] [ Continuar ]         │
│ [ Voltar sem enviar ]                        │
└──────────────────────────────────────────────┘
```

Os wireframes são estruturais. Não definem identidade visual, ilustrações, tipografia, cores, componentes ou responsividade final.

## 17. Estados alternativos obrigatórios

Deverão ser detalhados posteriormente:

- visitante que deseja apenas explorar;
- visitante que seleciona iniciar sem autenticação;
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

## 18. Privacidade, proteção e segurança

A HOME pública deverá:

- evitar coleta de conteúdo pessoal;
- não ativar microfone, câmera, upload ou leitura de arquivos;
- explicar a transição antes de encaminhar ao fluxo protegido;
- preservar exploração geral sem autenticação.

O início protegido da jornada deverá:

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

## 19. Presença companheira na primeira entrada

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

## 20. Critérios de aceite

A arquitetura poderá avançar quando demonstrar que:

1. a diferença entre HOME, início protegido da jornada e Tela Hoje é compreendida;
2. a proposta de impacto da Guivos aparece antes das soluções comerciais;
3. iniciar a jornada é voluntário;
4. explorar o ecossistema sem personalização é possível;
5. a HOME pública não coleta nem processa relatos pessoais;
6. a transição para o ambiente protegido é consciente e explicada;
7. autenticação e consentimento antecedem persistência, voz, arquivos, fontes externas e personalização;
8. texto, voz, arquivos e perguntas progressivas possuem controles equivalentes;
9. a pessoa compreende o que acontecerá com suas informações;
10. a Guivos não afirma compreensão antes de apresentar sua base;
11. a compreensão inicial pode ser corrigida, limitada ou rejeitada;
12. recomendações pessoais permanecem bloqueadas antes do gate;
13. Guivos Mall e Guivos Ads aparecem com seus nomes oficiais;
14. soluções do ecossistema mantêm identidade e intenção comercial visíveis;
15. a transição para a Tela Hoje explica continuidade e controles;
16. estados de insuficiência não são preenchidos artificialmente;
17. acessibilidade, baixa conectividade e privacidade possuem alternativas;
18. a leitura independe do identificador técnico;
19. nenhum comportamento exige design visual ou implementação para ser compreendido.

## 21. Limites

Este documento não:

- define textos finais de marketing ou interface;
- aprova identidade visual da HOME;
- cria ilustrações, vídeo, animação ou fotografia;
- define formatos técnicos definitivos de arquivos;
- define reconhecimento de voz ou modelo de inteligência artificial;
- autoriza análise de dados sensíveis sem governança especializada;
- cria protótipo navegável;
- executa testes de usabilidade;
- define componentes técnicos ou interfaces de programação;
- inicia Engenharia de Produto ou desenvolvimento;
- altera as responsabilidades de Organização e Coletivo;
- transforma a HOME em canal obrigatório para cada retorno;
- autoriza coleta pessoal na superfície pública.

## 22. Próximo ponto de decisão

Após integração deste incremento, o próximo ato deverá ser autorizado separadamente e poderá escolher entre:

1. validar funcionalmente a HOME pública com cenários de primeira entrada;
2. validar funcionalmente a entrada do fluxo protegido;
3. criar arquivos gráficos vetoriais dos wireframes de baixa fidelidade;
4. detalhar os estados de captura por texto, voz e arquivo;
5. detalhar a revisão da compreensão inicial;
6. validar a transição entre HOME, início protegido da jornada e Tela Hoje.

Nenhuma dessas etapas é iniciada automaticamente.
