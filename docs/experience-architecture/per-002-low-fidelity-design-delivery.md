---
id: GKR-UX-PER002-DESIGN-DELIVERY-001
title: PER-002 — Materialização Low-Fidelity Funcional de Design
status: active
version: 0.1.0
owner: Design Guivos
last_updated: 2026-09-09
normative: false
maturity: low_fidelity_design_delivery_pending_functional_validation
depends_on:
  - GKR-UX-PER002-DESIGN-AUTH-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-HOME-MASTER-001
  - UXA-020
  - UXA-023
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-STATE-001
  - PER-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Materialização Low-Fidelity Funcional de Design

## 1. Finalidade da entrega

Esta entrega materializa em baixa fidelidade a responsabilidade existente `PER-002 — Entrada protegida`, conforme autorização `GKR-UX-PER002-DESIGN-AUTH-001` e boundary funcional congelado em `GKR-UX-PER002-MAT-ELIGIBILITY-001`.

O artefato torna o contrato funcional visualmente inspecionável sem criar nova superfície, novo `PER-ID`, UXA numerada, UI de alta fidelidade, protótipo ou implementação.

```text
DESIGN AUTHORIZATION
→ GRANTED

DESIGN DELIVERY
→ EXECUTED
→ LOW-FIDELITY
→ FUNCTIONAL
→ PER-002 ONLY

FUNCTIONAL VALIDATION
→ NOT YET PERFORMED

VISUAL MATURITY PROMOTION
→ NOT INFERRED
```

Esta entrega é **não normativa**. A autoridade funcional continua pertencendo à Experience Architecture e aos registries vigentes; a autoridade desta entrega é somente sobre a proposta visual low-fidelity submetida à validação.

## 2. Decisão de composição

A cobertura obrigatória foi materializada como **quatro frames principais e três variantes**, e não como sete telas independentes.

```text
PER-002
├─ FRAME 01 — ORIENTAÇÃO PROTEGIDA / PRÉ-AUTH
├─ FRAME 02 — GATE DE ACESSO
│  ├─ VARIANTE A — SESSÃO JÁ AUTENTICADA
│  └─ VARIANTE B — RECUPERAÇÃO / RESTRIÇÃO / FALHA
├─ FRAME 03 — CONTINUAÇÃO AUTENTICADA / CONTROLES
├─ VARIANTE C — SAIR / INTERROMPER / EXPLORAR SEM PERSONALIZAÇÃO
└─ FRAME 04 — HANDOFF READY
                 ↓
               TRN-002
                 ↓
               PER-003
```

A estrutura reduz fricção e evita converter estados operacionais em novas superfícies canônicas.

```text
ESTADO VISUALMENTE DISTINTO
≠ NOVA RESPONSABILIDADE
≠ NOVO PER-ID
```

## 3. Princípios de Design aplicados

A primeira materialização segue estes princípios:

1. **contexto antes de credencial** — a pessoa entende onde está antes de entrar ou criar conta;
2. **proteção visível sem alarmismo** — a interface deixa claro o ambiente protegido sem linguagem de ameaça;
3. **autenticação como gate, não destino** — entrar serve à continuidade de `PER-002`, não encerra o fluxo;
4. **controles antes de materialidade** — finalidades, privacidade e reversibilidade precedem qualquer compartilhamento relevante;
5. **saída sempre legítima** — voltar, interromper e explorar sem personalização permanecem disponíveis;
6. **não linearidade controlada** — sessão válida pula o gate de acesso sem pular responsabilidades funcionais posteriores;
7. **handoff explícito** — `PER-003` aparece somente como próximo destino, sem antecipar suas modalidades;
8. **low-fidelity real** — estrutura, prioridade e estado são definidos; estética final, branding refinado, motion, tokens e componentes finais permanecem fora de escopo.

## 4. Linguagem e fidelidade

O texto abaixo é **working copy funcional de baixa fidelidade**, utilizado para testar clareza e hierarquia. Não constitui copy final de Marca, UX Writing aprovado ou superfície publicada.

```text
WORKING COPY
→ INSPECIONÁVEL
→ EDITÁVEL NA VALIDAÇÃO
→ NOT FINAL BRAND COPY
```

