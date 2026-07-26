---
id: UXA-020
title: Página Inicial da Guivos e Início da Jornada
status: active
version: 0.3.0
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
  - UXA-021
  - UXA-022
  - UXA-023
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - GIA-000
normative: true
---

# Página Inicial da Guivos e Início da Jornada

## 1. Decisão arquitetural

A experiência pessoal da Guivos possui três superfícies distintas e sequenciais:

1. **Página Inicial pública da Guivos**, denominada **Home**;
2. **início protegido da jornada**;
3. **Tela Hoje** como superfície pessoal recorrente.

A Home apresenta a Guivos, seu propósito, os caminhos do ecossistema e o convite voluntário para iniciar uma jornada. Ela não coleta nem processa relatos pessoais.

O início protegido recebe informações pessoais somente depois de uma transição consciente, de proteção compatível e das decisões necessárias da própria pessoa.

A Tela Hoje utiliza contexto pessoal somente depois de uma compreensão inicial suficiente, revisável e autorizada.

## 2. Sequência pessoal vigente

```text
Página Inicial pública da Guivos
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido e das alternativas
→ autenticação ou criação de conta
→ finalidades, privacidade e controles
→ escolha de modalidade de relato
→ compartilhamento mínimo e progressivo
→ revisão do que foi recebido
→ autorização específica para processamento aplicável
→ processamento visível e interrompível
→ compreensão inicial apresentada
→ revisão, correção, limitação e decisão da pessoa
→ Tela Hoje, jornada sem personalização material ou exploração geral
```

A sequência não constitui um formulário obrigatório. A pessoa poderá pausar, retomar, corrigir, compartilhar menos, retirar autorizações, excluir ou continuar sem personalização material.

## 3. Responsabilidades por superfície

| Superfície | Responsabilidade principal | Limite principal |
|---|---|---|
| Página Inicial pública | explicar a Guivos, seus caminhos e o início voluntário | não coleta relato, voz, arquivos ou fontes pessoais |
| Início protegido da jornada | receber relato, governar proteção, processamento e compreensão inicial | não apresenta personalização material antes da revisão |
| Tela Hoje | organizar mudanças, atenções, possibilidades e Próximos Passos contextuais | não substitui a Home nem o processo inicial de compreensão |

## 4. Página Inicial pública

A Home deverá permitir que uma pessoa compreenda:

- o que é a Guivos;
- como o ecossistema pode ser utilizado;
- que iniciar uma jornada é voluntário;
- que explorar não exige personalização;
- que nenhuma coleta pessoal começa automaticamente;
- o que acontecerá depois da escolha de iniciar;
- que a pessoa mantém suas próprias decisões.

A Home não deverá:

- afirmar que já compreende o momento da pessoa;
- apresentar oportunidades como personalizadas;
- solicitar texto livre, voz, imagem, documento ou arquivo pessoal;
- ativar gravação, câmera, upload ou conexão externa;
- transformar patrocínio, popularidade ou posição comercial em relevância pessoal;
- obrigar a criação de conta para conhecer o ecossistema.

A validação funcional e o wireframe da Home são governados pelos identificadores UXA-021 e UXA-022.

## 5. Transição consciente para o ambiente protegido

Ao selecionar `Iniciar minha jornada`, a pessoa deverá chegar a uma superfície que declare:

- que saiu da Home pública;
- que o ambiente seguinte poderá receber informações pessoais;
- que nenhuma coleta foi iniciada;
- que poderá conhecer o processo antes de autenticar;
- que poderá voltar ou explorar sem personalização.

Ações de referência:

- `Continuar com segurança`;
- `Entender como funciona`;
- `Voltar à Página Inicial`;
- `Explorar sem personalização`.

## 6. Autenticação e criação de conta

A pessoa poderá conhecer as etapas, modalidades, finalidades e controles antes da autenticação.

Autenticação será necessária antes de:

- salvar relato associado a uma pessoa;
- gravar ou processar voz;
- enviar, armazenar ou analisar arquivos;
- conectar fontes externas;
- formar compreensão persistente;
- iniciar personalização material.

