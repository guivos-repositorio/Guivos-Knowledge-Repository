---
id: PAS-001-CV-INTEGRATION-001
title: Integrações Funcionais do Contexto Vivo
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
  - PAS-001-CV-VIEW-001
  - PAS-001-CV-EVENT-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-INTEGRATION-001 — Integrações Funcionais do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`, das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0`, das seções 60 a 83 do `PAS-001-CV-UPDATE-001 1.0.0`, das seções 84 a 113 do `PAS-001-CV-CONFLICT-001 1.0.0`, das seções 114 a 148 do `PAS-001-CV-VIEW-001 1.0.0` e das seções 149 a 208 do `PAS-001-CV-EVENT-001 1.0.0`.

A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

# 209. Integrações funcionais do Contexto Vivo

As integrações funcionais definem como o Contexto Vivo recebe informações, fornece recortes autorizados, comunica mudanças e preserva coerência com as demais capacidades, camadas e fontes externas da Guivos.

Uma integração funcional não representa apenas transferência de dados.

Ela deverá estabelecer:

- finalidade;
- responsabilidade de cada parte;
- informações permitidas;
- origem e temporalidade;
- condições de utilização;
- permissões;
- efeitos possíveis;
- tratamento de conflitos;
- comportamento diante de falhas;
- revogação;
- explicabilidade ao participante.

> O Contexto Vivo não funciona como um repositório irrestrito de dados do participante. Ele atua como representação contextual governada, seletiva, temporal e orientada por finalidade.

# 210. Objetivos das integrações

As integrações deverão permitir que o Contexto Vivo:

1. receba informações relevantes sem exigir repetição desnecessária;
2. preserve origem, contexto e significado;
3. forneça apenas o recorte necessário a cada finalidade;
4. seja atualizado por experiências e mudanças reais;
5. informe capacidades consumidoras quando o contexto utilizado deixar de ser adequado;
6. interrompa usos após revogação ou limitação;
7. diferencie fatos, declarações, observações e inferências;
8. mantenha consistência entre canais;
9. evite dependências ocultas;
10. sustente explicações ao participante.

# 211. Princípios gerais de integração

## 211.1 Finalidade explícita

Nenhuma integração deverá existir apenas porque determinada informação está tecnicamente disponível.

Toda integração deverá responder:

> Qual valor funcional esta informação permite entregar ao participante?

## 211.2 Minimização

Somente informações necessárias deverão ser recebidas ou compartilhadas.

## 211.3 Autoridade limitada da fonte

Uma fonte poderá ser adequada para confirmar determinado fato e inadequada para interpretar seu significado.

Exemplo:

- uma instituição poderá confirmar a conclusão de um curso;
- ela não poderá concluir que o participante evoluiu profissionalmente;
- uma plataforma esportiva poderá registrar uma atividade;
- ela não poderá definir o objetivo de saúde da pessoa.

## 211.4 Contexto antes de reutilização

Informações recebidas para uma finalidade não deverão ser reutilizadas automaticamente em outra.

## 211.5 Controle do participante

O participante deverá poder compreender:

- quais integrações existem;
- que informações fornecem;
- para que são utilizadas;
- quais efeitos produzem;
- como pausá-las ou revogá-las.

## 211.6 Falha segura

Quando uma integração estiver indisponível ou produzir informação incerta, o sistema deverá reduzir confiança ou suspender efeitos críticos, em vez de presumir continuidade.

## 211.7 Independência funcional

A indisponibilidade de uma integração não deverá impedir todo o funcionamento da jornada quando alternativas legítimas existirem.

# 212. Tipos funcionais de integração

## 212.1 Integração de entrada

Fornece informações ao Contexto Vivo.

Exemplos:

- declaração do participante;
- experiência concluída;
- Evento de Vida;
- atividade registrada;
- conclusão certificada;
- alteração de permissão.

## 212.2 Integração de saída

Recebe um recorte contextual para executar finalidade autorizada.

Exemplos:

- selecionar oportunidades;
- construir Próximos Passos;
- adaptar uma intervenção;
- explicar uma recomendação.

