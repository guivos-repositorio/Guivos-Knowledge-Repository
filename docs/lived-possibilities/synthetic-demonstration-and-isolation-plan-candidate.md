---
id: GKR-LIVED-POSSIBILITIES-PRE-REPLIT-DEMONSTRATION-PLAN-CANDIDATE-001
title: Possibilidades Vividas — Plano Documental de Demonstração Sintética e Isolamento
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-23
normative: false
---

# Plano pré-Replit — RD-01, RD-02 e RD-03

Plano estritamente documental, sem execução, acesso ou autorização de Replit. Apoia a [auditoria consolidada](consolidated-readiness-audit-candidate.md) e o [G08](isolated-prototype-and-explicit-authorization-candidate.md). **Nenhum item deste documento cria D3**. Todo material é uma especificação de fixtures e testes a construir futuramente, não dados já carregados ou ensaios realizados.

## RD-01 — Catálogo rastreável de dados inteiramente sintéticos

### A. Objetos de oportunidade

| Fixture | Oportunidade sintética | Formato e objeto | Edição/etapa | CAPA e identidade |
|---|---|---|---|---|
| O-S01 | Oficina de Fotografia | Gratuita; presencial; ofertador Coletivo-S | E-S01; participação em oficina | CAPA-S01, ativo artificial |
| O-S02 | Conversa sobre Finanças | Gratuita; online; ofertador Profissional-S, somente papel de demonstração | E-S02; sessão síncrona | CAPA-S02, ativo artificial |
| O-S03 | Passeio Ciclístico | Paga; híbrida simulada; ofertador Organização-S | E-S03-A/E-S03-B, etapas distintas | CAPA-S03, ativo artificial |

Esses rótulos não designam eventos, empresas, pessoas ou perfis reais, nem selecionam cobertura real no UXA-057. Não utilizar fotografias de pessoas reais, imagens de obras identificáveis de terceiros, logos de organizações reais, links externos ou dados de serviços reais. CAPAs e avatares são especificações gráficas artificiais a criar *somente se houver D3*.

### B. Pessoas e avaliações

| Pessoa sintética | Vivência elegível no cenário | Relevância | Natureza | Expressões / função de teste |
|---|---|---|---|---|
| P-S01 | O-S01/E-S01 | Muito significativo | Positivamente | Me inspirou; Aprendi algo novo; compartilhar somente agregado após escolha afirmativa simulada |
| P-S02 | O-S01/E-S01 | Muito significativo | Negativamente | Me decepcionou; Me fez repensar; identificação autorizada somente na simulação após confirmação |
| P-S03 | O-S01/E-S01 | Moderadamente significativo | De forma positiva e negativa | Me motivou; Me senti desconfortável; sem foto pública |
| P-S04 | O-S01/E-S01 | Nada significativo | Não percebi impacto | Nenhuma expressão selecionada; contribuição privada sem projeção |
| P-S05 | O-S01/E-S01 | Ainda não sei dizer | Ainda não sei dizer | Sem expressão; contribuição coletiva autorizada simuladamente, sem identificação |
| P-S06 | O-S02/E-S02 | Pouco significativo | Positivamente | Descobri novas possibilidades; vínculo de perfil não autorizado |
| P-S07 | O-S02/E-S02 | Sem resposta | De forma positiva e negativa | Texto livre; eixo de relevância ausente |
| P-S08 | O-S03/E-S03-A | Extremamente significativo | Positivamente | Superei um desafio; etapa A, não implica vivência da B |
| P-S09 | O-S03/E-S03-B | Moderadamente significativo | Negativamente | Me senti excluído; edição/etapa distinta |
| P-S10 | Apenas inscrição em E-S03-B | — | — | Inelegível à avaliação de impacto da vivência posterior |

**Dados não equivalem a registros reais:** os IDs locais são somente fixtures de teste e não representam nomes, contas, presença comprovada ou perfis existentes. Os casos devem ser expandidos em versões e cenários de permissão antes dos testes, sem dados reais.

### C. Transições e invariantes sintéticos

