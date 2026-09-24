---
id: UXA-069
title: Validação Funcional e Reformulação da Expressão Guiada do Momento Atual por Texto e Voz
status: active
version: 0.1.2
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-068
depends_on:
  - UXA-001
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-020
  - UXA-023
  - UXA-035
  - UXA-037
related:
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - M7.71
normative: false
---

# Validação Funcional e Reformulação da Expressão Guiada do Momento Atual por Texto e Voz

> **F-016-A — proveniência sem baseline visual.** A antiga materialização `UXA-068` foi removida do corpus vigente. O vínculo `parent: UXA-068` preserva somente proveniência histórica; os antigos estados móveis, SVGs, composição e contagens de materialização não constituem entrada corrente de Design/IA. A responsabilidade funcional vigente é consumida por `GKR-SURF-PER-004`, pela Jornada da Pessoa e pelos registries correntes.

## 1. Finalidade

Este documento preserva as decisões funcionais extraídas dos oito estados móveis historicamente materializados pela UXA-068 e governa como a Pessoa pode expressar seu Momento Atual por texto ou voz com finalidade compreensível, ajuda proporcional, efeitos conhecidos e revisão anterior ao uso material.

A pergunta de validação é:

> **A Pessoa consegue distinguir relato de origem, ajuda temporária de organização, transcrição, síntese derivada, preparação da compreensão inicial, persistência e personalização, sem autorização implícita, direcionamento coercitivo ou descarte silencioso?**

## 2. Resultado

> **A família funcional permanece válida após reformulação.**

As decisões funcionais extraídas da antiga materialização permanecem vigentes como contrato textual. Os oito estados históricos não constituem baseline visual, pacote low-fidelity corrente nem requisito de composição para Design/IA.

A validação não aprova modelo de IA, algoritmo adaptativo, gravação, transcrição, armazenamento, textos jurídicos, protocolo clínico, protótipo, teste com pessoas ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. orientação anterior ao relato;
2. equivalência entre texto e voz;
3. início, pausa, descarte e conclusão de gravação;
4. tratamento separado de áudio, transcrição e declaração revisada;
5. organização temporária do rascunho;
6. perguntas adaptativas e alternativas apresentadas;
7. separação de assuntos e destino de trechos;
8. síntese estruturada e sua natureza derivada;
9. salvamento, saída e perda de alterações;
10. revisão e autorização da UXA-034;
11. base insuficiente e pontos desconhecidos;
12. acessibilidade funcional e ausência de pressão.

## 4. Diagnóstico transversal

### 4.1 Promessa de ausência total de processamento

A UXA-068 afirmava que nada seria processado antes da revisão e autorização. Entretanto, três recursos já pressupõem alguma análise do rascunho:

- identificação de lacuna para pergunta adaptativa;
- identificação de mais de um assunto;
- geração de síntese estruturada.

A afirmação absoluta era incompatível com a própria experiência.

A reformulação distingue quatro camadas:

| Camada | Finalidade | Regra |
|---|---|---|
| conteúdo de origem | texto, voz ou correção fornecida pela Pessoa | permanece distinguível e revisável |
| ajuda temporária solicitada | organizar o rascunho, localizar lacuna ou sugerir separação | somente após ação consciente; não prepara compreensão inicial; não personaliza |
| preparação da compreensão inicial | utilizar itens revisados para formar hipótese temporária | exige inventário e autorização específica na UXA-034 |
| persistência e personalização | manter compreensão ou adaptar superfícies futuras | permanecem bloqueadas até o gate da UXA-036 e UXA-037 |

Digitar ou gravar não autoriza automaticamente nenhuma das três camadas derivadas.

### 4.2 Ajuda derivada aparecia como resultado automático

No rascunho por texto, a seção `O que já aparece no relato` podia ser interpretada como análise automática durante a digitação.

A reformulação apresenta inicialmente:

> **Ajuda de organização ainda não solicitada.**

A Pessoa escolhe conscientemente:

> **Solicitar ajuda temporária para organizar este rascunho.**

A ação informa que utilizará somente o rascunho atual para produzir ajuda revisável, sem iniciar compreensão, persistência ou personalização.

### 4.3 Escolha de modalidade possuía ação duplicada

A orientação apresentava ações próprias para texto e voz e, simultaneamente, uma ação genérica `Escolher como começar`.

A duplicidade poderia criar destino indeterminado ou sugerir uma escolha adicional.

A reformulação mantém ações diretas e equivalentes em cada modalidade e remove a ação genérica redundante.

### 4.4 Salvamento sem destino conhecido

`Salvar e sair` não declarava se o rascunho seria mantido no dispositivo, associado à conta ou persistido remotamente.

Como o pacote não define armazenamento, a ação passa a ser:

> **Pausar e ver opções de rascunho.**

