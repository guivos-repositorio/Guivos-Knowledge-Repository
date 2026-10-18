---
id: GKR-UX-ORGCOL-MULTI-ENTITY-ACCESS-001
title: Jornada de Organizações e Coletivos — Um Acesso, Múltiplas Entidades e Planos Independentes
status: proposed
version: 0.1.0
owner: Guivos — Experience Architecture
last_updated: 2026-10-18
normative: false
depends_on:
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-JOURNEY-ORCHESTRATION-001
  - GKR-PLANS-ORGANIZATION-001
  - GKR-PLANS-COLLECTIVE-001
---

# Um acesso, múltiplas Organizações e Coletivos, planos independentes

## 1. Decisão de produto recebida (18/10/2026)

**Um único acesso de Pessoa pode estar legitimamente vinculado a zero, uma ou múltiplas Organizações, zero, um ou múltiplos Coletivos, e a uma combinação de ambos.** O usuário não precisa criar uma nova conta para cada entidade. Cadastro, identidade, gestão, capacidades e contratação são **isolados por entidade**. O número de entidades gerenciadas por um acesso não determina plano, compartilhamento de faturamento, direitos ou representação.

Este documento preserva direção expressa do fundador, como contrato candidato de jornada/UX a reconciliar com autoridades de autenticação, vínculos, planos, finanças, proteção e persistência. Não cria acesso jurídico, plano comercial novo nem autorização de produção.

## 2. Tela unificada: selecionar entidade ou cadastrar nova

Substituir a separação excludente `Acessar minha organização` versus `Acessar meu coletivo` por uma **tela comum de entidades vinculadas**, acessível após identificar a Pessoa. Nela:

- Exibir **todas as entidades realmente vinculadas ao mesmo acesso** que a Pessoa tem legitimidade de consultar/gerir: Organizações e Coletivos, cada uma com nome, tipo, ícone/foto autorizada, plano próprio (se conhecido), papel/possibilidade de gestão e estado de cadastro.
- Exibir ações **Cadastrar nova organização** e **Cadastrar novo coletivo** sem criar credenciais adicionais. O cadastro individual mantém dados, logo, fotos, responsáveis, autorização e plano próprios.
- Se não houver entidades, apresentar estado vazio com ambas as ações de cadastro; se houver várias, permitir distinguir cada uma e reabrir rascunhos sem duplicar cadastros.
- Se houver entidade vinculada sem permissão de administração, exibir somente ações autorizadas. Vinculação à conta **não equivale a autoridade irrestrita**.
- A lista deve permitir retornar e **trocar entidade ativa** a partir do menu/contexto da área interna, com identificação textual do tipo e nome; preservar identidade visual Organização Purple 4 `#5D34A9`, Coletivo Pink 4 `#E84CAB`. Botões funcionais comuns permanecem Black 2 `#232323`.
- Não inventar perfis `Eu teste`, `Comunidade Guivos` ou vínculos de produção como se reais; dados de desenvolvimento não podem conceder representação institucional.

## 3. Contexto e segregação (invariantes)

`ACCOUNT/PERSONA` **1:N** `ENTITY_MEMBERSHIP` **N:1** `ENTITY`. Cada vínculo declara `entity_id`, `entity_type`, `person_id`, `role`, `authority_scope`, estado, proveniência e vigência. `ACTIVE_CONTEXT` identifica explicitamente **uma** entidade ativa por vez. As operações, oportunidades, participantes, evidências, fotos e relações são sempre filtradas/autorizadas por entidade; não confiar somente em um seletor de UI ou `entity_id` enviado pelo cliente.

Trocar contexto deve descartar/cancelar requisições antigas, proteger rascunhos não salvos mediante confirmação, revalidar permissões, evitar exposição cruzada e impedir que eventos ou uploads de uma entidade apareçam em outra. Não transferir automaticamente relações O↔C, reputação, pontos, privilégios nem evidências.

Vínculo humano legítimo, representação legal, delegação administrativa e acesso baseado em papel seguem contratos específicos. Cadastro não concede automaticamente controle administrativo produtivo sobre CNPJ ou Coletivo existente. Suporte a múltiplas entidades **não autoriza bypass**.

## 4. Planos e cobrança individualizados por entidade

