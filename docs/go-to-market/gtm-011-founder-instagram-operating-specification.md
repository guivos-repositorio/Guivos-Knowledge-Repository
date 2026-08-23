---
id: GTM-011
title: Instagram do Fundador — Especificação Operacional v1
status: active
version: 1.0.0
owner: Guivos Brand & Growth
last_updated: 2026-08-23
depends_on:
  - GTM-010
  - GKR-BRAND-PUBLIC-AUTHORITY-001
  - GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-CHRISTIAN-FOUNDATION-001
  - GTM-009
related:
  - GPA-005
  - GOG-001
normative: true
---

# Instagram do Fundador — Especificação Operacional v1

## 1. Finalidade

Este documento transforma a arquitetura conceitual de `GTM-010` em uma **baseline operacional v1** para o Instagram pessoal de **Guilherme Oliveira**, fundador da Guivos.

Ele governa a materialização do perfil, a transição da presença existente, os três conteúdos fixados iniciais, os primeiros ciclos editoriais, o sistema de produção, a estrutura mínima de equipe, acessos, métricas, incidentes e a futura internacionalização da presença pública do fundador.

A relação de autoridade é:

```text
GKR-BRAND-PUBLIC-AUTHORITY-001
→ autoridade pública da marca e papel do fundador

GTM-010
→ especificação mestre do Instagram pessoal do fundador

GTM-011
→ operacionalização da especificação mestre
```

`GTM-011` **não redefine `GTM-010`**. Em qualquer divergência, a autoridade-mãe e as autoridades de Brand vigentes prevalecem.

Esta especificação também não transforma o Instagram do fundador em canal institucional da Guivos.

```text
PERFIL DO FUNDADOR
≠ PERFIL INSTITUCIONAL

OPERAÇÃO PROFISSIONAL
≠ MARCA PESSOAL PARALELA

IMPLEMENTAÇÃO OPERACIONAL
≠ AUTORIZAÇÃO AUTOMÁTICA DE EXECUÇÃO REAL
```

## 2. Estado operacional e limites

Os doze movimentos operacionais que originam esta especificação foram conceitualmente convergidos.

O estado passa a ser:

```text
ARQUITETURA CONCEITUAL
→ CONVERGIDA EM GTM-010

ARQUITETURA OPERACIONAL
→ CONVERGIDA EM GTM-011

ALTERAÇÃO DO INSTAGRAM REAL
→ NÃO EXECUTADA POR ESTE DOCUMENTO

PUBLICAÇÃO DE CONTEÚDO REAL
→ NÃO EXECUTADA POR ESTE DOCUMENTO
```

A integração de `GTM-011` ao GKR não autoriza automaticamente:

- alteração de nome, bio, foto, link ou categoria no perfil real;
- mudança do tipo de conta;
- arquivamento ou exclusão de publicações existentes;
- produção ou publicação dos três posts fixados;
- criação de Destaques;
- contratação de equipe ou fornecedor;
- concessão de acesso a terceiros;
- uso de mídia paga;
- ativação de Meta Verified ou serviço equivalente;
- criação de e-mail público do fundador;
- criação de página pessoal, newsletter, podcast, curso ou submarca;
- internacionalização operacional do perfil;
- uso sintético de voz ou imagem do fundador.

A execução real exige gate operacional separado.

## 3. Mapeamento dos doze movimentos

A arquitetura operacional v1 é composta por:

| Movimento | Escopo |
|---|---|
| M1 | nome exibido e bio |
| M2 | foto, conta, link e configuração estrutural |
| M3 | transição do perfil existente |
| M4 | fixado 1 — `Quem sou e por que estou aqui` |
| M5 | fixado 2 — `Por que a Guivos existe` |
| M6 | fixado 3 — `Do possível ao vivido.` |
| M7 | primeiros 30 dias de conteúdo |
| M8 | sistema operacional de produção |
| M9 | equipe, papéis, acessos e governança |
| M10 | métricas e painel dos primeiros 90 dias |
| M11 | crises, correções, ataques e incidentes |
| M12 | internacionalização da presença do fundador |

Os movimentos formam uma única camada operacional e não devem ser tratados como doze projetos independentes.

---

# PARTE I — MATERIALIZAÇÃO DO PERFIL

## 4. Nome exibido

Baseline operacional:

```text
Guilherme Oliveira | Guivos
```

Função semântica:

```text
GUILHERME OLIVEIRA
→ pessoa

GUIVOS
→ associação institucional imediata
```

A presença de `Guivos` no nome exibido permite que a bio utilize `Fundador` sem repetir desnecessariamente `da Guivos`.

A composição não cria perfil institucional e não transforma a pessoa em extensão gráfica da marca.

## 5. Bio v1

Baseline operacional:

```text
Fundador
Do possível ao vivido.
“E Jesus continuava crescendo em sabedoria, em desenvolvimento e em graça diante de Deus e das pessoas.” Lucas 2:52
```

A implementação deve preservar:

```text
PAPEL
→ Fundador

ASSINATURA AUTORAL
→ Do possível ao vivido.

REFERÊNCIA DE FÉ
→ Lucas 2:52
```

O texto bíblico de referência permanece:

> **“E Jesus continuava crescendo em sabedoria, em desenvolvimento e em graça diante de Deus e das pessoas.” — Lucas 2:52**

A materialização real deve ser novamente conferida contra os limites técnicos vigentes da plataforma no momento da execução.

## 6. `Engenheiro` e `Cristão`

As identidades permanecem válidas e governadas, ainda que não apareçam literalmente na bio curta.

```text
AUSÊNCIA DE “ENGENHEIRO” NA BIO
≠ REMOÇÃO DA IDENTIDADE PROFISSIONAL

LUCAS 2:52 NA BIO
→ expressão pública concreta da identidade cristã
```

`Engenheiro` pode aparecer naturalmente no primeiro fixado, em apresentações, entrevistas, LinkedIn e outros contextos biográficos legítimos.

`Cristão` pode ser explicitado em conteúdo pessoal, apresentações e demais superfícies quando fizer sentido.

## 7. Idioma da bio

Na v1 brasileira:

```text
Fundador
```

permanece preferível a `Founder`.

Globalidade não é tratada como anglicização decorativa.

Em contexto internacional, o título permitido permanece:

```text
Guilherme Oliveira — Founder of Guivos
```

Uma eventual mudança permanente da bio para inglês pertence ao gate de internacionalização.

## 8. Foto de perfil

A foto deve identificar a pessoa.

```text
FOTO DE GUILHERME
→ SIM

LOGO DA GUIVOS
→ NÃO
```

Direção preferencial:

- rosto claramente reconhecível;
- cabeça e parte dos ombros;
- expressão natural e segura;
- olhar preferencialmente para a câmera;
- fundo simples;
- tratamento profissional sem excesso;
- roupa coerente com a pessoa, sem figurino obrigatório de executivo.

