---
id: UXA-097
title: Validação Integrada da Continuidade Compreensão Inicial → Tela Hoje
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-006
  - UXA-010
  - UXA-011-A1
  - UXA-023
  - UXA-036
  - UXA-037
  - UXA-096
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-007
  - GKR-SURF-PER-008
  - GKR-TRN-007
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-GAPS-001
  - M7.84
normative: false
---

# UXA-097 — Validação Integrada da Continuidade Compreensão Inicial → Tela Hoje

## 1. Finalidade

A UXA-097 fecha a prioridade de validação `V1` registrada após a UXA-096: examinar ponta a ponta a passagem da compreensão inicial revisada para a primeira `Tela Hoje`.

O objeto principal é:

```text
GKR-SURF-PER-007 — compreensão inicial revisável
→ GKR-TRN-007
→ GKR-SURF-PER-008 — Tela Hoje
```

A iniciativa não revalida a Tela Hoje recorrente em geral, não cria novo ID de superfície ou transição e não promove a Jornada da Pessoa.

## 2. Evidência de entrada

A auditoria encontrou duas lacunas que impediam promover `GKR-TRN-007` como estava representada:

1. UXA-006 e UXA-010 registravam a **primeira Tela Hoje após a confirmação da compreensão inicial** como estado ainda não materializado separadamente;
2. em `PER-007`, a ação `Usar somente nesta sessão e continuar sem personalização` não explicitava o destino da continuidade.

A Tela Hoje recorrente vigente pressupõe acontecimentos já em andamento. Usá-la como primeira entrada poderia fabricar mudança, avanço, urgência, Próximo Passo pronto ou relevância comercial sem histórico suficiente.

## 3. Reformulação controlada

A UXA-097 realiza somente duas alterações visuais.

### 3.1 PER-007 — decisão

O SVG existente:

`docs/assets/wireframes/uxa-036-initial-understanding-decision-mobile.svg`

passa a explicitar:

> **Usar nesta sessão e ir para Hoje sem personalização**

A rota `Excluir compreensão e continuar explorando` permanece fora de `TRN-007`.

### 3.2 PER-008 — primeira Tela Hoje

É criado um novo estado visual dentro do ID existente `PER-008`:

`docs/assets/wireframes/uxa-097-first-today-after-initial-understanding-mobile.svg`

A variante representa a primeira entrada depois das escolhas explícitas da pessoa. Ela não substitui o SVG recorrente `uxa-006-hoje-mobile.svg`.

## 4. Contrato da primeira Tela Hoje

A primeira variante deve demonstrar que:

- concluir a compreensão inicial não constitui avanço humano por si só;
- não existe obrigação de apresentar atenção, oportunidade, atividade ou Próximo Passo;
- somente afirmações confirmadas e informações autorizadas podem sustentar personalização;
- itens em aberto, desconhecidos, rejeitados ou contestados não viram fatos;
- a condição de persistência não é alterada pela navegação;
- a condição de personalização não é ampliada pela navegação;
- a pessoa pode revisar compreensão e escolhas;
- não personalizar não bloqueia acesso a Hoje, Jornada ou Explorar;
- publicidade ou disponibilidade comercial não podem criar prioridade artificial na primeira entrada.

## 5. Ramos válidos de TRN-007

### 5.1 Personalização autorizada

```text
PER-007
→ escolhas válidas explicitamente confirmadas
→ autorização vigente para a finalidade apresentada
→ TRN-007
→ primeira PER-008
→ somente base confirmada, autorizada e vigente pode orientar blocos pessoais
```

A primeira Tela Hoje pode apresentar uma possibilidade pessoal, mas deve explicar a base, as incertezas, as alternativas e a ausência de garantia.

### 5.2 Sem personalização

```text
PER-007
→ pessoa escolhe continuar sem personalização ou adia a autorização
→ TRN-007
→ primeira PER-008
→ blocos pessoais são omitidos
→ navegação e exploração geral continuam disponíveis
```

Entrar em Hoje não autoriza personalização implicitamente.

### 5.3 Fora de TRN-007

Não pertencem a `TRN-007`:

- `Excluir compreensão e continuar explorando`;
- base autorizada insuficiente sem decisão válida para usar a compreensão;
- retorno à revisão;
- retorno aos conteúdos e autorizações.

## 6. Ordem de efeito

