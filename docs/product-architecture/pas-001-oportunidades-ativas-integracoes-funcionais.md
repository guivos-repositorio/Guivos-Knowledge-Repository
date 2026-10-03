---
id: PAS-001-OA-INTEGRATION-001
title: Integrações Funcionais da Capacidade de Oportunidades Ativas
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-15
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
  - PAS-001-OA-EVENT-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-OA-INTEGRATION-001 — Integrações Funcionais da Capacidade de Oportunidades Ativas

## 1. Autoridade e vínculo

Este documento é a **quinta extensão normativa da Capacidade 06 — Oportunidades Ativas** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade:

- do `PAS-001-OA-FOUNDATION-001 1.0.0`;
- do `PAS-001-OA-LIFECYCLE-001 1.0.0`;
- do `PAS-001-OA-VIEW-001 1.0.0`;
- do `PAS-001-OA-EVENT-001 1.0.0`;
- das seções 2061 a 2523;
- do `PAS-001 0.5.0`.

Esta extensão mantém a capacidade no estado `In progress` e eleva o progresso editorial de referência de `80%` para `90%`.

# 2524. Finalidade das integrações

As integrações deverão permitir que Oportunidades Ativas recebam, avaliem e forneçam informações funcionais sem transferir titularidade, autoridade ou decisão entre capacidades, produtos, organizações ou sistemas.

Elas deverão impedir que:

- disponibilidade técnica seja tratada como autorização;
- catálogo seja tratado como relevância;
- publicidade seja tratada como oportunidade neutra;
- compra seja tratada como progresso;
- inscrição seja tratada como aceitação;
- participação seja tratada como transformação;
- fonte externa determine interesse pessoal;
- comissão altere prioridade;
- integração amplie silenciosamente o uso de contexto;
- falha externa produza estado falso;
- sincronização duplique oportunidades ou relações;
- dados de terceiros formem perfis paralelos.

# 2525. Fluxo funcional comum

```text
produtor ou fonte
→ identidade e associação
→ validação de autoridade
→ finalidade
→ permissões
→ minimização
→ proveniência
→ qualidade e confiança
→ temporalidade
→ transformação controlada
→ admissão como sinal, proposta, comando ou fato
→ avaliação por Oportunidades Ativas
→ persistência
→ evento funcional
→ recorte autorizado
→ consumidor
→ processamento confirmado
```

# 2526. Princípios obrigatórios

Toda integração deverá preservar:

1. titularidade;
2. autoridade limitada;
3. finalidade explícita;
4. minimização;
5. proveniência;
6. temporalidade;
7. qualidade separada de autoridade;
8. neutralidade comercial;
9. revogabilidade;
10. explicabilidade;
11. auditabilidade;
12. idempotência;
13. ordenação;
14. prevenção de ciclos;
15. proteção de terceiros;
16. ausência de vigilância excessiva;
17. ausência de precisão fabricada;
18. falha segura;
19. responsabilidade própria do consumidor;
20. controle do participante.

# 2527. Definição de integração funcional

Integração funcional é o intercâmbio governado de:

- sinais;
- fatos;
- propostas;
- comandos;
- evidências;
- consultas;
- recortes;
- estados;
- confirmações;
- resultados externos;
- solicitações de reavaliação.

A integração não representa transferência automática de decisão.

# 2528. Tipos de integração

As integrações poderão ser:

- internas entre capacidades do Journey;
- internas entre camadas da Guivos;
- entre produtos especializados;
- organizacionais;
- institucionais;
- profissionais;
- pessoais;
- temporárias;
- públicas;
- comerciais;
- comunitárias;
- transacionais;
- informacionais;
- síncronas;
- assíncronas;
- unidirecionais;
- bidirecionais.

# 2529. Modos funcionais

Uma integração poderá possuir permissão para:

- consultar;
- ler;
- propor;
- registrar;
- confirmar;
- atualizar;
- sincronizar;
- notificar;
- executar operação externa;
- compartilhar;
- exportar;
- revogar;
- auditar.

Cada modo deverá possuir escopo próprio.

# 2530. Contrato funcional comum

Toda integração deverá registrar:

| Campo | Finalidade |
|---|---|
| `integration_id` | Identidade da integração |
| `producer` | Produtor da informação ou operação |
| `consumer` | Consumidor autorizado |
| `participant_id` | Participante relacionado |
| `participant_category` | Pessoa, Organização ou Coletivo |
| `purpose` | Finalidade explícita |
| `mode` | Leitura, escrita, proposição, confirmação ou execução |
| `authority_scope` | Escopo de autoridade |
| `data_scope` | Campos permitidos |
| `sensitivity` | Classificação de sensibilidade |
| `source` | Fonte original |
| `provenance` | Cadeia de transformação |
| `quality` | Qualidade técnica |
| `confidence` | Confiança funcional |
| `validity` | Período de validade |
| `frequency` | Frequência autorizada |
| `retention` | Retenção aplicável |
| `permissions` | Permissões e restrições |
| `commercial_relation` | Relação comercial conhecida |
| `synchronization_state` | Estado da sincronização |
| `revocation_state` | Estado da revogação |

# 2531. Requisitos de admissão

Uma integração somente deverá ser admitida quando houver:

- identidade do produtor;
- identidade do consumidor;
- participante ou público associado;
- finalidade legítima;
- autoridade suficiente;
- escopo delimitado;
- campos necessários;
- temporalidade;
- sensibilidade;
- política de retenção;
- forma de pausa;
- forma de revogação;
- tratamento de falhas;
- possibilidade de auditoria.

# 2532. Integrações proibidas na admissão

Não deverão ser admitidas integrações que:

- dependam de finalidade genérica;
- exijam acesso integral à jornada;
- ocultem o consumidor final;
- permitam redistribuição irrestrita;
- não permitam revogação quando aplicável;
- utilizem vulnerabilidade para segmentação;
- misturem publicidade e relevância funcional;
- ampliem autoridade por contrato técnico;
- não permitam reconstrução de proveniência;
- tratem falha como sucesso.

# 2533. Identidade

A integração deverá validar:

- identidade do participante;
- identidade da fonte;
- identidade do fornecedor;
- identidade da organização;
- identidade do profissional;
- identidade do produto ou sistema;
- vínculos entre as partes;
- categoria do participante.

# 2534. Associação incerta

Quando a associação com o participante for incerta:

- a informação deverá permanecer não associada ou em avaliação;
- efeitos pessoais deverão ser bloqueados;
- apresentação deverá ser impedida;
- contexto não deverá ser ampliado;
- a incerteza deverá ser registrada;
- confirmação proporcional poderá ser solicitada.

# 2535. Associação incorreta

Quando uma associação incorreta for identificada:

- novos usos deverão ser interrompidos;
- recortes deverão ser recompostos;
- consumidores deverão ser notificados;
- oportunidades afetadas deverão ser reavaliadas;
- o histórico deverá ser preservado;
- dados indevidos deverão ser eliminados ou anonimizados conforme aplicável.

# 2536. Autoridade da fonte

Cada fonte somente poderá confirmar fatos dentro de sua autoridade.

Exemplos:

| Fonte | Pode confirmar |
|---|---|
| Fornecedor | Características, preço, condições e disponibilidade próprias |
| Organização | Regras, benefícios e processos institucionais próprios |
| Plataforma comercial | Estoque e situação transacional registrada |
| Instituição pública | Programa, edital, requisito ou benefício publicado |
| Profissional | Orientação ou avaliação dentro de sua competência |
| Participante | Preferências, interesse, decisão e experiência pessoal |
| Guivos Intelligence | Estimativas, hipóteses, comparações e justificativas |
| Guivos Ads | Patrocínio, campanha e relação publicitária |

# 2537. Autoridade proibida

Nenhuma fonte externa deverá confirmar:

- relevância pessoal absoluta;
- interesse não declarado;
- prioridade pessoal;
- compromisso;
- transformação;
- progresso;
- valor humano;
- estado emocional não declarado;
- fé;
- intenção;
- satisfação;
- experiência concluída sem evidência suficiente.

# 2538. Proveniência

A integração deverá preservar:

- fonte original;
- identificador original;
- momento original;
- intermediários;
- transformações;
- normalizações;
- enriquecimentos;
- estimativas;
- correções;
- limitações;
- relações comerciais.

# 2539. Cadeia de transformação

A cadeia deverá permitir reconstruir:

```text
registro original
→ validação
→ normalização
→ classificação
→ enriquecimento
→ avaliação funcional
→ recorte produzido
→ consumidor
```

# 2540. Qualidade técnica

A qualidade técnica poderá considerar:

- completude;
- formato;
- consistência;
- precisão declarada;
- atualidade;
- disponibilidade;
- duplicidade;
- integridade;
- estabilidade da fonte.

Qualidade técnica não representa autoridade.

# 2541. Confiança funcional

A confiança funcional deverá considerar:

- autoridade;
- evidências;
- convergência;
- histórico da fonte;
- temporalidade;
- limitações;
- possibilidade de verificação;
- conflitos conhecidos.

Confiança não representa certeza.

# 2542. Qualidade, confiança e autoridade

As dimensões deverão permanecer separadas.

Uma fonte poderá possuir:

- alta qualidade técnica e baixa autoridade;
- alta autoridade e informação desatualizada;
- boa confiança e precisão temporal limitada;
- informação completa e finalidade incompatível.

# 2543. Temporalidades

As integrações deverão distinguir:

- tempo do fato;
- tempo do registro externo;
- tempo da publicação;
- tempo da sincronização;
- tempo do conhecimento;
- tempo do processamento;
- tempo da aplicação;
- tempo da propagação;
- tempo da correção.

# 2544. Atualização em tempo real

Tempo real deverá significar atualização tecnicamente próxima do fato.

Não deverá representar:

- verdade definitiva;
- autorização permanente;
- relevância atual;
- contexto integral;
- interesse;
- execução;
- progresso.

# 2545. Dados históricos

Dados históricos poderão apoiar:

- verificação;
- reconstrução;
- comparação;
- correção;
- avaliação temporal;
- compreensão de disponibilidade;
- auditoria.

Dados históricos não deverão ser utilizados para criar vigilância contínua ou perfil comercial paralelo.

# 2546. Validade

Cada campo material deverá possuir validade proporcional.

Exemplos:

- estoque poderá exigir atualização frequente;
- edital poderá possuir validade definida;
- preço poderá possuir período;
- elegibilidade poderá depender de regra vigente;
- localização poderá possuir validade curta;
- preferência declarada poderá permanecer até revisão.

# 2547. Transformações permitidas

Poderão ser realizadas:

- normalização de formato;
- tradução;
- classificação;
- deduplicação;
- vinculação segura;
- extração de campos;
- agregação proporcional;
- estimativa explicitada;
- comparação;
- anonimização;
- pseudonimização;
- minimização;
- geração de justificativa.

# 2548. Transformações proibidas

Não deverão ser fabricados:

- disponibilidade;
- elegibilidade;
- aprovação;
- intenção;
- interesse;
- prioridade;
- urgência pessoal;
- compromisso;
- causalidade;
- resultado;
- progresso;
- transformação;
- diagnóstico;
- precisão temporal inexistente.

# 2549. Normalização comercial

A normalização de produtos, serviços ou ofertas não deverá:

- ocultar fornecedor;
- ocultar preço total;
- ocultar comissão;
- eliminar alternativas;
- converter anúncio em oportunidade neutra;
- alterar ordem funcional;
- reduzir risco material.

# 2550. Sincronização

A sincronização deverá controlar:

- versão;
- idempotência;
- cursor;
- sequência;
- duplicidade;
- atraso;
- conflito;
- atualização parcial;
- indisponibilidade;
- repetição;
- reconciliação;
- estado pendente.

# 2551. Estados da sincronização

Os estados poderão ser:

- não iniciada;
- ativa;
- atualizada;
- parcialmente atualizada;
- pendente;
- atrasada;
- divergente;
- pausada;
- falha;
- recuperando;
- revogada;
- encerrada.

# 2552. Sincronização divergente