## 212.3 Integração bidirecional

A capacidade recebe contexto, executa uma função e devolve resultado ou evidência.

Exemplo:

```text
Contexto Vivo
→ fornece restrições e objetivo
→ Oportunidades Ativas encontra alternativa
→ participante realiza experiência
→ resultado retorna ao Contexto Vivo
```

## 212.4 Integração de validação

Uma fonte ajuda a confirmar ou contestar determinado elemento.

## 212.5 Integração de notificação

Recebe informação de que o contexto utilizado mudou e deverá reavaliar decisões.

## 212.6 Integração temporária

A informação é utilizada durante uma sessão ou ação específica, sem integração ao contexto persistente.

## 212.7 Integração mediada pelo participante

A transferência depende de revisão, seleção ou confirmação da pessoa.

# 213. Modos funcionais de interação

As integrações poderão funcionar por:

- solicitação pontual;
- atualização periódica;
- evento funcional;
- sincronização iniciada pelo participante;
- consulta para finalidade específica;
- devolução de resultado;
- revisão manual;
- importação temporária.

Esses modos são funcionais e não determinam API, fila, protocolo ou tecnologia específica.

# 214. Contrato funcional de integração

Toda integração deverá possuir contrato próprio contendo:

| Atributo | Finalidade |
|---|---|
| Integração | Identificar a relação funcional |
| Participantes do contrato | Definir origem e destino |
| Finalidade | Justificar o uso |
| Direção | Entrada, saída ou bidirecional |
| Dados permitidos | Limitar o conteúdo |
| Dados proibidos | Impedir extrapolação |
| Natureza da informação | Fato, declaração, evidência, observação ou inferência |
| Temporalidade | Indicar atualidade e validade |
| Frequência | Definir quando poderá ocorrer |
| Confiança da fonte | Apoiar avaliação |
| Sensibilidade | Aplicar proteção |
| Permissões | Determinar usos autorizados |
| Condição de confirmação | Definir participação necessária |
| Efeitos permitidos | Limitar alterações possíveis |
| Eventos produzidos | Preservar rastreabilidade |
| Falhas previstas | Definir comportamento seguro |
| Revogação | Interromper usos |
| Retenção | Limitar permanência |
| Explicação | Permitir transparência |

# 215. Identificação do participante

Uma integração somente deverá associar informações ao Contexto Vivo quando existir base suficiente para identificar o participante correto.

A identificação deverá considerar:

- conta autenticada;
- autorização vigente;
- vínculo com a fonte;
- possibilidade de duplicidade;
- múltiplos perfis ou identidades digitais;
- informação compartilhada entre pessoas;
- dispositivos coletivos;
- atividades realizadas em nome de terceiros.

Exemplo:

> Uma atividade registrada em dispositivo compartilhado não deverá ser automaticamente atribuída a um único participante.

Quando houver dúvida, a informação deverá permanecer sem associação definitiva ou depender de confirmação.

# 216. Proveniência integrada

Toda informação recebida deverá preservar:

- fonte original;
- fonte intermediária, quando existir;
- participante ou organização responsável;
- data do fato;
- data de envio;
- data de recebimento;
- transformação realizada;
- finalidade autorizada;
- confiança;
- confirmação;
- limitações conhecidas.

Uma informação não deverá perder sua origem ao ser transformada em elemento contextual.

# 217. Integração com a Capacidade 01 — Captura de Contexto

A Captura de Contexto representa a principal entrada consciente do participante.

## Informações fornecidas

- declarações;
- objetivos iniciais;
- condições atuais;
- preferências;
- capacidades;
- restrições;
- relacionamentos;
- autorizações;
- correções.

## Responsabilidade do Contexto Vivo

- avaliar admissibilidade;
- criar ou atualizar elementos;
- preservar a linguagem original quando relevante;
- diferenciar resposta direta de interpretação;
- identificar lacunas;
- evitar transformar respostas incompletas em conclusões definitivas.

## Retorno para Captura de Contexto

