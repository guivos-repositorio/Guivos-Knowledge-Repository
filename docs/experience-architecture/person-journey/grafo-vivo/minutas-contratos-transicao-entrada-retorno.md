---
title: Grafo Vivo — Duas Minutas Candidatas de Transição entre Hoje e a Experiência Expandida
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-08
normative: false
maturity: transition_drafts_pending_adjudication
---

# Grafo Vivo — Minutas Candidatas de Entrada e Retorno

> **Duas minutas documentais, não contratos vigentes.** A Direção aprovou a **necessidade** de contratos formais próprios (CT-02) e a diretriz R2 de responsabilidade funcional distinta, **mas não aprovou texto normativo, IDs, alterações de Surface/Transition Registries, implementação, testes ou publicação**.

## 1. Base e identidade funcional provisória

- **Origem da entrada e destino do retorno:** PER-008 — Hoje, conforme Master v0.1.0.
- **Destino da entrada e origem do retorno:** Grafo Vivo expandido — **responsabilidade distinta, sem identificador oficial**.
- **Alternativa B, R2 e CT-01/CT-02:** aprovadas **conceitualmente**; ver [decisão da Direção — R2](decisao-direcao-r2.md), [CT-01/02](decisao-direcao-ct01-ct02.md) e [contrato funcional candidato](contrato-funcional-candidato-passagem-retorno.md).
- **Surface Registry** v0.36.22 e **Transition Registry** v0.29.26 continuam fontes vigentes; o destino e os dois contratos ainda não estão incorporados.
- Transições existentes `TRN-007` e `TRN-008..013` **mantêm exatamente suas origens/destinos**, sem reutilização ou renumeração.

## 2. Minuta candidata de entrada — Hoje → Grafo Vivo

| Cláusula | Condição proposta, ainda sujeita à aprovação |
| --- | --- |
| Origem | PER-008 — Hoje, primeira entrada ou estado recorrente |
| Destino | Grafo Vivo expandido, responsabilidade distinta sob representação R2 ainda a formalizar |
| Gatilho | Ação expressa e voluntária da Pessoa, nunca abertura automática de modalidade |
| Pré-condição de identidade | Sessão legitimamente autenticada, sem bypass de PER-007 ou TRN-007 |
| Pré-condição de conteúdo | Contexto permitido, suficiente **para a finalidade e modalidade concretas**; ausência de histórico por si só não bloqueia |
| Envelope mínimo | Referência de sessão autorizada, origem, finalidade, contexto elegível, proveniência, versão ou indicador de vigência, estado pertinente de escolhas independentes |
| Renderização inicial | Compreensão atual, lacunas e relações sustentadas; ausência legítima e hipótese identificadas; alternativa textual |
| Consentimento e privacidade | A entrada não concede retenção, memória persistente, personalização, gravação/transcrição de voz ou transferência a fornecedor |
| Efeito de domínio | Nenhuma criação, confirmação, priorização ou conclusão de objetivo/passo/evolução |
| Falha e cancelamento | Cancelar abertura sem efeito; ausência ou revogação limita a apresentação; fallback seguro e explícito |
| Concorrência | Detectar mudanças de versão ou permissão antes de tratar projeção ou narrativa como atual |
| Idempotência | Repetir acionamento não duplica efeitos materiais, consentimento ou sessão persistida |
| Acessibilidade | Forma não exclusivamente visual, com comunicação de estados e saída explícita |
| Resultado | Entrada em responsabilidade distinta **somente quando contrato formal futuro permitir**, sem declarar mudança já validada |

**Questões em aberto:** regime documental de identidade do destino, contrato preciso de elegibilidade por modo e versão canônica, tratamento de conteúdo insuficiente, autorização efetiva de sessão e processamento por provedores.

## 3. Minuta candidata de retorno — Grafo Vivo → Hoje

