---
id: GKR-UX-PER013-MASTER-001
title: Jornada da Pessoa — PER-013 — Captura e Revisão de Arquivo — Documento Mestre de Superfície
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-JOURNEY-PERSON-FUNCTIONAL-COMPLETENESS-001
  - GKR-SURF-PER-003
  - GKR-SURF-PER-005
  - GKR-DATA-PRIVACY-CONSENT-001
related:
  - GKR-TRN-014
  - GKR-TRN-015
  - GKR-SURF-PER-006
---

# Jornada da Pessoa — PER-013 — Captura e Revisão de Arquivo — Documento Mestre de Superfície

## 1. Propósito

Este documento governa a responsabilidade funcional corrente de **capturar e revisar Arquivo** depois que a Pessoa escolhe conscientemente essa modalidade em `PER-003` e antes do inventário/autorização de `PER-005`.

Ele não define layout, tela final, file picker específico, storage, provedor, formatos concretos, limites numéricos, mecanismo de segurança, OCR, extração técnica ou implementação.

```text
PER-003 / ARQUIVO
→ TRN-014
→ PER-013 — CAPTURA E REVISÃO DE ARQUIVO
→ TRN-015
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
```

`PER-004` permanece exclusivamente responsável por Texto/Voz. `TRN-003` não é reutilizada para Arquivo.

## 2. Job da Pessoa

A Pessoa precisa conseguir:

> selecionar conscientemente um arquivo, compreender sua finalidade imediata, acompanhar sua captura quando material, revisar o que foi recebido, corrigir/remover/substituir e somente então entregar conteúdo revisado ao inventário — sem que upload seja confundido com autorização de processamento.

## 3. Fronteiras semânticas

```text
ESCOLHER ARQUIVO
≠ ABRIR SELETOR
≠ UPLOAD

UPLOAD
≠ AUTORIZAÇÃO DE PROCESSAMENTO

ARQUIVO RECEBIDO
≠ EXTRAÇÃO IRRESTRITA

EXTRAÇÃO
≠ FATO DECLARADO PELA PESSOA

TRN-015 → PER-005
≠ AUTORIZAÇÃO MATERIAL
```

A autorização específica continua pertencendo a `PER-005`.

## 4. Origem e disponibilidade

A origem canônica é `PER-003`, após seleção explícita de Arquivo.

`TRN-014` deve preservar:
- modalidade escolhida;
- ausência de upload automático;
- ausência de autorização material;
- possibilidade de voltar ou interromper;
- nenhuma inferência de finalidade adicional.

Combinar Arquivo com outra modalidade não transfere permissões ou autorizações entre modalidades.

## 5. Finalidade antes da captura

Antes da captura material, a Pessoa deve compreender em nível proporcional:
- para que o arquivo será usado no fluxo corrente;
- que selecionar o arquivo exige ação consciente;
- que conteúdo de terceiros exige proteção;
- que disponibilidade técnica não autoriza uso irrestrito;
- que eventuais extrações permanecem distinguíveis de conteúdo de origem;
- que revisão antecede autorização material.

Formatos, tamanhos, quantidades e limites só podem ser apresentados quando houver autoridade técnica real.

## 6. Estados funcionais

A responsabilidade deve acomodar, quando aplicável:

1. pronto para selecionar;
2. seletor solicitado conscientemente;
3. arquivo selecionado localmente, ainda não enviado;
4. captura/upload em preparação;
5. captura/upload em andamento;
6. captura concluída;
7. arquivo recebido e identificável;
8. revisão necessária;
9. pronto para substituir;
10. pronto para remover;
11. múltiplos arquivos, quando legitimamente suportados;
12. cancelado antes da conclusão;
13. interrompido;
14. falha recuperável;
15. arquivo indisponível, ilegível ou incompatível quando tecnicamente comprovado;
16. conteúdo revisado pronto para `PER-005`.

Nenhum estado visual específico é imposto.

## 7. Ações e controles

Conforme aplicável, a Pessoa deve poder:
- selecionar arquivo;
- confirmar a captura quando uma confirmação separada for necessária;
- cancelar antes ou durante operação interrompível;
- revisar identificação e conteúdo recebido em nível apropriado;
- substituir;
- remover;
- adicionar outro quando a capacidade existir;
- voltar;
- interromper;
- tentar novamente após falha recuperável;
- concluir a revisão e seguir ao inventário.

Nenhuma ação deve iniciar processamento material de compreensão.

## 8. Revisão do conteúdo recebido

A revisão deve permitir distinguir:
- arquivo/fonte de origem;
- metadados necessários e legítimos;
- conteúdo extraído, quando existir;
- transformação/derivação, quando existir;
- item removido ou substituído.

Uma extração não pode ser apresentada como declaração direta da Pessoa.

Quando a natureza do arquivo impedir revisão integral útil, a experiência deve fornecer representação proporcional suficiente para a Pessoa reconhecer a fonte e controlar sua inclusão, sem fingir compreensão inexistente.

## 9. Remoção, substituição e combinação

Remover ou substituir deve produzir consequência compreensível.

