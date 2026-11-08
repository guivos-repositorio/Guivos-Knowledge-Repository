---
title: Grafo Vivo — Quadro Focal de Fronteiras Funcionais
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: diagnostic_non_operational
---

# Grafo Vivo — Quadro Focal de Fronteiras Funcionais

> Diagnóstico documental condicionado, sem seleção definitiva de localização, autoridade adicional, transição ou tecnologia. Preserva as autoridades de PER-007/008/010/011/012, PAS-001, GPA-006/GIA-COG-001, Surface Registry e Transition Registry.

## 1. Objeto

Separar e confrontar cinco capacidades do Grafo Vivo da Jornada: (F1) síntese em Hoje; (F2) exploração expandida; (F3) explicação narrada; (F4) conversa contextual; (F5) persistência de informações novas. Evitar que a adoção de uma interface multimodal amplie por inferência responsabilidades de domínio ou permissões pessoais.

## 2. Matriz focal

| Capacidade | Finalidade proposta | Fronteira vigente identificada | Compatibilidade documental | Decisão pendente |
| --- | --- | --- | --- | --- |
| **F1 — Síntese em Hoje** | Apresentar conteúdo contextual autorizado, conciso e revisável, com possível escolha de modalidade | PER-008 já governa síntese de primeira entrada e retorno; proíbe score humano, histórico ou urgência fabricados | **Potencialmente compatível**, caso opcional e fundamentado | Autorizar ou não affordance interno e delimitar conteúdo |
| **F2 — Exploração expandida** | Examinar múltiplos nós, filtros, relações, possibilidades e cenários | PER-008 não absorve funções de Objetivos, Passos e Evolução; rotas entre PER-010/011/012 não são diretas | **Insuficiente para implantação**; requer competência e posição funcional | Estado em superfície existente, aprofundamento especializado ou eventual novo escopo, após Registry |
| **F3 — Explicação narrada** | Escutar síntese e, eventualmente, relatório aprofundado versionado | Conteúdo e finalidade de PER-008; explicações de outros domínios seguem seus próprios contratos; permissões de dados independentes | **Síntese de Hoje potencialmente compatível**; relatório integral requer adjudicação | Alcance, versão do contexto, autorização, acessibilidade, armazenamento de áudio |
| **F4 — Conversa contextual** | Perguntar por texto/voz, esclarecer conexões, explorar hipóteses, interromper narração | Intelligence interpreta sob GIA-COG-001/GPA-006; diálogo não altera objetos de domínio por si | **Explicação candidata**; continuidade transversal e ações com efeitos carecem de contrato | Dono funcional do diálogo, contexto de sessão, gatilhos de confirmação e integridade |
| **F5 — Persistência de novas informações** | Incorporar fatos declarados e correções à compreensão contínua | PER-007 exige decisões independentes de persistência e personalização; governança da Journey/dados permanece | **Não autorizada apenas por PER-008 ou pela conversa** | Finalidade, base/autorização aplicável, vigência, origem, correção/revogação, retenção e propagação |

**Classificações são diagnósticas, não estados normativos.** Potencial compatibilidade não autoriza criação de botões, comportamento operacional ou API.

## 3. Fronteiras entre as cinco capacidades

### F1 → F2 — Da síntese à exploração

A apresentação de uma conexão contextual em Hoje não permite inferir a existência de nova superfície, rota ou editor de nós. Se o aprofundamento versar sobre objetivo, Próximo Passo ou evolução, manter a responsabilidade de PER-010, PER-011 ou PER-012. Para exploração transversal, competência e transição continuam pendentes de adjudicação.

### F1 → F3 — Da leitura à escuta

A narração equivalente da síntese pode ser examinada como alternativa de acesso ao mesmo conteúdo, desde que haja informação essencial textual, versão identificável e finalidade legítima. Um relatório completo que incorpore interpretação temporal ou recomendações especializadas ultrapassa automaticamente o escopo de mera equivalência e demanda exame específico.

### F3 ↔ F4 — Da escuta ao diálogo

Interromper áudio para perguntar é uma possibilidade de UX, não autorização para persistir a gravação, transcrição ou resposta. A consulta ao trecho narrado pode usar contexto mínimo e referência à versão de análise. Se novas informações legitimamente alterarem o contexto, a narração anterior deve continuar reconhecível como versão anterior ou ser explicitamente substituída por nova versão, nunca reescrita silenciosamente.

### F4 → F5 — Da conversa à memória

A Intelligence pode identificar uma afirmação candidata, mas sua consolidação não decorre apenas de ter sido falada. Identificar:
- declaração da Pessoa;
- hipótese/inferência;
- pergunta contrafactual;
- revisão, correção ou contestação;
- dado potencialmente sensível;
- relevância e finalidade;
- autorização/decisão vigente de persistência e personalização.

Quando não existir permissão, limitar o tratamento à finalidade temporária legitimamente autorizada e não presumir continuidade entre sessões. Persistência é diferente de personalização. Permissão geral de conversar não equivale a permissão de memória duradoura.

### F5 → F1/F2/F3 — Da mudança governada à apresentação

Após uma alteração legitimamente consolidada, efeitos derivados devem respeitar proveniência, versão, escopo de acesso e temporalidade. Grafo, síntese e áudio não podem exibir dados revogados como vigentes. A diferença entre estados pode ser explicada, mas não convertida em evolução humana reconhecida sem PER-012 e PAS-001.

## 4. Fluxo focal com gates