Quando houver divergência:

- as versões deverão ser preservadas;
- a autoridade de cada fonte deverá ser considerada;
- o estado provisório deverá ser explícito;
- automações materiais deverão ser limitadas;
- o participante poderá contestar;
- não deverá haver escolha comercial silenciosa.

# 2553. Prevenção de ciclos

As integrações deverão impedir ciclos como:

```text
Oportunidade Ativa
→ Próximo Passo sugerido
→ oportunidade considerada relevante por causa do passo
→ prioridade ampliada
→ nova sugestão de passo
```

Cada capacidade deverá governar sua própria decisão.

# 2554. Chaves de prevenção de ciclo

Poderão ser utilizados:

- `correlation_id`;
- `causation_id`;
- `originating_capability`;
- `decision_owner`;
- `processing_depth`;
- `reassessment_reason`;
- `idempotency_key`.

# 2555. Finalidade

A finalidade deverá ser específica.

Exemplos adequados:

- localizar cursos compatíveis com Próximo Passo educacional;
- verificar disponibilidade de atendimento;
- comparar alternativas de transporte;
- acompanhar inscrição já autorizada;
- identificar benefícios institucionais.

Exemplos inadequados:

- melhorar experiência;
- personalizar tudo;
- aumentar engajamento;
- gerar valor;
- otimizar conversão.

# 2556. Minimização

A integração deverá utilizar apenas os dados necessários.

Exemplo:

Para verificar uma oportunidade local, poderá ser suficiente utilizar:

- cidade;
- raio aproximado;
- modalidade;
- período;
- necessidade funcional.

Não deverá ser necessário fornecer endereço residencial completo sem fundamento.

# 2557. Recortes funcionais

Um recorte deverá conter:

- finalidade;
- campos autorizados;
- validade;
- sensibilidade;
- autoridade;
- limitações;
- versão;
- consumidores permitidos.

# 2558. Permissões

As permissões deverão permitir controle por:

- finalidade;
- categoria;
- fonte;
- consumidor;
- campo;
- frequência;
- período;
- localização;
- sensibilidade;
- compartilhamento;
- redistribuição.

# 2559. Consentimento e outras bases legítimas

Quando consentimento for aplicável, deverá ser:

- específico;
- informado;
- compreensível;
- granular;
- revogável;
- registrado.

Outras bases legítimas não deverão eliminar transparência, minimização ou contestação.

# 2560. Pausa

Pausar uma integração deverá:

- interromper novas coletas;
- interromper atualizações;
- preservar fatos históricos legítimos;
- marcar o estado;
- reduzir automações dependentes;
- permitir retomada controlada.

# 2561. Desconexão

Desconectar deverá:

- invalidar novos acessos;
- encerrar sincronizações futuras;
- preservar histórico permitido;
- recompor recortes;
- informar consumidores;
- permitir exportação quando aplicável.

# 2562. Revogação

Revogar deverá interromper:

- novos acessos;
- novos recortes;
- novos compartilhamentos;
- novas avaliações dependentes;
- personalização incompatível;
- publicidade derivada.

# 2563. Propagação da revogação

A revogação somente deverá ser concluída após:

- identificação dos consumidores;
- bloqueio de novos usos;
- envio da revogação;
- confirmação de processamento;
- recomposição de recortes;
- registro de falhas;
- validação de encerramento.

# 2564. Retenção

A retenção deverá considerar:

- finalidade;
- sensibilidade;
- relação externa;
- obrigação legal;
- contestação;
- auditoria;
- reprocessamento;
- anonimização;
- revogação.

# 2565. Falha segura

Em falha, a integração deverá:

- preservar o último estado válido;
- marcar desatualização;
- impedir falsa disponibilidade;
- impedir falsa elegibilidade;
- bloquear efeitos críticos;
- evitar duplicidade;
- permitir recuperação;
- informar impacto material.

# 2566. Degradação controlada

A capacidade poderá operar com:

- informação parcial;
- busca reduzida;
- atualização manual;
- confirmação adicional;
- apresentação limitada;
- ausência temporária de comparação;
- suspensão de automações.

A degradação não deverá ser ocultada.

# 2567. Integração com Captura de Contexto

Captura de Contexto poderá fornecer:

- necessidade declarada;
- preferência;
- restrição;
- localização autorizada;
- orçamento;
- horizonte;
- modalidade;
- categoria de interesse;
- condição atual.

# 2568. Limites da Captura de Contexto

Captura de Contexto não deverá:

- ativar oportunidade;
- declarar relevância definitiva;
- confirmar elegibilidade;
- criar interesse;
- iniciar inscrição;
- autorizar publicidade.

# 2569. Retorno à Captura de Contexto

Oportunidades Ativas poderá solicitar esclarecimento sobre:

- localização;
- orçamento;
- modalidade;
- requisito;
- preferência;
- sensibilidade;
- finalidade.

A solicitação deverá ser proporcional e não coercitiva.

# 2570. Integração com Contexto Vivo

Contexto Vivo poderá fornecer recortes mínimos de:

- Momento;
- Direção;
- Capacidades;
- Restrições;
- Preferências;
- Relacionamentos;
- localização contextual;
- condições funcionais atuais.

# 2571. Limites do Contexto Vivo

Oportunidades Ativas não deverá:

- copiar o Contexto Vivo integral;
- formar perfil comercial paralelo;
- armazenar narrativas desnecessárias;
- ampliar finalidades;
- utilizar contexto sensível para publicidade;
- interpretar ausência de dado como ausência de necessidade.

# 2572. Reavaliação por Contexto Vivo

Mudanças contextuais poderão solicitar reavaliação de:

- relevância;
- elegibilidade;
- disponibilidade local;
- custo;
- risco;
- temporalidade;
- alternativas.

# 2573. Retorno ao Contexto Vivo

Oportunidades Ativas poderá fornecer fatos objetivos como:

- interesse declarado;
- oportunidade salva;
- inscrição iniciada;
- relação externa existente;
- preferência explicitamente alterada.

Esses fatos não deverão redefinir automaticamente o contexto.

# 2574. Integração com Objetivos