Evitar como baseline:

- foto de corpo inteiro;
- palco como primeira referência;
- óculos escuros;
- foto de viagem;
- outras pessoas no enquadramento;
- logo dominante da Guivos;
- estética de `CEO de braços cruzados`;
- moldura, borda, watermark ou submarca pessoal.

```text
PROFISSIONAL
≠ CORPORATIVO
```

## 9. Tipo de conta

Baseline operacional, sujeito à disponibilidade técnica vigente no momento da implementação:

```text
CONTA
→ profissional

MODALIDADE PREFERENCIAL
→ Creator / Criador

VISIBILIDADE
→ pública
```

A escolha busca compatibilidade com uma presença pública individual e não transforma Guilherme em influenciador generalista.

Se a plataforma alterar nomenclatura ou recursos, a função desejada prevalece sobre o nome técnico da modalidade.

## 10. Categoria profissional

A categoria técnica pode existir quando necessária, mas não deve dominar a primeira impressão.

Preferência:

```text
CATEGORIA
→ equivalente funcional legítimo

RÓTULO PÚBLICO
→ oculto na v1, quando tecnicamente possível
```

Evitar como baseline uma autoclassificação de status como `Figura pública` / `Public Figure`.

```text
AUTORIDADE
→ construída

NÃO
→ autoproclamada
```

## 11. Link principal

Baseline inicial:

```text
guivos.com
```

Função:

```text
PERFIL DO FUNDADOR
↓
INTERESSE NA PRINCIPAL CONSTRUÇÃO PÚBLICA
↓
GUIVOS.COM
```

Na v1, um único destino claro é preferível a um agregador de links sem hierarquia.

Não criar página pessoal, domínio pessoal ou Linktree equivalente apenas para preencher espaço.

## 12. Contatos públicos

Baseline:

```text
TELEFONE PESSOAL
→ não publicar

WHATSAPP PESSOAL
→ não publicar

ENDEREÇO
→ não publicar

E-MAIL PÚBLICO DO FUNDADOR
→ não necessário até existir operação governada
```

Se futuramente houver canal público para imprensa, eventos ou oportunidades, ele deverá possuir ownership e triagem próprios.

```text
FUNDADOR
≠ SAC
```

## 13. Verificação e segurança

Meta Verified ou serviço equivalente não constitui requisito da v1.

```text
SELO
≠ AUTORIDADE
```

Pode ser reavaliado futuramente por proteção contra impersonação, suporte ou autenticidade.

Baseline de segurança:

```text
2FA
→ obrigatório

RECUPERAÇÃO
→ controlada

TELEFONE DE RECUPERAÇÃO
→ não público

CREDENCIAL COMPARTILHADA EM MENSAGENS
→ proibida
```

---

# PARTE II — TRANSIÇÃO DO PERFIL EXISTENTE

## 14. Princípio de continuidade

A nova fase deve organizar o futuro sem apagar artificialmente o passado.

> **A nova fase deve organizar o futuro sem apagar artificialmente o passado.**

```text
EVOLUÇÃO VISÍVEL
→ SIM

REINVENÇÃO RETROATIVA DA HISTÓRIA
→ NÃO
```

O perfil existente permanece como baseline quando for legitimamente de Guilherme e não houver problema estrutural que justifique nova conta.

## 15. Não zerar o feed

Não criar uma nova conta nem arquivar todo o histórico apenas para obter grade visual perfeita.

Não arquivar publicação apenas porque:

- a cor não combina com a estética futura;
- a fotografia é antiga;
- não menciona Guivos;
- não segue padrão de design atual;
- representa uma fase anterior legítima.

```text
COERÊNCIA FUTURA
≠ PADRONIZAÇÃO RETROATIVA
```

## 16. Classificação de publicações antigas

### 16.1 Manter

Estado padrão quando a publicação:

- representa legitimamente Guilherme;
- registra experiência real;
- não cria risco relevante;
- ajuda a mostrar história e evolução;
- continua aceitável como parte da presença pública.

### 16.2 Manter como registro de outra fase

Uma opinião antiga ou uma etapa profissional anterior pode permanecer quando sua manutenção não cria dano material.

```text
“EU NÃO FARIA ISSO HOJE”
≠
“PRECISO APAGAR QUE ISSO EXISTIU”
```

### 16.3 Arquivar

Quando houver razão concreta, como:

- exposição pessoal excessiva;
- informação confidencial;
- localização ou dado sensível;
- exposição inadequada de terceiros;
- contexto completamente perdido;
- conteúdo que o titular legitimamente não deseja mais manter público.

### 16.4 Excluir

Mais excepcional, aplicável a:

- publicação acidental;
- violação de privacidade;
- material indevido;
- duplicação sem valor;
- risco que não justifique preservação pública.

```text
ARQUIVAR
> EXCLUIR
```

quando a intenção é apenas retirar da superfície pública.

## 17. Conteúdo com terceiros

A revisão deve considerar:

- familiares;
- crianças;
- antigos relacionamentos;
- colegas;
- pessoas que podem não desejar exposição atual;
- endereço e localização;
- documentos e informações de trabalho.

```text
HISTÓRIA PESSOAL
≠ DIREITO AUTOMÁTICO DE EXPOR TERCEIROS
```

## 18. Não reescrever o passado

Não:

- editar dezenas de legendas antigas para inserir Guivos;
- adicionar `Do possível ao vivido.` retroativamente;
- alterar todas as capas;
- aplicar identidade gráfica da Guivos a conteúdo pessoal antigo;
- tentar fazer o passado parecer parte de um plano que ainda não existia.

```text
NOVA ARQUITETURA
→ COMEÇA A PARTIR DA NOVA FASE
```

## 19. Sequência operacional de transição

```text
1. revisar o perfil existente
2. tratar apenas riscos reais
3. atualizar a cabeça do perfil
4. iniciar conteúdos novos
5. publicar progressivamente os três conteúdos estruturais
6. fixá-los
7. permitir que o novo padrão se consolide
```

Destaques devem nascer de Stories reais, e não de capas vazias criadas antecipadamente.

```text
DESTAQUE
→ NASCE DE CONTEÚDO REAL
```

---

# PARTE III — TRÊS CONTEÚDOS FIXADOS

## 20. Arquitetura conjunta

Os três fixados formam a progressão:

```text
1. QUEM SOU
→ PESSOA

2. POR QUE A GUIVOS EXISTE
→ OBRA

3. DO POSSÍVEL AO VIVIDO.
→ PENSAMENTO
```

A ordem conceitual é:

```text
PESSOA
↓
OBRA
↓
PENSAMENTO
```

Eles não precisam ser publicados consecutivamente nem no mesmo dia.

## 21. Fixado 1 — `Quem sou e por que estou aqui`