| Cláusula | Condição proposta, ainda sujeita à aprovação |
| --- | --- |
| Origem | Grafo Vivo expandido, responsabilidade distinta ainda sem identificador oficial |
| Destino | PER-008 — Hoje |
| Gatilho | Comando explícito de retorno; saída de recuperação quando incidente tornar necessária uma volta segura |
| Pré-condição | Não depende da conclusão de conversa, áudio, objetivo, ação ou progresso; exigir apenas segurança legítima do fluxo |
| Contexto de saída | Referências mínimas permitidas de sessão/retorno; não exportar o conjunto do grafo ou transcrição por padrão |
| Estado de áudio/conversa | Interromper produção/reprodução que não possa continuar autorizadamente, sem assumir retenção |
| Estado canônico | Reconsultar síntese vigente de Hoje e permissões; sinalizar ausência de confirmação quando a consulta falhar |
| Persistência | Não salvar automaticamente conversa, gravação, objetivo, passo ou alteração de preferência ao sair |
| Efeito de domínio | Retorno neutro, sem aceitar, iniciar ou concluir objeto e sem reconhecer evolução |
| Erro/revogação | Caminho de saída disponível quando possível; invalidar derivados desautorizados; evitar reexposição de conteúdo antigo |
| Idempotência | Retry de retorno não gera efeito material nem múltiplos registros de aceite |
| Acessibilidade | Retorno operável por teclado e leitores de tela, com alternativa ao controle visual |
| Resultado | Hoje em contexto legítimo; não declarar sucesso de reconsulta ou persistência sem evidência |

**Questões em aberto:** representação oficial da origem, tratamento de queda de sessão, interrupções em processamento assíncrono e política de retomada de contexto efêmero.

## 4. Modos internos e preservação de autoridade

**Explorar**, **Escutar** e **Conversar** são diferentes perspectivas na mesma responsabilidade funcional. Alternar apresentação/foco/forma de interação **não constitui um terceiro ou quarto contrato de transição por padrão**. Quando uma interação pretender modificar Objetivos (PER-010), Próximos Passos (PER-011) ou Evolução (PER-012), a autoridade especializada e suas transições efetivamente válidas deverão ser preservadas; relações do grafo não criam novos atalhos.

Guivos Intelligence detém a interpretação governada; a projeção em grafo, a narração e fornecedores de áudio **não são fontes canônicas**. Declaração, hipótese, confirmação, uso de sessão, persistência e personalização permanecem separados.

## 5. Matriz de suficiência para adjudicação posterior

| Critério | Cobertura destas minutas | Pendência para contrato normativo |
| --- | --- | --- |
| Distinção dos dois sentidos e efeitos neutros | Redigido conceitualmente | Aprovação específica de cláusulas e origem/destino oficiais |
| Compatibilidade com Hoje primeiro/recorrente | Examinado | Condições operacionais por contexto/modalidade |
| Identidade e maturidade do destino | R2 aprovada como diretriz | Registro/ID e owner/maturidade, mediante ato próprio |
| Contexto e proveniência | Envelope lógico candidato | Esquema e fontes permitidas aprovados |
| Versão, correção, revogação | Invariantes candidatos | Contratos de dados, controles e evidências de validação |
| Falha, concorrência, cancelamento, idempotência | Casos propostos | Sem testes nem validação operacional |
| Acessibilidade e fallback | Requisitos preliminares | Critérios de aceite e Design funcional autorizados |
| Relação com `TRN-007..013` | Não redirecionadas | Verificação final de Registry ao formalizar |

## 6. Pendências para a Direção

1. **Forma e maturidade do reconhecimento da responsabilidade R2** no Surface Registry, inclusive se e quando um identificador deverá ser atribuído por processo competente.
2. **Adjudicação das duas minutas** como base para futuros contratos formais, sem automaticamente lançá-las no Transition Registry.
3. **Escopo de dados e critérios de elegibilidade**: versão, finalidade, proveniência, persistência de sessão, privacidade, revogação e uso multimodal.
4. **Atos separados** para eventual reconciliação normativa e auditoria técnica do Replit; a aprovação de minutas não autorizará por si testes, implementação ou publicação.

**Parecer de encaminhamento:** submeter à Direção a **adoção destas duas minutas como base documental de reconciliação**, sujeita a contratos de dados e decisão posterior sobre identificação; sem afirmar que são transições já validadas ou operacionais.
