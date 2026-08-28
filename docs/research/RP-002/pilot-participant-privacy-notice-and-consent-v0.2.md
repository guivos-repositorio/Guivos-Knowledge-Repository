---
id: RP-002-PILOT-NOTICE-CONSENT-002
title: Piloto — Aviso ao Participante e Consentimento v0.2
status: draft
version: 0.2.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: final_documentary_target_pending_A12_and_operational_release
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-NOTICE-CONSENT-FLOW-DEC-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-RETENTION-DEC-001
  - RP-002-PILOT-OPS-REG-001
  - RP-002-PILOT-OPENAI-API-DEC-001
  - RP-002-PILOT-SEARCH-WEB-DEC-001
---

# Piloto — Aviso ao Participante e Consentimento v0.2

## 1. Status de uso

> **TARGET DOCUMENTAL — AINDA NÃO AUTORIZADO PARA PARTICIPANTE REAL.**

Esta versão reconcilia o Notice com a arquitetura documental atual do `RP-002`.

Ela somente poderá ser promovida para uso real após:

- revisão A12;
- implantação do stack;
- testes sintéticos aplicáveis;
- confirmação de que operadores, retenção e controles reais correspondem ao texto;
- liberação explícita de `Participant 001`.

## 2. Controlador

**Guivos Ltda**  
**CNPJ 43.530.598/0001-33**

Canais oficiais de privacidade:

- `privacidade@guivos.com` — português;
- `privacy@guivos.com` — internacional/inglês.

Canal operacional de Research:

- `research@guivos.com`.

## 3. O que é o Dry Run

A Guivos está realizando um experimento de Research para testar se consegue compreender um Momento real de uma Pessoa, identificar caminhos plausíveis, encontrar oportunidades concretas compatíveis e aprender com o que acontece depois da experiência.

O Dry Run não é serviço médico, psicológico, jurídico ou financeiro de alto risco e não garante emprego, renda, contratação, transformação ou resultado específico.

## 4. Participação voluntária

A participação é voluntária.

A Pessoa pode:

- recusar participar;
- não responder perguntas;
- interromper a sessão;
- desistir do ciclo;
- revogar consentimento quando aplicável;
- exercer direitos relativos aos seus dados pessoais.

A recusa ou desistência não gera penalidade.

## 5. Quem pode participar nesta fase

O primeiro Dry Run foi desenhado para adultos com 18 anos ou mais e Momentos compatíveis com escopo de menor risco regulatório.

Se surgir situação fora do escopo, crise, emergência ou necessidade de orientação especializada, o Safety Gate prevalece e a experiência pode ser interrompida/redirecionada.

## 6. Finalidades do tratamento

Os dados poderão ser tratados somente para:

1. recrutamento e elegibilidade operacional;
2. agendamento e administração da participação;
3. registro do Notice e da decisão de consentimento;
4. compreensão proporcional do Momento;
5. identificação de objetivos, restrições e preferências materiais;
6. pesquisa e verificação de Possibilidades/oportunidades;
7. benchmark experimental;
8. registro da decisão voluntária e eventual ação;
9. follow-up autorizado;
10. compreensão da experiência, contribuição percebida e Novo Momento;
11. análise metodológica pseudonimizada/agregada;
12. governança de privacidade, segurança e direitos.

Não coletar dado apenas por conveniência.

## 7. Dados operacionais mínimos

Quando necessários, podem incluir:

- nome;
- canal de contato;
- confirmação 18+;
- cidade/região quando material;
- idioma;
- disponibilidade;
- status de recrutamento;
- versão/status/timestamp de Notice e consentimento;
- status de follow-up;
- status de direitos, correção, exclusão e fechamento.

## 8. Dados do episódio de Research

Em base separada e pseudonimizada, podem incluir:

- `participant_id`;
- `episode_id`;
- síntese do Momento;
- objetivo/direção;
- Possibilidades;
- restrições/preferências materiais;
- evidências `EG-0..EG-5`;
- contextual fit;
- benchmark;
- intenção/ação;
- follow-up;
- contribuição percebida;
- Novo Momento;
- observações metodológicas necessárias.

## 9. Dados não coletados por padrão

