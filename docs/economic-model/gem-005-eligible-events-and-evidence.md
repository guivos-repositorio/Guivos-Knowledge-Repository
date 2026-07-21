---
id: GEM-005-ELIGIBLE-EVENTS-EVIDENCE-001
title: Eventos Elegíveis e Evidências
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Eventos Elegíveis e Evidências

## 1. Objetivo

Definir condições mínimas para que uma ação, contribuição ou transação possa originar progresso, reconhecimento ou recompensa.

## 2. Evento elegível

Um evento será elegível somente quando possuir:

- objetivo legítimo;
- regra anterior à ação;
- ator elegível;
- período definido;
- limite aplicável;
- evidência proporcional;
- fonte de financiamento, quando econômico;
- prevenção de duplicidade;
- tratamento de erro;
- possibilidade de contestação.

## 3. Evento verificado

Evento elegível acompanhado das evidências mínimas requeridas e submetido à autoridade de validação correspondente.

Verificação não significa, por si só:

- impacto comprovado;
- mérito universal;
- obrigação econômica;
- autorização de emissão;
- conformidade especializada.

## 4. Catálogo inicial de eventos

### Participação e aprendizagem

- conclusão de conteúdo;
- participação em experiência;
- etapa de jornada;
- atividade formativa;
- presença validada.

### Contribuição

- produção de conteúdo;
- apoio profissional;
- moderação;
- contribuição comunitária;
- voluntariado;
- participação em pesquisa.

### Relação econômica

- compra elegível;
- reserva concluída;
- contratação;
- indicação consentida e validada;
- renovação autorizada.

### Evolução pessoal

- objetivo concluído;
- hábito registrado;
- reflexão;
- atualização de contexto;
- participação em plano de desenvolvimento.

Eventos de evolução pessoal devem priorizar progresso e reconhecimento, não recompensa econômica automática.

## 5. Eventos de controle reforçado

Exigem avaliação adicional:

- saúde;
- atividade física;
- finanças;
- espiritualidade;
- estado emocional;
- compra e gasto;
- indicação;
- produtividade;
- participação de menores;
- localização;
- biometria;
- ação com risco físico;
- dados sensíveis;
- impacto sobre terceiros.

## 6. Níveis de evidência

| Nível | Descrição | Uso típico candidato |
|---|---|---|
| E0 | autodeclaração | progresso pessoal de baixo risco |
| E1 | confirmação simples de terceiro | participação ou contribuição básica |
| E2 | registro de sistema ou parceiro | transação, acesso ou presença |
| E3 | documento verificável | certificação, horas ou entrega |
| E4 | validação humana independente | evento relevante ou contestado |
| E5 | múltiplas fontes consistentes | alto risco ou alta responsabilidade |

## 7. Proporcionalidade

O nível exigido deverá considerar:

- valor econômico da recompensa;
- risco de fraude;
- sensibilidade dos dados;
- impacto sobre terceiros;
- reversibilidade;
- custo de verificação;
- possibilidade de erro;
- acessibilidade;
- escala.

Autodeclaração poderá ser suficiente para progresso pessoal, mas poderá ser insuficiente para recompensa econômica relevante.

## 8. Registro mínimo do evento

```yaml
eligible_event_id: string
program_id: string
event_type: string
layer:
  progress |
  recognition |
  economic_reward
eligible_actor: string
period: string
limits:
  - string
required_evidence_level: string
evidence_sources:
  - string
funding_required: boolean
duplicate_key: string | null
verification_authority: string
appeal_available: true
status: candidate
```

## 9. Duplicidade

Deverão ser considerados:

- mesmo evento em mais de um programa;
- reenvio do mesmo documento;
- mais de uma conta;
- registro por participante e parceiro;
- evento cancelado e recriado;
- indicação atribuída a múltiplos canais;
- compra seguida de devolução;
- horas sobrepostas;
- confirmação entre partes relacionadas.

A chave de duplicidade deverá ser adequada ao contexto e minimizar dados.

## 10. Qualidade da evidência

Uma evidência deverá ser:

- pertinente;
- suficiente;
- íntegra;
- temporalmente relacionada;
- acessível à revisão autorizada;
- minimizada;
- armazenada pelo período necessário;
- contestável;
- protegida contra alteração indevida.

## 11. Autoridade

A autoridade futura poderá envolver:

- sistema;
- parceiro;
- organização responsável;
- profissional;
- moderador;
- revisor humano;
- combinação de fontes.

O financiador não será automaticamente a autoridade sobre a veracidade do evento.

## 12. Erro e contestação

Toda decisão material deverá permitir:

- razão compreensível;
- correção de dados;
- nova evidência;
- revisão humana quando necessária;
- registro da decisão;
- suspensão proporcional;
- resultado documentado.

## 13. Dados

Não deverá ser coletado dado adicional apenas porque uma recompensa existe. A evidência deverá ser a mínima necessária para o risco e a finalidade.

## 14. Fora do escopo

- catálogo final por produto;
- integrações;
- documentos aceitos;
- algoritmos de validação;
- limites quantitativos;
- implementação.
