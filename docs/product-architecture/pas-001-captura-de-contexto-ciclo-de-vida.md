---
id: PAS-001-CC-LIFECYCLE-001
title: Regras do Ciclo de Vida e Estados Funcionais da Captura de Contexto
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-18
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-RECON-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - PAS-001-IC-CONTRACT-001
  - PAS-001-EXP-CONTRACT-001
  - PAS-001-EC-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-007
---

# PAS-001-CC-LIFECYCLE-001 — Regras do Ciclo de Vida e Estados Funcionais da Captura de Contexto

# 4566. Autoridade e vínculo

Este documento é a primeira extensão normativa complementar da Capacidade 01 — Captura de Contexto.

Ele deve ser interpretado em conjunto com:

- as seções 8 a 27 do `PAS-001 0.5.0`;
- `PAS-001-RECON-001 1.0.0`;
- os contratos finais das Capacidades 02 a 09;
- `GLPA-001`;
- `GIA-000`;
- as decisões canônicas vigentes.

Em caso de divergência, este documento deve refinar ou substituir as disposições específicas do ciclo de vida da captura, preservando o histórico documental.

# 4567. Estado da capacidade

A Capacidade 01 permanece:

> **Substantially complete — formal functional closure required.**

A publicação desta extensão conclui a primeira das três etapas obrigatórias de fechamento:

1. ciclo de vida e estados;
2. eventos e integrações;
3. KPIs, guardrails, cenários e contrato final.

A capacidade não deve ser classificada como `Functionally complete` nesta etapa.

# 4568. Finalidade do ciclo de vida

O ciclo de vida deve governar como uma interação inicial de compreensão é:

- iniciada;
- explicada;
- autorizada;
- conduzida;
- pausada;
- retomada;
- processada;
- transcrita;
- interpretada;
- sintetizada;
- apresentada;
- revisada;
- parcialmente confirmada;
- confirmada;
- corrigida;
- limitada;
- mantida temporariamente;
- encaminhada;
- contestada;
- revogada;
- encerrada;
- abandonada;
- expirada;
- reconstruída;
- protegida diante de falhas.

# 4569. Pergunta central

> **Como permitir que um participante expresse seu contexto e seja inicialmente compreendido sem transformar captura, transcrição, interpretação, síntese, confirmação ou persistência em conceitos equivalentes?**

# 4570. Princípio normativo central

A Captura de Contexto deve preservar a seguinte cadeia:

```text
expressão do participante
→ entrada original
→ transcrição, quando aplicável
→ interpretação proposta
→ síntese apresentada
→ revisão do participante
→ confirmação, confirmação parcial, correção, limitação ou recusa
→ recorte autorizado
→ capacidade consumidora realiza decisão própria
```

Nenhuma etapa deve ser silenciosamente omitida quando sua ausência puder alterar materialmente o significado ou o controle do participante.

# 4571. Singularidade funcional

A singularidade da capacidade é:

> **Iniciar uma compreensão autorizada, revisável e suficientemente útil do participante, preservando sua expressão original e seu controle sobre interpretação, síntese, persistência e uso posterior.**

A capacidade não deve representar:

- cadastro universal;
- entrevista obrigatória;
- diagnóstico;
- perfil definitivo;
- Contexto Vivo integral;
- definição de Objetivos;
- confirmação de Eventos de Vida;
- decisão de Próximos Passos;
- ativação de Oportunidades;
- emissão de Intervenções;
- confirmação de Experiências;
- reconhecimento de Evolução Contínua.

# 4572. Unidade funcional principal

A unidade funcional principal é:

> **Registro de Captura de Contexto**

O registro deve funcionar como agregado capaz de preservar o histórico completo e autorizado de uma sessão ou conjunto relacionado de sessões.

# 4573. Conteúdo do Registro de Captura de Contexto

O agregado deve preservar, conforme aplicável:

- identificador permanente;
- participante;
- modo de identidade;
- sessão;
- finalidade;
- canais;
- entradas originais;
- anexos;
- transcrições;
- interpretações;
- sínteses;
- confirmações;
- correções;
- limitações;
- remoções;
- autorizações;
- persistência;
- recortes produzidos;
- temporalidades;
- proveniência;
- sensibilidade;
- confiança;
- incerteza;
- versões;
- contestações;
- revogações;
- falhas;
- histórico.

# 4574. Identidade permanente do agregado

O `Registro de Captura de Contexto` deve possuir identidade permanente independente:

- do canal;
- do dispositivo;
- da conta;
- da sessão técnica;
- da transcrição;
- da síntese;
- do perfil do participante;
- do recorte enviado a outra capacidade.

Mudanças de canal não devem criar automaticamente um novo agregado.

# 4575. Sessão de captura

A sessão é uma unidade temporal e operacional dentro do registro.

Um registro pode possuir:

- uma sessão única;
- múltiplas sessões relacionadas;
- sessões retomadas;
- sessões em canais diferentes;
- sessões temporárias;
- sessões expiradas;
- sessões encerradas sem propagação.

Sessão e agregado não devem ser tratados como equivalentes.

# 4576. Identidade do participante

A captura pode operar com:

- participante autenticado;
- participante em autenticação progressiva;
- identidade provisória;
- sessão pseudonimizada;
- sessão temporária sem vínculo permanente;
- representante legítimo;
- participante coletivo ou institucional autorizado.

A ausência de cadastro completo não deve impedir o início quando a finalidade permitir.

# 4577. Papéis funcionais

Devem permanecer distintos:

- participante;
- titular;
- representante;
- acompanhante;
- operador;
- profissional;
- organização;
- fonte;
- intérprete;
- produtor da síntese;
- revisor;
- consumidor do recorte;
- administrador técnico;
- Guivos Intelligence;
- Platform Layer.

Acesso técnico não representa autoridade para interpretar ou confirmar o contexto.

# 4578. Finalidade da captura

Antes da coleta, a finalidade deve ser:

- apresentada;
- compreensível;
- específica;
- proporcional;
- compatível com a sensibilidade;
- temporalmente limitada;
- separada de publicidade;
- separada de termos genéricos;
- revisável;
- passível de recusa.

Não constituem finalidade suficiente:

- conhecer melhor o usuário;
- aumentar engajamento;
- melhorar conversão;
- personalizar publicidade;
- prever comportamento;
- criar perfil completo;
- maximizar dados coletados.

# 4579. Fluxo funcional geral

```text
início solicitado
→ identidade mínima ou modo temporário
→ finalidade apresentada
→ canal selecionado
→ autorização aplicável
→ captura
→ pausa, continuação ou encerramento
→ processamento
→ transcrição, quando aplicável
→ interpretação inicial
→ síntese
→ reflexão ao participante
→ revisão
→ confirmação total, parcial, correção, limitação ou recusa
→ decisão de persistência
→ produção de recorte autorizado
→ encerramento
```

Nem toda sessão deve percorrer todas as etapas.

# 4580. Estados independentes

Devem permanecer independentes:

1. estado funcional da sessão;
2. estado da entrada;
3. estado do canal;
4. estado da transcrição;
5. estado da interpretação;
6. estado da síntese;
7. estado da confirmação;
8. estado da autorização;
9. estado da persistência;
10. estado da propagação;
11. estado da contestação;
12. estado da revogação;
13. estado da sensibilidade;
14. estado técnico.

Nenhuma dimensão deve substituir automaticamente outra.

# 4581. Estado funcional da sessão

| Estado | Significado |
|---|---|
| `Not initiated` | Nenhuma sessão funcional foi iniciada |
| `Explaining purpose` | Finalidade, controles e condições estão sendo apresentados |
| `Awaiting participant` | A capacidade aguarda expressão ou decisão do participante |
| `Capturing` | Uma entrada está sendo recebida |
| `Paused` | A captura foi temporariamente interrompida |
| `Processing` | Conteúdo recebido está sendo preparado ou interpretado |
| `Reflecting understanding` | Uma interpretação ou síntese está sendo apresentada |
| `Awaiting review` | A capacidade aguarda revisão do participante |
| `Partially confirmed` | Parte da síntese foi confirmada |
| `Confirmed` | Existe síntese suficientemente confirmada para a finalidade |
| `Correction requested` | Foi solicitada alteração material |
| `Limited` | Escopo, campos, uso ou persistência foram limitados |
| `Temporary` | A sessão opera sem persistência permanente |
| `Abandoned` | O participante interrompeu sem conclusão |
| `Expired` | O período válido da sessão terminou |
| `Contested` | Associação, interpretação, síntese ou efeito foi questionado |
| `Revoked` | Autorização ou uso aplicável foi revogado |
| `Closed` | O ciclo operacional da sessão terminou |
| `Failed` | Não foi possível produzir estado confiável |

# 4582. Estado não iniciado

No estado `Not initiated`:

- nenhuma captura deve ocorrer;
- nenhum áudio deve ser gravado;
- nenhum campo deve ser presumido;
- nenhuma autorização deve ser inferida;
- nenhuma sessão permanente deve ser criada sem necessidade;
- informações técnicas mínimas podem ser utilizadas apenas para funcionamento e segurança.

# 4583. Explicação da finalidade

Em `Explaining purpose`, a capacidade deve informar:

- por que a captura está sendo proposta;
- o que poderá ser informado;
- quais canais estão disponíveis;
- que perguntas podem ser recusadas;
- como pausar ou abandonar;
- o que poderá ser persistido;
- como revisar;
- quais usos posteriores são possíveis;
- como limitar ou revogar;
- se existe gravação;
- se existe processamento automatizado.

A finalidade deve ser explicada antes da coleta material.

# 4584. Aguardando participante

Em `Awaiting participant`, a capacidade pode:

- aguardar escolha do canal;
- aguardar autorização;
- aguardar início da fala ou escrita;
- oferecer exemplos neutros;
- permitir retorno posterior;
- oferecer sessão temporária.

Não deve pressionar, gerar urgência artificial ou utilizar silêncio como consentimento.

# 4585. Início da captura

A transição para `Capturing` deve exigir:

- finalidade apresentada;
- canal definido;
- indicação visível da captura;
- autorização aplicável;
- identidade ou modo temporário suficiente;
- condições técnicas mínimas;
- possibilidade de pausa e encerramento.

# 4586. Captura em andamento

Durante `Capturing`, a capacidade deve:

- permitir expressão livre;
- reduzir interrupções;
- preservar a entrada original;
- indicar que a captura está ativa;
- permitir pausar;
- permitir continuar;
- permitir apagar ou recomeçar;
- evitar perguntas não necessárias;
- evitar interpretação apresentada como fato;
- impedir recomendação prematura.

# 4587. Pausa

A pausa deve:

- interromper novas entradas;
- interromper gravação;
- preservar o conteúdo já recebido dentro da autorização;
- impedir processamento adicional opcional quando solicitado;
- indicar o estado ao participante;
- permitir retomada ou encerramento;
- respeitar expiração e segurança.

Pausa não representa abandono, recusa ou revogação.

# 4588. Retomada

A retomada deve validar:

- identidade ou continuidade da sessão;
- validade da finalidade;
- validade da autorização;
- canal;
- conteúdo já preservado;
- tempo transcorrido;
- alterações materiais;
- sensibilidade;
- necessidade de nova explicação.

Uma sessão expirada não deve ser retomada silenciosamente.

# 4589. Processamento

Em `Processing`, a capacidade pode executar:

- preparação técnica;
- conversão de formato;
- transcrição;
- segmentação;
- identificação de idioma;
- classificação inicial;
- extração de elementos candidatos;
- análise de confiança;
- identificação de sensibilidade;
- identificação de pontos incertos.

Processamento não representa compreensão confirmada.

# 4590. Reflexão da compreensão

Em `Reflecting understanding`, a capacidade deve:

- apresentar uma síntese compreensível;
- separar fatos declarados de inferências;
- indicar pontos incertos;
- evitar linguagem definitiva;
- permitir detalhamento progressivo;
- apresentar fontes quando necessário;
- explicar por que determinado elemento foi incluído;
- oferecer controles claros.

# 4591. Aguardando revisão

Em `Awaiting review`, o participante deve poder:

- confirmar;
- confirmar parcialmente;
- corrigir;
- acrescentar;
- remover;
- limitar;
- recusar persistência;
- manter temporariamente;
- contestar interpretação;
- solicitar nova síntese;
- encerrar sem concluir.

# 4592. Confirmação parcial

`Partially confirmed` deve representar que:

- alguns elementos foram confirmados;
- outros permanecem pendentes, limitados ou contestados;
- somente os elementos confirmados ou legitimamente autorizados podem produzir recortes;
- a síntese integral não deve ser apresentada como confirmada;
- áreas não confirmadas devem permanecer identificáveis.

# 4593. Confirmação suficiente

`Confirmed` deve significar:

> **Existe uma síntese suficientemente confirmada para a finalidade autorizada.**

Não deve significar:

- verdade absoluta;
- descrição completa da pessoa;
- autorização universal;
- permanência indefinida;
- concordância com inferências futuras;
- confirmação de Objetivo;
- confirmação de Evento de Vida;
- compromisso;
- evolução;
- diagnóstico.

# 4594. Correção solicitada

Em `Correction requested`:

- efeitos derivados materiais devem ser suspensos quando necessário;
- o valor anterior deve ser preservado;
- o elemento contestado deve ser identificado;
- a correção deve possuir autoria;
- nova síntese deve ser produzida quando aplicável;
- consumidores devem ser corrigidos em extensão posterior;
- o participante deve revisar o resultado.

# 4595. Estado limitado

`Limited` pode atingir:

- campo;
- trecho;
- tema;
- finalidade;
- consumidor;
- período;
- persistência;
- interpretação;
- personalização;
- compartilhamento;
- canal.

Limitação não deve excluir automaticamente toda a sessão.

# 4596. Sessão temporária

No estado `Temporary`:

- deve existir prazo ou condição de expiração;
- a finalidade permanece específica;
- a persistência é mínima;
- não deve existir perfil permanente por padrão;
- recortes permanentes dependem de autorização adicional;
- o participante deve conhecer os limites;
- dados temporários devem ser descartados ou anonimizados conforme contrato.

# 4597. Abandono

`Abandoned` deve representar interrupção sem conclusão funcional.

O abandono:

- não representa fracasso;
- não representa recusa definitiva;
- não autoriza nova pressão;
- não confirma a síntese;
- não permite propagação ampla;
- pode preservar somente o necessário e autorizado;
- pode permitir retomada futura consciente.

# 4598. Expiração

Uma sessão deve expirar quando:

- terminar sua validade;
- a autorização vencer;
- o contexto se tornar materialmente desatualizado;
- a continuidade não puder ser confirmada;
- o modo temporário terminar;
- ocorrer condição contratual de encerramento.

Expiração não deve apagar automaticamente fatos legitimamente preservados.

# 4599. Contestação

`Contested` pode atingir:

- identidade;
- autoria;
- entrada;
- transcrição;
- interpretação;
- síntese;
- confirmação;
- finalidade;
- autorização;
- persistência;
- recorte;
- consumidor;
- temporalidade;
- proveniência.

Contestações materiais devem limitar efeitos até análise.

# 4600. Revogação

`Revoked` deve indicar que determinada autorização, finalidade, associação ou uso deixou de ser válido.

A revogação pode atingir:

- coleta futura;
- gravação;
- persistência;
- interpretação opcional;
- personalização;
- produção de novos recortes;
- compartilhamento;
- integração;
- retenção não obrigatória.

A revogação não deve ser declarada concluída antes da propagação suficiente, a ser governada pela próxima extensão.

# 4601. Encerramento

`Closed` deve representar o término do ciclo operacional da sessão.

O encerramento deve registrar:

- motivo;
- estado da síntese;
- estado da confirmação;
- persistência escolhida;
- recortes produzidos;
- elementos pendentes;
- limitações;
- revogações;
- validade;
- possibilidade de retomada ou nova captura.

# 4602. Falha

`Failed` deve ser utilizado quando não houver estado funcional confiável.

A falha deve distinguir:

- falha de canal;
- falha de gravação;
- falha de transcrição;
- falha de interpretação;
- falha de persistência;
- falha de autenticação;
- falha de autorização;
- falha de propagação;
- falha parcial;
- indisponibilidade externa.

Falha não deve ser apresentada como captura concluída.

# 4603. Transições fundamentais

São transições permitidas, conforme condições aplicáveis:

```text
Not initiated
→ Explaining purpose
→ Awaiting participant
→ Capturing
→ Paused ou Processing
→ Reflecting understanding
→ Awaiting review
→ Partially confirmed, Confirmed, Correction requested ou Limited
→ Temporary ou persistência autorizada
→ Closed
```