O Contexto Vivo poderá informar:

- informação já existente;
- confirmação necessária;
- conflito;
- pergunta redundante;
- sensibilidade elevada;
- dimensão que não precisa ser aprofundada.

A Captura não deverá solicitar novamente algo que já esteja disponível e vigente sem justificativa.

# 218. Integração com a Capacidade 03 — Objetivos

A capacidade de Objetivos utilizará recortes de:

- Direção;
- Momento;
- Restrições;
- Capacidades;
- Preferências;
- Evolução.

## Contexto Vivo fornece

- objetivos declarados;
- prioridades;
- conflitos;
- temporalidade;
- restrições relevantes;
- capacidade disponível;
- evidências relacionadas;
- permissões.

## Objetivos devolve

- objetivo criado;
- objetivo priorizado;
- objetivo alterado;
- objetivo pausado;
- objetivo concluído;
- objetivo retirado;
- critérios de sucesso;
- relação com outras direções.

A capacidade de Objetivos não deverá alterar diretamente dimensões não relacionadas sem nova avaliação contextual.

# 219. Integração com a Capacidade 04 — Eventos de Vida

Eventos de Vida representam mudanças relevantes capazes de afetar uma ou mais dimensões.

## Eventos de Vida poderá fornecer

- tipo de evento;
- data;
- impacto declarado;
- duração;
- dimensões possivelmente afetadas;
- evidências;
- sensibilidade;
- confirmação.

## Contexto Vivo deverá

- avaliar cada dimensão separadamente;
- distinguir fato ocorrido de interpretação de impacto;
- registrar estados anteriores;
- identificar conflitos;
- atualizar somente elementos sustentados;
- notificar capacidades consumidoras.

Um Evento de Vida não deverá reconstruir automaticamente todo o contexto.

# 220. Integração com a Capacidade 05 — Próximos Passos

Próximos Passos utilizará o Contexto Vivo para propor ações compatíveis com o momento atual.

## Recorte possível

- objetivo ativo;
- prioridade;
- disponibilidade;
- capacidades;
- restrições;
- preferências;
- experiências recentes;
- relacionamentos relevantes;
- informações incertas.

## Próximos Passos devolve

- proposta apresentada;
- ação selecionada;
- ação recusada;
- ação iniciada;
- ação concluída;
- ação adiada;
- motivo informado;
- aprendizado da interação.

A recusa de um Próximo Passo não deverá automaticamente alterar objetivo ou preferência.

# 221. Integração com a Capacidade 06 — Oportunidades Ativas

Oportunidades Ativas deverá receber somente o recorte necessário para avaliar relevância e compatibilidade.

## Contexto possível

- direção;
- localização aproximada;
- disponibilidade;
- restrições;
- capacidades;
- preferências;
- condições financeiras autorizadas;
- relações com organizações;
- sensibilidade aplicável.

## Oportunidades Ativas devolve

- oportunidade considerada;
- compatibilidade identificada;
- incompatibilidade;
- inscrição;
- participação;
- conclusão;
- desistência;
- resultado institucional;
- avaliação do participante.

Visualização, inscrição e conclusão deverão permanecer distintas.

# 222. Integração com a Capacidade 07 — Intervenções Contextuais

Intervenções Contextuais decidirá quando:

- agir;
- perguntar;
- sugerir;
- lembrar;
- observar;
- esperar;
- silenciar.

## Contexto Vivo fornece

- relevância;
- urgência;
- atualidade;
- confiança;
- fadiga de confirmação;
- preferências de contato;
- sensibilidade;
- conflitos;
- permissões.

## Intervenções devolve

- intervenção apresentada;
- canal utilizado;
- resposta;
- adiamento;
- rejeição;
- ausência de resposta;
- efeito observado.

A ausência de resposta não deverá ser tratada como desinteresse permanente.

# 223. Integração com a Capacidade 08 — Experiências

Experiências registrará a participação efetiva em oportunidades, projetos, atividades ou relações.

## Experiências poderá fornecer