A superfície declara `Rascunho ainda não persistido` até que uma futura implementação apresente destino e consequência antes da escolha.

## 5. Reformulação da orientação comum

O estado reformulado:

- mantém texto e voz em paridade;
- explica as dimensões de referência sem exigir todas;
- declara que o relato não será utilizado para preparar compreensão inicial ou personalização antes da revisão e autorização;
- explica que perguntas, separação ou síntese exigem solicitação consciente de ajuda temporária;
- remove a ação genérica duplicada;
- mantém saída sem compartilhar e sem iniciar compreensão.

A linguagem não promete que maior volume de conteúdo produzirá melhor resultado.

## 6. Reformulação do rascunho por texto

O estado reformulado:

- preserva campo livre e orientações opcionais;
- declara o estado de persistência do rascunho;
- remove organização automática aparente;
- oferece solicitação explícita de ajuda temporária;
- explica a finalidade e o limite dessa ajuda;
- permite revisar o conteúdo de origem sem solicitar análise;
- mantém troca para voz e pausa com efeitos conhecidos;
- não presume que uma pergunta adicional será necessária.

A ação de continuidade passa a ser condicional:

```text
solicitar ajuda temporária
→ se houver lacuna material, apresentar pergunta opcional
→ se houver assuntos possivelmente distintos, apresentar separação revisável
→ caso contrário, oferecer síntese temporária
```

Nenhum caminho transforma o rascunho em compreensão inicial.

## 7. Reformulação da preparação para voz

As opções de tratamento do áudio são mutuamente exclusivas e passam a utilizar controles circulares.

Nenhuma opção vem selecionada.

As alternativas são:

- manter o áudio somente até a decisão após a revisão;
- apagar automaticamente o áudio quando a transcrição estiver disponível.

A ação para iniciar permanece indisponível até existir uma escolha e passa a declarar sua consequência:

> **Iniciar gravação e transcrição para este rascunho.**

Essa ação autoriza somente gravação e transcrição para revisão do rascunho. Não autoriza preparação da compreensão inicial, persistência da compreensão ou personalização.

## 8. Reformulação da gravação em andamento

O estado reformulado:

- mantém microfone, tempo e tratamento do áudio visíveis;
- substitui saída ambígua por `Interromper e decidir sobre esta parte`;
- mantém pausa sem concluir;
- substitui `Concluir esta parte` por `Concluir e gerar transcrição`;
- exige confirmação futura antes de descarte destrutivo;
- evita troca para texto com perda silenciosa do áudio;
- declara que finalizar gera transcrição, mas não confirma seu conteúdo;
- mantém alternativa para continuar por texto após decidir o destino da parte gravada.

A orientação durante a gravação permanece não avaliativa e não interrompe o relato.

## 9. Reformulação da revisão da transcrição

O estado reformulado distingue:

- áudio original;
- transcrição automática não confirmada;
- correções realizadas pela Pessoa;
- versão que poderá ser adicionada ao rascunho.

Foram explicitados:

- retorno à gravação sem perda silenciosa de correções;
- remoção do áudio com confirmação e sem remoção automática da transcrição;
- descarte conjunto com confirmação;
- efeito de usar a transcrição revisada;
- ausência de autorização para preparação da compreensão inicial.

A transcrição automática não recebe natureza de declaração confirmada.

## 10. Reformulação da pergunta adaptativa

A pergunta passa a declarar que foi produzida por uma ajuda temporária solicitada.

A superfície demonstra:

- qual lacuna foi identificada;
- por que a resposta pode reduzir incerteza;
- que as alternativas são exemplos, não recomendações;
- que nenhuma opção vem marcada;
- que texto livre permanece disponível;
- que a Pessoa poderá manter a dimensão em aberto;
- que `não sei ainda` e `prefiro não informar` são legítimos;
- que responder adiciona conteúdo ao rascunho, mas não autoriza compreensão ou recomendação.

`Pular por enquanto` passa a ser `Manter esta dimensão em aberto`, com efeito conhecido.

## 11. Reformulação da separação de focos

A linguagem deixa de afirmar de forma conclusiva que existem dois assuntos e passa a declarar:

> **O rascunho pode mencionar mais de um assunto.**

A superfície informa que essa é uma organização sugerida pela ajuda temporária e que a relação permanece não confirmada.

A Pessoa poderá:

- manter a relação em aberto;
- manter os assuntos juntos;
- usar um como foco e outro como condição;
- separar em dois assuntos revisáveis;
- deixar um trecho fora da síntese sem excluí-lo do rascunho;
- editar o conteúdo de origem.

Nenhuma opção vem marcada. A organização somente é aplicada após ação explícita. Excluir conteúdo de origem permanece ação separada e destrutiva.

## 12. Reformulação da síntese estruturada

O título `O que entendemos do seu relato` antecipava a compreensão inicial da Guivos.

A superfície passa a utilizar:

> **Como seu rascunho foi organizado.**

Cada bloco identifica:

- natureza: conteúdo informado ou organização sugerida;
- origem: texto ou transcrição revisada;
- estado: não confirmado, corrigido ou mantido em aberto;
- ação de editar ou remover somente da síntese.

A síntese:

- não substitui o conteúdo de origem;
- não é diagnóstico;
- não é compreensão inicial;
- não será utilizada automaticamente;
- poderá ser descartada sem excluir o rascunho;
- poderá ser adicionada ao inventário como item derivado revisado;
- poderá permanecer com desconhecidos;
- não transforma ponto em aberto em fato.

A Pessoa escolhe entre:

1. continuar para o inventário usando somente conteúdos de origem;
2. revisar e adicionar a síntese como item derivado;
3. voltar ao rascunho;
4. descartar somente a síntese.

Nenhuma ação implica aceitação silenciosa da organização sugerida.

## 13. Continuidade funcional resultante

```text
escolha de modalidade
→ orientação comum
→ relato de origem por texto ou voz
→ revisão de transcrição, quando aplicável
→ solicitação opcional de ajuda temporária
→ pergunta ou separação, somente quando materialmente útil
→ síntese temporária e revisável
→ decisão sobre usar somente origens ou incluir síntese derivada
→ inventário governado por UXA-023/035 e GKR-SURF-PER-005
→ autorização específica para preparar compreensão inicial
→ processamento governado por UXA-023/037 e GKR-SURF-PER-006
→ compreensão inicial revisável
```

A Pessoa poderá seguir diretamente do conteúdo de origem ao inventário sem solicitar pergunta, separação ou síntese.

## 14. Critérios funcionais confirmados

Após reformulação, a família demonstra que:

- texto e voz permanecem equivalentes;
- nenhuma modalidade vem pré-selecionada;
- o microfone não inicia automaticamente;
- gravação e transcrição possuem finalidade específica;
- opções mutuamente exclusivas usam controles apropriados;
- áudio, transcrição e declaração revisada permanecem separados;
- perda ou descarte exigem consequência visível e confirmação futura;
- rascunho não possui destino de salvamento inventado;
- ajuda temporária depende de solicitação consciente;
- ajuda temporária não equivale a preparação da compreensão inicial;
- perguntas são opcionais e não recomendam uma direção;
- assuntos não são separados nem descartados silenciosamente;
- síntese derivada possui natureza, origem e uso explícitos;
- conteúdo de origem permanece preservado;
- desconhecidos não são transformados em fatos;
- continuar não autoriza processamento material;
- persistência e personalização permanecem bloqueadas até gates posteriores;
- compartilhar pouco não gera culpa ou bloqueio.

## 15. Cobertura funcional corrente

| Responsabilidade | Autoridade funcional corrente | Estado |
|---|---|---|
| escolha de modalidade | `PER-003` + `UXA-020/023/035` | contrato funcional corrente |
| expressão guiada por texto ou voz | `PER-004` + `UXA-069` | contrato funcional corrente |
| inventário e revisão anterior ao processamento | `PER-005` + `UXA-023/035` | contrato funcional corrente |
| processamento e compreensão inicial | `PER-006/007` + `UXA-023/037/097` | contratos funcionais correntes |

As antigas contagens de estados materializados pertencem à proveniência do Git e não governam a cobertura atual nem a quantidade futura de telas, estados, componentes ou breakpoints.

## 16. Proteções preservadas

- autenticação não autoriza relato ou processamento;
- digitar não autoriza análise automática;
- gravar autoriza somente a operação explicitamente apresentada;
- transcrever não confirma conteúdo;
- ajuda temporária não cria compreensão persistente;
- síntese não substitui fonte;
- nenhum resultado é diagnóstico;
- nenhuma pergunta é obrigatória por padrão;
- ausência de resposta não é falha;
- conteúdo de terceiros não é solicitado;
- continuidade sem personalização permanece legítima;
- nenhuma atividade é apresentada como evolução humana;
- nenhum Próximo Passo pessoal é produzido nesta família.

## 17. Limites

Esta validação não:

- define modelo de IA ou regras de inferência;
- define algoritmo adaptativo;
- define armazenamento local ou remoto;
- implementa gravação, transcrição ou exclusão;
- define retenção jurídica final;
- cria protocolo clínico ou emergencial;
- materializa envio guiado de arquivos;
- cria referência para computador ou tablet;
- cria protótipo navegável;
- executa teste com pessoas;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto;
- inicia ambiente de simulação;
- inicia `Meus Coletivos`.

## 18. Próxima transição recomendada

Após integração, a lacuna de expressão guiada estará materializada e funcionalmente validada.

A próxima transição deverá ser decidida por autorização separada entre frentes já registradas, sem início automático de protótipo, simulador, Engenharia ou continuidade de Coletivos.