```text
PESSOA EM HOJE (PER-008)
  → síntese contextual autorizada (F1)
  ├─ exploração visual opcional (F2, localização pendente)
  ├─ escuta de síntese ou relatório (F3, escopo pendente)
  └─ conversa contextual (F4, competência pendente)
       → extração de informação candidata
       → classificação / proveniência / sensibilidade
       → GATE: finalidade + persistência + personalização independentes
       → GATE: necessidade de confirmação/correção
       → consolidação por autoridade competente (F5)
       → projeções derivadas reavaliadas
       → atualização explicável de F1/F2 e oferta de nova versão F3
```

Se um gate não estiver satisfeito, a experiência deve retornar a caminho legítimo de esclarecimento ou uso temporário permitido; não realizar gravação silenciosa.

## 5. Contratos de entrada e saída — candidatos, não APIs

| Capacidade | Entradas legitimamente possíveis | Saída conceitual | Nunca assume |
| --- | --- | --- | --- |
| F1 | Contexto confirmado/autorizado/vigente e estados canônicos | Síntese concisa, ausência explícita, aprofundamentos já legítimos | Criação de objetivos/passos/evolução |
| F2 | Subgrafo permitido, origem, incerteza, instante e cenário | Relações e explicação navegáveis | Fonte única de verdade, navegação não contratada |
| F3 | Snapshot de análise autorizado, roteiro, escopo de divulgação | Áudio e texto correspondentes, com versão | Nova evidência, autorização, guarda ilimitada |
| F4 | Pergunta, contexto mínimo, referência da conversa/snapshot | Resposta contextual e possíveis informações candidatas | Decisão pela Pessoa, escrita de domínio automática |
| F5 | Candidata classificada + decisões e verificações necessárias | Atualização válida ou pendência/recusa, evento rastreável se autorizado | Personalização presumida, reescrita da origem |

## 6. Dependências de integração por fronteira

- **Journey / autoridade transacional:** identidade, estados, autorizações e objetos canônicos.
- **Guivos Intelligence:** interpretação governada, detecção de lacunas, explicação, reavaliação e classificação de afirmações candidatas.
- **Representação em grafo:** projeção relacional por Pessoa e finalidade; Neo4j Aura permanece candidato técnico, não autoridade sobre os fatos.
- **Grok/xAI:** candidato prioritário para síntese de voz e conversação em tempo real, sem autoridade de memória, autorização ou mutação de objetos.
- **Gemini e outras alternativas de STT:** transcrição revisável, distinta de afirmação validada ou conteúdo persistível.
- **Autenticação e segurança:** privilégio mínimo e separação entre usuário, provedores, cache e dados derivados.
- **Evolução (PER-012):** determina critérios aplicáveis à trajetória, evidência, baseline e interpretação; alteração gráfica não comprova progresso.
- **Surface/Transition Registries:** determinam se há lugar legítimo para os modos e quais handoffs são reconhecidos.

## 7. Quadro de decisões pendentes

| Questão | Alternativas em estudo | Evidência/competência necessária | Estado |
| --- | --- | --- | --- |
| D-01 — Porta de entrada | resumo em Hoje; entrada para exploração expandida; distribuição por superfícies existentes | PER-008 + Surface Registry + UX/Journey | Não adjudicado |
| D-02 — Escopo de F2 | leitura de subgrafo; simulações; aprofundamentos especializados | PER-010/011/012 + PAS-001 + Intelligence | Não adjudicado |
| D-03 — Forma de F3 | áudio equivalente de Hoje; relatório por capítulos; narração com destaques no grafo | contratos de conteúdo, acessibilidade, dados e versão | Não adjudicado |
| D-04 — Canal F4 | estado interno, canal transversal ou responsabilidade autônoma | Surface/Transition Registries + GIA | Não adjudicado |
| D-05 — Política F5 | contexto só na sessão; persistência autorizada; personalização separada | PER-007, privacidade, segurança, dados, GIA | Não adjudicado |
| D-06 — Atualizações | avisos discretos; resumo de mudanças; regeneração opt-in de narração | proveniência, temporalidade, controle da Pessoa | Não adjudicado |
| D-07 — Envio a provedores | dados mínimos para TTS/voz e LLMs; alternativas locais/gerenciadas | exame jurídico, segurança, custo e qualidade | Não adjudicado |
| D-08 — Planos | uso comum ou diferenças por capacidade, se existir fundamento contratual | autoridades atuais de Free/Plus/Pro | Não adjudicado |

Nenhuma opção foi selecionada. Nenhum `D-xx` desta tabela constitui novo identificador oficial; trata-se apenas de referência local ao estudo.

## 8. Recomendações documentais para continuidade

1. **Prioridade 1:** delimitar F1 como explicação de síntese em Hoje sem modificar PER-008, e determinar se F2/F3/F4 exigem responsabilidades distintas. Elaborar confronto focal com Surface Registry e Transition Registry.
2. **Prioridade 2:** aprofundar F4→F5, separando uso de contexto na sessão, persistência e personalização; examinar direitos de revisão, revogação e exclusão antes de contratos de integração.
3. **Prioridade 3:** elaborar matriz de passagem de dados Journey ↔ Intelligence ↔ grafo ↔ voz, com finalidades, versões, limites e falhas.
4. **Prioridade 4:** somente após adjudicação das autoridades, escolher tecnologias e exigir autorizações específicas para protótipos/testes/engenharia.

## 9. Parecer

O maior risco arquitetural não é a escolha da tecnologia de grafo ou do provedor de voz. É **confundir apresentar, compreender, conversar, persistir e decidir** como se fossem a mesma operação.

**Parecer condicionado:** manter F1 como ponto de aproximação mais diretamente compatível com Hoje; tratar F2/F3 ampliada/F4 como capacidades ainda carentes de delimitação funcional; F5 só pode ocorrer dentro de autorização e autoridade vigentes, sem transferência de competência ao grafo ou à voz.

**Sem efeitos normativos, implementação, APIs, Design operacional, novos IDs, testes ou publicação.**