Também podem ocorrer:

```text
Capturing → Abandoned
Paused → Capturing
Paused → Closed
Awaiting review → Correction requested
Confirmed → Contested
Contested → Correction requested
Correction requested → Reflecting understanding
qualquer estado material → Failed
```

# 4604. Transições proibidas

Não devem ocorrer:

- `Not initiated → Capturing` sem finalidade;
- `Awaiting participant → Confirmed`;
- `Capturing → Confirmed` sem síntese;
- `Processing → Confirmed` sem reflexão;
- `Reflecting understanding → propagação integral` sem revisão;
- `Partially confirmed → confirmação integral` por inferência;
- `Abandoned → Confirmed`;
- `Expired → Capturing` sem revalidação;
- `Revoked → nova propagação`;
- `Failed → sucesso integral`;
- `Contested → efeitos de alto impacto` sem análise;
- `Temporary → persistência permanente` sem nova autorização.

# 4605. Unidade de entrada

Uma entrada deve possuir identidade própria dentro do registro.

Podem ser entradas:

- fala;
- texto;
- resposta guiada;
- documento;
- imagem;
- vídeo;
- áudio;
- seleção;
- correção;
- declaração externa autorizada;
- dado importado.

# 4606. Estados da entrada

Uma entrada pode estar:

- iniciada;
- parcial;
- recebida;
- interrompida;
- incompleta;
- corrompida;
- preservada;
- descartada;
- limitada;
- contestada;
- corrigida;
- revogada;
- indisponível.

Entrada recebida não representa interpretação correta.

# 4607. Entrada original

A entrada original deve ser preservada, quando aplicável, para:

- revisão;
- correção;
- explicabilidade;
- auditoria;
- reconstrução;
- comparação com a transcrição;
- contestação.

A preservação deve respeitar:

- finalidade;
- autorização;
- sensibilidade;
- minimização;
- retenção;
- direito de remoção;
- proteção de terceiros.

# 4608. Captura por voz

A voz deve:

- ser opção, não obrigação;
- possuir indicação clara de gravação;
- permitir pausa;
- permitir encerramento;
- permitir ouvir, quando aplicável;
- permitir corrigir transcrição;
- permitir excluir áudio, quando aplicável;
- evitar ativação silenciosa;
- proteger ambientes compartilhados.

A voz não deve ser usada para inferir personalidade, emoção, saúde ou intenção sem contrato legítimo específico.

# 4609. Captura por texto

O texto deve:

- possuir valor equivalente à voz;
- permitir edição antes do envio;
- permitir complementação;
- permitir exclusão;
- preservar autoria;
- evitar manipulação por sugestões;
- ser acessível;
- permitir fluxo livre ou estruturado.

Texto mais longo não representa melhor qualidade de contexto.

# 4610. Fluxo guiado

O fluxo guiado deve:

- ser opcional;
- explicar por que cada pergunta é feita;
- permitir pular;
- permitir resposta livre;
- evitar categorias rígidas;
- adaptar profundidade;
- impedir questionário excessivo;
- evitar repetição;
- permitir encerramento.

Não deve constituir cadastro obrigatório disfarçado.

# 4611. Arquivos e documentos

Arquivos podem ser utilizados quando:

- necessários;
- autorizados;
- proporcionais;
- protegidos;
- compatíveis com a finalidade;
- acompanhados de proveniência;
- sujeitos a retenção limitada.

O envio de documento não autoriza extração irrestrita de todos os dados contidos.

# 4612. Continuidade entre canais

A continuidade pode ocorrer entre:

- voz e texto;
- aplicativo móvel e web;
- fluxo guiado e expressão livre;
- sessão síncrona e retomada posterior;
- dispositivo pessoal e ambiente protegido;
- canal conversacional e interface estruturada.

A troca de canal deve preservar:

- identidade;
- finalidade;
- estado;
- conteúdo;
- autorização;
- sensibilidade;
- versão;
- controles.

# 4613. Estado do canal

O canal pode estar:

- disponível;
- limitado;
- indisponível;
- degradado;
- protegido;
- inadequado para conteúdo sensível;
- aguardando permissão;
- desconectado.

A indisponibilidade de um canal deve oferecer alternativa quando possível.

# 4614. Unidade de transcrição

A transcrição deve permanecer distinta:

- do áudio;
- da entrada original;
- da interpretação;
- da síntese;
- da confirmação.

Ela é uma representação textual potencialmente imperfeita de uma entrada.

# 4615. Estados da transcrição

Uma transcrição pode estar:

- não aplicável;
- pendente;
- em processamento;
- produzida;
- parcial;
- baixa confiança;
- revisada automaticamente;
- apresentada;
- corrigida pelo participante;
- contestada;
- substituída;
- indisponível.

# 4616. Correção da transcrição

A correção deve preservar:

- conteúdo anterior;
- conteúdo corrigido;
- responsável;
- momento;
- fundamento;
- trecho afetado;
- impacto em interpretações;
- necessidade de nova síntese.

A correção da transcrição não deve corrigir silenciosamente interpretações já produzidas.

# 4617. Unidade de interpretação

Uma interpretação é uma leitura proposta sobre uma ou mais entradas.

Ela deve possuir:

- autoria;
- papel;
- método;
- fontes;
- confiança;
- incerteza;
- temporalidade;
- finalidade;
- limitações;
- alternativas;
- versão.

# 4618. Estados da interpretação

Uma interpretação pode estar:

- candidata;
- proposta;
- baixa confiança;
- em revisão;
- parcialmente aceita;
- aceita dentro de escopo;
- contestada;
- corrigida;
- limitada;
- substituída;
- revogada;
- inconclusiva.

Interpretação aceita não se transforma em fato original.

# 4619. Separação entre fato e inferência

A capacidade deve distinguir:

- declaração explícita;
- fato externo validado;
- observação;
- interpretação;
- hipótese;
- inferência;
- estimativa;
- sugestão;
- desconhecido.

Inferência não deve ser apresentada como declaração do participante.

# 4620. Confiança, proveniência e temporalidade

Toda interpretação relevante deve responder:

- de onde veio;
- quem informou;
- quando ocorreu;
- quando foi declarada;
- quando foi conhecida;
- quando foi interpretada;
- qual método foi utilizado;
- qual confiança possui;
- quais incertezas permanecem;
- se foi confirmada;
- se continua válida.

# 4621. Unidade de síntese

A síntese é uma representação organizada e compreensível de elementos selecionados da captura.

Ela deve permanecer distinta:

- das entradas;
- das transcrições;
- das interpretações individuais;
- do Contexto Vivo;
- do perfil permanente;
- do recorte propagado.

# 4622. Estados da síntese

Uma síntese pode estar:

- não iniciada;
- em produção;
- provisória;
- produzida;
- apresentada;
- em revisão;
- parcialmente confirmada;
- confirmada dentro de finalidade;
- corrigida;
- limitada;
- contestada;
- substituída;
- expirada;
- revogada.

# 4623. Estrutura da síntese

A síntese pode organizar:

- Momento Atual declarado;
- temas mencionados;
- intenções;
- desejos;
- objetivos candidatos;
- limitações;
- condições;
- preferências;
- recursos;
- relações;
- prioridades declaradas;
- pontos incertos;
- fatos;
- interpretações;
- temas excluídos;
- validade;
- controles.

Ela não deve afirmar que descreve integralmente o participante.

# 4624. Reflexão ao participante

A apresentação da síntese deve permitir respostas como:

- está suficientemente correta;
- está parcialmente correta;
- quero corrigir;
- quero acrescentar;
- quero remover;
- não concordo com esta interpretação;
- prefiro não registrar;
- quero manter temporariamente;
- quero encerrar.

As opções devem ser acessíveis e não manipulativas.

# 4625. Confirmação granular

A confirmação deve poder ocorrer por:

- campo;
- afirmação;
- tema;
- bloco;
- finalidade;
- consumidor;
- período;
- sensibilidade.

Uma confirmação geral não deve ser utilizada para absorver elementos materialmente diferentes ou sensíveis.

# 4626. Estado da confirmação

A confirmação pode estar:

- não solicitada;
- pendente;
- parcial;
- confirmada dentro de escopo;
- recusada;
- contestada;
- corrigida;
- expirada;
- revogada;
- não aplicável.

Silêncio não representa confirmação.

# 4627. Estado da autorização

A autorização pode estar:

- não solicitada;
- em explicação;
- pendente;
- concedida;
- concedida com limitações;
- temporária;
- expirada;
- suspensa;
- revogada;
- não aplicável por fundamento legítimo.

Autorização de captura não equivale a autorização de todos os usos posteriores.

# 4628. Consentimento e controle

Quando consentimento for aplicável, deve ser:

- informado;
- específico;
- granular;
- livre;
- verificável;
- revogável;
- temporalmente delimitado;
- separado de publicidade;
- separado de termos gerais;
- compatível com a capacidade do participante.

# 4629. Estado da persistência

A persistência pode estar:

- não solicitada;
- temporária;
- pendente de decisão;
- autorizada;
- autorizada parcialmente;
- bloqueada;
- em execução;
- concluída;
- falha;
- expirada;
- em descarte;
- descartada;
- sob retenção residual legítima.

# 4630. Persistência temporária

A persistência temporária deve declarar:

- conteúdo;
- finalidade;
- duração;
- proteção;
- possibilidade de retomada;
- condição de descarte;
- consumidores permitidos;
- restrições;
- revogação.

Ela não deve ser convertida em persistência permanente por conveniência técnica.

# 4631. Estado da propagação

A propagação pode estar:

- não solicitada;
- bloqueada;
- candidata;
- autorizada;
- em produção de recorte;
- pendente;
- parcialmente concluída;
- concluída;
- contestada;
- em correção;
- em revogação;
- falha.

A estrutura dos eventos e contratos de propagação será definida na próxima extensão.

# 4632. Recorte para Contexto Vivo

A captura pode produzir um recorte contendo apenas:

- elementos necessários;
- fatos declarados;
- interpretações identificadas;
- síntese confirmada ou parcial;
- temporalidades;
- proveniência;
- confiança;
- incertezas;
- autorizações;
- limitações;
- sensibilidade;
- validade;
- necessidade de revisão.

A Captura de Contexto não deve criar silenciosamente uma representação definitiva do participante.

# 4633. Primeiro valor

O primeiro valor pode ser:

- síntese clara;
- organização do que foi relatado;
- identificação de pontos incertos;
- confirmação de que nada precisa ser decidido ainda;
- solicitação de avaliação por capacidade competente;
- apresentação de alternativa já validada;
- orientação neutra de continuidade.

A Captura de Contexto não deve criar diretamente:

- Objetivo confirmado;
- Evento de Vida confirmado;
- Próximo Passo assumido;
- Oportunidade Ativa;
- Intervenção obrigatória;
- Experiência;
- trajetória de Evolução.

# 4634. Correção

A correção deve:

- preservar o valor anterior;
- registrar o valor corrigido;
- identificar o responsável;
- indicar o fundamento;
- registrar o momento;
- identificar elementos derivados afetados;
- permitir nova revisão;
- preparar propagação compensatória.

Correção não deve reescrever destrutivamente o histórico.

# 4635. Remoção

A remoção pode atingir:

- entrada;
- trecho;
- áudio;
- transcrição;
- interpretação;
- síntese;
- anexo;
- vínculo;
- persistência opcional;
- recorte ainda não propagado.

A remoção deve considerar obrigações legítimas, segurança, auditoria minimizada e proteção de terceiros.

# 4636. Limitação de uso

O participante deve poder impedir, conforme aplicável:

- interpretação adicional;
- uso para recomendação;
- uso comercial;
- compartilhamento;
- determinado consumidor;
- determinado tema;
- persistência permanente;
- retenção após prazo;
- integração externa.

A limitação deve produzir efeitos verificáveis.

# 4637. Contestação e efeitos

Quando uma contestação for material:

- novos efeitos devem ser limitados;
- o elemento deve permanecer identificado;
- a autoria deve ser preservada;
- interpretações alternativas podem coexistir;
- a análise deve ser registrada;
- correções devem ser compensatórias;
- nenhuma penalidade deve ser aplicada ao participante.

# 4638. Revogação e retenção residual

Retenção residual somente pode ocorrer quando houver fundamento legítimo.

Ela deve declarar:

- conteúdo preservado;
- fundamento;
- finalidade;
- duração;
- proteção;
- acesso;
- proibição de novos usos incompatíveis.

# 4639. Reabertura da sessão

Uma sessão pode ser reaberta quando:

- a finalidade permanecer válida;
- a autorização permanecer aplicável;
- a identidade puder ser validada;
- a sessão não estiver expirada de forma incompatível;
- o conteúdo anterior permanecer disponível;
- a retomada for compreensível;
- a sensibilidade permitir.

Caso contrário, deve ser criada nova sessão relacionada.

# 4640. Nova sessão relacionada

Nova sessão deve ser criada quando houver mudança material de:

- finalidade;
- participante;
- representante;
- contexto temporal;
- autorização;
- canal de risco;
- sensibilidade;
- jurisdição;
- método;
- escopo;
- relação institucional.

A relação com a sessão anterior pode ser preservada sem unificação indevida.

# 4641. Informações sensíveis

Informações sensíveis devem exigir:

- finalidade reforçada;
- minimização;
- proteção visual;
- controles granulares;
- canais adequados;
- retenção reduzida;
- acesso limitado;
- explicabilidade;
- ausência de publicidade;
- revisão humana quando necessária.

# 4642. Saúde

A capacidade não deve:

- diagnosticar;
- prescrever;
- concluir estado clínico;
- inferir saúde mental por linguagem;
- substituir profissional;
- utilizar informação de saúde para publicidade;
- ocultar limitações.

Risco ou urgência deve seguir protocolo específico.

# 4643. Espiritualidade e religião

A capacidade deve preservar:

- liberdade de crença;
- liberdade de não responder;
- pluralidade;
- privacidade;
- não julgamento.

Ela não deve medir:

- fé;
- proximidade de Deus;
- nível espiritual;
- mérito religioso;
- superioridade moral.

# 4644. Crianças e adolescentes

A captura deve considerar:

- idade;
- desenvolvimento;
- representação legítima;
- autonomia progressiva;
- linguagem adequada;
- minimização;
- proteção reforçada;
- limitações de persistência;
- prevenção de exploração comercial;
- direitos do participante menor.

# 4645. Informações de terceiros

Informações sobre terceiros devem ser:

- necessárias;
- minimizadas;
- protegidas;
- limitadas à finalidade;
- impedidas de formar perfil paralelo;
- separáveis;
- removíveis quando aplicável.

A declaração do participante não transfere automaticamente autoridade sobre o terceiro.

# 4646. Risco grave ou urgência

Quando houver sinal de risco grave ou urgência, a capacidade deve:

- limitar inferências;
- explicar seus limites;
- priorizar segurança;
- apresentar orientação apropriada;
- encaminhar a protocolo específico;
- evitar diagnóstico;
- evitar promessa de atendimento;
- registrar somente o necessário;
- respeitar jurisdição e autoridade.

# 4647. Dispositivos compartilhados

Em dispositivos compartilhados, a capacidade deve:

- utilizar títulos neutros;
- reduzir prévias;
- evitar reprodução automática;
- exigir autenticação proporcional;
- limitar armazenamento local;
- impedir retomada por pessoa incorreta;
- proteger conteúdos sensíveis;
- oferecer encerramento seguro.

# 4648. Acessibilidade

A captura deve oferecer, conforme aplicável:

- voz;
- texto;
- legendas;
- transcrição;
- leitura por tecnologia assistiva;
- navegação por teclado;
- linguagem clara;
- tempo adicional;
- pausa;
- repetição;
- confirmação acessível;
- canal alternativo.

Acessibilidade não deve exigir exposição adicional.

# 4649. Notificações e retomadas

Notificações devem:

- ser proporcionais;
- utilizar conteúdo minimizado;
- respeitar preferências;
- evitar títulos sensíveis;
- não pressionar conclusão;
- permitir desativação;
- distinguir lembrete funcional de publicidade.

Abandono não deve gerar sequência insistente de mensagens.

# 4650. Idempotência

O reprocessamento não deve duplicar:

- registro;
- sessão;
- entrada;
- transcrição;
- interpretação;
- síntese;
- confirmação;
- autorização;
- persistência;
- correção;
- contestação;
- encerramento;
- recorte.

# 4651. Duplicidade semântica