Formato preferencial:

```text
REEL
→ Guilherme falando diretamente para a câmera
```

Baseline de duração:

```text
aprox. 60–90 segundos
```

A peça deve comunicar:

```text
QUEM É?
→ Guilherme Oliveira

QUAL SUA RELAÇÃO COM A GUIVOS?
→ fundador

O QUE O MOVE?
→ pessoas, possibilidades, evolução e construção

POR QUE O PERFIL EXISTE?
→ compartilhar construção, aprendizados, decisões e perspectivas
```

Não deve funcionar como currículo, lista de resultados, autopromoção ou pitch de autoridade.

### 21.1 Estrutura narrativa

```text
QUEM SOU
↓
O QUE FUI PERCEBENDO
↓
O QUE ESTOU CONSTRUINDO
↓
POR QUE COMPARTILHAR
↓
FECHAMENTO AUTORAL
```

A engenharia e a fé podem aparecer naturalmente:

> `Eu sou Guilherme Oliveira. Sou engenheiro, cristão e fundador da Guivos.`

A Guivos entra como construção real, sem tour de produtos.

### 21.2 Direção de fala

A fala deve ser:

```text
CALMA
DIRETA
REFLEXIVA
PESSOAL
```

Roteiro orienta a ideia, mas não deve exigir decoração palavra por palavra.

### 21.3 Fechamento possível

```text
Do possível ao vivido.
```

O uso é permitido, não obrigatório em todo conteúdo futuro.

## 22. Fixado 2 — `Por que a Guivos existe`

Formato preferencial:

```text
REEL
```

Sua função é responder à pergunta fundadora antes de explicar produtos.

Tese:

> **Muitas possibilidades já existem. O problema é que nem sempre conseguimos percebê-las, encontrá-las, acessá-las, compreendê-las ou reconhecer quando podem fazer sentido para nossa vida.**

A Guivos pode ampliar valor ao:

```text
TORNAR VISÍVEL
APROXIMAR
CONECTAR
ORGANIZAR CONTEXTO
FACILITAR ACESSO
REDUZIR DISTÂNCIAS
```

Sem decidir pela pessoa.

```text
GUIVOS
→ amplia campo de possibilidades

PESSOA
→ continua escolhendo
```

### 22.1 Formulação central

> **A Guivos existe para aproximar pessoas de possibilidades que podem fazer sentido para suas vidas.**

Essa formulação não é promessa de resultado.

### 22.2 Estrutura narrativa

```text
REALIDADE HUMANA
↓
PROBLEMA
↓
CONVICÇÃO
↓
GUIVOS
↓
AUTONOMIA
↓
CONSTRUÇÃO
```

Tecnologia permanece meio.

```text
TECNOLOGIA
→ MEIO

PESSOAS E POSSIBILIDADES
→ FIM
```

Não utilizar linguagem de promessa como `transformar vidas`, `desbloquear potencial` ou equivalente como baseline institucional do conteúdo.

### 22.3 Fechamento preferencial

> **É isso que estamos construindo.**

O post não precisa fechar com a assinatura institucional nem com a assinatura pessoal.

## 23. Fixado 3 — `Do possível ao vivido.`

Formato preferencial:

```text
CARROSSEL
```

Função: tornar compreensível o território autoral da assinatura pessoal.

A progressão é:

```text
POSSIBILIDADE
↓
PERCEPÇÃO
↓
COMPREENSÃO
↓
ESCOLHA
↓
ACESSO / AÇÃO
↓
EXPERIÊNCIA
↓
VIVIDO
```

Mas:

```text
POSSÍVEL
≠ GARANTIDO
≠ CORRETO PARA TODOS
≠ OBRIGAÇÃO
```

Uma pessoa pode descobrir, considerar e decidir não viver uma possibilidade.

### 23.1 Estrutura baseline do carrossel

1. `Do possível ao vivido.`
2. Nem tudo que pode fazer parte da nossa vida já faz parte dela.
3. Às vezes a possibilidade já existe; o que ainda não existe é a conexão entre ela e nós.
4. Não enxergar / não conhecer / não compreender / não acessar / não escolher.
5. Perceber não significa precisar viver; a escolha continua sendo nossa.
6. Quando algo faz sentido, ganha contexto e se torna acessível, o possível pode deixar de ser apenas abstrato.
7. `POSSÍVEL → ESCOLHA → EXPERIÊNCIA → VIVIDO`.
8. Fechamento autoral.

### 23.2 Separação da marca

```text
DO POSSÍVEL AO VIVIDO.
→ GUILHERME OLIVEIRA

POSSIBILITY, LIVED.
POSSIBILIDADE, VIVIDA.
#POSSIBILITYLIVED
→ GUIVOS
```

Não traduzir automaticamente a assinatura pessoal para criar versão internacional sem gate específico.

---

# PARTE IV — PRIMEIROS 30 DIAS

## 24. Função do ciclo inicial

Os primeiros 30 dias são ciclo de calibração e repertório, não campanha de lançamento pessoal.

```text
30 DIAS
→ CRIAR CONTEXTO

NÃO
→ PROVAR AUTORIDADE
→ MAXIMIZAR ALCANCE
→ PREENCHER CALENDÁRIO
```

Baseline:

```text
2–3 publicações por semana
≈ 8–12 publicações
```

Referência operacional inicial:

```text
10 publicações totais
```

incluindo os três fixados.

Essa quantidade é baseline, não quota canônica.

## 25. Sequência editorial inicial sugerida

```text
01 — Quem sou e por que estou aqui
02 — Uma perspectiva
03 — Construindo a Guivos
04 — Experiência que gerou perspectiva
05 — Por que a Guivos existe
06 — Fé / princípio / aprendizado
07 — Construindo a Guivos
08 — Uma perspectiva
09 — Do possível ao vivido.
10 — Construção / aprendizado do ciclo
```

Depois, fixar os conteúdos 01, 05 e 09 quando estiverem publicados e maduros para a função de porta de entrada.

## 26. Primeiro conteúdo de construção

Tema preferencial:

> **Por que a Guivos não deve decidir pelas pessoas.**

Estrutura:

```text
PROBLEMA
→ plataformas podem induzir

CONVICÇÃO
→ ampliar possibilidades não é determinar caminho

DECISÃO
→ autonomia permanece com a pessoa

IMPLICAÇÃO
→ isso influencia como construímos a Guivos
```

## 27. Experiências

O conteúdo deve seguir:

```text
O QUE ACONTECEU
↓
O QUE CHAMOU ATENÇÃO
↓
POR QUE IMPORTA
↓
O QUE PASSEI A ENXERGAR DIFERENTE
```

```text
“FUI A UM LUGAR”
→ contexto

“O QUE AQUELE LUGAR ME FEZ PERCEBER”
→ possível conteúdo autoral
```