Objetivos poderá fornecer:

- direção;
- natureza;
- prioridade declarada;
- horizonte;
- critérios relevantes;
- restrições;
- estado funcional;
- permissões.

# 2575. Limites da integração com Objetivos

Uma oportunidade não deverá:

- criar objetivo;
- confirmar objetivo;
- ativar objetivo;
- alterar prioridade;
- confirmar progresso;
- concluir objetivo;
- transformar compra em avanço.

# 2576. Vínculo com objetivo

O vínculo deverá indicar:

- relação funcional;
- finalidade;
- confiança;
- limitações;
- alternativas;
- validade.

O vínculo não deverá representar dependência obrigatória.

# 2577. Reavaliação de objetivo

Oportunidades Ativas poderá solicitar revisão quando:

- surgir meio materialmente novo;
- alternativa crítica desaparecer;
- custo inviabilizar estratégia;
- risco mudar;
- elegibilidade for recusada.

Objetivos continuará responsável pela decisão.

# 2578. Integração com Eventos de Vida

Eventos de Vida poderá fornecer:

- mudança reconhecida;
- temporalidade;
- impactos confirmados;
- dimensões afetadas;
- sensibilidade;
- permissões;
- relevância.

# 2579. Reavaliação por Evento de Vida

Um Evento de Vida poderá alterar:

- relevância;
- elegibilidade;
- necessidade;
- custo;
- disponibilidade;
- localização;
- temporalidade;
- risco;
- proteção.

# 2580. Limites comerciais

Eventos de Vida sensíveis não deverão ser utilizados para:

- publicidade;
- aumento de preço;
- manipulação;
- pressão;
- urgência comercial;
- exploração de vulnerabilidade;
- venda de dados.

# 2581. Oportunidades associadas a Eventos de Vida

A associação deverá ser:

- explicável;
- minimizada;
- revisável;
- contestável;
- temporária quando necessário;
- sem interpretação emocional automática.

# 2582. Integração com Próximos Passos

Próximos Passos poderá fornecer:

- movimento delimitado;
- função necessária;
- estado;
- prontidão;
- dependências;
- bloqueios;
- temporalidade;
- orçamento;
- risco;
- alternativas.

# 2583. Função da oportunidade no passo

A oportunidade poderá atuar como:

- meio principal;
- alternativa;
- fornecedor;
- recurso;
- conteúdo;
- local;
- financiamento;
- apoio institucional;
- experiência potencial.

# 2584. Limites da integração com Próximos Passos

Oportunidades Ativas não deverá:

- criar o passo automaticamente;
- confirmar o passo;
- alterar prioridade;
- iniciar execução;
- cancelar;
- substituir;
- concluir;
- atribuir responsabilidade.

# 2585. Alteração da oportunidade vinculada

Mudanças poderão solicitar reavaliação de:

- prontidão;
- dependência;
- bloqueio;
- agenda;
- custo;
- risco;
- alternativa;
- execução.

# 2586. Conclusão independente

A conclusão de uma transação ou inscrição não deverá concluir automaticamente o Próximo Passo.

# 2587. Integração com Intervenções Contextuais

Oportunidades Ativas deverá fornecer:

- oportunidade;
- justificativa;
- disponibilidade;
- elegibilidade;
- prazo real;
- risco;
- sensibilidade;
- relação comercial;
- alternativas;
- necessidade de decisão;
- restrições de canal.

# 2588. Autoridade de Intervenções Contextuais

Intervenções Contextuais deverá decidir:

- apresentar;
- perguntar;
- lembrar;
- alertar;
- aguardar;
- observar;
- silenciar;
- não interromper.

# 2589. Limites da apresentação

Oportunidades Ativas não deverá determinar sozinha:

- momento;
- canal;
- frequência;
- urgência;
- repetição;
- tom;
- interrupção.

# 2590. Retorno da intervenção

A capacidade poderá receber:

- apresentação realizada;
- apresentação adiada;
- silêncio;
- interação;
- rejeição;
- fadiga;
- canal indisponível.

Visualização não deverá representar interesse.

# 2591. Integração com Experiências

Uma oportunidade poderá originar uma experiência quando houver participação efetiva.

Estados anteriores deverão permanecer distintos:

```text
apresentação
→ interesse
→ inscrição
→ aceitação
→ contratação
→ participação
→ experiência
```

# 2592. Limites da integração com Experiências

Oportunidades Ativas não deverá confirmar:

- experiência vivida;
- satisfação;
- aprendizado;
- mudança;
- resultado humano;
- transformação.

# 2593. Retorno de Experiências

Experiências poderá fornecer:

- participação declarada;
- experiência registrada;
- resultado percebido;
- avaliação;
- interrupção;
- evidência.

Essas informações deverão ser avaliadas pelas capacidades responsáveis.

# 2594. Integração com Evolução Contínua

Evolução Contínua poderá receber:

- experiências;
- resultados;
- evidências;
- mudanças;
- relações com objetivos.

Não deverá utilizar:

- quantidade de oportunidades;
- quantidade de visualizações;
- compras;
- inscrições;
- tempo de tela;
- valor gasto;

como medida direta de evolução humana.

# 2595. Retorno de Evolução Contínua

Evidências de evolução poderão alterar critérios futuros de relevância, desde que:

- autorizadas;
- explicáveis;
- minimizadas;
- não determinísticas;
- não classificatórias;
- não comerciais.

# 2596. Integração com Guivos Intelligence

Guivos Intelligence poderá:

- descobrir candidatos;
- classificar;
- deduplicar;
- comparar;
- estimar relevância;
- estimar elegibilidade;
- identificar riscos;
- detectar divergências;
- produzir justificativas;
- sugerir alternativas;
- identificar relações comerciais ocultas.

# 2597. Limites da Guivos Intelligence

Guivos Intelligence não deverá:

- ativar oportunidade sem contrato funcional;
- declarar interesse;
- iniciar inscrição;
- contratar;
- confirmar aprovação;
- criar compromisso;
- concluir Próximo Passo;
- concluir objetivo;
- atribuir transformação;
- utilizar vulnerabilidade comercialmente.