- **F-S01:** P-S01 complementa a mesma avaliação meses depois; nova versão de R1 simulado, sem duplicar pessoa.
- **F-S02:** P-S02 retira autorização de identificação, mantendo apenas agregação permitida; retirar nome, avatar e arestas identificáveis.
- **F-S03:** P-S03 retira foto e acesso ao perfil; agregação ainda permitida permanece.
- **F-S04:** P-S05 retira autorização de agregação; revisar bases, agrupamentos e ausência de ressurreição.
- **F-S05:** O-S01 troca CAPA oficial simulada; avaliações, edições e histórico não mudam.
- **F-S06:** P-S01 expressa mais de um item da mesma família; união de pessoas distintas, nunca soma simples.
- **F-S07:** Envio duplicado e falha de rede; idempotência, sem sucesso falso.
- **F-S08:** Tentativa de publicação sem escolha válida; permanecer R1 privado.
- **F-S09:** Pequena base/cenário sensível artificial; estado de supressão demonstrativo, **sem fixar limiar jurídico/estatístico real**.
- **F-S10:** Perfil sintético torna-se privado; link contextual desabilitado.
- **F-S11:** Ofertador sintético contesta; simulação de R-C/R-D sem poderes de edição do registro.
- **F-S12:** Participação sem resposta, neutralidade, impacto misto, negativo e incerto não são colapsados.

Toda contagem de referência decorre de registros elegíveis e autorização efetivamente simulada em cada estado, nunca da quantidade nominal de linhas. Não predefinir que todas as pessoas da tabela integram um mesmo grafo público.

### D. Rastreabilidade

Cada caso futuro deverá identificar: fixture ID, oportunidade/edição/etapa, Pessoa sintética, evidência simulada e categoria, autorização por escopo e versão, R1 lógico/versão, eventual P1 simulado, manifestações, resultado esperado e qual cenário G02–G08 comprova. Não permitir P1 ou agregação sem estado válido. O plano documenta a estrutura; a **montagem do dataset executável** e sua verificação ocorreriam apenas após D3.

## RD-02 — Roteiro de avaliação visual e funcional futura

| Etapa de observação | Tarefa demonstrativa | Evidência prevista | Critério de aceite a observar |
|---|---|---|---|
| V-01 — Abertura | Abrir O-S01 | Captura/série de estados | CAPA e nós visíveis, fit-to-view, grid pontilhado |
| V-02 — Exploração | Selecionar famílias, expressões e arestas | Capturas antes/depois | Destaque sem apagar demais elementos, relações compreensíveis |
| V-03 — Painel | Selecionar nós rapidamente, fechar fora/Escape | Registro de interação | Janela única, estável, sem salto de scroll/zoom |
| V-04 — Contagens | Alternar P-S01 e P-S03, atualizar e retirar | Comparação de valores | União/interseção corretas, bases explícitas, sem duplicação |
| V-05 — Participantes | Observar diferentes identidades sintéticas e permissões | Comparação de visibilidade | Sem divulgar foto/nome/vínculo não autorizados |
| V-06 — Instrumento | Responder positivo, negativo, misto, neutro, incerto e omissão | Fluxo e resumo | Perguntas neutras, revisão livre, sem indução, eixo independente |
| V-07 — Compartilhamento | Testar três modalidades e ausência de ação | Registro de estado simulado | Primeira opção prioritária, **nenhuma autorização por silêncio** |
| V-08 — Continuidade | Revisar uma avaliação e retirar permissão | Histórico de versões sintético | Uma identidade lógica, projeção atualizada e não ressuscitável |
| V-09 — Acessibilidade | Testar teclado, foco, leitores de tela, zoom e movimento reduzido | Checklist e evidência reproduzível | Alternativa textual, foco estável, controles acessíveis |
| V-10 — Responsividade | Examinar desktop/tablet/mobile | Registros em larguras distintas | Janela e detalhes utilizáveis, gestos sem aprisionamento |
| V-11 — Falhas | Simular dados indisponíveis, base suprimida e rede lenta | Logs sintéticos e captura | Estados verdadeiros, sem vazamento ou sucesso falso |
| V-12 — Compartilhamento futuro | Inspecionar módulo central e pontos de uso planejados | Mapa de componentes candidato | Reutilização sem cópia de autoridade, sem integração real |

