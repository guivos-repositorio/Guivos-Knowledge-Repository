---
id: GKR-BRAND-ASSET-GOVERNANCE-001
title: Governança de Marca, Naming e Ativos Digitais
status: proposed
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GPA-000
  - GPA-002
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
  - GKR-DIGITAL-ASSET-CONTROL-001
  - GKR-UPDATE-PROGRAM-001
normative: true
---

# Governança de Marca, Naming e Ativos Digitais

## 1. Finalidade

Este documento estabelece a política de governança para nomes, marcas, domínios, subdomínios, perfis, identificadores públicos e demais ativos digitais associados à Guivos.

O objetivo é permitir expansão, proteção e consistência de identidade sem transformar intenção, pesquisa, reserva, compra, protocolo, registro ou controle técnico em fatos equivalentes.

Esta política governa **como uma afirmação de naming ou ativo digital se torna autoridade no GKR**. Ela não constitui, por si só, pedido de registro de marca, compra de domínio, transferência, alteração de DNS, contratação de serviço, enforcement ou comprovação de titularidade.

## 2. Princípios

1. **nome canônico ≠ marca registrada**;
2. **marca registrada ≠ domínio controlado**;
3. **domínio pesquisado ≠ domínio adquirido**;
4. **domínio adquirido ≠ DNS corretamente controlado**;
5. **DNS controlado ≠ e-mail/certificado/serviço em produção**;
6. **protocolo ≠ concessão**;
7. **registro nacional ≠ proteção global**;
8. **plano de proteção ≠ execução**;
9. **presença pública ≠ titularidade jurídica**;
10. **alias histórico ≠ nome oficial vigente**.

Toda afirmação sobre ativo deve indicar seu objeto, estado, evidência e autoridade.

## 3. Escopo

A política se aplica, quando pertinente, a:

- marca institucional Guivos e extensões oficiais;
- nomes de Produtos Especializados;
- nomes de programas, iniciativas e experiências;
- domínios e subdomínios;
- usernames e perfis institucionais;
- aplicativos, packages e identificadores técnicos públicos;
- endereços de e-mail institucionais e domínios de envio;
- certificados e ativos de confiança associados a nomes públicos;
- nomes de campanhas permanentes ou propriedades editoriais relevantes;
- ativos defensivos necessários à proteção de identidade.

## 4. Classificação de informação

Nem todo ativo deve ser publicado no GKR.

| Classe | Pode aparecer no corpus público? | Exemplos de conteúdo |
|---|---|---|
| **Público** | sim | nome oficial, finalidade pública, URL já publicada quando comprovada |
| **Interno** | somente em repositório/controladoria apropriada | inventário resumido, estado de renovação, responsável por função |
| **Restrito** | não no corpus público | registrador, account identifiers, contatos de contingência, detalhes operacionais de DNS |
| **Secreto** | nunca no GKR | senhas, MFA seeds, recovery codes, chaves privadas, tokens, credenciais, auth cookies |

O GKR público deve conter políticas, naming canônico e referências de evidência suficientes para governança, mas não um mapa operacional que aumente risco de tomada de conta.

## 5. Estados governados de naming

Um nome pode assumir um dos seguintes estados:

| Estado | Significado |
|---|---|
| `candidate` | nome em avaliação; não deve ser apresentado como oficial |
| `approved_internal` | nome aprovado para uso interno/preparação, ainda não necessariamente lançado |
| `canonical` | nome oficial vigente no GKR para o objeto definido |
| `public_active` | nome canônico e publicamente utilizado, com evidência de uso |
| `superseded` | substituído por outro nome; pode permanecer apenas como histórico/migração |
| `retired` | uso encerrado sem substituição obrigatória |
| `contested` | autoridade ou uso em disputa; exige decisão antes de nova propagação |

`canonical` não afirma disponibilidade registral, titularidade jurídica ou proteção marcária.

## 6. Estados governados de ativos digitais

Um ativo digital deve usar estados factuais separados:

| Estado | Significado mínimo |
|---|---|
| `candidate` | intenção de proteger/adquirir; sem comprovação de controle |
| `evidence_pending` | existe alegação de posse/registro, mas falta evidência suficiente |
| `confirmed_control` | controle técnico/administrativo comprovado na data da evidência |
| `registered` | registro contratual/registral comprovado para o objeto e jurisdição indicados |
| `delegated` | operação confiada a terceiro com responsabilidade definida |
| `active_service` | ativo sustenta serviço efetivamente publicado/operacional comprovado |
| `suspended` | mantido, porém temporariamente não utilizado ou bloqueado |
| `superseded` | substituído por outro ativo |
| `retired` | encerrado ou liberado mediante decisão governada |
| `unknown` | estado não verificável; nenhuma afirmação operacional é permitida |

Esses estados não são uma escada obrigatória. Um domínio, por exemplo, pode estar `confirmed_control` sem sustentar serviço público.

## 7. Autoridade de naming

A autoridade corrente de nomes deve ser registrada em `GKR-OFFICIAL-NAMING-AUTHORITY-001` ou em documento temático superior explicitamente relacionado.

Uma alteração de naming exige:

1. objeto claramente identificado;
2. nome anterior, quando houver;
3. nome novo;
4. decisão e responsável;
5. data de vigência;
6. consumidores afetados;
7. aliases de migração necessários;
8. avaliação de colisão com outros produtos/papéis;
9. plano de atualização documental;
10. classificação do nome anterior como `superseded` ou `retired`.

Mudança de nome não cria automaticamente novo produto, entidade jurídica, domínio, preço, contrato, jornada ou registro marcário.

## 8. Regra de aliases e nomes legados

Alias antigo pode permanecer somente quando uma das condições for verdadeira:

- documento histórico;
- registro de migração;
- campo `former_name` ou equivalente;
- pesquisa que precisa reproduzir terminologia anterior;
- evidência externa cujo texto original não pode ser reinterpretado.

Alias legado não pode aparecer como nome corrente em títulos, navegação, tabelas comerciais, jornadas, ofertas, metadados de produto ou materiais públicos atuais.

A substituição `Guivos Marketplace → Guivos Mall` é exemplo governado dessa regra: `Guivos Mall` é o nome canônico do produto; `Guivos Marketplace` permanece apenas como referência de migração/histórico conforme `GPA-002`.

## 9. Domínios e subdomínios

O GKR deve separar três decisões:

```text
estratégia de namespace
→ decisão de aquisição/proteção
→ evidência de controle/operação
```

A estratégia pode definir padrões como:

- domínio institucional principal;
- subdomínios funcionais;
- domínios territoriais;
- domínios defensivos;
- redirecionamentos;
- propriedades editoriais ou de produto.

Porém, **nenhum hostname específico deve ser marcado como adquirido, registrado ou operacional sem evidência verificável**.

O inventário completo de domínios defensivos, registradores, contas e configurações não deve ser publicado no corpus aberto.

## 10. Controles mínimos por criticidade

### 10.1 Crítico

Ativos capazes de afetar identidade institucional, autenticação, e-mail, pagamentos, tráfego principal ou confiança pública exigem, no mínimo:

- responsável de negócio e custodiante técnico distintos ou explicitamente acumulados;
- MFA resistente a phishing quando tecnicamente disponível;
- recuperação protegida e fora do GKR;
- controle de acesso mínimo necessário;
- renovação automática quando adequada, acompanhada de revisão humana;
- alertas de expiração/alteração;
- DNS e delegações revisáveis;
- registro de mudanças;
- plano de transferência/continuidade;
- evidência periódica de controle.

### 10.2 Alto

Ativos de produto, campanha permanente, perfis oficiais e propriedades comerciais relevantes exigem ownership, MFA, revisão periódica, continuidade e rastreabilidade de alterações.

### 10.3 Médio/Baixo

Ativos experimentais ou não críticos podem ter controles proporcionais, mas nunca devem depender exclusivamente de conta pessoal sem decisão e plano de transição documentados.

## 11. Ciclo de vida

