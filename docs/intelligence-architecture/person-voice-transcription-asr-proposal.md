---
id: GKR-INT-PERSON-VOICE-ASR-PROPOSAL-001
title: Proposta — Transcrição de Voz na Jornada da Pessoa — Camada ASR
status: proposed
version: 0.1.0
owner: Guivos Intelligence / Arquitetura da Experiência
last_updated: 2026-10-27
normative: false
maturity: candidate_architecture_decision
related:
  - GKR-UX-PER003-MASTER-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
---

# Proposta — Serviço especializado de transcrição de voz na Jornada da Pessoa

> **Proposta para revisão e adjudicação.** Não constitui aprovação de fornecedor, contrato, licença, segurança ou liberação para produção. Não promove maturidade de PER-004, PER-005, PER-006 ou transições.

## 1. Problema e objetivo

A Guivos Intelligence prevê colaboração de três famílias de modelos — GPT, Anthropic e Gemini — para operações cognitivas autorizadas. **Transcrição (ASR) não é compreensão do Momento Atual.** A Pessoa deve poder narrar por voz e revisar a representação textual antes de decidir solicitar ajuda temporária ou autorizar elaboração da compreensão inicial.

## 2. Decisão técnica candidata

- **Transcrição principal proposta:** Google Gemini API, modelo `gemini-3.5-transcribe`, modalidade não streaming inicialmente, modo `verbatim` (transcrição literal).
- **Contingência candidata:** OpenAI `gpt-4o-transcribe` somente após validação de custo, privacidade, precisão e regras para falha; não enviar automaticamente ao segundo fornecedor sem base legal e transparência.
- **Anthropic/Claude:** não designado como engine de ASR. Permanece entre as inteligências de análise textual quando essa finalidade estiver autorizada.
- Modelo configurável e substituível; decisão definitiva depende de teste comparativo em PT-BR e ambientes de uso reais. Não equiparar escolha do fornecedor à autorização de processamento ou uso futuro.

Referências técnicas públicas (consultadas em 2026-10-27):
- https://ai.google.dev/gemini-api/docs/transcribe
- https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe
- https://platform.openai.com/docs/guides/speech-to-text

## 3. Fluxo funcional e autoridades existentes

1. **PER-003:** Pessoa escolhe Voz conscientemente, sem iniciar microfone ou transcrição.
2. **PER-004:** escolha explícita do tratamento do áudio; gravação perceptível, concluir gravação e solicitar transcrição sob finalidade específica.
3. **ASR:** devolver transcrição textual marcada como automática/não confirmada, com controle de erros, indisponibilidade e resultado parcial; registrar proveniência, modelo/versão, idioma, data e correções sem misturar áudio e texto.
4. **PER-004:** Pessoa revisa e corrige, podendo rejeitar, descartar, conservar/remover áudio conforme política e escolher continuar com o original. A ajuda temporária de organização por IA é opt-in distinto e produz item derivado separadamente revisável; nunca substitui a origem silenciosamente.
5. **PER-005:** inventário de origem, transcrição revisada e derivado conscientemente incluído; nenhuma autorização de compreensão pré-marcada.
6. **PER-006 e PER-007:** processamento apenas dos itens/finalidades autorizados e compreensão inicial revisável. O fato de Gemini ter transcrito **não** autoriza compartilhamento com GPT, Anthropic ou Gemini para análise da vida da Pessoa.

Não criar novo PER-ID ou superfície visual para ASR. ASR é serviço sob a responsabilidade de PER-004.

## 4. Integração Replit — pré-produção

- Isolar provedor/modelo de ASR em configuração do servidor, com chaves somente em secrets e sem exposição no cliente.
- Executar transcrição real somente se houver credenciais, integração validada e autorização operacional pertinente. Sem integração, não alegar que uma gravação foi transcrita; usar simulação de demonstração apenas em contexto de testes.
- Não usar modo `smart` como fonte primária de palavras da Pessoa; refinamento posterior requer controle separado.
- Avaliar limite/tamanho/formato de áudio e custo por minuto; controlar tentativas, falhas, cancelamento, proteção contra repetição e descarte.
- Evitar envio paralelo do mesmo áudio às três IAs para transcrever. O processamento cognitivo posterior deve ter autorização própria.

## 5. Gates abertos para decisão institucional

- Avaliar qualidade com amostras consentidas de fala espontânea em português brasileiro, diferentes sotaques, ruído e nomes próprios.
- Definir retenção do áudio, exclusão efetiva, região/transferência internacional, subprocessadores, auditoria e fundamentos de privacidade/LGPD.
- Definir limites de duração, custo, limites de tamanho, latência, política de contingência e critérios de indisponibilidade.
- Validar conveniência de `verbatim` versus alternativas para acessibilidade sem sobrepor texto de origem e síntese.
- Homologar contrato de autorização para a transcrição e impedir que aceite para ASR seja interpretado como aceite para compreensão posterior.
- Submeter à autoridade competente do GKR antes de marcar `approved`/operacional.

## 6. Resultado pretendido

Transcrição é uma etapa técnica especializada para converter voz em conteúdo revisável da Pessoa. A arquitetura GPT + Anthropic + Gemini permanece independente como camada cognitiva de análises autorizadas, sem promover automaticamente os três modelos a receptores do áudio.
