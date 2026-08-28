---
id: RP-002-PILOT-FINAL-LEGAL-PRIVACY-REVIEW-001
title: Piloto — Checklist A12 de Revisão Jurídica e Privacidade Final
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: review_checklist_ready_not_executed
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-NOTICE-CONSENT-FLOW-DEC-001
  - RP-002-PILOT-RETENTION-DEC-001
  - RP-002-PILOT-NOTICE-CONSENT-002
  - RP-002-PILOT-OPS-REG-001
---

# Piloto — Checklist A12 de Revisão Jurídica e Privacidade Final

## 1. Finalidade

Este documento define o checklist que deverá ser aplicado antes da liberação do primeiro participante real do `RP-002`.

Ele não constitui parecer jurídico e não declara conformidade por si só.

```text
A12 CHECKLIST
→ DOCUMENTED

A12 REVIEW EXECUTION
→ NOT COMPLETED

A12 OPERATIONAL STATUS
→ HOLD
```

## 2. Regra de aprovação

A12 somente poderá passar quando a revisão comparar **documentação + configuração real + evidência dos testes**.

```text
DOCUMENTATION ONLY
→ INSUFFICIENT FOR A12 PASS

CONFIGURATION ONLY
→ INSUFFICIENT FOR A12 PASS

DOCUMENTATION + REAL STACK + TEST EVIDENCE + REVIEW
→ REQUIRED
```

## 3. Controlador e responsabilidade

Verificar:

- [ ] controlador identificado corretamente como Guivos Ltda;
- [ ] dados societários/cadastrais do Notice conferidos;
- [ ] Pilot Owner funcional definido;
- [ ] Data Steward definido quando aplicável;
- [ ] canais de privacidade operacionais;
- [ ] canal de Research segregado funcionalmente.

## 4. Finalidades

Verificar:

- [ ] todas as finalidades estão específicas e compatíveis com o Dry Run;
- [ ] não existe finalidade genérica de “melhorar produtos” sem delimitação;
- [ ] marketing, Ads, prospecção e newsletter permanecem fora do consentimento;
- [ ] follow-up está delimitado ao ciclo;
- [ ] dados coletados são necessários às finalidades.

## 5. Categorias de dados

Verificar:

- [ ] dados operacionais mínimos estão definidos;
- [ ] Research Base permanece pseudonimizada;
- [ ] Linkage Key contém somente ligação mínima;
- [ ] CPF/RG/documentos não são coletados por padrão;
- [ ] áudio e vídeo permanecem `OFF`;
- [ ] transcrição bruta identificável não é criada por padrão;
- [ ] dado sensível não é requisito normal do Dry Run.

## 6. Base legal

Verificar:

- [ ] matriz de base legal está consistente com as operações reais;
- [ ] consentimento é específico, informado e inequívoco para o núcleo voluntário quando utilizado;
- [ ] silêncio/omissão não é tratado como consentimento;
- [ ] revogação é gratuita e facilitada;
- [ ] operações auxiliares não usam consentimento como base universal por conveniência;
- [ ] qualquer conservação excepcional possui fundamento aplicável e necessidade demonstrável.

## 7. Notice e consentimento

Verificar:

- [ ] A11 corresponde ao stack real;
- [ ] versão exata do Notice é identificável;
- [ ] a Pessoa recebe o Notice antes do episódio;
- [ ] existe oportunidade de esclarecimento;
- [ ] manifestação afirmativa está registrada;
- [ ] prova mínima não exige cópia excessiva da conversa;
- [ ] retirada/revogação foi testada sinteticamente;
- [ ] nenhum campo `TBD` permanece na versão de uso.

## 8. Direitos do titular

Verificar:

- [ ] canais `privacidade@guivos.com` e `privacy@guivos.com` estão operacionais;
- [ ] P2C continua válido para o fluxo real;
- [ ] acesso, correção, eliminação e revogação são executáveis no stack;
- [ ] A7 demonstra correção/deletion drill no stack-alvo;
- [ ] respostas e registros são proporcionais;
- [ ] backups não reintroduzem dados excluídos deliberadamente.

## 9. Retenção

Verificar A10:

- [ ] 30 dias para candidato não admitido continua proporcional;
- [ ] 90 dias para Identity Vault continua necessário;
- [ ] Linkage Key não excede o Identity Vault e pode ser removida antes;
- [ ] 12 meses para Research Base pseudonimizada continua justificado;
- [ ] 24 meses para prova mínima de Notice/consentimento continua justificado;
- [ ] 24 meses para registro mínimo de direitos continua justificado;
- [ ] logs de 90 dias são suficientes e não excessivos;
- [ ] residual de backup de até 30 dias é tecnicamente executável;
- [ ] dado sensível incidental desnecessário é removido rapidamente;
- [ ] Notice reflete os prazos aprovados.

Se qualquer prazo for alterado, atualizar A10 e A11 antes da liberação.

## 10. Identity Vault — A3

Verificar:

- [ ] implementação corresponde ao target aprovado ou mudança foi versionada;
- [ ] criptografia em repouso está ativa;
- [ ] localização não sincronizada foi verificada;
- [ ] permissões reais são mínimas;
- [ ] auto-mount/password cache/session controls estão coerentes;
- [ ] teste sintético passou;
- [ ] nenhum segredo entrou no GKR.

## 11. Research Base — A4

Verificar:

- [ ] boundary separado do Identity Vault;
- [ ] pseudônimo é usado por padrão;
- [ ] não há identidade direta no schema normal;
- [ ] conteúdo é proporcional ao episódio;
- [ ] acessos por função estão coerentes;
- [ ] exportação/correção/exclusão são possíveis;
- [ ] teste sintético passou.

## 12. Linkage Key — A5