## 28. Fé no primeiro ciclo

A fé deve aparecer cedo o suficiente para ser reconhecida como dimensão real, sem calendário religioso artificial.

Lucas 2:52 é um ponto de partida legítimo para reflexão sobre crescimento.

```text
FÉ
→ IDENTIDADE

FÉ
≠ POST OBRIGATÓRIO DA SEMANA
```

O conteúdo de fé não precisa terminar conectando tudo à Guivos.

## 29. Perspectivas sobre tecnologia

Um território inicial possível:

> **Tecnologia fica mais interessante quando deixa de ser o centro da conversa.**

A tese deve manter:

```text
TECNOLOGIA
→ ferramenta

POSSIBILIDADE HUMANA
→ finalidade
```

## 30. Stories no primeiro ciclo

Stories funcionam como camada de contexto, não como obrigação de promoção do feed.

Podem mostrar:

```text
ANTES DO POST
→ contexto real

DURANTE
→ bastidor

DEPOIS
→ reflexão ou pergunta complementar
```

Evitar repetição mecânica de chamadas como `novo post`, `corre no feed` ou equivalente.

A regra permanente de `GTM-010` continua:

> **A vida não deve ser organizada para alimentar o Instagram. O Instagram pode registrar partes relevantes da vida.**

## 31. Interação no primeiro mês

Observar:

- perguntas recorrentes;
- palavras utilizadas pelas pessoas;
- mal-entendidos;
- temas que geram conversas reais;
- conteúdos que parecem naturais ou artificiais.

```text
PERGUNTA RECORRENTE
→ INSUMO EDITORIAL

NÃO
→ ALTERAÇÃO CANÔNICA AUTOMÁTICA
```

Comentários e DMs não constituem pesquisa formal nem validação de mercado.

## 32. Produção mínima

Baseline suficiente:

```text
boa câmera de celular
microfone adequado
boa luz
edição limpa
design simples
organização editorial
```

Não exigir estúdio permanente ou grande equipe para iniciar.

---

# PARTE V — SISTEMA OPERACIONAL DE PRODUÇÃO

## 33. Fluxo de produção

```text
EXPERIÊNCIA / IDEIA / DECISÃO
↓
CAPTURA
↓
TRIAGEM
↓
TESE
↓
FORMATO
↓
ESTRUTURA
↓
GRAVAÇÃO / PRODUÇÃO
↓
EDIÇÃO
↓
REVISÃO
↓
PUBLICAÇÃO
↓
APRENDIZADO
```

O processo não deve começar em `precisamos postar`.

## 34. Fontes legítimas

- decisões;
- perguntas;
- conversas;
- erros;
- mudanças de opinião;
- aprendizados;
- experiências;
- livros;
- viagens;
- reuniões;
- observações;
- notícias relevantes;
- construção da Guivos;
- fé;
- perspectivas sobre futuro e tecnologia.

A existência de uma fonte não cria automaticamente um post.

## 35. Captura de ideias

Formatos permitidos:

- áudio curto;
- nota;
- frase;
- pergunta;
- print de referência;
- link;
- fotografia;
- marcação de conversa.

Estrutura mínima:

```text
O QUE ACONTECEU?
O QUE ME CHAMOU ATENÇÃO?
O QUE EU PENSO SOBRE ISSO?
POR QUE ISSO PODE IMPORTAR PARA OUTRA PESSOA?
```

## 36. Banco editorial

Estados sugeridos:

```text
CAPTURADO
↓
EM AVALIAÇÃO
↓
APROVADO COMO PAUTA
↓
EM ESTRUTURAÇÃO
↓
PRONTO PARA PRODUÇÃO
↓
PRODUZIDO
↓
PUBLICADO
↓
APRENDIZADO REGISTRADO
```

O banco é repositório de ideias, teses, perguntas, experiências e decisões — não uma obrigação de transformar tudo em conteúdo.

## 37. Triagem editorial

Perguntas obrigatórias:

```text
1. há perspectiva autoral?
2. Guilherme é a melhor voz?
3. pertence a território legítimo?
4. existe matéria-prima real?
5. há risco de confidencialidade?
6. seria melhor em Guivos, Media ou outro canal?
```

Se Guilherme não for a melhor voz, não forçar autoria do fundador.

## 38. Tese antes do formato

```text
IDEIA
→ DEFINE O FORMATO

FORMATO
→ NÃO DEFINE A IDEIA
```

Uma pauta relevante pode conter:

```text
TEMA
TESE CENTRAL
POR QUE GUILHERME?
EXPERIÊNCIA / EVIDÊNCIA DE ORIGEM
O QUE A PESSOA DEVE ENTENDER
O QUE NÃO PODE SER DITO
FORMATO
FECHAMENTO POSSÍVEL
```

## 39. Roteiro

Estrutura preferencial:

```text
ABERTURA
↓
CONTEXTO
↓
TESE
↓
EXEMPLO
↓
IMPLICAÇÃO
↓
FECHAMENTO
```

Roteiro palavra por palavra é reservado a contextos que exijam precisão maior, como risco jurídico, números, crise, anúncio material ou tema técnico sensível.

## 40. Gravação em lote

Permitida para:

- temas perenes;
- explicações estruturais;
- perguntas amadurecidas;
- conteúdos planejados.

Não deve substituir o presente em:

- bastidores;
- decisões recentes;
- aprendizados do momento;
- experiências reais;
- fé contextual.

```text
BATCH
→ EFICIÊNCIA

BATCH EXCESSIVO
→ PERDA DE PRESENTE
```

## 41. Edição

Função:

```text
REMOVER RUÍDO
MELHORAR CLAREZA
DAR RITMO
FACILITAR COMPREENSÃO
```

Não fabricar personalidade.

Permitidos:

- cortes limpos;
- legendas;
- B-roll real;
- ajuste de áudio;
- pequenas correções;
- elementos visuais simples.

Evitar edição hiperestimulada como baseline.

## 42. Revisões

Três perguntas distintas:

```text
REVISÃO AUTORAL
→ isso representa o que penso?

REVISÃO FACTUAL
→ está correto?

REVISÃO INSTITUCIONAL
→ posso dizer isso publicamente?
```

Se o conteúdo parece bom, mas não parece algo que Guilherme diria, ele não está pronto.

## 43. Níveis de aprovação

### Nível 1 — autoral de baixo risco

Exemplos: perspectiva, experiência, fé, aprendizado.

```text
EQUIPE ESTRUTURA
→ GUILHERME APROVA
→ PUBLICA
```

### Nível 2 — Guilherme + Guivos

Exemplos: decisão da Guivos, produto, equipe, parceria ou estratégia já pública.

```text
GUILHERME
+
ÁREA RESPONSÁVEL QUANDO NECESSÁRIO
→ PUBLICAÇÃO
```