O Dry Run não foi desenhado para coletar normalmente:

- CPF;
- RG;
- documento oficial;
- endereço residencial completo;
- dado bancário;
- senha;
- credencial de terceiros;
- áudio;
- vídeo;
- transcrição bruta identificável;
- dado pessoal sensível como requisito normal.

## 10. Dados sensíveis

A Guivos não pretende coletar nem inferir dado sensível como parte normal deste Dry Run.

Se informação sensível surgir espontaneamente:

- não aprofundar sem necessidade;
- não persistir conteúdo desnecessário;
- aplicar Safety Gate quando necessário;
- reavaliar previamente qualquer tratamento persistente futuro.

## 11. Gravação

```text
AUDIO
→ OFF

VIDEO
→ OFF
```

Não haverá gravação por padrão.

## 12. Separação dos dados

A arquitetura documental prevê três boundaries distintos:

```text
IDENTITY VAULT
→ identidade + operação mínima

RESEARCH BASE
→ conteúdo pseudonimizado

LINKAGE KEY
→ ligação mínima e mais restrita
```

Pseudonimização reduz exposição, mas não equivale automaticamente a anonimização.

## 13. E-mail e operador

O canal `research@guivos.com` e os canais de privacidade utilizam **Hostinger Mail** como operador de e-mail.

O e-mail pode receber identificadores diretos necessários ao contato e aos direitos, mas não deve ser utilizado como repositório do dossiê rico de Research.

A política pública do fornecedor indica possibilidade de processamento/armazenamento em múltiplas jurisdições. Portanto, transferência/processamento internacional deve ser considerado material.

## 14. Uso de IA

O target documental prevê eventual uso de **OpenAI API** em projeto dedicado ao `RP-002`.

Regras do piloto:

```text
DIRECT IDENTIFIERS
→ NO BY DEFAULT

LINKAGE KEY
→ NEVER

CONTEXT
→ minimum necessary / pseudonymized / sanitized

VOLUNTARY DATA SHARING WITH OPENAI
→ NO
```

A saída da IA é assistiva e passa por revisão humana.

A documentação oficial atual informa que dados da API não são usados para treinamento por padrão, salvo opt-in, e que abuse monitoring logs podem reter conteúdo por até 30 dias por padrão. O piloto não presume Zero Data Retention.

## 15. Search / Web

O target documental prevê pesquisa pública minimizada para localizar e verificar oportunidades.

A consulta não deve conter nome, e-mail, telefone, documento, Linkage Key ou outro identificador direto por padrão.

O método primário previsto é Web Search no projeto dedicado da OpenAI API, seguido de verificação humana em fontes públicas originais quando necessário.

Abrir uma fonte pública para verificação não autoriza preencher formulários, criar conta, candidatar, comprar ou realizar transação em nome da Pessoa.

## 16. Transferência internacional

Pode ocorrer processamento internacional por operadores externos, especialmente serviços de e-mail e API.

A versão liberada deverá corresponder à configuração efetivamente implantada e revisada antes da primeira Pessoa real.

## 17. Retenção-alvo

Os prazos documentais atualmente definidos são:

- candidato não selecionado: até **30 dias** após encerramento do recrutamento;
- Identity Vault: até **90 dias** após encerramento individual;
- Linkage Key: até **90 dias**, preferencialmente menos quando não necessária;
- Research Base pseudonimizada: até **12 meses** após encerramento do ciclo do piloto;
- prova mínima de Notice/consentimento/revogação: **24 meses** após encerramento individual;
- registro mínimo de solicitação de direitos: **24 meses** após fechamento da solicitação;
- logs mínimos: **90 dias**;
- residual recuperável em backup após exclusão no primário: até **30 dias adicionais**;
- dado sensível incidental desnecessário: eliminar assim que tecnicamente possível, target de até **24 horas** após identificação.

Esses prazos podem ser encurtados quando a finalidade terminar antes e estão sujeitos à revisão final A12 antes de uso real.

## 18. Base legal

O núcleo voluntário do Dry Run está documentado com **consentimento** para o tratamento de dados pessoais comuns necessários às finalidades apresentadas, sujeito à revisão final.