- início;
- participação;
- conclusão;
- abandono;
- duração;
- organização responsável;
- resultados;
- avaliação;
- evidências;
- relações formadas.

## Contexto Vivo deverá avaliar

- capacidade desenvolvida;
- preferência possivelmente alterada;
- restrição reduzida;
- relacionamento criado;
- objetivo impactado;
- evidência de evolução.

Nenhum desses efeitos deverá ser presumido apenas pela conclusão da experiência.

# 224. Integração com a Capacidade 09 — Evolução Contínua

Evolução Contínua utilizará elementos históricos para compreender mudanças ao longo do tempo.

## Contexto Vivo fornece

- estados anteriores;
- estados atuais;
- eventos relevantes;
- evidências;
- objetivos relacionados;
- confiança;
- temporalidade;
- contestações.

## Evolução Contínua devolve

- mudança observada;
- progresso evidenciado;
- progresso autodeclarado;
- resultado misto;
- marco alcançado;
- dificuldade relatada;
- interpretação suspensa.

A interpretação de evolução deverá poder ser contestada pelo participante.

# 225. Integração com Guivos Intelligence

Guivos Intelligence apoia interpretação, classificação, síntese e geração de hipóteses.

Ela não deverá possuir autoridade unilateral para transformar hipóteses em fatos contextuais.

## Contexto Vivo poderá fornecer

- recorte autorizado;
- objetivo da análise;
- elementos relevantes;
- temporalidade;
- conflitos;
- evidências;
- limitações;
- sensibilidade.

## Guivos Intelligence poderá devolver

- hipótese;
- síntese;
- possível relação;
- alerta de conflito;
- sugestão de revisão;
- nível de confiança;
- explicação;
- evidências utilizadas.

## Regras

- inferências deverão permanecer identificadas;
- sensibilidade deverá limitar o processamento;
- finalidade deverá restringir a análise;
- modelos não deverão ampliar permissões;
- contestação do participante deverá rebaixar ou retirar inferências incompatíveis.

# 226. Integração com a Platform Layer

A Platform Layer poderá oferecer capacidades comuns, como:

- identidade e autenticação;
- autorizações;
- notificações;
- auditoria;
- armazenamento;
- busca;
- registro de eventos;
- integrações externas;
- segurança;
- observabilidade.

O Contexto Vivo define o significado funcional das informações.

A Platform Layer não deverá redefinir:

- estado funcional;
- autoridade da fonte;
- finalidade;
- confiança;
- sensibilidade;
- regra de confirmação;
- significado de um evento.

# 227. Integração com Guivos Business

Guivos Business poderá fornecer ou consumir contexto em relações com organizações.

Exemplos:

- programa de desenvolvimento;
- benefício corporativo;
- voluntariado;
- oportunidade profissional;
- treinamento;
- projeto social;
- experiência organizacional.

## Regras

- a organização receberá apenas o recorte autorizado;
- informações pessoais não deverão ser convertidas em dados organizacionais irrestritos;
- participação institucional não autoriza avaliação integral da pessoa;
- o participante deverá compreender o compartilhamento;
- dados fornecidos pela organização deverão preservar sua natureza institucional.

# 228. Integração com Guivos Mall

Guivos Mall poderá utilizar contexto para apresentar produtos ou serviços compatíveis.

## Recortes possíveis

- objetivo;
- necessidade;
- preferência;
- localização;
- disponibilidade;
- faixa de valor autorizada;
- restrições.

## Limites

- contexto sensível não deverá ser utilizado para publicidade sem autorização específica;
- compra não deverá automaticamente criar identidade, objetivo ou preferência permanente;
- comportamento comercial não deverá redefinir o Contexto Vivo;
- contexto de jornada e perfil de consumo deverão permanecer funcionalmente distintos.

# 229. Integração com Guivos Travel

Guivos Travel poderá utilizar:

- preferências de viagem;
- disponibilidade;
- localização;
- restrições;
- relacionamentos;
- objetivos;
- condições de acessibilidade;
- orçamento autorizado.

Uma viagem poderá gerar:

- experiência;
- novos relacionamentos;
- mudança de preferência;
- Evento de Vida;
- evidência de evolução.

Esses efeitos deverão ser avaliados separadamente.

# 230. Integração com Guivos Media

Guivos Media poderá receber recortes para:

- relevância editorial;
- acessibilidade;
- idioma;
- tema de interesse;
- formato preferido.

## Limites

- consumo de conteúdo não significa objetivo;
- exposição a tema não significa concordância;
- tempo de visualização não define identidade;
- informações sensíveis não deverão ser utilizadas para seleção editorial sem finalidade autorizada.

# 231. Integração com Guivos Ads

Guivos Ads deverá possuir separação reforçada em relação ao Contexto Vivo.

## Regras mínimas

- autorização específica por finalidade;
- ausência de uso automático de informações sensíveis;
- separação entre personalização da jornada e publicidade;
- transparência sobre critérios utilizados;
- possibilidade de recusa;
- não utilização de restrições pessoais para exploração comercial indevida;
- não compartilhamento irrestrito com anunciantes;
- reavaliação imediata após revogação.

O fato de uma informação melhorar uma recomendação não autoriza seu uso publicitário.

# 232. Fontes externas autorizadas

Fontes externas poderão incluir:

- calendários;
- plataformas esportivas;
- instituições de ensino;
- empresas;
- organizações sociais;
- serviços de viagem;
- plataformas profissionais;
- dispositivos;
- aplicações pessoais;
- sistemas públicos, quando legítimo;
- fontes financeiras, futuramente e sob regras específicas.

Cada fonte deverá possuir autoridade funcional delimitada.

# 233. Classes de fontes externas

## 233.1 Fonte declarativa

Fornece informação afirmada por participante ou organização.

## 233.2 Fonte observacional

Registra atividade ou ocorrência.

## 233.3 Fonte certificadora

Confirma fato institucional, como conclusão ou vínculo.

## 233.4 Fonte operacional

Fornece agenda, disponibilidade ou situação de uso.

## 233.5 Fonte inferencial

Produz interpretações ou probabilidades.

## 233.6 Fonte pública

Fornece informação legitimamente pública.

Ser pública não significa automaticamente autorizada para qualquer finalidade.

# 234. Avaliação da qualidade da fonte

A integração deverá considerar:

- adequação ao tipo de informação;
- precisão conhecida;
- frequência de atualização;
- possibilidade de erro;
- nível de detalhe;
- existência de contestação;
- transparência;
- vínculo com o participante;
- validade da autorização;
- risco de associação incorreta.

A confiança deverá ser aplicada ao fato que a fonte pode sustentar, não à pessoa ou organização de forma genérica.

# 235. Transformações permitidas

Informações recebidas poderão ser:

- normalizadas;
- classificadas;
- contextualizadas;
- relacionadas;
- resumidas;
- convertidas em evidência;
- transformadas em hipótese.

Toda transformação deverá preservar:

- origem;
- natureza;
- temporalidade;
- finalidade;
- limitações;
- possibilidade de explicação.

Uma transformação não deverá elevar artificialmente o grau de certeza.

# 236. Integrações e informações de terceiros

Uma integração poderá conter informações sobre outras pessoas.

Exemplos:

- relacionamento familiar;
- equipe;
- grupo;
- organização;
- acompanhante;
- responsável;
- contato profissional.

O Contexto Vivo deverá:

- limitar detalhes;
- evitar criar perfil de terceiro sem base;
- proteger informações não autorizadas;
- distinguir vínculo declarado de informação sobre a outra pessoa;
- não compartilhar dados de terceiros indevidamente.

# 237. Integração de calendários

Um calendário poderá informar:

- compromissos;
- horários ocupados;
- períodos livres;
- eventos;
- localização associada.

Ele não deverá determinar automaticamente:

- disponibilidade real;
- prioridade;
- disposição;
- finalidade do período livre;
- contexto familiar;
- capacidade de participação.

Exemplo:

> Ausência de compromisso no calendário não significa que o participante está disponível.