### Nível 3 — sensível

Exemplos: crise, jurídico, dados, finanças, regulação, segurança.

```text
AUTORIDADE COMPETENTE
↓
REVISÃO
↓
GUILHERME QUANDO SUA VOZ FOR NECESSÁRIA
↓
PUBLICAÇÃO
```

## 44. Uso permitido de IA

Pode apoiar:

- transcrição;
- resumo de áudio;
- organização de ideias;
- agrupamento de temas;
- estrutura de roteiro;
- revisão de clareza;
- versões de legenda;
- legendas de vídeo;
- pesquisa preparatória;
- identificação de perguntas recorrentes;
- relatórios de performance.

Sempre com revisão humana proporcional ao risco.

## 45. Uso não permitido de IA

IA não deve:

- inventar experiência de Guilherme;
- inventar opinião;
- criar posição política em seu nome;
- criar testemunho falso;
- simular memória;
- fabricar convicção;
- responder como se fosse Guilherme sem autorização;
- gerar história pessoal que não aconteceu.

```text
IA
→ ORGANIZA EXPRESSÃO

NÃO
→ FABRICA AUTORIA
```

## 46. Documentar não é publicar

Uma camada histórica privada pode preservar:

- áudios;
- vídeos;
- fotografias;
- decisões;
- reflexões;
- marcos.

```text
DOCUMENTAR
≠ PUBLICAR
```

Material sensível ou prematuro pode ser preservado para uso futuro sem virar conteúdo atual.

---

# PARTE VI — EQUIPE, PAPÉIS E ACESSOS

## 47. Estrutura mínima

Capacidades necessárias:

```text
1. AUTORIA
2. EDITORIAL
3. PRODUÇÃO / DISTRIBUIÇÃO
```

Na fase inicial, a estrutura pode operar com:

```text
GUILHERME
+
1 PESSOA EDITORIAL / SOCIAL
+
1 APOIO DE EDIÇÃO / DESIGN
```

Uma mesma pessoa pode acumular funções, desde que as responsabilidades permaneçam claras.

## 48. Guilherme — Founder / Autor

Responsável por:

- pensamento;
- convicções;
- experiências;
- decisões próprias;
- perspectiva;
- fala pessoal;
- aprovação final autoral;
- temas sensíveis de sua própria identidade.

Não deve ser obrigado a executar toda a mecânica de edição, agendamento, relatórios ou publicação.

## 49. Editorial Lead

Responsável por:

- captura e organização de pautas;
- identificação de teses;
- profundidade;
- separação de canal;
- roteiro;
- revisão de legenda;
- coerência de território;
- risco editorial;
- coordenação de produção.

```text
EDITORIAL
→ PROPÕE EXPRESSÃO

GUILHERME
→ VALIDA AUTORIA
```

Não é ghostwriting irrestrito.

## 50. Social / Publisher

Pode executar:

- publicação;
- agendamento;
- marcações;
- organização de Destaques;
- triagem de comentários;
- encaminhamento de DMs;
- registro de performance;
- calendário operacional.

Não decide autonomamente convicções, política, posição institucional ou resposta pessoal do fundador.

## 51. Produção audiovisual / Design

Pode cuidar de:

- edição de vídeo;
- áudio;
- legendas;
- B-roll;
- imagem;
- carrossel;
- capa;
- adaptações de formato.

Não deve criar submarca pessoal por iniciativa própria.

## 52. Brand e áreas especialistas

Brand entra quando houver relação institucional relevante.

Especialistas entram conforme o tema:

```text
JURÍDICO
SEGURANÇA
PRODUTO
TECNOLOGIA
DADOS
FINANÇAS
COMUNICAÇÃO
```

```text
GUILHERME PODE TER A PERSPECTIVA
+
ESPECIALISTA PRESERVA PRECISÃO
```

## 53. Acesso à conta

Princípio:

```text
MENOR ACESSO NECESSÁRIO
```

A senha principal não deve circular entre agência, designer, editor, social, freelancer ou fornecedor.

```text
ACESSO OPERACIONAL
→ mecanismo de permissão

SENHA MESTRA
→ titular / recuperação controlada
```

O perfil pertence a Guilherme; operação pode ser delegada, propriedade não.

## 54. Saída de membro da equipe

Fluxo mínimo:

```text
REMOVER ACESSO
↓
REVISAR PERMISSÕES
↓
REVOGAR SESSÕES QUANDO NECESSÁRIO
↓
REVISAR FERRAMENTAS ASSOCIADAS
↓
PRESERVAR ARQUIVOS
```

## 55. Impersonação interna

Equipe não deve responder em primeira pessoa como Guilherme sem que a resposta seja realmente dele.

Três modos:

```text
PESSOAL
→ Guilherme responde

APOIO DE EQUIPE
→ equipe organiza; Guilherme decide/responde

OPERACIONAL
→ equipe direciona para canal apropriado
```

## 56. DMs

Classificação:

```text
PESSOAL / AUTORAL
IMPRENSA
EVENTOS
PARCERIA
COMERCIAL
SUPORTE
EMPREGO
SPAM
RISCO
```

Direcionamento conforme autoridade responsável.

```text
TRIAGEM
≠ COMPROMISSO
```

Equipe não promete participação, parceria, contratação, produto ou posição institucional em nome do fundador.

## 57. Relação com Marketing e Media

```text
MARKETING
→ otimiza comunicação

NÃO
→ define a pessoa
```

`Guivos Media` pode estruturar conversas, entrevistas e derivações editoriais, mas não se torna dono da voz do fundador.

```text
MEDIA
≠ DONO DA VOZ DO FUNDADOR
```

## 58. GKR como verdade institucional

Se um conteúdo pessoal estiver prestes a afirmar algo sobre a Guivos em conflito com autoridade vigente:

```text
CONTEÚDO
→ deve ser corrigido

GKR
→ não é alterado silenciosamente para acompanhar o post
```

```text
INSTAGRAM
≠ FONTE CANÔNICA
```

Se houver mudança real de visão institucional, a decisão deve ser deliberada e governada antes da comunicação quando aplicável.

---

# PARTE VII — MÉTRICAS E PRIMEIROS 90 DIAS

## 59. Princípio

> **Métrica deve orientar aprendizado, não governar identidade.**

Arquitetura:

```text
DISTRIBUIÇÃO
↓
INTERESSE
↓
VALOR
↓
RELACIONAMENTO
↓
AUTORIDADE PERCEBIDA
```

## 60. Camada 1 — Distribuição

Registrar quando disponível:

- alcance;
- visualizações;
- impressões;
- não seguidores alcançados;
- novos seguidores;
- visitas ao perfil.

```text
ALCANCE
≠ VALOR
≠ AUTORIDADE
```

## 61. Camada 2 — Interesse