A representação é mobile-first e estrutural. Dimensões exatas, grid final, tipografia, cor, ícones, componentes, breakpoints e microinterações não são definidos nesta etapa.

## 5. Fluxo estrutural

```text
PER-001 — HOME PÚBLICA
        |
        | "Iniciar minha jornada"
        v
+-------------------------------+
| FRAME 01                      |
| orientação protegida          |
+-------------------------------+
        |
        | continuar
        v
  sessão válida?
     /     \
   sim     não
   |        |
   |        v
   |   +-----------------------+
   |   | FRAME 02              |
   |   | gate de acesso        |
   |   +-----------------------+
   |        |
   |        | autenticação concluída
   |        v
   +------> +-----------------------+
            | FRAME 03              |
            | controles / contexto  |
            +-----------------------+
                    |
                    | continuar conscientemente
                    v
            +-----------------------+
            | FRAME 04              |
            | handoff ready         |
            +-----------------------+
                    |
                    | TRN-002
                    v
            PER-003 — ESCOLHA DE MODALIDADE
```

A rota `Login` da Home para relação já existente permanece fora deste fluxo de primeira entrada:

```text
HOME
→ LOGIN
→ AUTHENTICATION
→ RESUME / RECOVER LEGITIMATE EXISTING STATE
```

Ela não é redesenhada nem absorvida por esta entrega.

## 6. Frame 01 — Orientação protegida / pré-auth

Objetivo: informar que a pessoa deixou o ambiente público, explicar o que muda e oferecer alternativas antes de solicitar autenticação.

```text
+--------------------------------------------------+
| GUIVOS                                           |
| Entrada protegida                                |
|--------------------------------------------------|
|                                                  |
| Você está entrando em um ambiente protegido.     |
|                                                  |
| Aqui, você poderá decidir o que quer             |
| compartilhar e como essas informações poderão   |
| ser utilizadas.                                  |
|                                                  |
| [ status ] Nenhuma coleta pessoal foi iniciada. |
|                                                  |
| O que acontece a seguir                          |
|  • você pode conhecer o processo antes de entrar|
|  • entrar ou criar conta não inicia análise     |
|  • você poderá revisar controles antes de       |
|    compartilhar qualquer relato                 |
|                                                  |
| [ Continuar com segurança ]                      |
|                                                  |
|   Entender como funciona                         |
|   Explorar sem personalização                    |
|   Voltar à Página Inicial                        |
|                                                  |
+--------------------------------------------------+
```

### 6.1 Hierarquia

```text
PRIMARY
→ Continuar com segurança

SECONDARY
→ Entender como funciona

ALTERNATIVES
→ Explorar sem personalização
→ Voltar à Página Inicial
```

### 6.2 Guardrails visíveis

- nenhuma caixa pré-marcada;
- nenhum campo pessoal;
- nenhuma gravação, upload ou conexão;
- nenhuma promessa de personalização;
- nenhum bloqueio à exploração pública;
- nenhuma linguagem que trate criação de conta como compromisso com processamento.

## 7. Frame 02 — Gate de acesso

Objetivo: permitir autenticação, criação ou recuperação sem transformar credencial em autorização de uso material.

```text
+--------------------------------------------------+
| GUIVOS                                           |
| Entrada protegida                                |
|--------------------------------------------------|
|                                                  |
| Acesse para continuar com segurança              |
|                                                  |
| Entrar permite associar sua jornada a você.      |
| Isso não autoriza análise, personalização ou     |
| processamento do que você vier a compartilhar.  |
|                                                  |
| [ Entrar ]      [ Criar conta ]                  |
|                                                  |
| Identificação                                    |
| [..............................................] |
|                                                  |
| Credencial                                       |
| [..............................................] |
|                                                  |
| [ Continuar ]                                    |
|                                                  |
|   Recuperar acesso                               |
|   Voltar                                         |
|   Explorar sem personalização                    |
|                                                  |
| Privacidade do acesso                            |
| O estado de uma conta não deve ser exposto       |
| indevidamente durante tentativa ou recuperação.  |
|                                                  |
+--------------------------------------------------+
```

A representação de `Identificação` e `Credencial` é propositalmente genérica: a tecnologia de autenticação não é definida por Design nesta etapa.

### 7.1 Regra funcional explícita

