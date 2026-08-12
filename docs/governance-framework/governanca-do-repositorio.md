---
id: GKR-GOV-CONSUMPTION-001
title: Governança do Guivos Knowledge Repository
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-11
depends_on:
  - ADR-001
  - ADR-002
  - ADR-003
  - ADR-004
  - ADR-005
  - ADR-006
normative: false
---

# Governança do Guivos Knowledge Repository

## 1. Finalidade

Este documento consolida as regras de governança necessárias para compreender como o GKR deve ser mantido, interpretado e evoluído.

Artefatos históricos, validações mecânicas, changelogs, adendos e decisões detalhadas permanecem disponíveis no repositório para rastreabilidade, mas não precisam ocupar a navegação principal.

---

## 2. Fonte oficial de conhecimento

O Guivos Knowledge Repository é a **fonte oficial de conhecimento arquitetural governado da Guivos**.

Conversas, rascunhos, apresentações e protótipos podem produzir conhecimento, mas uma decisão somente se torna parte do estado governado quando é registrada e reconciliada no GKR.

Isso não significa que todo arquivo possui a mesma autoridade.

---

## 3. Hierarquia de autoridade

Quando documentos divergem, deve-se considerar:

1. estado atual transversal;
2. autoridade temática vigente;
3. documento explicitamente normativo quando aplicável;
4. decisão mais recente que substitui uma anterior;
5. evidência real sobre intenção ou projeção;
6. artefato histórico apenas como contexto.

Um arquivo antigo não recupera autoridade apenas porque continua no histórico Git.

---

## 4. Rastreabilidade

Decisões importantes devem permitir responder:

- de onde vieram;
- qual problema resolvem;
- quais documentos dependem delas;
- o que substituíram;
- qual estado possuem;
- que evidência as sustenta;
- quando precisam ser revistas.

Rastreabilidade não exige que todos os artefatos técnicos apareçam no menu público.

---

## 5. Navegação de consumo versus estrutura interna

A navegação pública do GKR é uma **interface de leitura**, não um espelho da árvore de arquivos.

Regra vigente:

```text
menu público
→ assuntos e documentos mestres

arquivos internos
→ contratos, auditorias, validações, históricos e fontes de rastreabilidade
```

Um documento pode permanecer necessário no repositório e, ao mesmo tempo, não precisar aparecer como item independente de navegação.

---

## 6. Consolidação

Quando um assunto amadurece e passa a exigir a abertura de muitos arquivos para ser compreendido, deve ser criado ou atualizado um documento mestre de consumo.

Esse documento precisa:

- refletir o estado vigente;
- remover contradições já resolvidas;
- distinguir fato de hipótese;
- preservar os limites importantes;
- ser legível isoladamente;
- permitir impressão útil;
- referenciar autoridades internas quando necessário.

A consolidação não deve simplesmente concatenar textos históricos.

Ela deve produzir uma leitura coerente do estado atual.

---

## 7. Histórico e obsolescência

Existem três tratamentos diferentes.

### Ainda válido, mas técnico

Permanece no repositório e sai do menu principal.

### Substituído, mas necessário para rastreabilidade histórica

Pode permanecer fora da navegação, claramente sem autoridade atual.

### Substituído e prejudicial à interpretação vigente

Deve ser removido da superfície de consumo e, quando não houver obrigação arquitetural de preservação no working tree, pode ser excluído. O histórico Git continua preservando sua existência anterior.

---

## 8. Evidência e estado operacional

O GKR precisa distinguir:

```text
conceito
≠ decisão
≠ arquitetura
≠ implementação
≠ operação
≠ evidência real
```

Exemplos:

- país candidato ≠ operação internacional;
- tecnologia selecionada ≠ tecnologia provisionada;
- preço candidato ≠ disposição a pagar validada;
- arquitetura de IA ≠ IA em produção;
- modelo de caixa ≠ runway calculável;
- página governada ≠ página implementada.

---

## 9. Responsabilidade arquitetural

Toda decisão permanente precisa possuir responsabilidade identificável.

A responsabilidade inclui:

- manter coerência;
- avaliar conflitos;
- registrar alterações;
- preservar fronteiras;
- assegurar que implementação futura não redefina silenciosamente a estratégia.

---

## 10. Ordem de dependência

A evolução do GKR deve respeitar dependências.

Uma camada posterior não deve redefinir uma camada anterior sem decisão explícita.

Exemplo conceitual:

```text
fundamentos
→ modelo fundamental
→ estratégia
→ arquitetura
→ experiência
→ produtos
→ economia
→ implementação
```

A ordem não é uma proibição de trabalho paralelo; é uma regra contra inversão silenciosa de autoridade.

---

## 11. Mudança proporcional à permanência

Quanto mais permanente e transversal uma decisão, maior deve ser o rigor para alterá-la.

Mudanças em:

- essência;
- propósito;
- tipos de participante;
- princípios de autonomia;
- arquitetura do ecossistema;
- autoridade de dados;
- identidade de produtos;

exigem mais governança do que ajustes editoriais, exemplos, copy ou organização de menu.

---

## 12. Auditoria

Auditorias arquiteturais devem buscar:

- contradições;
- autoridade duplicada;
- dependências quebradas;
- estados impossíveis;
- informações obsoletas apresentadas como atuais;
- claims sem evidência;
- lacunas entre arquitetura e implementação;
- expansão de escopo não autorizada.

Auditoria não existe para produzir volume documental. Existe para reduzir risco de incoerência.

---

## 13. Validação mecânica e semântica

Alterações relevantes do GKR devem passar pelos gates oficiais disponíveis.

### Validação mecânica

Verifica, entre outros pontos:

- front matter;
- IDs;
- links;
- navegação;
- nomenclatura;
- whitespace;
- build estrito da documentação;
- integridade da árvore rastreada.

### Validação semântica

Verifica coerência de estado e contratos governados.

Sucesso mecânico não prova que uma decisão estratégica é correta, mas impede classes importantes de inconsistência documental.

---

## 14. Pull requests e integração

Mudanças governadas devem preferir:

```text
baseline identificada
→ branch própria
→ diff controlado
→ PR em draft
→ gates no head exato
→ decisão de integração
→ reconciliação da main
```

Merge é um ato de governança separado da criação do conteúdo.

---

## 15. Impressão e consumo

O GKR deve permitir dois modos de uso:

### Leitura por assunto

Um documento mestre deve ser imprimível isoladamente e suficiente para compreender o tema.

### Corpus completo

A versão agregada pode reunir o repositório para arquivo, auditoria ou revisão ampla.

A existência do corpus completo não justifica fragmentar o menu cotidiano.

---

## 16. Regra de simplicidade

> **A complexidade necessária para governar o conhecimento não deve ser transferida desnecessariamente para quem precisa lê-lo.**

O repositório pode possuir centenas de arquivos internos e ainda assim oferecer uma navegação curta, estável e humana.

Essa é a regra vigente para a organização pública do GKR.