---
id: GKR-UX-EVALUATION-REPUTATION-PERSON-SURFACE-PARTITION-001
title: Avaliação e Reputação — Partição Candidata das Responsabilidades da Pessoa
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-29
related:
  - UXA-057
  - GKR-UX-EVALUATION-REPUTATION-RESPONSIBILITY-ADJUDICATION-001
  - GKR-UX-EVALUATION-REPUTATION-INITIAL-COVERAGE-001
  - GKR-UX-EVALUATION-REPUTATION-SURFACE-PROPOSAL-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Avaliação e Reputação — Partição Candidata das Responsabilidades da Pessoa

## 1. Finalidade e autoridade

Esta proposta não normativa desenvolve a segunda dependência da adjudicação UXA-057: separar **entrada contextual**, **registro protegido da avaliação** e **continuidade da autora**, sem presumir que cada responsabilidade exige tela, rota ou ID próprios. UXA-057 governa critérios, elegibilidade, unidade da experiência, visibilidade, atualização e direitos da autora. Os registries e Masters vigentes prevalecem para superfícies e transições.

A matriz de cobertura inicial permanece candidata: nenhum objeto ou edição foi selecionado para lançamento. Os 24 estados de UXA-057 não correspondem a 24 telas.

## 2. Matriz de partição

| Responsabilidade | Contexto/entrada candidata | Contrato especializado necessário | Limite |
|---|---|---|---|
| Descobrir que uma experiência pode ser avaliada | PER-108 para experiência pertinente ao Coletivo; PER-203 para oportunidade; outras entradas somente após inventário e autoridade | Explicar objeto, edição, etapa, motivo de elegibilidade, voluntariedade e destino legítimo | PER-108/PER-203 não herdam formulário, inbox ou transição nova por analogia |
| Verificar elegibilidade e escolher a unidade | Fluxo de registro protegido, sem superfície identificada | Distinguir inscrição válida como experiência de inscrição de participação, contratação e resultados posteriores; revalidar proveniência, papel, edição e duplicidade | Navegação, interesse ou inscrição em etapa diferente não comprovam experiência posterior |
| Preencher e revisar | Mesmo contrato de registro, salvo decisão posterior | Critérios específicos, opção não aplicável/informação insuficiente, comentário opcional, identidade/visibilidade e revisão consciente | Não converter expressão inicial da Jornada em avaliação; não exigir comentário |
| Enviar e obter retorno | Fluxo de registro protegido | Persistência idempotente, referência estável da avaliação, estado de envio, retorno neutro ao contexto | Falha não produz avaliação; envio não concede vínculo, resultado ou avanço |
| Consultar avaliações próprias | Responsabilidade de continuidade, com ponto de acesso permanente a adjudicar | Listar avaliações autorizadas, objeto/edição, período, estado, visibilidade, local de publicação e histórico pertinente | PER-009 é Conta e direitos transversais; não vira painel completo por analogia |
| Editar, atualizar ou retirar | Continuidade da autora, eventualmente acionada pelo contexto da avaliação | Preservar unidade, histórico e versões; atualizar experiência distinta apenas com evidência própria; retirar comentário ou avaliação conforme retenção legítima | Não gerar múltiplas avaliações artificiais da mesma experiência |
| Alterar visibilidade, contestar moderação ou denunciar resposta | Continuidade com handoff governado para proteção especializada | Mostrar efeitos da escolha, decisão, fundamento e recurso quando cabível | A autora não recebe poder de moderação; denúncia e contestação são fluxos distintos |

**Partição funcional candidata:** (A) entrada contextual, (B) registro protegido, (C) continuidade da autora. B e C têm responsabilidades e ciclos de vida distintos, mas sua materialização em uma ou mais superfícies permanece **indeterminada**. A entrada contextual não constitui superfície especializada nova.

## 3. Contrato candidato de registro protegido

**Pré-condições:** objeto e unidade identificáveis; etapa efetivamente vivida; evidência proporcional; autorização vigente; critérios/versionamento aplicáveis; ausência de duplicidade não resolvida. A elegibilidade poderá ser verificada, confirmada pelo responsável, declarada, externa ou insuficiente, sem converter automaticamente as categorias em equivalentes.

**Sequência funcional, não navegação aprovada:** receber contexto legítimo → informar motivo e voluntariedade → verificar unidade/evidência → selecionar critérios da etapa → responder → escolher comentário e visibilidade → revisar → enviar → apresentar estado e retorno. Quando a inscrição em si for o objeto, inscrição válida poderá ser evidência dessa etapa, sem atestar participação posterior.