```text
SUCCESSFUL AUTHENTICATION
→ CONTINUE PER-002

SUCCESSFUL AUTHENTICATION
≠ HANDOFF TO PER-003
≠ PROCESSING AUTHORIZATION
```

## 8. Variante A — Sessão já autenticada

Quando a sessão já estiver legitimamente válida, o gate de acesso não deve criar fricção artificial.

```text
FRAME 01
   |
   | continuar
   v
[ sessão válida detectada ]
   |
   | gate de acesso já satisfeito
   v
FRAME 03
```

Sinal de contexto possível no início do Frame 03:

```text
+--------------------------------------------------+
| Sessão ativa                                     |
| Você já está autenticado.                        |
| Vamos apenas revisar o contexto e os controles   |
| antes de qualquer compartilhamento material.     |
+--------------------------------------------------+
```

Essa variante não deve obrigar a pessoa a repetir login, redefinir credencial ou atravessar uma tela de sucesso sem função.

## 9. Variante B — Recuperação / restrição / falha

Objetivo: oferecer recuperação compreensível sem expor existência de conta, dados ou motivos sensíveis.

```text
+--------------------------------------------------+
| GUIVOS                                           |
| Acesso protegido                                 |
|--------------------------------------------------|
|                                                  |
| Não foi possível concluir o acesso com segurança.|
|                                                  |
| Seus dados de jornada não foram processados por  |
| esta tentativa.                                  |
|                                                  |
| [ Tentar novamente ]                             |
|                                                  |
|   Recuperar acesso                               |
|   Usar outra forma de acesso, se disponível      |
|   Voltar à entrada protegida                     |
|   Explorar sem personalização                    |
|                                                  |
| Precisa de ajuda?                                |
| [ orientação de suporte / proteção aplicável ]   |
|                                                  |
+--------------------------------------------------+
```

### 9.1 Regras

- erro não revela se uma identificação específica possui conta;
- recuperação não inicia onboarding novo por inferência;
- restrição deve explicar ação possível sem expor motivo sensível desnecessário;
- falha não remove alternativas de saída;
- estado recuperável não deve parecer encerramento da Journey.

## 10. Frame 03 — Continuação autenticada / finalidades, privacidade e controles

Objetivo: confirmar o contexto protegido e tornar compreensíveis os controles antes de `PER-003` e antes de qualquer processamento material.

```text
+--------------------------------------------------+
| GUIVOS                                           |
| Entrada protegida                                |
|--------------------------------------------------|
|                                                  |
| Antes de você compartilhar qualquer coisa        |
|                                                  |
| Você continua no controle.                       |
|                                                  |
| O que pode acontecer                             |
| +----------------------------------------------+ |
| | Você escolhe o que compartilhar              | |
| | Nada é analisado só porque você entrou.      | |
| +----------------------------------------------+ |
|                                                  |
| Para que suas informações poderão ser usadas     |
| +----------------------------------------------+ |
| | Finalidades serão apresentadas no momento    | |
| | em que cada uso material for solicitado.     | |
| +----------------------------------------------+ |
|                                                  |
| Seus controles                                   |
| +----------------------------------------------+ |
| | revisar · corrigir · limitar · retirar       | |
| | remover · interromper                        | |
| +----------------------------------------------+ |
|                                                  |
| [ Continuar ]                                    |
|                                                  |
|   Ver detalhes de privacidade                    |
|   Sair por agora                                 |
|   Explorar sem personalização                    |
|                                                  |
+--------------------------------------------------+
```

### 10.1 Decisão de Design

Não existe checkbox `Aceito tudo`, consentimento omnibus ou autorização material antecipada neste frame.

```text
UNDERSTAND CONTROLS
≠ AUTHORIZE ALL FUTURE PURPOSES

AUTHENTICATED
≠ SHARED PERSONAL NARRATIVE
≠ PROCESSING AUTHORIZED
```

## 11. Variante C — Sair / interromper / explorar sem personalização

Esta variante pode ser aberta a partir dos frames principais sempre que a ação fizer sentido.

```text
+--------------------------------------------------+
| Como você quer continuar?                        |
|--------------------------------------------------|
|                                                  |
| Você não precisa concluir agora.                 |
|                                                  |
| [ Explorar a Guivos sem personalização ]         |
|                                                  |
| [ Voltar à Página Inicial ]                      |
|                                                  |
| [ Pausar por agora ]                             |
|                                                  |
|   Continuar na entrada protegida                 |
|                                                  |
+--------------------------------------------------+
```