```text
necessidade
→ pesquisa
→ decisão de naming/proteção
→ verificação de disponibilidade/risco
→ aquisição ou registro quando autorizado
→ comprovação
→ configuração
→ publicação/uso
→ monitoramento
→ renovação/revisão
→ transferência, supersessão ou encerramento
```

Cada passagem que altera estado factual deve produzir evidência correspondente.

## 12. RACI por função

| Atividade | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| naming institucional/produto | liderança da Guivos | Brand/Product Architecture | Jurídico, Produto, GTM | áreas consumidoras |
| estratégia de proteção | liderança da Guivos | Brand/Legal | Segurança, Financeiro, Produto | governança |
| aquisição/renovação de domínio | função autorizada de ativos digitais | custodiante designado | Financeiro, Segurança | owner do produto |
| DNS/certificados | função técnica autorizada | custodiante técnico | Segurança, owner do serviço | governança |
| registro marcário | autoridade jurídica/empresarial | Jurídico/agente autorizado | Brand, liderança | governança |
| incidente de identidade/conta | autoridade de incidente | Segurança/operador autorizado | Jurídico, Brand, Produto | liderança afetada |
| aposentadoria/transferência | owner do ativo | custodiante | Jurídico, Segurança, Produto | consumidores |

Os nomes acima representam **funções**, não comprovam que cargos, equipes ou fornecedores específicos já estejam contratados.

## 13. Evidências aceitáveis

Conforme o objeto, podem sustentar estado:

- comprovante oficial do registrador/registry;
- protocolo ou certificado oficial de propriedade intelectual;
- fatura/contrato que identifique inequivocamente o ativo e titularidade aplicável;
- consulta técnica autenticada e controlada;
- registro administrativo da plataforma proprietária;
- documento jurídico verificável;
- evidência operacional controlada e datada.

Captura de tela isolada, conversa, intenção, orçamento, pesquisa de disponibilidade ou presença pública não devem ser tratados automaticamente como prova suficiente de titularidade.

## 14. Gates para internacionalização de marca

Antes de afirmar proteção em nova jurisdição:

1. objeto e classe de proteção definidos;
2. pesquisa jurídica/registral adequada;
3. titular pretendido definido;
4. rota de depósito/registro escolhida;
5. protocolo ou registro comprovado;
6. país/região e escopo explicitados;
7. vigência e renovação conhecidas;
8. limitações registradas.

O GKR não pode usar expressões como “marca protegida globalmente” sem evidência compatível com o alcance afirmado.

## 15. Incidentes e mudanças sensíveis

Incidentes de domínio, DNS, e-mail, perfil, marca ou identidade digital devem ser registrados em sistema restrito apropriado. O GKR público pode registrar apenas política, impacto arquitetural sanitizado e decisão resultante quando necessário.

Não publicar durante incidente:

- vetor de tomada de conta;
- credenciais ou recovery path;
- dados de contato restritos;
- configuração explorável;
- inventário defensivo completo.

## 16. Relação com P1.1

P1.1 reconcilia nomenclaturas já comprovadamente substituídas no corpus. P3 estabelece a política permanente que impede novas derivas.

Portanto:

```text
P1.1 = limpeza e gate de legado
P3 = autoridade e ciclo de vida de naming/ativos
```

## 17. Fora do escopo

Este documento não:

- registra marca;
- compra ou transfere domínio;
- altera DNS;
- cria conta em registrador;
- comprova titularidade de qualquer ativo específico;
- contrata TMCH, bloqueio, monitoramento ou agente de propriedade intelectual;
- executa enforcement;
- publica carteira defensiva;
- declara cobertura internacional.

## 18. Critério de adoção

A política pode ser considerada adotada no GKR quando:

- a autoridade oficial de naming estiver vinculada;
- o modelo de registro de ativos estiver disponível;
- consumidores não apresentarem aliases superseded como nomes correntes;
- afirmações de posse/registro/operação exigirem evidência;
- informações restritas e secretas permanecerem fora do corpus público;
- gates mecânicos e semânticos do GKR permanecerem verdes.