Observar sinais como:

- tempo de consumo;
- retenção;
- conclusão;
- abandono;
- replay;
- continuidade em carrossel quando disponível.

A retenção não justifica hiperestimulação ou clickbait.

## 62. Camada 3 — Valor percebido

Priorizar leitura de:

- compartilhamentos;
- salvamentos;
- comentários qualificados;
- respostas em Stories;
- envio para outras pessoas.

```text
CURTIDA
→ sinal leve

SALVAMENTO / COMPARTILHAMENTO / CONVERSA
→ sinais mais ricos
```

## 63. Camada 4 — Relacionamento

Observar:

- pessoas que retornam;
- comentários recorrentes;
- DMs relevantes;
- conversas que continuam;
- referências a conteúdos anteriores;
- perguntas mais profundas.

## 64. Camada 5 — Autoridade percebida

Sinais:

- entrevistas;
- podcasts;
- palestras;
- conversas com especialistas;
- conexões com fundadores e lideranças;
- citações;
- pedidos de opinião sobre temas coerentes.

A pergunta qualitativa é:

> **Convidaram Guilherme para falar sobre o quê?**

O tema da oportunidade ajuda a medir associação real.

## 65. Associação espontânea

Observar palavras que começam a descrever Guilherme espontaneamente.

Desejáveis:

```text
GUIVOS
FUNDADOR
POSSIBILIDADES
CONSTRUÇÃO
PERSPECTIVAS
EVOLUÇÃO
FUTURO
TECNOLOGIA
```

Alertas de possível desvio:

```text
COACH
GURU
INFLUENCIADOR GENERALISTA
MOTIVACIONAL
CEO LIFESTYLE
```

Não existe `Authority Score` canônico.

## 66. Painel mínimo por conteúdo

Campos recomendados:

- data;
- pilar;
- formato;
- tema;
- tese;
- alcance;
- visualizações;
- compartilhamentos;
- salvamentos;
- comentários qualificados;
- visitas ao perfil;
- novos seguidores;
- DMs relevantes;
- aprendizado qualitativo.

O campo central é:

```text
O QUE APRENDEMOS?
```

## 67. Métrica por função do conteúdo

A interpretação deve respeitar a função de cada pilar.

### Construindo a Guivos

Priorizar compreensão, comentários qualificados, compartilhamentos, visitas à Guivos e perguntas sobre decisões.

### Perspectivas

Priorizar salvamentos, compartilhamentos, comentários reflexivos e recorrência.

### `Do possível ao vivido.`

Priorizar identificação, compartilhamento, associação autoral e profundidade.

### Experiências

Priorizar conexão, respostas, conversa e perspectiva gerada.

### Fé

Priorizar autenticidade, coerência e qualidade das interações.

Fé não entra em competição de performance com os demais pilares.

## 68. Horizontes de análise

```text
CONTEÚDO INDIVIDUAL
→ aprendizado tático

30 DIAS
→ sinais iniciais

90 DIAS
→ posicionamento emergente
```

Após 90 dias, produzir síntese executiva de uma página com:

- o que foi publicado;
- o que foi aprendido;
- como Guilherme está sendo percebido;
- associações surgidas;
- formatos que ajudaram;
- desvios;
- oportunidades;
- ajustes para o próximo ciclo.

## 69. Não otimizar identidade

Pode testar:

```text
HORÁRIO
DURAÇÃO
FORMATO
CAPA
ABERTURA
RITMO
LEGENDA
ESTRUTURA
```

Não alterar rapidamente por performance:

```text
TERRITÓRIO CENTRAL
PAPEL DE FUNDADOR
DO POSSÍVEL AO VIVIDO.
RELAÇÃO COM A GUIVOS
FÉ
PERSONALIDADE
MATRIZ DE AUTORIA
```

```text
IDENTIDADE
≠ A/B TEST
```

## 70. Dependência e distância da Guivos

Monitorar dois riscos opostos.

### Dependência excessiva da marca no fundador

Sinais:

- anúncios sempre exigem sua presença;
- imprensa só quer falar com ele;
- especialistas permanecem invisíveis;
- produtos só ganham atenção quando ele publica.

### Distância excessiva do fundador da Guivos

Sinais:

- seguidores não sabem que fundou a Guivos;
- não entendem o que está construindo;
- a obra desaparece do território público.

Objetivo:

```text
IDENTIDADE PRÓPRIA
+
ASSOCIAÇÃO FORTE COM GUIVOS
```

---

# PARTE VIII — CRISES, CORREÇÕES E INCIDENTES

## 71. Princípio de resposta

> **Nem todo problema exige resposta pública, e nem toda resposta pública deve vir do fundador.**

Fluxo:

```text
DETECTAR
↓
PRESERVAR EVIDÊNCIAS
↓
CLASSIFICAR
↓
DEFINIR AUTORIDADE
↓
VERIFICAR FATOS
↓
DECIDIR: RESPONDER / CORRIGIR / REMOVER / SILENCIAR
↓
EXECUTAR
↓
MONITORAR
↓
REGISTRAR APRENDIZADO
```

## 72. Preservação de evidência

Quando material:

- print;
- link;
- data/hora;
- conta envolvida;
- conteúdo original;
- contexto;
- alcance aparente.

Especialmente em ameaça, impersonação, fraude, acusação, vazamento, assédio ou conflito material.

## 73. Níveis de incidente

### Nível 1 — baixo

Comentário negativo, discordância, erro pequeno, crítica pontual, spam isolado.

### Nível 2 — moderado

Erro factual relevante, mal-entendido, conteúdo fora de contexto, crítica recorrente, confusão Guilherme ↔ Guivos.

### Nível 3 — alto

Acusação relevante, impersonação, fraude, tema político sensível, vazamento, exposição indevida, conflito institucional.

### Nível 4 — crítico

Ameaça física, doxxing, conta comprometida, vazamento material de dados, litígio ativo, grave incidente de segurança ou fraude relevante.

```text
NÍVEL 4
→ sem post espontâneo
```

## 74. Crítica e moderação

```text
DISCORDÂNCIA
≠ CRISE

CRÍTICA
≠ ATAQUE AUTOMATICAMENTE
```

Distinguir:

```text
CRÍTICA
→ pode responder

PROVOCAÇÃO
→ geralmente não precisa

OFENSA
→ pode ignorar / moderar

ASSÉDIO
→ moderar / preservar

AMEAÇA
→ escalar
```

Nunca mobilizar a audiência para atacar terceiro.

## 75. Correção de erro

```text
ERRO PEQUENO
→ corrigir quando suficiente

ERRO MATERIAL
→ corrigir de forma visível

ERRO COM CONSEQUÊNCIA
→ reconhecer + corrigir + esclarecer
```

Mudança de opinião é distinta de erro factual e pode ser explicada como evolução quando verdadeiro.