### 11.1 Regra de efeito

O efeito real deve depender do estado existente:

| Estado | Efeito esperado em baixa fidelidade |
|---|---|
| pré-auth | nenhuma persistência de relato é criada |
| autenticado sem relato | sessão pode existir, mas nenhum relato/processamento é iniciado |
| recuperação em curso | tentativa pode ser abandonada sem iniciar Journey material |
| controles revisados | pessoa pode sair antes do handoff sem ser coagida |

A ação `Pausar por agora` não define persistência técnica. Ela sinaliza intenção de interrupção; a implementação futura deverá respeitar o estado efetivamente existente.

## 12. Frame 04 — Handoff ready

Objetivo: tornar visível que `PER-002` cumpriu as responsabilidades desta entrada e que a próxima ação leva a `PER-003`, sem materializar as opções internas de `PER-003`.

```text
+--------------------------------------------------+
| GUIVOS                                           |
| Entrada protegida                                |
|--------------------------------------------------|
|                                                  |
| Você está pronto para escolher como começar.     |
|                                                  |
| Antes de seguir                                  |
|  ✓ ambiente protegido compreendido               |
|  ✓ acesso concluído ou já válido                 |
|  ✓ controles e alternativas apresentados         |
|  ✓ nenhum relato foi processado por este passo   |
|                                                  |
| O próximo passo será escolher como você prefere  |
| começar a se expressar.                          |
|                                                  |
| [ Escolher como quero começar ]                  |
|                                                  |
|   Revisar privacidade e controles                |
|   Sair por agora                                 |
|                                                  |
+--------------------------------------------------+
```

### 12.1 Handoff

```text
[ Escolher como quero começar ]
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE
```

Nenhuma opção de texto, voz, arquivo ou outra modalidade é desenhada neste frame.

```text
SHOW THAT PER-003 COMES NEXT
≠ MATERIALIZE PER-003
```

## 13. Matriz de cobertura do boundary

| Requisito autorizado | Materialização |
|---|---|
| orientação protegida / pré-auth | Frame 01 |
| gate de autenticação quando necessário | Frame 02 |
| sessão já autenticada | Variante A |
| continuação autenticada de `PER-002` | Frame 03 |
| acesso / recuperação / restrição / falha | Variante B |
| voltar / interromper / não prosseguir / explorar sem personalização | Variante C + ações persistentes |
| condição de handoff legítimo para `PER-003` | Frame 04 |

Cobertura:

```text
7 / 7 AUTHORIZED COVERAGE AREAS
→ MATERIALIZED
```

Essa contagem é de requisitos de cobertura, não de superfícies canônicas.

## 14. Estados e roteamento

| Condição | Próximo estado visual |
|---|---|
| visitante inicia Journey | Frame 01 |
| visitante continua sem sessão | Frame 02 |
| sessão já válida | Frame 03 |
| autenticação concluída | Frame 03 |
| acesso falha / precisa recuperação | Variante B |
| pessoa decide sair | Variante C |
| controles compreendidos e pessoa decide continuar | Frame 04 |
| pessoa confirma continuidade no Frame 04 | `TRN-002 → PER-003` |

Não existe roteamento automático do simples login para `PER-003`.

## 15. Estados que esta entrega não materializa

Os estados posteriores descritos em `UXA-020` e `UXA-023` continuam válidos em suas autoridades, mas não pertencem ao boundary desta entrega Q de `PER-002`:

- escolha detalhada de modalidade;
- texto / voz / arquivos;
- rascunho de relato;
- inventário do que foi recebido;
- autorizações específicas de processamento de conteúdo;
- processamento visível;
- compreensão inicial;
- revisão da compreensão;
- Tela Hoje.

```text
CURRENT DELIVERY
→ ENTRY PROTECTION / ACCESS / CONTROLS / HANDOFF

CURRENT DELIVERY
≠ FULL PROTECTED-JOURNEY PROCESS
```

## 16. Responsividade low-fidelity

A entrega é mobile-first, mas não depende de um único viewport.

### Mobile