Para a continuidade validada, a ordem lógica é:

1. a pessoa conclui escolhas compatíveis;
2. a confirmação explícita aplica somente as escolhas apresentadas;
3. a navegação para Hoje ocorre depois da condição escolhida estar efetiva;
4. a primeira Tela Hoje consulta a condição canônica vigente;
5. qualquer retirada, exclusão ou alteração posterior prevalece sobre estado visual obsoleto.

A representação não define API, transação, lock, fila, cache ou implementação técnica.

## 7. Estado obsoleto e concorrência

Se persistência, personalização, conteúdo de origem ou autorização mudarem entre `PER-007` e `PER-008`:

- a condição canônica mais recente prevalece;
- informação sem autorização vigente não pode ser usada;
- personalização retirada faz os blocos pessoais serem omitidos;
- compreensão excluída não pode reaparecer por cache ou retorno;
- a navegação não restaura uma escolha antiga;
- a pessoa pode continuar em Hoje de forma não personalizada quando isso for compatível com sua condição atual.

## 8. Idempotência e retorno

- clique repetido não cria duas jornadas, dois Próximos Passos ou dois efeitos de persistência;
- recarga não conta como avanço nem nova confirmação;
- voltar à compreensão não desfaz silenciosamente escolhas já efetivadas;
- alterar escolhas exige novo ato explícito;
- retornar a Hoje usa o estado vigente, não uma cópia histórica;
- visualizar a primeira Tela Hoje não marca atividade, presença, streak ou evolução.

## 9. Validação funcional da variante inicial

A variante `uxa-097-first-today-after-initial-understanding-mobile.svg` é considerada funcionalmente válida porque:

- declara que é a primeira entrada;
- recusa presumir avanço;
- expõe a condição usada para personalização;
- mantém itens abertos e desconhecidos fora de fatos confirmados;
- admite legitimamente ausência de atenção;
- apresenta possibilidade como possibilidade, não obrigação;
- oferece explicação, alternativas e `Agora não`;
- explica o comportamento quando personalização não estiver autorizada;
- preserva acesso à navegação sem exigir personalização.

## 10. Revalidação de PER-007

A versão corrente do estado de decisão de `PER-007` é considerada revalidada após a troca controlada de rótulo porque:

- as escolhas continuam independentes;
- nenhuma alternativa é pré-selecionada;
- combinações incompatíveis continuam bloqueadas;
- o destino da continuidade sem personalização passa a ser explícito;
- exclusão + exploração permanece uma rota distinta;
- nenhuma escolha é feita pela navegação.

Os demais quatro estados UXA-036 permanecem inalterados e conservam sua validação anterior.

## 11. Veredito de TRN-007

Com origem, destino inicial e regras de efeito agora explícitos, `GKR-TRN-007` pode ser promovida de `não examinada` para:

> **integralmente validada**

O veredito global da UXA-097 é:

> **Aprovada após materialização mínima do primeiro estado de Hoje, reformulação controlada de PER-007 e validação integrada de GKR-TRN-007.**

## 12. Impacto de cobertura

Após eventual integração:

- SVGs: **109**;
- associações individuais: **109**;
- perfis de rastreabilidade: **28**;
- validações funcionais vigentes: **99**;
- pendências de validação específica: **10**, exclusivamente UXA-055;
- IDs com referência visual: **30/40**;
- responsabilidades sem SVG dedicado: **9**;
- superfícies: **40**;
- transições: **37**.

A nova validação corresponde ao novo SVG. A reformulação do SVG de decisão é revalidada dentro desta mesma iniciativa e não reduz a cobertura anterior.

## 13. Limites

A UXA-097 não:

- altera a Tela Hoje recorrente vigente;
- materializa todos os estados alternativos de Hoje;
- valida os dez estados UXA-055;
- fecha `TRN-001`, `TRN-003`, `TRN-004` ou `TRN-005`;
- promove a Jornada da Pessoa;
- inicia protótipo ou teste com pessoas;
- inicia W0-01 ou Engenharia de Produto;
- define UXA-098 automaticamente.

## 14. Próxima priorização possível

Com `V1` fechada, a fila de validação passa a iniciar por **V2 — publicação → descoberta/mapa/lista/detalhe**, seguida por **V3 — dez estados residuais UXA-055**, salvo nova decisão governada baseada em evidência.

A UXA-098 não foi iniciada.