# 238. Integração com plataformas esportivas

Uma plataforma esportiva poderá fornecer:

- tipo de atividade;
- data;
- duração;
- distância;
- frequência;
- participação em grupo;
- conclusão de desafio.

Ela não deverá definir automaticamente:

- objetivo de saúde;
- preferência;
- capacidade;
- identidade esportiva;
- progresso pessoal;
- condição clínica.

Atividades poderão ser evidências auxiliares, não conclusões integrais.

# 239. Integração com instituições de ensino

Uma instituição poderá confirmar:

- matrícula;
- presença;
- conclusão;
- certificação;
- carga horária;
- resultado acadêmico institucional.

Ela não poderá definir unilateralmente:

- aplicação prática;
- competência atual;
- satisfação;
- transformação pessoal;
- relevância para objetivo;
- evolução percebida.

# 240. Integração com organizações sociais e coletivos

Organizações poderão registrar:

- participação;
- voluntariado;
- contribuição;
- projeto;
- função exercida;
- reconhecimento;
- impacto institucional.

Essas informações poderão apoiar:

- capacidades;
- relacionamentos;
- experiências;
- evolução;
- identidade declarada.

O participante deverá poder definir o significado daquele vínculo em sua jornada.

# 241. Integração com informações profissionais

Fontes profissionais poderão fornecer:

- vínculo;
- função;
- projeto;
- competência declarada;
- certificação;
- experiência;
- mudança de emprego.

Limites:

- cargo não representa identidade integral;
- histórico profissional não define objetivo atual;
- recomendação de carreira exige contexto adicional;
- desligamento ou mudança profissional poderá ser sensível.

# 242. Consentimento e autorização

Toda integração externa deverá estabelecer:

- ação de autorização;
- informações incluídas;
- finalidades;
- duração;
- frequência;
- destinatários;
- possibilidade de revogação;
- consequências funcionais;
- política de retenção.

Autorizações amplas e genéricas deverão ser evitadas.

# 243. Revogação de integração

Após revogação:

1. novas coletas deverão cessar;
2. novos usos deverão ser interrompidos;
3. recortes contextuais deverão ser recompostos;
4. capacidades consumidoras deverão ser notificadas;
5. inferências dependentes deverão ser reavaliadas;
6. informações deverão ser preservadas, arquivadas ou removidas conforme finalidade, autorização e obrigação legítima;
7. o participante deverá receber confirmação.

Revogar a integração não significa necessariamente apagar fatos históricos legítimos.

# 244. Pausa de integração

A pausa representa interrupção temporária.

Durante a pausa:

- novas coletas serão interrompidas;
- informações existentes poderão continuar válidas;
- elementos dinâmicos poderão envelhecer;
- o participante deverá compreender os efeitos;
- a retomada dependerá de autorização vigente.

# 245. Falhas de integração

Falhas poderão incluir:

- fonte indisponível;
- autorização expirada;
- resposta incompleta;
- dados inválidos;
- atraso;
- duplicidade;
- identificação incerta;
- formato incompatível;
- revogação não propagada;
- divergência com o contexto.

## Comportamento funcional

O sistema deverá:

- preservar o contexto anterior quando ainda válido;
- reduzir confiança quando necessário;
- impedir decisões críticas baseadas em dados incertos;
- registrar a falha;
- evitar apresentar atualização como concluída;
- permitir nova tentativa;
- informar o participante quando houver impacto real.

# 246. Degradação controlada

Quando uma integração deixar de funcionar, a Guivos deverá priorizar:

1. continuidade segura;
2. transparência;
3. redução de efeitos;
4. alternativas manuais;
5. revisão futura.

Exemplo:

> Se o calendário estiver indisponível, oportunidades não deverão ser automaticamente excluídas. A disponibilidade poderá ser confirmada diretamente com o participante.

# 247. Sincronização divergente

Quando a fonte externa e o Contexto Vivo apresentarem valores diferentes:

- nenhuma informação deverá ser sobrescrita silenciosamente;
- temporalidade e contexto deverão ser comparados;
- declaração atual do participante deverá orientar elementos subjetivos;
- fatos observados poderão permanecer registrados;
- conflitos relevantes deverão ser abertos;
- usos críticos poderão ser suspensos.

# 248. Frequência de atualização

A frequência deverá ser proporcional à natureza da informação.

Exemplos:

| Informação | Frequência funcional |
|---|---|
| Disponibilidade | frequente ou sob demanda |
| Certificação concluída | eventual |
| Atividade esportiva | após atividade ou sincronização |
| Objetivo | após manifestação ou revisão |
| Permissão | efeito imediato |
| Localização aproximada | apenas quando necessária |
| Resultado histórico | não exige atualização recorrente |

Maior frequência não significa necessariamente maior qualidade.

# 249. Integrações iniciadas pela Guivos

A Guivos poderá solicitar integração quando:

- reduzir repetição;
- comprovar experiência;
- melhorar compatibilidade;
- facilitar atualização;
- aumentar explicabilidade;
- apoiar objetivo ativo.

A solicitação deverá explicar:

- benefício;
- dados necessários;
- finalidade;
- duração;
- alternativa sem integração;
- forma de revogação.

A integração não deverá ser condição obrigatória quando uma alternativa razoável existir.

# 250. Integrações iniciadas pelo participante

O participante poderá:

- conectar fonte;
- importar informação;
- escolher dados;
- limitar período;
- autorizar finalidade;
- pausar;
- revogar;
- solicitar atualização;
- contestar resultado.

A interface deverá informar o que foi efetivamente incorporado ao Contexto Vivo.

# 251. Explicabilidade das integrações

O participante deverá conseguir responder:

- qual fonte forneceu a informação;
- quando ocorreu a última atualização;
- quais elementos foram criados;
- quais interpretações foram produzidas;
- quais capacidades utilizam esses elementos;
- qual finalidade está autorizada;
- como interromper o uso;
- o que permanece após revogação.

Exemplo:

> Sua conclusão neste curso foi confirmada pela instituição responsável em 10/07/2026. Essa informação está sendo utilizada apenas para registrar sua experiência e apoiar a compreensão de capacidades relacionadas.

# 252. Auditoria funcional

As integrações deverão permitir reconstruir:

- autorização concedida;
- informação recebida;
- transformação realizada;
- elemento contextual afetado;
- evento produzido;
- capacidade consumidora notificada;
- decisão reavaliada;
- revogação aplicada;
- falha ocorrida.

A auditoria deverá respeitar minimização e sensibilidade.

# 253. Prevenção de ciclos indevidos

Integrações bidirecionais poderão criar ciclos.

Exemplo:

```text
Contexto gera recomendação
→ recomendação gera interação
→ interação gera hipótese
→ hipótese altera contexto
→ contexto gera nova recomendação
```

Para evitar ciclos indevidos:

- interação isolada não deverá alterar contexto;
- hipóteses deverão permanecer identificadas;
- atualizações deverão exigir base suficiente;
- o evento original deverá ser preservado;
- efeitos repetidos deverão ser reconhecidos;
- recomendações não deverão validar a si próprias.

# 254. Integrações e exclusão de oportunidades

Uma integração não deverá eliminar oportunidades relevantes apenas porque:

- determinado dado não está disponível;
- a fonte está temporariamente indisponível;
- existe baixa confiança;
- uma preferência não foi confirmada;
- a integração foi recusada.

Nesses casos, a Guivos poderá:

- solicitar confirmação;
- apresentar alternativa;
- indicar incerteza;
- evitar automação;
- permitir decisão manual.

# 255. Integrações e informações sensíveis

Para informações sensíveis, a integração deverá possuir:

- finalidade específica;
- autorização explícita;
- minimização reforçada;
- acesso limitado;
- confirmação proporcional;
- uso decisório controlado;
- revogação clara;
- explicação acessível;
- retenção reduzida quando possível.

Informações sensíveis não deverão ser inferidas apenas porque uma integração disponibiliza sinais relacionados.