## 76. Remoção de conteúdo

Remover quando houver:

- risco de segurança;
- violação de privacidade;
- exposição indevida;
- informação materialmente falsa;
- publicação acidental;
- obrigação legal;
- dano desnecessário a terceiro.

Não remover apenas por crítica, baixo alcance ou discordância.

## 77. Impersonação e fraude

Fluxo:

```text
PRESERVAR
↓
CONFIRMAR
↓
REPORTAR
↓
AVALIAR RISCO PARA TERCEIROS
↓
ALERTAR PUBLICAMENTE SOMENTE SE MATERIAL
```

Em caso de scam, canal oficial deve definir a verdade operacional.

## 78. Conta comprometida

```text
INTERROMPER PUBLICAÇÃO
↓
RECUPERAR ACESSO
↓
REVOGAR SESSÕES
↓
ALTERAR CREDENCIAIS
↓
REVISAR 2FA
↓
VERIFICAR POSTS / DMs
↓
COMUNICAR SE TERCEIROS PUDEREM TER SIDO AFETADOS
```

```text
SEGURANÇA
> CONTINUIDADE EDITORIAL
```

## 79. Vazamento

Se Story ou publicação expuser documento, tela, parceiro, valor, roadmap ou informação não pública:

```text
REMOVER
↓
PRESERVAR EVIDÊNCIA
↓
IDENTIFICAR O QUE FOI EXPOSTO
↓
ACIONAR ÁREA RESPONSÁVEL
↓
AVALIAR CONSEQUÊNCIA
```

## 80. Crise institucional

A primeira pergunta é:

> **De quem é a autoridade sobre o problema?**

Exemplos:

```text
FALHA TÉCNICA
→ Produto / Tecnologia

DADOS / PRIVACIDADE
→ Segurança / Jurídico / Privacidade

COBRANÇA
→ Operação / Financeiro

CONDUTA
→ Liderança / Pessoas / Jurídico

VISÃO / DECISÃO FUNDADORA
→ Guilherme pode precisar entrar
```

```text
CRISE DA GUIVOS
≠ GUILHERME PRECISA GRAVAR VÍDEO
```

## 81. Estrutura de fala em crise

Quando o fundador for a autoridade correta:

```text
O QUE ACONTECEU
↓
O QUE SABEMOS
↓
O QUE AINDA NÃO SABEMOS
↓
QUAL É NOSSA RESPONSABILIDADE
↓
O QUE ESTAMOS FAZENDO
↓
COMO ATUALIZAREMOS
```

`Ainda não sabemos` é resposta válida quando verdadeira.

## 82. Política, fé e tragédias

Política sensível exige gate alto e não deve ser motor de crescimento.

Fé não deve funcionar como escudo reputacional, justificativa comercial ou mecanismo para encerrar crítica.

Tragédia pública não cria obrigação de comunicação. Perguntar se existe algo real a dizer, relação legítima ou contribuição concreta.

## 83. Deepfake e conteúdo sintético falso

Se vídeo ou áudio falso for atribuído a Guilherme:

```text
PRESERVAR
↓
CONFIRMAR FALSIDADE
↓
REPORTAR
↓
AVALIAR RISCO
↓
DESMENTIR SE MATERIAL
```

O uso legítimo de voz ou imagem sintética do fundador não pertence a esta v1 e exige gate próprio com transparência.

## 84. Pausa editorial

Social pode interromper agenda normal em crise material.

```text
PAUSAR CALENDÁRIO
→ decisão operacional legítima
```

Silêncio também pode ser decisão legítima quando responder apenas amplificaria o problema e não houver responsabilidade pública a ser assumida.

---

# PARTE IX — INTERNACIONALIZAÇÃO

## 85. Princípio

> **A presença do fundador deve se tornar global porque sua atuação se tornou global — não porque o inglês parece mais internacional.**

```text
REALIDADE
↓
AUDIÊNCIA
↓
CONTEXTO
↓
IDIOMA
```

## 86. Estado inicial

```text
IDIOMA PRIMÁRIO
→ português

IDENTIDADE
→ brasileira

AMBIÇÃO
→ global

GUIVOS
→ ecossistema global
```

Português não limita a ambição global.

## 87. Inglês como função

Gatilhos legítimos:

- entrevista internacional;
- parceiro internacional;
- evento fora do Brasil;
- convidado estrangeiro;
- expansão real da Guivos;
- audiência internacional material;
- conversa global relevante.

Não tornar todos os conteúdos bilíngues sem necessidade real.

## 88. Tradução e acesso

Uma fase intermediária pode usar:

```text
ÁUDIO
→ português

LEGENDAS
→ português

ACESSO INTERNACIONAL
→ tradução / legenda em inglês quando estrategicamente relevante
```

Tradução deve preservar significado e voz, não apenas palavras.

IA pode apoiar tradução e legendas, com revisão humana proporcional ao risco.

## 89. Assinaturas

```text
GUILHERME
→ Do possível ao vivido.

GUIVOS
→ Possibility, lived.
→ Possibilidade, vivida.
→ #PossibilityLived
```

Não criar tradução oficial da assinatura pessoal sem gate próprio.

## 90. Um único perfil

Baseline:

```text
UM PERFIL PESSOAL
→ atravessa mercados
```

Não criar automaticamente perfil `BR` e perfil `global` do fundador.

Segundo perfil somente com necessidade operacional robusta e gate específico.

## 91. Internacionalização não é americanização

A origem brasileira pode permanecer parte relevante da presença pública.

```text
GLOBAL
≠ CULTURALMENTE NEUTRO
≠ PERSONAGEM DE VALE DO SILÍCIO
```

Experiências brasileiras podem gerar reflexões universais.

## 92. Relação com `@guivosglobal`

A expansão internacional pode aumentar conexão natural entre fundador e perfil institucional global, preservando funções:

```text
GUILHERME
→ visão / construção / fundador

@guivosglobal
→ instituição / ecossistema / produtos / experiências
```

A Guivos pode internacionalizar mais rápido que Guilherme e vice-versa.

## 93. Fases futuras

```text
FASE A
→ PT predominante + conteúdo internacional ocasional

FASE B
→ PT predominante + traduções EN selecionadas

FASE C
→ presença bilíngue orgânica conforme contexto

FASE D
→ autoridade internacional recorrente
```

A transição entre fases depende de evidência, não de calendário.

## 94. Gate de internacionalização

Sinais conjuntos:

```text
AUDIÊNCIA NÃO BRASILEIRA RECORRENTE
+
CONVERSAS INTERNACIONAIS
+
OPORTUNIDADES REAIS
+
ATUAÇÃO GLOBAL DA GUIVOS
+
NECESSIDADE EDITORIAL MULTILÍNGUE
```