# 2598. Explicabilidade da inteligência

Resultados deverão registrar:

- modelo ou método;
- versão;
- dados utilizados;
- critérios;
- limitações;
- incertezas;
- fatores excluídos;
- possibilidade de contestação.

# 2599. Inferências sensíveis

Inferências sensíveis deverão:

- ser evitadas quando não necessárias;
- permanecer claramente identificadas;
- possuir efeitos limitados;
- não alimentar publicidade;
- não ser compartilhadas com fornecedores;
- permitir correção e remoção.

# 2600. Integração com Platform Layer

A Platform Layer deverá fornecer:

- identidade;
- autenticação;
- autorização;
- armazenamento;
- grafo;
- APIs;
- filas;
- eventos;
- busca;
- notificações;
- localização;
- pagamentos;
- observabilidade;
- auditoria;
- segurança;
- versionamento;
- idempotência.

# 2601. Limites da Platform Layer

A Platform Layer não deverá definir:

- relevância;
- prioridade;
- elegibilidade humana;
- interesse;
- valor da oportunidade;
- decisão do participante;
- significado de um resultado.

# 2602. Busca da plataforma

A busca deverá sustentar:

- indexação minimizada;
- filtros;
- ordenação funcional;
- proteção sensível;
- exclusão;
- desindexação;
- atualização;
- proveniência.

# 2603. Notificações da plataforma

A infraestrutura deverá preservar:

- finalidade;
- tipo funcional ou publicitário;
- sensibilidade;
- canal;
- frequência;
- preferências;
- rastreabilidade;
- revogação.

# 2604. Integração com Guivos Business

Guivos Business poderá fornecer:

- programas organizacionais;
- benefícios;
- vagas;
- capacitações;
- projetos;
- convites;
- processos;
- requisitos;
- disponibilidade institucional.

# 2605. Limites do Guivos Business

Organizações não deverão:

- acessar a jornada pessoal integral;
- definir relevância pessoal absoluta;
- transformar obrigação em interesse;
- utilizar contexto fora da finalidade;
- confirmar progresso pessoal;
- ocultar caráter institucional.

# 2606. Oportunidades obrigatórias

Uma obrigação institucional deverá ser apresentada como obrigação, não como oportunidade espontaneamente desejada.

# 2607. Integração com Guivos Mall

Guivos Mall poderá fornecer:

- produtos;
- serviços;
- fornecedores;
- preços;
- estoque;
- condições;
- avaliações;
- entrega;
- transações;
- cancelamentos;
- reembolsos.

# 2608. Limites do Guivos Mall

Mall não deverá definir:

- relevância humana;
- prioridade;
- interesse;
- adequação final;
- resultado;
- evolução;
- conclusão de objetivo.

# 2609. Transação comercial

A contratação deverá permanecer sob responsabilidade do Mall ou fornecedor.

Oportunidades Ativas deverá receber apenas:

- estado necessário;
- autorização;
- protocolo;
- alteração material;
- cancelamento;
- entrega ou prestação objetiva.

# 2610. Alternativas comerciais

Mall não deverá ocultar:

- fornecedores não parceiros;
- alternativas gratuitas;
- opções públicas;
- opções sem comissão;
- substitutos funcionalmente adequados.

# 2611. Integração com Guivos Travel

Guivos Travel poderá fornecer:

- destinos;
- experiências;
- hospedagens;
- transportes;
- roteiros;
- disponibilidade;
- preços;
- reservas;
- requisitos;
- riscos;
- condições de cancelamento.

# 2612. Limites do Guivos Travel

Reserva ou viagem não deverá confirmar:

- experiência transformadora;
- satisfação;
- Evento de Vida;
- progresso;
- evolução.

# 2613. Riscos de viagem

Deverão permanecer visíveis:

- documentação;
- segurança;
- saúde;
- deslocamento;
- acessibilidade;
- cancelamento;
- sazonalidade;
- custos adicionais;
- limitações locais.

# 2614. Integração com Guivos Media

Guivos Media poderá fornecer:

- conteúdo;
- histórias;
- guias;
- entrevistas;
- eventos editoriais;
- materiais educativos;
- conteúdo patrocinado.

# 2615. Limites do Guivos Media

Consumo de conteúdo não deverá representar:

- aprendizado confirmado;
- mudança;
- progresso;
- adesão;
- concordância;
- transformação.

# 2616. Conteúdo patrocinado

Conteúdo patrocinado deverá permanecer identificado e não poderá ser classificado como oportunidade neutra apenas por sua origem editorial.

# 2617. Integração com Guivos Ads

Guivos Ads poderá fornecer:

- campanhas;
- patrocinadores;
- condições comerciais;
- segmentação autorizada;
- conteúdo publicitário;
- períodos;
- limites;
- relatórios agregados.

# 2618. Separação funcional

Guivos Ads deverá permanecer separado de Oportunidades Ativas.

Publicidade não deverá:

- produzir relevância;
- elevar ordem;
- utilizar contexto sensível;
- substituir ausência legítima;
- ocultar alternativas;
- apresentar-se como recomendação neutra.

# 2619. Conversão publicitária

Clique, visualização ou conversão publicitária não deverão produzir automaticamente:

- interesse funcional;
- salvamento;
- vínculo;
- prioridade;
- oportunidade ativa.

# 2620. Integração com organizações e fornecedores

Organizações e fornecedores deverão informar:

- identidade;
- autoridade;
- condições;
- disponibilidade;
- elegibilidade;
- preço;
- riscos;
- políticas;
- relação comercial;
- atualizações;
- cancelamentos.

# 2621. Responsabilidade do fornecedor

O fornecedor será responsável por fatos próprios.

A Guivos permanecerá responsável por:

- avaliação funcional;
- explicabilidade;
- minimização;
- apresentação;
- neutralidade;
- controle do participante.

# 2622. Atualização pelo fornecedor

Alterações materiais deverão gerar:

- nova versão;
- reavaliação;
- histórico;
- notificação quando necessária;
- revisão de processos iniciados.

# 2623. Serviços profissionais

Integrações profissionais poderão envolver:

- educação;
- saúde;
- jurídico;
- finanças;
- carreira;
- assistência social;
- esporte;
- bem-estar;
- aconselhamento;
- orientação espiritual.

# 2624. Autoridade profissional

O profissional somente deverá operar dentro de:

- competência;
- habilitação;
- relação estabelecida;
- finalidade;
- autorização;
- jurisdição;
- validade.

# 2625. Limites profissionais

Oportunidades Ativas não deverá substituir:

- diagnóstico;
- prescrição;
- parecer jurídico;
- análise financeira regulada;
- decisão clínica;
- decisão institucional;
- discernimento espiritual pessoal.

# 2626. Integrações educacionais

Fontes educacionais poderão fornecer:

- cursos;
- programas;
- vagas;
- requisitos;
- certificações;
- horários;
- preços;
- bolsas;
- modalidade;
- resultados acadêmicos objetivos.

Participação não deverá confirmar aprendizado ou progresso de objetivo.

# 2627. Integrações de saúde

Integrações de saúde deverão aplicar:

- finalidade estrita;
- minimização reforçada;
- autoridade profissional;
- linguagem não diagnóstica;
- ausência de publicidade sensível;
- retenção reduzida;
- acesso restrito.

# 2628. Integrações financeiras

Integrações financeiras deverão apresentar:

- custos;
- taxas;
- juros;
- riscos;
- autoridade regulada;
- condições;
- elegibilidade distinta de aprovação;
- ausência de garantia de retorno.

# 2629. Calendários

Calendários poderão fornecer:

- disponibilidade;
- compromissos;
- janelas;
- conflitos;
- eventos;
- lembretes.

Calendário não confirma:

- participação;
- execução;
- resultado;
- interesse.

# 2630. Localização

Localização poderá apoiar:

- distância;
- modalidade;
- disponibilidade regional;
- deslocamento;
- acessibilidade;
- risco local.

A integração deverá utilizar precisão mínima necessária.

# 2631. Esportes e atividade física

Integrações esportivas poderão fornecer:

- atividade objetiva;
- evento;
- inscrição;
- local;
- grupo;
- horário;
- distância;
- participação registrada.

Atividade não deverá confirmar:

- saúde;
- disciplina;
- progresso;
- identidade;
- transformação.

# 2632. Organizações sociais e voluntariado

Integrações sociais poderão fornecer:

- ações;
- causas;
- vagas;
- competências necessárias;
- local;
- período;
- riscos;
- responsabilidades;
- apoio oferecido.

# 2633. Pontos e recompensas sociais

Pontos ou recompensas deverão:

- permanecer transparentes;
- não medir bondade;
- não criar ranking moral;
- não substituir a causa;
- não pressionar participação;
- não ocultar patrocinador;
- não transformar voluntariado em obrigação.

# 2634. Comunidades religiosas

Integrações religiosas deverão preservar:

- liberdade de crença;
- privacidade;
- pluralidade;
- não discriminação;
- liberdade de recusa;
- transparência institucional;
- ausência de exploração da fé.

# 2635. Limites religiosos

Participação não deverá ser utilizada para medir:

- fé;
- espiritualidade;
- proximidade com Deus;
- valor moral;
- comprometimento religioso pessoal.

# 2636. Serviços jurídicos

Integrações jurídicas deverão:

- identificar autoridade;
- apresentar jurisdição;
- distinguir informação de orientação profissional;
- proteger conteúdo;
- limitar retenção;
- evitar promessa de resultado.

# 2637. Fontes públicas

Fontes públicas poderão fornecer:

- editais;
- benefícios;
- programas;
- eventos;
- dados institucionais;
- registros oficiais;
- requisitos;
- prazos.

# 2638. Limites de informação pública

Informação pública não representa:

- finalidade irrestrita;
- reutilização ilimitada;
- ausência de sensibilidade;
- autorização para perfil pessoal;
- permissão publicitária.

# 2639. Integrações pessoais

O participante poderá conectar:

- calendário;
- planilhas;
- listas;
- aplicativos;
- arquivos;
- contas;
- fontes próprias.

A integração deverá permitir selecionar:

- campos;
- finalidade;
- frequência;
- consumidores;
- período;
- retenção;
- notificações.

# 2640. Integrações temporárias

Uma integração temporária deverá possuir:

- início;
- finalidade;
- expiração;
- escopo;
- campos;
- consumidor;
- condição de encerramento;
- tratamento do histórico.

# 2641. Expiração automática

Após a expiração:

- novos acessos deverão cessar;
- sincronizações deverão parar;
- recortes deverão ser recompostos;
- consumidores deverão ser notificados;
- histórico legítimo poderá permanecer.

# 2642. Informações de terceiros

Informações sobre terceiros deverão ser:

- minimizadas;
- vinculadas à finalidade;
- protegidas;
- não reutilizadas;
- não transformadas em perfil independente;
- removíveis quando possível.

# 2643. Oportunidades compartilhadas

Uma oportunidade compartilhada deverá distinguir:

- oportunidade global;
- relações individuais;
- permissões;
- responsabilidades;
- estado coletivo;
- estado de cada participante;
- conteúdo público;
- conteúdo privado.

# 2644. Confirmações individuais

Interesse, inscrição, compartilhamento ou responsabilidade deverão ser confirmados individualmente ou por papel autorizado.

Silêncio não representa aceitação.

# 2645. Canais conversacionais

Canais conversacionais poderão permitir:

- busca;
- comparação;
- explicação;
- salvamento;
- descarte;
- interesse;
- contestação;
- limitação;
- revogação.

Comandos ambíguos deverão exigir esclarecimento proporcional.

# 2646. Notificações

Integrações de notificação deverão preservar:

- finalidade;
- sensibilidade;
- canal;
- frequência;
- preferência;
- relação comercial;
- possibilidade de silêncio;
- rastreabilidade.

# 2647. Busca integrada

A busca poderá consultar múltiplas fontes, desde que:

- a origem permaneça visível;
- resultados patrocinados sejam separados;
- contexto sensível não seja redistribuído;
- critérios sejam explicáveis;
- deduplicação preserve diferenças materiais.