Cada **Organização** ou **Coletivo** tem um `ENTITY_PLAN/ENTITLEMENT` com `entity_id` único, histórico, estado contratual, limites, consumo e, quando houver, cobrança/assinatura próprios. O plano de uma entidade não altera nem paga automaticamente o plano de outra — mesmo quando ambas são administradas pela mesma Pessoa.

| Entidade | Baseline comercial vigente | Regra |
|---|---|---|
| Organização | **Conecta, Eleva, Transforma**: planos pagos | Cada Organização pode ter sua própria contratação; **não presumir existência de plano gratuito de Organização** |
| Coletivo | **Livre** gratuito; **Mobiliza, Impacta e Rede** pagos | Cada Coletivo escolhe/possui plano independente, conforme contratação e capacidades legítimas |
| Nova entidade ainda sem contratação | Cadastro em rascunho/sem assinatura confirmada, com estado explícito | **Cadastro sem assinatura não equivale a plano comercial gratuito**, nem autoriza benefícios pagos |
| Pessoa com múltiplas entidades | Múltiplos planos coexistentes, com titularidades distintas | Uma entidade pode estar Livre e outra em plano pago; não transferir cotas, fotos, oportunidades, limites, saldo ou assinatura |

Se o fundador desejar **Organização gratuita**, abrir decisão comercial separada e atualizar taxonomia/preços/limites antes de disponibilizá-la como plano vigente; a expressão "cadastro gratuito" pode designar **abertura de perfil sem contratação**, não plano Organizações Livre.

## 5. Jornadas e telas

```text
IDENTIFICAR PESSOA / ACESSO ÚNICO
   → MINHAS ORGANIZAÇÕES E COLETIVOS
       ├── [Organização A] → entrar → menu Organização e planos da Organização A
       ├── [Organização B] → entrar → menu Organização e planos da Organização B
       ├── [Coletivo C] → entrar → menu Coletivo e plano do Coletivo C
       ├── + Cadastrar organização → cadastro independente → retorno/listagem
       └── + Cadastrar coletivo → cadastro independente → retorno/listagem
```

A tela inicial de descoberta `O que você deseja cadastrar?` pode permanecer para quem inicia cadastro; não deve impedir ou fragmentar a **visão de todas as entidades do acesso**. `Acessar minha organização` e `Acessar meu coletivo` devem levar ao mesmo seletor unificado, opcionalmente com filtro inicial, sem esconder a outra natureza. A pessoa poderá entrar e sair de qualquer entidade legitimamente vinculada conforme seu vínculo.

Ao entrar em entidade, manter menus, formulários, oportunidades, galerias, vigência e responsabilidades específicos. O contrato comercial e eventual escolha de plano ocorrem **dentro do contexto da entidade** quando cabível, não como assinatura única do acesso.

## 6. Persistência e segurança para o Replit

A prototipação pode usar entidades de teste e persistência local segregada por `entity_id` para verificar experiência, sem afirmar login real, checagem de identidade ou faturamento; nunca mostrar dados reais sem autorização. A implementação produtiva exigirá autenticação de Pessoa, memberships validados no servidor, isolamento por tenant, controles de acesso e teste de autorização em cada operação, além de proteção de dados, auditoria, ciclo de vida e contratação por entidade.

Critérios de aceite no protótipo:
1. Um acesso apresenta múltiplas Organizações e Coletivos juntos, inclusive lista vazia e parcial.
2. Pode iniciar novos cadastros dos dois tipos e reabrir o individual sem sobrescrever outro.
3. Troca de contexto muda menu, cor predominante, identidade, oportunidades, galerias e plano, sem cruzar registros.
4. Cada entidade tem plano e capacidades independentes; exibir o Coletivo Livre gratuitamente, não fabricar Organização gratuita.
5. A criação de entidade não atribui autoridade/representação real; acesso à gestão requer vínculo/escopo coerentes.
6. Ações comuns usam botões Black 2, estrutura Gray/Black e canvas `#FFFFFF`; somente os 30 tokens oficiais da Guivos.
7. Interface em desktop/mobile e controle de teclado; nenhuma publicação ou cobrança real inferida.

**Estado:** `FOUNDER_MULTI_ENTITY_DIRECTION_ACCEPTED / DOCUMENTATION_CANDIDATE / REPLIT_PROTOTYPE_AUTHORIZED / PLAN_CONTRACTS_SEPARATE / PRODUCTION_NOT_AUTHORIZED`.