Criar uma conta não autoriza automaticamente gravação, transcrição, análise, conexão de fonte, formação de compreensão ou personalização.

O fluxo deverá oferecer entrada, criação de conta, recuperação de acesso, retorno à Home e explicação de eventuais restrições.

## 7. Finalidades, privacidade e controles

Antes de qualquer processamento material, a experiência deverá explicar:

- qual informação será utilizada;
- para qual finalidade;
- qual superfície ou decisão poderá ser afetada;
- o que será salvo, transcrito ou extraído;
- como corrigir, limitar, retirar ou excluir;
- o efeito de não autorizar uma finalidade opcional.

Autorizações específicas serão exigidas quando aplicáveis a:

- gravação e manutenção de áudio;
- transcrição;
- análise e extração de arquivos;
- conexão de fonte externa;
- formação de compreensão persistente;
- personalização de possibilidades e Próximos Passos;
- reconhecimento futuro de mudanças.

Uma confirmação genérica não autoriza todos esses usos.

## 8. Compartilhamento mínimo e progressivo

A pessoa não precisará relatar toda a sua vida para iniciar.

O mínimo inicial poderá conter:

- o que está acontecendo agora;
- o que deseja compreender, mudar ou construir;
- uma necessidade, possibilidade ou prioridade principal;
- restrições, preferências e limites relevantes;
- o que não deseja receber ou considerar.

Perguntas adicionais deverão ser justificadas, adiáveis e recusáveis. A pessoa poderá responder `não sei`, `prefiro não informar` ou `isso não se aplica`.

## 9. Modalidades de relato

Texto, voz, arquivos e perguntas progressivas são alternativas combináveis. Nenhuma modalidade será obrigatória ou apresentada como superior.

### 9.1 Texto

O texto deverá permitir escrita livre, perguntas opcionais, revisão, edição, remoção, salvamento explícito de rascunho e limitação de uso.

Digitar não equivale a autorizar processamento material.

### 9.2 Voz

Antes da gravação, a pessoa deverá compreender finalidade, transcrição, retenção do áudio, revisão, correção, regravação, remoção e risco de registrar informações de terceiros.

Áudio e transcrição deverão possuir controles separados quando produzirem efeitos diferentes.

### 9.3 Arquivos

Antes do envio, a pessoa deverá compreender finalidade, extração prevista, limites de leitura, informações sensíveis ou de terceiros, retenção e remoção.

Enviar um arquivo não autoriza leitura irrestrita nem uso de todas as informações contidas nele.

### 9.4 Fontes externas

Uma fonte externa somente poderá contribuir quando estiver identificada, possuir finalidade limitada, autorização revogável, dados visíveis e controles de correção e desconexão.

## 10. Revisão anterior ao processamento material

A pessoa deverá visualizar um inventário dos conteúdos recebidos:

- textos;
- respostas rápidas;
- gravações;
- transcrições;
- arquivos;
- extrações propostas;
- fontes externas;
- itens removidos ou limitados.

Ela poderá editar, remover, substituir, limitar finalidade, declarar conteúdo de terceiro, voltar e compartilhar menos.

## 11. Estados funcionais

O ambiente protegido deverá distinguir:

| Estado | Significado |
|---|---|
| não iniciado | nenhuma informação pessoal foi recebida |
| autenticação pendente | conta ainda não acessada ou criada |
| privacidade pendente | finalidades e controles ainda não foram decididos |
| rascunho | conteúdo salvo sem autorização de processamento material |
| aguardando revisão | conteúdo disponível para correção |
| autorizado para processamento | finalidades aplicáveis foram decididas |
| em processamento | a compreensão inicial está sendo organizada |
| ação necessária | falha, conflito ou proteção adicional exige decisão |
| compreensão disponível | síntese inicial pronta para revisão |
| pausado | processo interrompido sem avanço automático |
| exclusão solicitada | remoção pedida e efeito aplicável apresentado |
| encerrado | relato ou jornada encerrados pela pessoa |

Mensagens vagas não deverão substituir estados verificáveis.

## 12. Processamento visível e interrompível

Durante o processamento, a pessoa deverá saber:

- quais conteúdos foram autorizados;
- quais fontes estão sendo utilizadas;
- qual finalidade está ativa;
- quais transcrições ou extrações estão pendentes;
- se ocorreu falha;
- como pausar, cancelar, remover ou substituir.

A Guivos não deverá prometer compreensão imediata, completa ou infalível.

## 13. Pausa, retirada e exclusão

A experiência deverá distinguir:

- pausar o fluxo;
- salvar rascunho;
- retirar uma autorização;
- remover um item específico;
- apagar o relato e recomeçar;
- encerrar a jornada.

Cada ação deverá explicar seu efeito sobre conteúdo original, transcrição, extração, interpretação, personalização e continuidade.

## 14. Informações sensíveis e de terceiros

Proteção adicional será aplicada quando existir conteúdo sensível, informação de outra pessoa, risco de exposição, ausência de autoridade para compartilhar ou finalidade excessiva.

A proteção poderá reduzir escopo, ocultar visualização, remover trechos, bloquear processamento incompatível, suspender a etapa ou encaminhar a ajuda apropriada.

O envio por uma pessoa não representa autorização automática das demais pessoas mencionadas.

## 15. Compreensão inicial

Antes da personalização, a Guivos deverá apresentar:

```text
o que você contou
→ o que foi recebido de fontes autorizadas
→ o que compreendemos até agora
→ o que foi inferido
→ o que permanece desconhecido ou contestado
→ como as informações poderão ser utilizadas
→ seus controles e alternativas
```

A pessoa poderá confirmar, confirmar parcialmente, contestar, corrigir, remover, impedir uso para personalização, contar mais, continuar sem recomendações pessoais ou apagar e recomeçar.

Informações não confirmadas não serão promovidas silenciosamente a fatos.

## 16. Gate de personalização

Personalização material somente poderá começar quando existirem:

1. base suficiente para uma leitura inicial limitada;
2. origem e finalidade identificadas;
3. distinção entre confirmado, observado, externo autorizado, inferido, desconhecido e contestado;
4. revisão real;
5. correção e limitação possíveis;
6. autorização compatível;
7. ausência de conflito material não resolvido;
8. incertezas e alternativas visíveis.

Quando o gate não for atendido, a pessoa poderá contar mais, corrigir, pausar, continuar sem personalização, explorar o ecossistema ou encerrar e excluir.

A Tela Hoje não será recompensa por maior exposição de dados.

## 17. Roteamento por estado

### Visitante sem autenticação

Poderá conhecer o processo, as modalidades e os controles, mas não terá relato persistido ou processado.

### Pessoa autenticada sem relato

Poderá escolher modalidade, compartilhar o mínimo, adiar ou explorar sem personalização.

### Pessoa com rascunho

Poderá retomar, revisar, remover, apagar ou continuar sem processar.

### Pessoa com processamento em andamento

Visualizará estado real, fontes, finalidades, falhas e controles de interrupção.

### Pessoa com compreensão disponível

Revisará a síntese antes de qualquer personalização material.

### Pessoa com jornada iniciada

A entrada recorrente preferencial será a Tela Hoje. A Home continuará acessível como superfície institucional.

## 18. Acessibilidade

A experiência deverá prever navegação por teclado, leitores de tela, texto ampliado, alternativas textuais à voz, alternativa sem upload, tempo suficiente para decisão, confirmação antes de ações destrutivas e recuperação compreensível de falhas.

## 19. Autoridade da validação detalhada

A primeira validação funcional detalhada do início protegido é registrada pelo identificador UXA-023.

Ela confirma o contrato após reformulação, mas não cria wireframe, tecnologia, protótipo, design ou desenvolvimento.

## 20. Limites

Este documento não:

- define tecnologia de autenticação;
- define formatos e limites técnicos de voz ou arquivos;
- define armazenamento, criptografia ou infraestrutura;
- define modelo de inteligência artificial;
- autoriza inferências sensíveis;
- cria wireframe gráfico do início protegido;
- cria protótipo navegável;
- executa testes de usabilidade;
- inicia Engenharia de Produto;
- inicia automaticamente qualquer etapa empresarial.