```text
REMOVER DO FLUXO ATUAL
≠ PROVA DE ELIMINAÇÃO TÉCNICA TOTAL

SUBSTITUIR
→ NOVA FONTE
→ NOVA REVISÃO APLICÁVEL
```

Nenhum derivado pode permanecer silenciosamente elegível quando sua fonte deixa de possuir fundamento para o uso corrente.

## 10. Falha e recuperação

Devem ser tratadas sem simular sucesso:
- falha ao abrir/selecionar;
- formato não suportado, somente quando tecnicamente definido;
- limite excedido, somente quando tecnicamente definido;
- interrupção de transferência;
- falha de upload;
- arquivo corrompido/ilegível quando comprovável;
- perda de conexão;
- duplicação acidental;
- falha ao remover/substituir;
- estado indeterminado.

Recuperação deve preservar idempotência quando material e não pode duplicar arquivo silenciosamente.

Falha não autoriza coletar mais dados nem trocar automaticamente de modalidade.

## 11. Dados, privacidade e terceiros

A captura deve obedecer minimização e finalidade.

A presença de informação de terceiro:
- não transfere autoridade sobre essa pessoa;
- não autoriza compartilhamento adicional;
- não autoriza inferência sensível;
- exige proteção proporcional.

Dados sensíveis não se tornam autorizados apenas por estarem dentro de um arquivo.

Storage, retenção, descarte técnico e bases jurídicas concretas permanecem dependentes da governança de tratamento aplicável e da implementação futura.

## 12. Handoff para PER-005

`TRN-015` entrega somente um conjunto revisado de conteúdo de origem e representações legitimamente produzidas.

O handoff deve preservar:
- origem;
- identificação da fonte;
- distinção origem/derivado;
- remoções/limitações;
- ausência de autorização material;
- contexto necessário para revisão posterior.

`PER-005` continua responsável por inventário compreensível e autorização específica.

## 13. Retorno e interrupção

Antes da captura, retornar a `PER-003` não deve produzir conteúdo material.

Depois de existir conteúdo, voltar/interromper deve explicar o efeito sobre:
- captura em curso;
- arquivo recebido;
- substituições;
- itens removidos;
- eventual estado técnico temporário.

Não pode haver descarte silencioso.

## 14. Acessibilidade e linguagem

A experiência deve:
- funcionar sem depender exclusivamente de drag-and-drop;
- oferecer mecanismo operável por teclado quando aplicável;
- tornar estado/progresso perceptível por tecnologia assistiva;
- não depender apenas de cor;
- identificar erros junto ao item afetado;
- usar linguagem compreensível para limites e falhas;
- permitir tempo suficiente e recuperação quando houver operação temporizada.

## 15. Liberdade de Design

Este Master governa significado, estados, controles, consequências e limites.

Design permanece livre para decidir composição, hierarquia, tipografia, iconografia, componentes, responsividade e motion dentro das autoridades de marca e acessibilidade.

Não existe baseline visual obrigatório criado por este documento.

## 16. IA

IA pode apoiar exploração e compreensão somente dentro da finalidade e autoridade aplicáveis.

IA não pode:
- abrir/enviar arquivo sem ação consciente;
- presumir autorização de processamento;
- transformar extração em fato declarado;
- inventar formatos/limites;
- inferir dado sensível por mera disponibilidade;
- ampliar finalidade;
- ocultar falha;
- promover maturidade de transições sem evidência.

## 17. Critérios de aceitação documental

A responsabilidade é documentalmente coerente quando:
1. Arquivo continua opção em paridade em `PER-003`;
2. selecionar Arquivo não faz upload;
3. captura exige ação consciente;
4. finalidade é compreensível antes da captura material;
5. origem e derivados permanecem distinguíveis;
6. remoção/substituição têm consequência compreensível;
7. falhas e recuperação estão previstas;
8. upload não equivale a autorização;
9. `PER-005` permanece gate de autorização;
10. `PER-006` permanece processamento posterior;
11. informações de terceiros e dados sensíveis não recebem autoridade automática;
12. acessibilidade é preservada;
13. nenhuma implementação ou baseline visual é declarada.

## 18. Lacunas que permanecem abertas

Este documento não define:
- formatos suportados;
- limites de tamanho/quantidade;
- storage;
- retenção;
- antivírus/malware scanning;
- OCR/parser;
- extração técnica;
- criptografia;
- infraestrutura;
- política jurídica aplicada a cada tratamento;
- implementação;
- evidência de produção.

Essas lacunas não invalidam o contrato funcional e não podem ser preenchidas por invenção.

## 19. Estado

```text
PER-013 FUNCTIONAL RESPONSIBILITY
→ ADJUDICATED / CURRENT

ORIGIN
→ PER-003 / ARQUIVO

INBOUND
→ TRN-014 / CONTRACTED / UNCHANGED

OUTBOUND
→ TRN-015 / CONTRACTED / UNCHANGED

DESTINATION
→ PER-005

PER-004
→ UNCHANGED

PER-005
→ AUTHORIZATION GATE PRESERVED

PER-006
→ UNCHANGED

VISUAL BASELINE
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```