- conteúdo em uma coluna;
- ação principal imediatamente distinguível;
- alternativas empilhadas;
- explicações progressivas;
- nenhuma dependência de hover;
- área de toque futura deverá ser adequada, mas dimensões finais não são definidas aqui.

### Desktop / largura ampliada

- conteúdo central pode permanecer em coluna de leitura;
- informações auxiliares podem ocupar painel lateral somente se não alterarem ordem semântica;
- alternativas não devem ser escondidas por ganho de espaço;
- gate de acesso pode usar composição dividida sem transformar explicação em publicidade.

```text
RESPONSIVE ADAPTATION
→ MAY CHANGE COMPOSITION
→ MUST NOT CHANGE FUNCTIONAL ORDER OR RIGHTS
```

## 17. Acessibilidade incorporada ao low-fidelity

Mesmo sem UI final, a estrutura já exige:

- títulos claros por estado;
- ordem de leitura linear compreensível;
- ação primária distinguível sem depender somente de cor;
- alternativas textuais completas;
- nenhuma informação crítica apenas em ícone;
- foco conceitual previsível em erro/recuperação;
- ausência de contagem regressiva ou urgência artificial;
- ausência de seleção prévia de autorização;
- possibilidade de sair e retornar sem coerção.

Acessibilidade real permanece pendente de validação em UI/protótipo futuro; não é declarada como comprovada nesta etapa.

## 18. Decisões deliberadamente não tomadas

Esta entrega não define:

- identidade visual final;
- cor;
- tipografia;
- iconografia final;
- grid de produção;
- tokens;
- componentes de Design System;
- tecnologia de autenticação;
- MFA;
- SSO;
- social login;
- política técnica de sessão;
- storage;
- analytics;
- instrumentação;
- modal versus rota física final;
- copy final de Marca;
- comportamento de backend;
- persistência técnica de pausa;
- estrutura interna de `PER-003`.

Essas decisões não são necessárias para validar a aderência funcional da primeira materialização.

## 19. Anti-regressão

A validação futura deve rejeitar a entrega se qualquer interpretação visual resultar em:

```text
AUTHENTICATION
→ TREATED AS PER-002 COMPLETION

ACCOUNT CREATION
→ TREATED AS PROCESSING CONSENT

PER-003
→ ABSORBED INTO PER-002

EXISTING LOGIN
→ FORCED INTO FIRST-ENTRY ONBOARDING

EXIT / EXPLORE WITHOUT PERSONALIZATION
→ HIDDEN OR PUNITIVE

HISTORICAL UXA-034 APPEARANCE
→ RESTORED AS CURRENT BASELINE

HIGH-FIDELITY / PROTOTYPE / ENGINEERING
→ INFERRED FROM THIS DELIVERY
```

## 20. Maturidade após esta entrega

```text
PER-002 DESIGN AUTHORIZATION
→ GRANTED

PER-002 LOW-FIDELITY DESIGN DELIVERY
→ EXECUTED
→ GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0

FUNCTIONAL VALIDATION OF DELIVERY
→ NOT_STARTED

TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

AGGREGATE VISUAL WIREFRAME MATURITY
→ NOT_CERTIFIED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
```

A existência desta entrega não significa que seus frames foram aprovados, testados com pessoas, transformados em UI, prototipados ou implementados.

## 21. Próximo gate

O próximo ato governado é somente a **validação funcional da entrega low-fidelity de `PER-002`**.

A validação deverá confrontar esta entrega com:

1. `GKR-UX-PER002-MAT-ELIGIBILITY-001`;
2. `GKR-UX-PER002-DESIGN-AUTH-001`;
3. `UXA-020`;
4. `UXA-023`;
5. registries vigentes de superfícies e transições;
6. distinção Home / primeira entrada / login resumptivo;
7. guardrails de privacidade, autonomia, reversibilidade e acessibilidade funcional.

```text
NEXT
→ PER-002 LOW-FIDELITY FUNCTIONAL VALIDATION

DO NOT YET
→ PROMOTE VISUAL MATURITY
→ CREATE HIGH-FIDELITY UI
→ CREATE INTERACTIVE PROTOTYPE
→ START UXA-102/V5
→ MATERIALIZE PER-003 BEYOND HANDOFF
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ MERGE PR #363
```