Sessões ou entradas tecnicamente distintas podem representar a mesma interação.

A avaliação deve considerar:

- participante;
- período;
- finalidade;
- canal;
- conteúdo;
- versão;
- origem;
- retomada;
- sessão anterior;
- identificadores técnicos.

A unificação deve ser reversível e preservar proveniência.

# 4652. Ordenação

Elementos fora de ordem devem considerar:

- momento da expressão;
- momento da captura;
- momento do recebimento;
- momento da transcrição;
- momento da interpretação;
- momento da apresentação;
- momento da confirmação;
- momento da correção;
- versão;
- dependências;
- revogação.

Informação tardia não deve sobrescrever silenciosamente revisão posterior.

# 4653. Concorrência

Atualizações simultâneas devem preservar:

- versão esperada;
- ator;
- papel;
- autoridade;
- campos afetados;
- estado anterior;
- conflito;
- decisão de reconciliação;
- necessidade de nova revisão;
- histórico.

A interpretação do participante não deve ser sobrescrita por operador, organização ou modelo.

# 4654. Atomicidade

Operações materiais devem definir o que precisa ocorrer atomicamente.

Exemplo de falha segura:

```text
entrada preservada
+ transcrição parcial
+ interpretação suspensa
+ síntese não apresentada
+ confirmação bloqueada
+ propagação bloqueada
```

Falha parcial deve permanecer explícita.

# 4655. Reconstrução

O estado deve ser reconstruível a partir de:

- identidade do agregado;
- sessões;
- entradas;
- canais;
- transcrições;
- interpretações;
- sínteses;
- confirmações;
- autorizações;
- persistências;
- correções;
- limitações;
- contestações;
- revogações;
- falhas;
- versões.

O valor atual isolado não deve ser a única fonte de reconstrução.

# 4656. Falha segura

Na ausência de informação suficiente, a capacidade deve preferir:

- sessão pendente;
- processamento suspenso;
- transcrição parcial;
- interpretação inconclusiva;
- síntese não apresentada;
- confirmação pendente;
- persistência bloqueada;
- propagação bloqueada;
- estado desconhecido;
- revisão humana;
- canal alternativo;
- último estado válido.

# 4657. Observabilidade

A futura implementação deve permitir observar:

- sessões iniciadas;
- canais;
- pausas;
- abandonos;
- expirações;
- falhas;
- baixa confiança;
- correções;
- limitações;
- contestações;
- revogações;
- duplicidades;
- conflitos;
- persistências temporárias;
- propagação pendente;
- exposição sensível;
- incidentes de autorização.

A observabilidade deve avaliar o sistema, não o participante.

# 4658. Auditoria

A auditoria deve reconstruir:

- finalidade apresentada;
- autorização;
- canal;
- entrada original;
- transcrição;
- transformação;
- interpretação;
- síntese;
- apresentação;
- revisão;
- confirmação;
- correção;
- limitação;
- persistência;
- recorte;
- contestação;
- revogação;
- falha.

# 4659. Responsabilidades da capacidade

A Captura de Contexto é responsável por:

- explicar finalidade;
- receber entradas;
- preservar conteúdo original;
- organizar transcrição;
- produzir interpretações iniciais;
- produzir síntese;
- refletir compreensão;
- permitir revisão;
- governar confirmação;
- governar sessão temporária;
- aplicar correções e limitações;
- proteger conteúdo sensível;
- produzir recorte autorizado;
- preservar histórico;
- operar com falha segura.

# 4660. Limites da capacidade

A Captura de Contexto não é responsável por:

- manter o Contexto Vivo;
- criar Objetivo confirmado;
- confirmar Evento de Vida;
- assumir Próximo Passo;
- ativar Oportunidade;
- decidir Intervenção;
- confirmar Experiência;
- reconhecer Evolução;
- diagnosticar;
- garantir resultado;
- executar transação;
- decidir pelo participante;
- produzir perfil definitivo;
- maximizar quantidade de dados.

# 4661. Comportamentos proibidos

A capacidade não deve:

1. iniciar gravação sem indicação;
2. capturar antes de explicar finalidade;
3. obrigar voz;
4. obrigar cadastro extenso;
5. obrigar fluxo guiado;
6. impedir que uma pergunta seja ignorada;
7. utilizar silêncio como consentimento;
8. utilizar abandono como fracasso;
9. pressionar aprofundamento;
10. persistir permanentemente sem fundamento;
11. converter sessão temporária em permanente silenciosamente;
12. apresentar transcrição como entrada original;
13. apresentar interpretação como fato;
14. apresentar síntese como descrição integral da pessoa;
15. presumir confirmação;
16. transformar confirmação parcial em integral;
17. sobrescrever correção;
18. apagar histórico por correção destrutiva;
19. impedir contestação;
20. impedir revogação;
21. reutilizar dados em finalidade incompatível;
22. utilizar vulnerabilidade para publicidade;
23. criar Objetivo automaticamente;
24. confirmar Evento de Vida automaticamente;
25. criar Próximo Passo assumido;
26. ativar Oportunidade automaticamente;
27. diagnosticar;
28. medir fé ou valor humano;
29. formar perfil paralelo de terceiro;
30. duplicar efeitos em reprocessamento;
31. criar estado impossível por ordenação incorreta;
32. sobrescrever conflito silenciosamente;
33. apresentar falha parcial como sucesso;
34. declarar revogação concluída antes de propagação suficiente.

# 4662. Critérios de aceite

A extensão é considerada consolidada quando:

1. definir autoridade e vínculo;
2. preservar o estado `Substantially complete`;
3. definir finalidade;
4. definir pergunta central;
5. definir princípio normativo;
6. definir singularidade;
7. definir o Registro de Captura de Contexto;
8. definir identidade permanente;
9. distinguir registro e sessão;
10. definir modos de identidade;
11. definir papéis;
12. governar finalidade;
13. definir fluxo geral;
14. separar estados independentes;
15. definir estados da sessão;
16. definir transições válidas;
17. definir transições proibidas;
18. governar início;
19. governar explicação;
20. governar captura;
21. governar pausa;
22. governar retomada;
23. governar processamento;
24. governar reflexão;
25. governar revisão;
26. governar confirmação parcial;
27. governar confirmação suficiente;
28. governar correção;
29. governar limitação;
30. governar sessão temporária;
31. governar abandono;
32. governar expiração;
33. governar contestação;
34. governar revogação;
35. governar encerramento;
36. governar falha;
37. definir entradas;
38. preservar entrada original;
39. governar voz;
40. governar texto;
41. governar fluxo guiado;
42. governar arquivos;
43. governar continuidade entre canais;
44. governar transcrição;
45. governar interpretação;
46. separar fato e inferência;
47. governar confiança, proveniência e temporalidade;
48. governar síntese;
49. governar confirmação granular;
50. governar autorização;
51. governar persistência;
52. governar recorte para Contexto Vivo;
53. limitar primeiro valor;
54. proteger informações sensíveis;
55. proteger crianças e adolescentes;
56. proteger terceiros;
57. governar risco e urgência;
58. assegurar acessibilidade;
59. assegurar idempotência;
60. governar duplicidade;
61. governar ordenação;
62. governar concorrência;
63. assegurar reconstrução;
64. assegurar falha segura;
65. definir responsabilidades;
66. definir limites;
67. bloquear os 34 comportamentos proibidos;
68. definir o próximo ponto normativo.

# 4663. Relação com o PAS-001 0.5.0

Esta extensão deve:

- manter a pergunta central;
- manter voz, texto e fluxo guiado;
- manter a expressão livre;
- manter a reflexão da compreensão;
- manter controles anteriores à confirmação;
- manter profundidade progressiva;
- manter tratamento de temas sensíveis;
- refinar “contexto inicial confirmado”;
- refinar o primeiro valor;
- substituir lacunas de estado e transição;
- preservar o contrato-base como histórico normativo compatível.

# 4664. Relação com PAS-001-RECON-001

Esta extensão implementa o primeiro bloco determinado pela reconciliação:

- unidade funcional;
- sessão;
- estados;
- transições;
- entradas;
- transcrição;
- interpretação;
- síntese;
- confirmação;
- autorização;
- persistência;
- correção;
- limitação;
- remoção;
- abandono;
- expiração;
- contestação;
- revogação;
- reconstrução;
- falha segura.

# 4665. Elementos reservados à próxima extensão

Permanecem para `PAS-001-CC-EVENT-INTEGRATION-001`:

- envelope comum dos eventos;
- famílias de eventos;
- comandos e propostas;
- persistência anterior à publicação;
- produtores;
- consumidores;
- contratos de integração;
- recortes versionados;
- propagação;
- correção compensatória entre capacidades;
- confirmação de processamento;
- prevenção de ciclos;
- sincronização;
- compatibilidade;
- observabilidade de integração.

# 4666. Versões da extensão

- Arquitetura de Produtos: `1.22.0 → 1.23.0`;
- Roadmap: `11.3.0 → 11.4.0`;
- Knowledge Board: `11.3.0 → 11.4.0`;
- Matriz de Consolidação Canônica: `1.22.0 → 1.23.0`;
- Changelog: `0.50.0 → 0.51.0`;
- `PAS-001`: permanece `0.5.0`;
- `PAS-001-RECON-001`: permanece `1.0.0`.

# 4667. Consolidação da extensão

`PAS-001-CC-LIFECYCLE-001 1.0.0` é registrado como a primeira extensão complementar de fechamento da Capacidade 01.

A extensão:

- preserva o estado `Substantially complete`;
- conclui a etapa `1 de 3`;
- consolida o Registro de Captura de Contexto;
- consolida sessão, entradas, transcrição, interpretação, síntese e confirmação;
- consolida estados independentes;
- consolida transições válidas e proibidas;
- governa autorização e persistência temporária;
- governa correção, limitação, remoção, contestação e revogação;
- protege informações sensíveis, terceiros e dispositivos compartilhados;
- assegura acessibilidade, idempotência, ordenação, concorrência, reconstrução e falha segura;
- registra 34 comportamentos proibidos;
- registra 68 critérios de aceite;
- não conclui funcionalmente a Capacidade 01;
- não altera a prontidão do `PAS-001` para `1.0.0`.

# 4668. Próximo ponto exato

Após esta extensão, o próximo bloco é:

> **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto**, incluindo estrutura comum versionada, comandos, propostas, eventos reconhecidos, famílias de eventos, contratos de produtores e consumidores, recortes para Contexto Vivo, finalidade, autoridade, minimização, proveniência, temporalidades, confiança, incerteza, idempotência, ordenação, concorrência, prevenção de ciclos, correção compensatória, revogação propagada, sincronização, reconstrução e falha segura.

Documento projetado:

`PAS-001-CC-EVENT-INTEGRATION-001 — Eventos e Integrações Funcionais da Captura de Contexto`

Sequência preservada:

```text
PAS-001-CC-LIFECYCLE-001
→ PAS-001-CC-EVENT-INTEGRATION-001
→ PAS-001-CC-CONTRACT-001
→ auditoria final de prontidão
→ PAS-001 1.0.0
```