Verificar:

- [ ] boundary separado;
- [ ] schema é mínimo;
- [ ] acesso é mais restrito do que Research Base;
- [ ] não existe cópia na Research Base;
- [ ] IA/Search nunca recebem a chave;
- [ ] teste sintético passou.

## 13. Backup e recovery — A6

Verificar:

- [ ] backups estão criptografados;
- [ ] meio/boundary é separado do primário;
- [ ] identidade, linkage e Research continuam separados;
- [ ] restore sintético passou;
- [ ] exclusões conhecidas são reaplicadas após restore;
- [ ] residual window está dentro de A10;
- [ ] segredos não estão armazenados junto do payload.

## 14. Correction / deletion drill — A7

Verificar:

- [ ] drill foi executado sobre stack real com dados sintéticos;
- [ ] correção propagou de forma consistente;
- [ ] exclusão atingiu primário;
- [ ] Linkage Key foi tratada corretamente;
- [ ] backup/recovery foi considerado;
- [ ] não houve residual deliberado fora do boundary.

## 15. OpenAI API — A8

Verificar:

- [ ] projeto dedicado ao `RP-002` existe;
- [ ] produto utilizado é API empresarial/developer, não conta consumer usada ad hoc;
- [ ] data sharing voluntário está desabilitado;
- [ ] estado real de ZDR/MAM está documentado sem presunção;
- [ ] endpoint/capability selecionado não cria persistência desnecessária;
- [ ] `store`/application state está configurado conforme target;
- [ ] nenhuma API key está em GKR ou artefato de participante;
- [ ] DPA/termos aplicáveis à conta foram verificados;
- [ ] transferência internacional foi avaliada;
- [ ] entrada sintética sem identificador direto foi testada;
- [ ] human-in-the-loop está mantido.

## 16. Search / Web — A9

Verificar:

- [ ] queries são minimizadas;
- [ ] identidade direta não é enviada por padrão;
- [ ] método/operador real corresponde ao documentado;
- [ ] fonte primária é aberta para fatos materiais quando disponível;
- [ ] freshness é registrada;
- [ ] nenhum formulário/transação é executado em nome da Pessoa sem fluxo específico;
- [ ] resultado patrocinado não recebe privilégio metodológico;
- [ ] teste sintético passou.

## 17. Operadores e contratos

Verificar o registry:

- [ ] Hostinger Mail registrado para escopo real;
- [ ] OpenAI API/Web Search registrado para escopo real;
- [ ] qualquer operador adicional foi incluído antes de uso;
- [ ] categorias de dados por operador estão claras;
- [ ] DPA/contrato aplicável foi verificado;
- [ ] subprocessadores/transferências relevantes foram avaliados;
- [ ] nenhuma ferramenta disponível tecnicamente foi promovida por conveniência.

## 18. Transferência internacional

Verificar, à luz da LGPD e regulamentação ANPD aplicável:

- [ ] quais fluxos implicam transferência/processamento internacional;
- [ ] qual mecanismo/salvaguarda se aplica a cada operador quando exigido;
- [ ] o Notice informa o tema de maneira proporcional;
- [ ] contratos/DPA relevantes são compatíveis com a decisão;
- [ ] não há afirmação falsa de residência brasileira exclusiva.

Referências oficiais:

- LGPD: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>
- Resolução CD/ANPD nº 19/2024: <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024>

## 19. Segurança e minimização

Verificar:

- [ ] mínimo privilégio;
- [ ] MFA/controles de conta quando disponíveis e aplicáveis;
- [ ] nenhuma senha/token/secret em GKR;
- [ ] ausência de cloud sync não aprovado;
- [ ] dados temporários são minimizados;
- [ ] aplicações não criam cópias plaintext persistentes fora do boundary;
- [ ] incidente de segurança tem caminho de escalonamento e avaliação conforme obrigações aplicáveis.

## 20. Decisão automatizada

Verificar:

- [ ] nenhuma decisão relevante sobre a Pessoa é tomada unicamente pela IA;
- [ ] recomendação/opção é revisada por humano;
- [ ] benchmark e gates não são substituídos por output opaco;
- [ ] Safety Gate prevalece em domínio de maior risco.

## 21. Research ethics / experiência

Verificar:

- [ ] participação voluntária é real;
- [ ] recusa não gera penalidade;
- [ ] o piloto não cria expectativa indevida de resultado;
- [ ] oportunidade não é apresentada como promessa;
- [ ] patrocinado/comercial não é ocultado;
- [ ] follow-up não se transforma em contato indefinido.

## 22. GKR e publicação

Verificar:

- [ ] nenhum dado individual real foi publicado;
- [ ] nenhum mailbox resource ID interno foi publicado;
- [ ] nenhum segredo foi publicado;
- [ ] conhecimento que retorna ao GKR é desidentificado/agregado;
- [ ] contraexemplos não permitem reidentificação razoável.

## 23. Critério de resultado A12

Resultado permitido:

```text
PASS
→ all critical items satisfied with evidence

REVISE
→ correctable material gaps remain

STOP
→ risk or legal/privacy incompatibility blocks real pilot
```

Nenhum `PASS` deve ser inferido por ausência de comentário.

## 24. Efeito sobre gates superiores

Somente depois da execução de A12:

```text
P3-C
→ may be reevaluated

P3-D
→ may be reevaluated

P4
→ may be reevaluated

PARTICIPANT 001
→ may be considered for explicit release
```

A12 `PASS` não libera automaticamente Participant 001; ainda é necessária decisão explícita de release.

## 25. Estado final

```text
A12 DOCUMENTATION
→ CHECKLIST CLOSED

A12 REVIEW
→ NOT EXECUTED

A12 OPERATIONAL STATUS
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
