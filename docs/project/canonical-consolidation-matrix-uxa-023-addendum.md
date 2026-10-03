---
id: GKR-CANON-MATRIX-UXA-023
title: Adendo da Matriz de Consolidação Canônica — Validação do Início Protegido da Jornada
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-26
depends_on:
  - GKR-CANON-MATRIX-001
  - UXA-020
  - UXA-023
related:
  - GKR-STATE-001
  - ROADMAP-11.98.0
  - UXA-011-A1
  - M7.24
normative: false
---

# Adendo da Matriz de Consolidação Canônica — Validação do Início Protegido da Jornada

## 1. Finalidade

Este adendo registra as decisões consolidadas da primeira validação funcional detalhada do início protegido da jornada pessoal.

Ele não substitui a Matriz de Consolidação Canônica e não autoriza wireframe, protótipo, design, tecnologia ou desenvolvimento.

## 2. Decisões consolidadas

| Elemento | Decisão | Resultado consolidado |
|---|---|---|
| início protegido da jornada | Validar e reformular | superfície considerada funcionalmente válida após reformulação |
| transição a partir da Home | Tornar consciente | pessoa entende que saiu da superfície pública e que nenhuma coleta começou |
| explicação do processo | Anteceder autenticação | etapas, modalidades e controles podem ser conhecidos antes da conta |
| autenticação | Exigir antes de persistência e processamento associado | conta protege continuidade, mas não autoriza todos os usos |
| criação de conta | Separar de autorização | conta não libera gravação, transcrição, análise ou personalização |
| autorização genérica | Rejeitar | finalidades materiais exigem decisões específicas quando aplicáveis |
| compartilhamento | Minimizar e tornar progressivo | pessoa pode iniciar com pouco e compartilhar mais somente quando fizer sentido |
| modalidades | Manter alternativas | texto, voz, arquivos e perguntas não são obrigatórios nem superiores entre si |
| texto | Tornar revisável | digitação não equivale a autorização de processamento |
| voz | Separar gravação e transcrição | áudio, transcrição, correção, regravação e remoção possuem controles próprios |
| arquivos | Limitar finalidade e extração | envio não autoriza leitura irrestrita nem uso total |
| fontes externas | Exigir autorização limitada | origem, finalidade, escopo, correção e desconexão permanecem visíveis |
| inventário do relato | Exigir antes do processamento | conteúdos recebidos podem ser editados, removidos, substituídos ou limitados |
| estados funcionais | Tornar explícitos | rascunho, revisão, autorização, processamento, falha, pausa, exclusão e encerramento são distintos |
| processamento | Tornar visível e interrompível | finalidade, fontes, estado, falhas e controles permanecem acessíveis |
| pausa | Manter legítima | interrompe sem avanço automático |
| retirada de autorização | Separar de exclusão | efeitos futuros e conteúdos existentes são explicados |
| exclusão | Distinguir níveis | item, relato, informação derivada e encerramento não são a mesma ação |
| informações sensíveis | Aplicar proteção adicional | escopo pode ser reduzido ou processamento incompatível pode ser bloqueado |
| informações de terceiros | Não presumir autorização | envio por uma pessoa não representa consentimento das demais |
| conteúdo original e derivado | Distinguir | original, transcrição, extração, correção e interpretação permanecem identificados |
| compreensão inicial | Tornar revisável | confirmado, observado, externo autorizado, inferido, desconhecido e contestado são distintos |
| confirmação parcial | Permitir | informação não confirmada não vira fato silenciosamente |
| gate de personalização | Exigir | personalização somente após base suficiente, revisão e autorização |
| jornada sem personalização | Manter disponível | pessoa pode continuar sem recomendações pessoais |
| exploração geral | Manter disponível | pessoa pode retornar ao ecossistema sem concluir o relato |
| Tela Hoje | Manter posterior ao gate | não constitui recompensa por maior exposição de dados |
| wireframe do início protegido | Manter pendente | não iniciado |
| tecnologia e implementação | Manter pendentes | não iniciadas |

## 3. Hierarquia validada

```text
identificação do ambiente protegido
→ explicação curta do que acontecerá
→ alternativas legítimas antes da autenticação
→ autenticação e recuperação de acesso
→ finalidades, privacidade e controles
→ escolha de modalidade
→ relato mínimo e progressivo
→ revisão dos conteúdos recebidos
→ autorização específica de processamento
→ estado de processamento e possibilidade de interrupção
→ compreensão inicial revisável
→ decisão sobre uso e continuidade
```

## 4. Estados mínimos

- não iniciado;
- autenticação pendente;
- privacidade pendente;
- rascunho;
- aguardando revisão;
- autorizado para processamento;
- em processamento;
- ação necessária;
- compreensão disponível;
- pausado;
- exclusão solicitada;
- encerrado.

## 5. Estado empresarial preservado

- 18 de 18 decisões humanas concluídas;
- 9 candidatos em validação;
- 3 candidatos fundidos;
- 6 candidatos rejeitados;
- nenhum Resultado aprovado;
- nenhum código canônico criado;
- reaplicação dos quatro testes não iniciada;
- AQS-O01 e Capacidades Empresariais não iniciados.

## 6. Limites

Este adendo não:

- cria wireframe gráfico;
- cria referência móvel da Home;
- define tecnologia de autenticação;
- define formatos técnicos de voz ou arquivos;
- define armazenamento, criptografia ou infraestrutura;
- define modelo de inteligência artificial;
- autoriza inferências sensíveis;
- cria protótipo ou design;
- executa testes com usuários;
- inicia Engenharia de Produto;
- inicia a reaplicação dos testes dos Resultados Empresariais.
