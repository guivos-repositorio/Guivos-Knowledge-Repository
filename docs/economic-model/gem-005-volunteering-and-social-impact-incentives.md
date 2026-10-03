---
id: GEM-005-VOLUNTEERING-SOCIAL-IMPACT-INCENTIVES-001
title: Incentivos de Voluntariado e Impacto Social
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Incentivos de Voluntariado e Impacto Social

## 1. Objetivo

Definir como participação voluntária, contribuição, reconhecimento, recompensa e impacto social deverão permanecer separados e verificáveis.

## 2. Sequência de referência

```text
participação
→ evidência de contribuição
→ reconhecimento contextual
→ recompensa opcional financiada
→ impacto avaliado separadamente
```

Esses elementos não são equivalentes.

## 3. Princípios

1. a ação continuará válida sem recompensa econômica;
2. voluntariado não será reduzido a transação;
3. recompensa não medirá bondade;
4. horas não provarão impacto;
5. organização responsável deverá ser verificada;
6. pessoas beneficiárias serão protegidas;
7. patrocinador será identificado;
8. atividade deverá possuir condições de segurança;
9. relação de trabalho não será mascarada;
10. evidência será proporcional e contestável.

## 4. Tipos de contribuição

- participação presencial;
- participação remota;
- apoio técnico;
- mentoria;
- produção de conteúdo;
- mobilização;
- doação de produto;
- doação de serviço;
- organização de ação;
- suporte logístico;
- contribuição recorrente;
- competência profissional.

## 5. Registro de participação

```yaml
volunteering_event_id: string
organization_id: string
activity: string
participant_id: string
role: string
period: string
hours_declared: number | null
evidence_level: string
verification_authority: string
safety_requirements:
  - string
beneficiary_data_involved: false
recognition_eligible: boolean
reward_eligible: boolean
impact_claimed: false
status: string
```

## 6. Reconhecimento

Poderá incluir:

- certificado;
- registro de horas;
- agradecimento;
- selo contextual;
- histórico de contribuição;
- credencial de participação.

Deverá indicar:

- organização;
- atividade;
- papel;
- período;
- critério;
- evidência;
- limitações.

## 7. Recompensa opcional

Uma recompensa somente poderá existir quando:

- programa estiver previamente definido;
- fonte de financiamento estiver confirmada;
- evento for elegível;
- evidência for suficiente;
- benefício estiver disponível;
- responsabilidade estiver atribuída;
- comunicação deixar claro que a recompensa não mede mérito humano.

## 8. Patrocínio

O patrocinador poderá financiar:

- benefícios;
- transporte;
- alimentação;
- equipamentos;
- experiências;
- bolsas;
- acesso;
- reconhecimento público identificado;
- matching de recompensas;
- orçamento restrito de campanha.

O patrocinador não poderá:

- alterar horas ou evidências;
- selecionar narrativa enganosa;
- exigir exposição indevida;
- controlar conclusões sobre impacto;
- revogar retroativamente benefício constituído e coberto;
- usar participantes ou beneficiários em publicidade sem base legítima.

## 9. Impacto social

Impacto deverá possuir registro próprio e poderá considerar:

- problema abordado;
- população ou território;
- atividade realizada;
- resultado entregue;
- evidência;
- atribuição e contribuição;
- externalidades;
- limitações;
- período;
- responsável pela avaliação.

Pontos, horas ou número de voluntários não constituem, isoladamente, impacto comprovado.

## 10. Proteção das pessoas beneficiárias

Não será admissível:

- exposição sem necessidade;
- uso de imagem sem base legítima;
- competição sobre sofrimento;
- divulgação de condição sensível;
- troca de benefício por exposição;
- promessa de resultado não comprovado;
- acesso de patrocinador a dados individuais sem autoridade.

## 11. Segurança da atividade

Deverão ser avaliados:

- local;
- supervisão;
- equipamentos;
- transporte;
- alimentação;
- acessibilidade;
- competência necessária;
- risco físico;
- contato com grupos protegidos;
- participação de menores;
- seguro ou autorização futura quando aplicável.

## 12. Relação de trabalho

O incentivo não poderá ser utilizado para substituir remuneração ou mascarar prestação de trabalho quando houver características incompatíveis com voluntariado legítimo.

Dependências trabalhistas e jurídicas deverão ser identificadas antes de qualquer operação.

## 13. Fraude e duplicidade

Riscos:

- organização inexistente;
- evento não realizado;
- horas infladas;
- presença duplicada;
- confirmação entre partes relacionadas;
- atividade incompatível com o período;
- documento alterado;
- recompensa emitida após cancelamento;
- patrocinador contabilizado mais de uma vez.

## 14. Gate social

Um programa futuro somente poderá avançar quando:

- organização estiver verificada;
- atividade e finalidade estiverem claras;
- segurança estiver analisada;
- participação for voluntária;
- evidência estiver definida;
- reconhecimento e recompensa estiverem separados;
- cobertura existir;
- beneficiários estiverem protegidos;
- impacto não for inferido dos pontos;
- responsabilidades e interrupções estiverem registradas.

## 15. Fora do escopo

- organizações específicas;
- seleção de causas;
- quantidade de pontos;
- contratação de patrocinadores;
- apólices;
- regulamentos;
- operação de voluntariado;
- mensuração final de impacto.