Registrar para cada observação: referência V-ID/G-ID, dispositivo e condição de teste, fixture, ação, expectativa, evidência, resultado, problema, gravidade, decisão de ajuste e impacto no GKR. **Nenhum resultado visual foi observado nesta etapa**. Alterações cosméticas poderão ser propostas durante o teste; alterações de significado, dados, privacidade ou autoridade retornam à decisão documental.

## RD-03 — Checklist de isolamento e pré-execução

O checklist é **um documento de critérios futuros**, não confirmação de que um ambiente Replit já está seguro ou foi inspecionado.

| Gate de isolamento | Condição documental | Verificação real (bloqueada até D3) |
|---|---|---|
| ISO-01 | Workspace/aplicação nova, distinta; nunca editar Replits já existentes | **Não realizada** |
| ISO-02 | Ausência de contas, APIs, autenticação e bancos de produção | **Não realizada** |
| ISO-03 | Dados/avatares/CAPAs exclusivamente sintéticos | **Não realizada** |
| ISO-04 | Nenhum webhook, notificação, integração com terceiros ou convite real | **Não realizada** |
| ISO-05 | Sem domínio, deploy ou visibilidade pública automática; configuração inspecionada antes de operar | **Não realizada** |
| ISO-06 | Acesso administrativo limitado e sem segredos/chaves reais | **Não realizada** |
| ISO-07 | Separação entre R1/P1 simulados e grafo derivado, sem autoridade real | **Não realizada** |
| ISO-08 | Modalidades simuladas, estado privado inicial e autorização afirmativa explícita quando exigida | **Não realizada** |
| ISO-09 | Nenhuma importação/exportação de dados reais, logs pessoais ou arquivos de usuários | **Não realizada** |
| ISO-10 | Nenhuma integração com Home Pessoa, Card Oportunidades, Perfil ou O/C nesta fase | **Não realizada** |
| ISO-11 | Critérios de pausa/reversão e limpeza de dados sintéticos estabelecidos antes de executar | **Não realizada** |
| ISO-12 | Escopo exato de D3, responsáveis, ambiente, limites e eventual custo apresentados à Direção | **Não realizada** |

**Condição obrigatória:** se uma verificação falhar, suspender qualquer ação correspondente e solicitar decisão sobre o risco/escopo. Não assumir que “não conectado” significa “não publicado”; inspecionar configurações concretas apenas quando houver D3. Não utilizar autorização de documentação para tentar verificar ou alterar Replit agora.

## RD-04 — Regra de privacidade preservada

A modalidade **“Compartilhar minha participação”** permanece em primeiro lugar e com prioridade visual. A preferência anterior de pré-seleção foi registrada no GKR, mas não produz autorização por inação. Em toda demonstração futura, **R1 começa privado**; publicação sintética exige ação afirmativa simulada válida, por finalidade e escopo. A simulação não é consentimento real, não comprova base jurídica e não torna aceitável opt-out para produção. A análise de proteção/consentimento real continua reservada à autoridade competente.

## 5. Resultado e limitações

RD-01: **inventário e transições especificados**; fixtures executáveis não criadas. RD-02: **roteiro e formulário de evidências definidos**; testes não executados. RD-03: **checklist estabelecido**; nenhuma verificação de ambiente foi realizada. RD-04: **restrição mantida**, não adjudicação jurídica final. RD-05: aceite da auditoria consolidada registrado na decisão humana subsequente.

Esta preparação atende ao objeto **documental** de RD-01 a RD-03, mas não atesta isolamento técnico efetivo, acessibilidade, resultados de cenários, privacidade jurídica ou maturidade operacional. O próximo passo será uma reconciliação de completude documental, com decisão humana específica sobre a prontidão de documentação do protótipo — sem liberar Replit automaticamente, sem alterar main ou promover canon.
