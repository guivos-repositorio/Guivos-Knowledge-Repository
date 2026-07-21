---
id: GEM-005
title: Incentivos e Recompensas
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-000
depends_on:
  - GEM-004
  - GEM-004-DEPENDENCY-VALIDATION-CHECKPOINT-001
related:
  - GEM-005-INCENTIVE-LAYER-ARCHITECTURE-001
  - GEM-005-POINTS-CREDITS-POLICY-001
  - GEM-005-REWARD-FUNDING-MODEL-001
  - GEM-005-INCENTIVE-PROGRAM-CONTRACT-001
  - M6.4
---

# GEM-005 — Incentivos e Recompensas

## 1. Objetivo

Definir como a Guivos poderá reconhecer contribuições, estimular comportamentos benéficos e oferecer recompensas sem transformar evolução humana em pontuação, criar dependência comportamental, emitir benefícios sem cobertura ou comprometer autonomia, dignidade, privacidade e propósito.

## 2. Pergunta arquitetural

> Quais incentivos podem apoiar participação, contribuição e evolução no Ecossistema Guivos, como devem ser financiados, registrados, verificados, concedidos, resgatados, revertidos e encerrados sem transformar pessoas, propósito ou impacto em mercadoria?

## 3. Sequência de referência

```text
comportamento ou contribuição legítima
→ critério previamente compreensível
→ evidência proporcional
→ validação
→ progresso, reconhecimento ou recompensa
→ utilização voluntária
→ aprendizagem e continuidade
```

Não é admissível utilizar ansiedade, culpa, vulnerabilidade, urgência artificial, competição humilhante ou loops compulsivos para induzir comportamento.

## 4. Camadas independentes

### Progresso

Registra avanço em atividade, jornada, objetivo ou experiência. Não possui valor monetário, não é transferível e não representa valor humano.

### Reconhecimento

Registra contribuição ou participação em contexto determinado. Deve possuir fonte, critério, possibilidade de correção e não poderá ser comprado.

### Recompensa econômica

Representa benefício resgatável, desconto, produto, serviço, experiência, acesso ou utilidade financiada. Exige fonte de cobertura, responsabilidade, ciclo de vida e controles.

### Separação canônica

```text
progresso ≠ reconhecimento ≠ recompensa econômica
```

## 5. Princípios

1. incentivo deverá apoiar valor legítimo;
2. ação continuará significativa mesmo sem recompensa econômica;
3. progresso não será moeda;
4. reconhecimento não será reputação universal;
5. ponto não representará valor humano;
6. recompensa resgatável exigirá fonte ou capacidade identificada;
7. regra de ganho será anterior e compreensível;
8. evidência será proporcional ao risco;
9. emissão, resgate, expiração e reversão serão rastreáveis;
10. fraude e duplicidade possuirão tratamento;
11. participação permanecerá voluntária;
12. menores e grupos vulneráveis exigirão proteção reforçada;
13. patrocinador não comprará mérito ou autoridade;
14. nenhum valor monetário será definido nesta versão;
15. nenhuma regra será implementada por este ciclo.

## 6. Famílias iniciais

1. IF-01 — Progresso e Marcos;
2. IF-02 — Reconhecimento Simbólico;
3. IF-03 — Pontos de Recompensa;
4. IF-04 — Descontos e Condições Especiais;
5. IF-05 — Produtos, Serviços e Experiências;
6. IF-06 — Acesso e Capacidade;
7. IF-07 — Incentivos Patrocinados;
8. IF-08 — Incentivos Sociais e Comunitários;
9. IF-09 — Doação ou Direcionamento de Benefício;
10. IF-10 — Incentivos Organizacionais.

## 7. Fontes de financiamento

- orçamento Guivos;
- patrocinador;
- parceiro fornecedor;
- organização contratante;
- fundo social ou recurso vinculado;
- receita futura de campanha autorizada;
- benefício não monetário;
- combinação híbrida.

Nenhuma promessa não confirmada poderá sustentar emissão resgatável.

## 8. Estados de recompensa

- `candidate`;
- `eligible`;
- `pending_verification`;
- `approved`;
- `issued`;
- `available`;
- `reserved`;
- `redeemed`;
- `rejected`;
- `expired`;
- `cancelled`;
- `reversed`;
- `disputed`;
- `suspended`.

## 9. Requisitos mínimos de admissibilidade

Um programa somente poderá avançar quando:

- comportamento desejado e valor esperado estiverem claros;
- camada do incentivo estiver definida;
- elegibilidade e grupos protegidos estiverem registrados;
- evento e evidência estiverem especificados;
- fonte de financiamento existir quando houver recompensa econômica;
- responsabilidade pela entrega estiver atribuída;
- emissão, validade, resgate e reversão estiverem documentados;
- riscos comportamentais, de fraude e de dados estiverem avaliados;
- contestação e interrupção forem possíveis;
- dependências especializadas estiverem reconhecidas.

## 10. Limites desta versão

O GEM-005 não define:

- quantidade ou valor monetário de pontos;
- taxa de conversão;
- orçamento ou limite financeiro;
- transferência, saque ou negociação;
- token, criptomoeda ou blockchain;
- patrocinadores ou parceiros específicos;
- regulamento promocional final;
- contratos;
- tributação ou reconhecimento contábil;
- passivo calculado;
- carteira, ledger, API ou banco de dados;
- antifraude implementado;
- programa operacional;
- produção.

## 11. Critérios de conclusão

- três camadas independentes definidas;
- natureza dos pontos registrada;
- dez famílias catalogadas;
- fontes de financiamento estruturadas;
- eventos e evidências definidos;
- ciclo de vida publicado;
- validade, resgate, reversão e disputa documentados;
- política de segurança comportamental publicada;
- fraude e abuso classificados;
- voluntariado e impacto social separados;
- contrato canônico disponível;
- dez cenários e dezoito gates documentados;
- pendências do GEM-006 explícitas.