# 2648. Processos externos

Processos externos poderão incluir:

- inscrição;
- análise;
- contratação;
- pagamento;
- reserva;
- agendamento;
- entrega;
- atendimento;
- participação;
- cancelamento;
- reembolso.

Cada processo deverá permanecer sob autoridade do responsável.

# 2649. Retorno de processo externo

O retorno deverá distinguir:

- fato confirmado;
- estado estimado;
- falha;
- pendência;
- cancelamento;
- protocolo;
- fonte;
- temporalidade.

# 2650. Falha externa

Quando um sistema externo falhar:

- o último estado válido deverá ser preservado;
- o processo deverá ser marcado como pendente;
- repetição deverá utilizar idempotência;
- falsa confirmação deverá ser impedida;
- o participante deverá ser informado quando material.

# 2651. Conflitos entre fontes

Conflitos poderão envolver:

- disponibilidade;
- preço;
- elegibilidade;
- prazo;
- localização;
- fornecedor;
- risco;
- política;
- relação comercial.

# 2652. Tratamento de conflitos

O tratamento deverá considerar:

- autoridade;
- temporalidade;
- proveniência;
- evidências;
- versão;
- finalidade;
- confiança;
- impacto.

Não deverá existir hierarquia absoluta universal.

# 2653. Correções externas

Uma correção externa deverá:

- preservar o valor anterior;
- registrar o valor corrigido;
- identificar fonte;
- registrar momento;
- reavaliar consumidores;
- produzir eventos compensatórios;
- evitar reescrita silenciosa.

# 2654. Eventos retroativos

Eventos retroativos deverão distinguir:

- tempo real do fato;
- tempo do conhecimento;
- tempo da integração;
- tempo da aplicação;
- efeitos reconstruíveis;
- efeitos irreversíveis.

# 2655. Reconstrução

A integração deverá permitir reconstruir:

```text
fonte
→ autorização
→ dado original
→ transformação
→ admissão
→ avaliação
→ evento
→ recorte
→ consumidor
→ processamento
→ correção, falha ou revogação
```

# 2656. Eventos funcionais das integrações

Deverão ser previstos, entre outros:

- `IntegracaoDeOportunidadesSolicitada`;
- `IntegracaoDeOportunidadesAutorizada`;
- `IntegracaoDeOportunidadesAtivada`;
- `IntegracaoDeOportunidadesPausada`;
- `IntegracaoDeOportunidadesRetomada`;
- `IntegracaoDeOportunidadesRevogada`;
- `IntegracaoDeOportunidadesEncerrada`;
- `FonteExternaDeOportunidadeAssociada`;
- `AssociacaoDeFonteExternaContestada`;
- `AutoridadeDeFonteExternaValidada`;
- `RecorteDeContextoParaOportunidadesRecebido`;
- `SinalExternoDeOportunidadeRecebido`;
- `FatoExternoDeOportunidadeRecebido`;
- `PropostaExternaDeOportunidadeRecebida`;
- `ComandoExternoDeOportunidadeRecebido`;
- `DisponibilidadeExternaSincronizada`;
- `ElegibilidadeExternaSincronizada`;
- `PrecoExternoSincronizado`;
- `RiscoExternoSincronizado`;
- `RelacaoComercialExternaSincronizada`;
- `ConflitoEntreFontesDeOportunidadeIdentificado`;
- `CorrecaoExternaDeOportunidadeRecebida`;
- `EventoRetroativoDeOportunidadeRecebido`;
- `RecorteDeOportunidadeProduzidoParaConsumidor`;
- `RecorteDeOportunidadePropagado`;
- `ProcessamentoDeRecorteDeOportunidadeConfirmado`;
- `PropagacaoDeRecorteDeOportunidadeFalhou`;
- `SincronizacaoDeOportunidadePendente`;
- `SincronizacaoDeOportunidadeRecuperada`;
- `DuplicidadeDeIntegracaoDeOportunidadeIgnorada`;
- `RevogacaoDeIntegracaoEmPropagacao`;
- `RevogacaoDeIntegracaoPropagada`;
- `EstadoIntegradoDeOportunidadeReconstruido`.

# 2657. Métricas iniciais

As métricas poderão avaliar:

- integrações sem finalidade;
- fontes sem autoridade;
- associações incorretas;
- payloads excessivos;
- campos sensíveis desnecessários;
- sincronizações atrasadas;
- conflitos entre fontes;
- duplicidades;
- eventos fora de ordem;
- falhas parciais;
- recortes rejeitados;
- revogações incompletas;
- consumidores divergentes;
- relações comerciais ausentes;
- transformações não explicáveis;
- atualizações materiais não propagadas;
- tempo de recuperação;
- integrações temporárias não expiradas;
- publicidade confundida com oportunidade;
- exposição indevida de terceiros.

As métricas deverão avaliar o sistema, não o participante.

# 2658. Observabilidade

A observabilidade deverá permitir acompanhar:

- estado das integrações;
- latência;
- falhas;
- versões;
- conflitos;
- revogações;
- reprocessamentos;
- consumidores;
- volume de recortes;
- incidentes de autoridade;
- incidentes comerciais;
- incidentes de sensibilidade.

# 2659. Explicabilidade

O participante deverá poder compreender:

- quais fontes estão conectadas;
- quais dados são acessados;
- para qual finalidade;
- com qual frequência;
- quais transformações ocorrem;
- quais oportunidades dependem da fonte;
- quais consumidores recebem recortes;
- quais relações comerciais existem;
- como pausar;
- como revogar.

# 2660. Auditoria

A auditoria deverá reconstruir:

- identidade;
- associação;
- autorização;
- finalidade;
- autoridade;
- dado original;
- transformação;
- temporalidade;
- avaliação;
- decisão;
- evento;
- recorte;
- consumidor;
- processamento;
- correção;
- revogação;
- falha.

# 2661. Responsabilidades do produtor

O produtor deverá:

1. fornecer identidade;
2. declarar autoridade;
3. informar finalidade;
4. limitar escopo;
5. preservar proveniência;
6. indicar temporalidade;
7. declarar limitações;
8. declarar relações comerciais;
9. usar contrato vigente;
10. aplicar idempotência;
11. corrigir informações;
12. respeitar revogações;
13. proteger dados sensíveis;
14. informar falhas;
15. permitir auditoria.

# 2662. Responsabilidades do consumidor

O consumidor deverá:

1. validar contrato;
2. validar autoridade;
3. respeitar finalidade;
4. minimizar armazenamento;
5. respeitar permissões;
6. controlar versão;
7. aplicar idempotência;
8. tratar ordenação;
9. governar sua própria decisão;
10. não ampliar significado;
11. não fabricar causalidade;
12. tratar correções;
13. propagar revogações;
14. informar falhas;
15. permitir auditoria.

# 2663. Integrações proibidas

Não deverão existir integrações que:

1. transfiram titularidade;
2. ampliem autoridade;
3. utilizem finalidade genérica;
4. forneçam a jornada integral a organizações;
5. alimentem publicidade com contexto sensível;
6. fabriquem disponibilidade;
7. fabriquem elegibilidade;
8. fabriquem interesse;
9. fabriquem progresso;
10. fabriquem transformação;
11. ocultem patrocínio;
12. ocultem comissão;
13. priorizem por receita;
14. utilizem vulnerabilidade;
15. criem vigilância excessiva;
16. formem perfis independentes de terceiros;
17. dupliquem efeitos;
18. ignorem ordenação;
19. encerrem revogação sem propagação;
20. apresentem falha parcial como sucesso.

# 2664. Critérios de aceite

A extensão será considerada consolidada quando:

1. definir finalidade e princípios;
2. definir tipos e modos;
3. estabelecer contrato funcional comum;
4. estabelecer requisitos de admissão;
5. governar identidade e associação;
6. limitar autoridade;
7. preservar proveniência;
8. separar qualidade, confiança e autoridade;
9. governar temporalidades;
10. governar transformações;
11. governar sincronização;
12. prevenir ciclos;
13. aplicar finalidade e minimização;
14. governar permissões;
15. governar pausa, desconexão e revogação;
16. garantir propagação;
17. definir retenção;
18. operar com falha segura;
19. integrar Captura de Contexto;
20. integrar Contexto Vivo;
21. integrar Objetivos;
22. integrar Eventos de Vida;
23. integrar Próximos Passos;
24. integrar Intervenções Contextuais;
25. integrar Experiências;
26. integrar Evolução Contínua;
27. limitar Guivos Intelligence;
28. limitar Platform Layer;
29. integrar produtos especializados;
30. governar organizações e fornecedores;
31. governar serviços profissionais;
32. proteger integrações sensíveis;
33. governar fontes públicas;
34. governar integrações pessoais e temporárias;
35. proteger terceiros;
36. governar canais, busca e notificações;
37. tratar conflitos e correções;
38. definir eventos funcionais;
39. definir métricas e observabilidade;
40. preservar explicabilidade e auditoria;
41. definir responsabilidades;
42. manter o participante no controle.

# 2665. Regras fundamentais

1. Integração não representa decisão.
2. Disponibilidade técnica não representa autorização.
3. Fonte somente confirma fatos dentro de sua autoridade.
4. Titularidade não é transferida.
5. Finalidade precede acesso.
6. Minimização precede compartilhamento.
7. Qualidade técnica não representa autoridade.
8. Confiança não representa certeza.
9. Informação externa não representa relevância automática.
10. Catálogo não representa oportunidade ativa.
11. Publicidade não representa relevância funcional.
12. Compra não representa progresso.
13. Inscrição não representa aceitação.
14. Aceitação não representa participação.
15. Participação não representa transformação.
16. Calendário não representa execução.
17. Localização não representa ação.
18. Atividade não representa evolução.
19. Interesse não pode ser inferido por visualização.
20. Organização não recebe a jornada integral.
21. Contexto sensível não alimenta publicidade.
22. Comissão não altera relevância.
23. Patrocínio não altera prioridade.
24. Alternativas não patrocinadas não podem ser ocultadas.
25. Transformações não fabricam precisão.
26. Transformações não fabricam causalidade.
27. Integrações não criam objetivos.
28. Integrações não criam Próximos Passos confirmados.
29. Capacidades consumidoras governam suas decisões.
30. Platform Layer não redefine semântica.
31. Guivos Intelligence sugere e explica, mas não decide.
32. Produtos especializados governam transações e entregas.
33. Informação pública não representa uso irrestrito.
34. Dados de terceiros não formam perfis paralelos.
35. Integrações temporárias devem expirar.
36. Pausa interrompe novas coletas.
37. Revogação interrompe novos usos.
38. Revogação somente termina após propagação.
39. Reprocessamento não duplica efeitos.
40. Eventos fora de ordem não criam estados impossíveis.
41. Conflitos não são resolvidos silenciosamente.
42. Falha preserva o último estado válido.
43. Falha parcial não representa sucesso integral.
44. Métricas avaliam o sistema.
45. O participante permanece no controle.

# 2666. Continuidade normativa

`PAS-001-OA-INTEGRATION-001 1.0.0` deverá ser registrado como a **quinta extensão normativa da Capacidade 06 — Oportunidades Ativas**.

A extensão deverá:

- preservar fundamentos, ciclo de vida, visualização e contratos dos eventos;
- preservar o `PAS-001 0.5.0`;
- manter as Capacidades 02, 03, 04 e 05 como `Functionally complete`;
- manter a Capacidade 06 como `In progress`;
- elevar o progresso editorial de referência de `80%` para `90%`;
- consolidar integrações internas, externas, organizacionais, profissionais e comerciais;
- preservar finalidade, minimização, autoridade e proveniência;
- consolidar sincronização, idempotência, ordenação e prevenção de ciclos;
- governar pausa, desconexão, revogação e propagação;
- preservar neutralidade comercial;
- estabelecer KPIs, guardrails, baseline, cenários e contrato final como próxima etapa.

O bloco seguinte será:

> **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão e contrato final da Capacidade de Oportunidades Ativas.**