# 256. Integrações temporárias de sessão

Uma informação poderá ser utilizada somente durante uma interação.

Exemplo:

> O participante informa uma localização temporária para encontrar um evento hoje.

A informação poderá:

- orientar aquela busca;
- não integrar o contexto persistente;
- não alterar localização atual;
- não ser reutilizada em publicidade;
- ser descartada após a finalidade.

# 257. Integração com canais conversacionais

Informações fornecidas por conversa deverão:

- ser reconhecidas como declarações;
- preservar contexto da conversa;
- diferenciar intenção de fato;
- solicitar confirmação quando necessário;
- ficar visíveis em `Meu Contexto Hoje`;
- permitir correção posterior.

O canal conversacional não deverá criar um contexto paralelo à interface principal.

# 258. Integração com notificações

Notificações poderão utilizar:

- prioridade;
- urgência;
- preferências de contato;
- disponibilidade;
- sensibilidade;
- fadiga;
- permissões.

A abertura ou rejeição de uma notificação não deverá alterar automaticamente o Contexto Vivo.

# 259. Integração com busca

A busca poderá receber recortes temporários para ordenar resultados.

Exemplos:

- objetivo;
- localização;
- disponibilidade;
- formato;
- acessibilidade.

Consultas de busca não deverão ser automaticamente persistidas como objetivo, preferência ou intenção.

# 260. Integrações entre jornadas de participantes

Relacionamentos poderão permitir experiências conjuntas.

Exemplos:

- família;
- equipe;
- grupo;
- coletivo;
- organização;
- mentor e mentorado.

Cada participante deverá manter:

- contexto próprio;
- permissões próprias;
- visibilidade própria;
- capacidade de saída;
- ausência de exposição indevida.

Um participante não deverá alterar o contexto de outro sem base adequada.

# 261. Critérios funcionais de aceitação

As integrações do Contexto Vivo serão consideradas adequadas quando permitirem:

1. declarar finalidade e responsabilidades;
2. limitar os dados recebidos e compartilhados;
3. preservar origem e temporalidade;
4. diferenciar autoridade de cada fonte;
5. identificar corretamente o participante;
6. respeitar permissões por finalidade;
7. gerar hipóteses sem transformá-las em fatos;
8. tratar conflitos sem sobrescrita silenciosa;
9. operar com falha segura;
10. pausar e revogar integrações;
11. recompor recortes contextuais;
12. informar capacidades consumidoras;
13. impedir efeitos duplicados;
14. proteger informações de terceiros;
15. explicar o uso ao participante;
16. evitar ciclos de autoalimentação;
17. permitir alternativas sem integração;
18. manter consistência entre canais;
19. separar contexto de jornada de perfil comercial;
20. não prescrever tecnologia específica.

# 262. Regras fundamentais das integrações

1. Disponibilidade técnica não constitui finalidade legítima.
2. Toda fonte possui autoridade funcional limitada.
3. Integração não significa autorização irrestrita.
4. Somente o recorte necessário deverá ser compartilhado.
5. Origem e temporalidade deverão ser preservadas.
6. Informação externa não prevalece automaticamente sobre contestação.
7. Comportamento observado não define intenção.
8. Falhas deverão reduzir efeitos, não aumentar suposições.
9. Revogação deverá interromper novos usos.
10. Informações de terceiros exigirão proteção própria.
11. Integrações não deverão criar perfis paralelos.
12. A pessoa deverá compreender e controlar as integrações.
13. O Contexto Vivo define significado funcional; a infraestrutura apenas o suporta.
14. Nenhuma integração poderá ampliar silenciosamente finalidade, permissão ou sensibilidade.
15. A implementação técnica deverá respeitar os contratos funcionais definidos.

Com isso, ficam definidas as **integrações funcionais do Contexto Vivo com capacidades, camadas, serviços e fontes externas**.

O próximo bloco da Capacidade 02 é a definição dos **KPIs, indicadores de qualidade e critérios de desempenho funcional do Contexto Vivo**.