Consentimento não é tratado como base universal para todas as operações auxiliares. Segurança, direitos, obrigações ou conservação excepcional devem possuir fundamento próprio quando aplicável.

## 19. Direitos

Nos termos aplicáveis da LGPD, a Pessoa poderá solicitar, conforme o caso:

- confirmação da existência de tratamento;
- acesso;
- correção;
- anonimização, bloqueio ou eliminação quando aplicável;
- informação sobre compartilhamentos;
- revogação do consentimento;
- eliminação de dados tratados com consentimento, observadas hipóteses legais de conservação;
- esclarecimentos pelos canais oficiais.

Canais:

- `privacidade@guivos.com`;
- `privacy@guivos.com`.

## 20. Revogação

Quando o tratamento estiver sustentado por consentimento, a Pessoa poderá revogá-lo.

A revogação:

- interrompe novas operações sustentadas por aquele consentimento;
- pode encerrar a participação;
- aciona análise de exclusão/anonimização;
- não elimina automaticamente dado cuja conservação seja exigida ou legitimamente necessária sob fundamento aplicável.

## 21. Usos não autorizados

A participação não autoriza automaticamente:

- marketing;
- newsletter;
- Guivos Ads;
- prospecção comercial;
- venda de audiência;
- exposição pública de caso individual;
- recomendação patrocinada oculta;
- treinamento genérico de modelos;
- compartilhamento indiscriminado com parceiros;
- contato indefinido;
- finalidade incompatível com o Dry Run.

## 22. Oportunidades

Uma oportunidade apresentada durante o piloto:

```text
IS NOT A PROMISE
IS NOT A GUARANTEE
IS NOT AN AUTOMATIC GUIVOS PARTNERSHIP
```

A decisão final permanece humana e voluntária.

## 23. Follow-up

O follow-up ocorrerá apenas dentro do ciclo explicado e autorizado, para verificar ação, experiência, contribuição percebida e eventual Novo Momento.

Ele não autoriza contato indefinido.

## 24. Consentimento — manifestação proposta

> Li e compreendi o Aviso ao Participante do piloto RP-002 na versão indicada neste e-mail. Entendo que minha participação é voluntária e concordo com o tratamento dos dados pessoais comuns necessários às finalidades específicas descritas no Aviso, incluindo os follow-ups previstos no ciclo explicado.

A manifestação deve ser explícita e vinculada à versão enviada.

Silêncio, omissão ou simples continuidade da conversa não contam como consentimento.

## 25. Registro mínimo da manifestação

```text
NOTICE_VERSION
CONSENT_STATUS
TIMESTAMP
PARTICIPANT_ID
WITHDRAWAL_STATUS WHEN APPLICABLE
```

O registro individual não deve ser publicado no GKR.

## 26. Contato futuro fora do ciclo

Contato genérico futuro, newsletter, marketing ou prospecção não estão incluídos no consentimento do Dry Run.

Qualquer finalidade futura deve ser tratada separadamente.

## 27. O que pode retornar ao GKR

Somente conhecimento desidentificado/agregado, como:

- metodologia;
- taxas agregadas;
- falhas de gates;
- gaps de supply;
- limitações;
- contraexemplos desidentificados;
- decisões GO / REVISE / STOP;
- mudanças de hipótese.

Nunca publicar no GKR nome, e-mail, telefone, dossiê individual, solicitação individual de direitos ou Linkage Key.

## 28. Condições para promoção

Antes de uso real:

- [ ] A12 concluído;
- [ ] operadores reais confirmados;
- [ ] stack implantado conforme documentos;
- [ ] controles e retenção verificados;
- [ ] A2 testado sinteticamente;
- [ ] A3/A4/A5/A6 implantados e testados conforme gates;
- [ ] A8/A9 configurados e verificados;
- [ ] A7 executado no stack-alvo;
- [ ] versão final congelada;
- [ ] `Participant 001` explicitamente liberado.

## 29. Estado

```text
A11 DOCUMENTATION
→ RECONCILED TARGET v0.2.0

AUTHORIZED FOR REAL PARTICIPANT
→ NO

A11 OPERATIONAL / FINAL RELEASE
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD
```