Somente então deliberar alterações permanentes de bio, idioma predominante, tradução, rotina editorial e eventual expressão internacional da assinatura pessoal.

---

# PARTE X — GOVERNANÇA FINAL

## 95. Matriz de autoridade operacional

```text
PESSOAL / AUTORAL DE BAIXO RISCO
→ Guilherme + Editorial

SOBRE GUIVOS
→ Guilherme + autoridade institucional quando necessário

TÉCNICO
→ especialista competente

SENSÍVEL
→ coordenação apropriada

OPERACIONAL
→ canal / área responsável, não fundador por padrão
```

## 96. Escala da operação

A equipe cresce por:

```text
VOLUME REAL
+
COMPLEXIDADE REAL
+
RISCO REAL
+
OPORTUNIDADE REAL
```

Não por desejo de aparentar estrutura grande.

À medida que o sistema amadurece:

```text
GUILHERME
→ reduz aprovação mecânica

GUILHERME
→ preserva pensamento, experiência, decisão e autoria
```

## 97. Calendário e silêncio

O calendário organiza conteúdo maduro e janelas possíveis.

Não deve criar rotinas mecânicas como:

```text
SEGUNDA = MOTIVAÇÃO
TERÇA = GUIVOS
QUARTA = FÉ
```

Manter 3–5 conteúdos perenes como reserva é permitido.

```text
SILÊNCIO TEMPORÁRIO
> CONTEÚDO ARTIFICIAL
```

## 98. Critério de prontidão

Antes de produzir ou publicar:

```text
1. É verdadeiro?
2. É de Guilherme?
3. É relevante?
4. É publicável?
5. Está na melhor forma disponível?
```

## 99. Critério pós-publicação

```text
O QUE FUNCIONOU?
O QUE FOI MAL INTERPRETADO?
O QUE GEROU CONVERSA?
O FORMATO AJUDOU OU ATRAPALHOU?
O QUE APRENDEMOS?
```

Publicação não encerra o processo.

## 100. Invariantes operacionais

```text
BIO CURTA
≠ IDENTIDADE REDUZIDA

CREATOR
≠ INFLUENCIADOR

PERFIL PROFISSIONAL
≠ PERFIL CORPORATIVO

FOTO DO FUNDADOR
≠ LOGO DA GUIVOS

NOVA FASE
≠ NOVA PESSOA

EVOLUÇÃO
≠ APAGAMENTO DO PASSADO

APRESENTAÇÃO
≠ CURRÍCULO

GUIVOS
≠ PITCH DE PRODUTOS

DO POSSÍVEL AO VIVIDO.
→ ASSINATURA PESSOAL

DO POSSÍVEL AO VIVIDO.
≠ SLOGAN DA GUIVOS

POSSIBILIDADE
≠ PROMESSA

ESCOLHA
→ PERMANECE DA PESSOA

PRIMEIRO MÊS
≠ CAMPANHA DE LANÇAMENTO PESSOAL

CALENDÁRIO
≠ FONTE DE IDEIAS

TESE
→ VEM ANTES DO FORMATO

EQUIPE
→ ESTRUTURA

GUILHERME
→ AUTORIA

ROTEIRO
≠ FALA DECORADA

EDIÇÃO
≠ FABRICAÇÃO DE PERSONALIDADE

IA
→ ORGANIZA

IA
≠ INVENTA AUTORIA

DOCUMENTAR
≠ PUBLICAR

PROFISSIONALIZAR
≠ TERCEIRIZAR IDENTIDADE

ACESSO
→ MÍNIMO NECESSÁRIO

TRIAGEM
≠ IMPERSONAÇÃO

MARKETING
≠ DONO DA PERSONALIDADE

MEDIA
≠ DONO DA VOZ DO FUNDADOR

INSTAGRAM
≠ FONTE CANÔNICA

MÉTRICA
≠ IDENTIDADE

ALCANCE
≠ AUTORIDADE

VIEW
≠ VALOR ESTRATÉGICO

VIRAL
≠ NOVO POSICIONAMENTO

IDENTIDADE
≠ A/B TEST

CRÍTICA
≠ CRISE

CRISE DA GUIVOS
≠ FUNDADOR AUTOMATICAMENTE NO CENTRO

VELOCIDADE
≠ IMPROVISAÇÃO

FÉ
≠ ESCUDO REPUTACIONAL

GLOBAL
≠ INGLÊS EM TUDO

PORTUGUÊS
≠ LIMITAÇÃO DE AMBIÇÃO

INTERNACIONALIZAÇÃO
→ CONSEQUÊNCIA DE REALIDADE

NÃO
→ PERFORMANCE DE GLOBALIDADE
```

## 101. Critério de execução real

Antes de qualquer alteração real no Instagram, deve existir autorização operacional explícita para o escopo correspondente.

Uma autorização futura pode abranger, de forma separada ou combinada:

- auditoria do perfil atual;
- alteração da cabeça do perfil;
- sessão / seleção de foto;
- publicação do primeiro fixado;
- produção do ciclo inicial;
- criação da estrutura de equipe;
- configuração de acessos;
- implantação do painel de métricas;
- ativação de processo de incidentes;
- internacionalização.

A execução deve registrar o que foi realmente implementado e distinguir:

```text
ESPECIFICADO
≠ CONFIGURADO
≠ PUBLICADO
≠ EVIDENCIADO
```

## 102. Relação com o estado global do GKR

Esta especificação operacional não altera, por si só:

- milestone global;
- estado de UXA;
- Product Engineering;
- estado de Produtos Especializados;
- Homes;
- Design;
- Public Canon;
- filing;
- mercado;
- internacionalização territorial da Guivos;
- validação de mercado.

Portanto, sua integração não exige bump artificial de `GKR-STATE-001` enquanto nenhum desses estados materiais for alterado.

## 103. Síntese normativa

> **O Instagram pessoal de Guilherme Oliveira será operacionalizado como presença pública autoral do fundador da Guivos, com identidade humana, associação institucional clara e independência suficiente para não se converter em quarto perfil oficial da empresa. A operação deverá preservar a autoria de Guilherme, permitir suporte profissional de equipe, utilizar tecnologia e IA como meios, proteger privacidade e segurança, interpretar métricas como aprendizado e distribuir autoridade conforme competência.**
>
> **A v1 materializa nome, bio, foto, link, transição do histórico, três conteúdos fixados, primeiro ciclo editorial, produção, papéis, acessos, métricas, incidentes e uma futura progressão internacional. Nenhuma dessas especificações, contudo, altera automaticamente o perfil real. Execução, publicação e evidência permanecem gates separados.**

## 104. Estado da autoridade

```text
GTM-011
→ active
→ normative
→ operational baseline v1

DEPENDE DE
→ GTM-010

IMPLEMENTAÇÃO REAL DO INSTAGRAM
→ not executed by this authority
```