**Exceções:** recusa sem prejuízo; falta de evidência; edição ou responsável alterados; conflito de interesse; duplicidade; interrupção; perda de autorização; falha de envio; retomada após mudança material. Nenhum desses estados cria avaliação verificada por presunção.

## 4. Contrato candidato de continuidade da autora

A autora deverá poder localizar suas avaliações legítimas sem depender de retornar à oportunidade, atividade ou Coletivo original. A consulta distingue rascunho, enviada, publicada, contestada, em revisão, limitada, retirada e outros estados aplicáveis definidos por UXA-057. A consulta não expõe identidade ou participação protegida fora do escopo autorizado.

A continuidade deverá distinguir **atualizar a mesma experiência** de **avaliar uma experiência materialmente nova**, preservando objeto, edição, período, versão de critérios e histórico. Alterações de visibilidade e retirada deverão explicar efeitos sobre comentário público, agregado, retenção e integridade, sujeitos à política especializada ainda pendente. Contestação de moderação e denúncia de resposta inadequada são ações diferentes, com alçadas e retornos próprios.

**Ponto de acesso permanente:** a localização final continua pendente de adjudicação. PER-009 pode ser investigada como entrada para direitos transversais, mas não recebe o contrato especializado sem extensão expressa.

## 5. Alternativas de materialização para adjudicação futura

| Alternativa | Condição de viabilidade | Risco a testar | Estado |
|---|---|---|---|
| Um contrato especializado com dois modos (registro e continuidade) | Demonstrar que estados, permissões, retorno e acesso permanente permanecem inequívocos | Misturar formulário contextual com administração histórica | Candidata, não escolhida |
| Dois contratos especializados (registro e continuidade) | Demonstrar independência de ciclo de vida e necessidade de entradas/retornos distintos | Fragmentar uma mesma avaliação e duplicar autoridade | Candidata, não escolhida |
| Extensão de superfícies existentes | Comprovar aderência funcional de cada Master e limites de autoridade sem sobrecarga | Transferir poderes por analogia a PER-108, PER-203 ou PER-009 | Não demonstrada |

A escolha depende de inventário atualizado, cobertura inicial aprovada, proteção de identidade, evidência de necessidade e revisão dos Masters. Não derivar IDs de alternativas ou do número de estados.

## 6. Handoffs a especificar, sem criar transições

- **Entrada contextual → registro:** origem autorizada, objeto/edição/etapa, identidade protegida, motivo de elegibilidade e revalidação no destino.
- **Registro → origem:** retorno neutro após envio, recusa, interrupção ou falha, sem alterar vínculo ou etapa da oportunidade.
- **Registro → continuidade:** referência estável da avaliação, sem duplicar submissão.
- **Continuidade → proteção especializada:** contestação de moderação ou denúncia de resposta, com fundamento, autoridade, estado e retorno proporcionais.
- **Continuidade → objeto original:** somente quando o objeto e a versão ainda existirem e a pessoa mantiver autorização; indisponibilidade não elimina o acesso legítimo à própria avaliação.

Cada futuro handoff exige origem/destino efetivos no Registry, pré-condições, identidade do objeto, retorno, falha, interrupção e idempotência. Nenhum `GKR-TRN-*` é proposto aqui.

## 7. Critérios para adjudicação

1. Confirmar cobertura inicial e evidências por etapa; não presumir participação a partir de inscrição.
2. Inspecionar Masters/Registry vigentes de PER-108, PER-203 e PER-009 antes de qualquer extensão.
3. Validar acesso permanente, atualização, retirada, visibilidade e contestação sem ampliar indevidamente poderes da autora ou do responsável.
4. Decidir uma ou duas responsabilidades especializadas materializadas com base em ciclo de vida e handoffs, não na quantidade de estados.
5. Submeter IDs, transições, mudanças de autoridade, maturidade e eventual liberação de desenho a gates separados.

## 8. Estado

**DRAFT / NON-NORMATIVE / PARTITION CANDIDATE / NO SURFACE SELECTED / NO NEW IDS / NO TRANSITIONS / NO MATURITY PROMOTION / NO DESIGN OR ENGINEERING RELEASE.**

Esta proposta não altera UXA-057, registries, Masters, gaps, Current State Register ou a operação de avaliações.
