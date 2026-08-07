---
id: UXA-087
title: Validação Funcional e Reformulação da Visão Geral do Responsável do Coletivo
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-018
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-080
  - UXA-086
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-COL-002
  - GKR-SURF-COL-003
  - GKR-TRN-112
  - GKR-JOURNEY-GAPS-001
  - M7.74
normative: false
---

# Validação Funcional e Reformulação da Visão Geral do Responsável do Coletivo

## 1. Finalidade

A UXA-087 valida funcionalmente a referência materializada pela UXA-086 para `GKR-SURF-COL-002 — Visão Geral do Responsável` e aplica, no mesmo pacote, as correções estritamente necessárias para que a superfície cumpra seu contrato sem antecipar `GKR-SURF-COL-003`.

A validação verifica se uma pessoa legitimamente responsável por um Coletivo consegue responder, antes de operar qualquer área especializada:

> **Em nome de qual Coletivo estou atuando, qual é o meu escopo real de autoridade, o que precisa de cuidado agora, por que isso importa, quais alternativas tenho e como retorno sem executar uma decisão indevida?**

A validação não trata o wireframe como design final, protótipo ou implementação.

## 2. Autoridades utilizadas

O gate foi realizado contra:

- UXA-014 — fundação funcional de Organizações e Coletivos;
- UXA-018 — validação funcional do Início do Coletivo;
- UXA-056 — descoberta, perfil público, participação e gestão do Coletivo;
- UXA-058 — comunicação, origem, autoridade, proteção e reversibilidade das interações;
- UXA-059 — programa e priorização dos wireframes de Coletivos;
- UXA-080 — registros granulares promovidos;
- UXA-086 — contrato e materialização da Visão Geral do Responsável.

Também foram considerados os registros vigentes de superfícies, transições e lacunas.

## 3. Critérios do gate

A superfície foi examinada nas seguintes dimensões:

1. identidade do Coletivo e contexto protegido;
2. estado e escopo de representação;
3. compreensão do momento operacional;
4. legitimidade da atenção principal;
5. prazo, consequência e autoridade da ação destacada;
6. alternativa, adiamento e contestação;
7. separação entre síntese e operação especializada;
8. minimização de dados pessoais e protegidos;
9. distinção entre comunicação, atividade, pergunta, decisão e proteção;
10. autonomia do Coletivo diante de Organizações apoiadoras;
11. retorno, saída e reversibilidade;
12. ausência de ranking, coerção, popularidade e atividade como prova de avanço;
13. continuidade documental para `GKR-SURF-COL-003` sem presunção de implementação.

Falha material em autoridade, dados, reversibilidade ou coerção impede aprovação funcional.

## 4. Diagnóstico da materialização da UXA-086

A referência inicial acertou a estrutura principal:

- identidade e propósito do Coletivo;
- indicação de que a pessoa atua como responsável;
- síntese verificável do momento operacional;
- uma atenção principal em vez de lista de urgências artificiais;
- contagens operacionais separadas de desempenho;
- síntese de solicitações e vínculos;
- comunicação e atividades apresentadas como informações distintas;
- proteção exibida sem revelar conteúdo sensível;
- relação institucional sem transferência automática de autoridade;
- responsabilidades atuais sem ranking de participação;
- ausência de acesso automático à jornada pessoal dos participantes.

Contudo, quatro falhas impediam aprovação da versão materializada originalmente.

## 5. Achados que exigiram reformulação

### F01 — escopo e estado da autoridade estavam implícitos

O cabeçalho dizia que a pessoa atuava como Responsável do Coletivo e oferecia acesso a permissões, mas não mostrava no próprio campo visual:

- se a representação estava válida;
- qual escopo estava ativo;
- que a autoridade era limitada.

Isso poderia induzir a leitura de que o papel nominal concederia acesso integral às áreas listadas.

**Correção:** o cabeçalho passa a declarar `Representação válida` e um escopo resumido de participação, comunicação e proteção limitada. A interface também reforça que áreas listadas não concedem acesso por si mesmas.

### F02 — o prazo da atenção principal não era verificável

A versão inicial dizia `dentro do prazo informado`, mas o prazo não estava apresentado no wireframe.

Uma prioridade sem prazo visível pode produzir urgência artificial e não permite ao responsável avaliar se precisa agir agora.

**Correção:** a atenção principal passa a mostrar um prazo explícito no cenário canônico.

### F03 — alternativa legítima insuficiente

A versão inicial oferecia contestação da prioridade, porém não tornava explícito que a pessoa poderia adiar a análise dentro do prazo sem penalidade.

Isso enfraquecia voluntariedade operacional e poderia transformar recomendação em cobrança.

**Correção:** a superfície passa a declarar que adiar até o prazo ou contestar a prioridade não gera penalidade, mantendo separada a decisão posterior sobre cada solicitação.

### F04 — retorno ao contexto anterior não estava visível

O contrato de `GKR-SURF-COL-002` previa permanência, retorno ou escolha de outra área autorizada, mas o wireframe não apresentava uma saída clara do contexto de gestão.

**Correção:** foi incluído controle explícito para retornar ao contexto anterior, sem executar decisão operacional.

## 6. Reformulação aplicada

A UXA-087 altera o mesmo arquivo:

`docs/assets/wireframes/uxa-086-collective-responsible-overview-desktop.svg`

Não é criado um novo SVG e não surge um novo ID de superfície.

A versão reformulada preserva a hierarquia da UXA-086 e acrescenta somente:

- estado de representação válido;
- escopo resumido de autoridade;
- aviso de que a listagem de uma área não concede acesso;
- prazo verificável para a atenção principal;
- autoridade necessária para a ação destacada;
- ausência de decisão automática;
- adiamento e contestação sem penalidade;
- retorno explícito ao contexto anterior;
- alinhamento do rótulo de entrada para `Revisar solicitações`.

## 7. Validação por dimensão

| Dimensão | Resultado | Evidência |
|---|---|---|
| identidade e propósito | aprovado | nome e propósito permanecem no primeiro campo visual |
| representação | aprovado após reformulação | estado `Representação válida` explícito |
| escopo de autoridade | aprovado após reformulação | escopo resumido e permissões consultáveis |
| momento operacional | aprovado | síntese declara mudanças e fontes |
| atenção principal | aprovado após reformulação | responsabilidade única, prazo, autoridade e ausência de decisão automática |
| alternativa e contestação | aprovado após reformulação | adiamento até o prazo e contestação sem penalidade |
| solicitações e vínculos | aprovado no escopo de síntese | estados agregados e entrada para revisão, sem fila materializada |
| comunicação e atividades | aprovado | objetos permanecem distinguíveis na síntese |
| proteção | aprovado | evento agregado; conteúdo sensível não exposto |
| governança e relações | aprovado | apoio institucional não transfere autoridade |
| dados pessoais | aprovado | somente dados operacionais mínimos são apresentados |
| retorno e reversibilidade | aprovado após reformulação | retorno ao contexto anterior explícito |
| anti-coerção | aprovado | sem ranking, engajamento como prova ou penalidade por adiamento |
| continuidade para COL-003 | parcial por desenho | origem válida; destino operacional continua ausente |

## 8. Estado sem responsabilidade urgente

A ausência de responsabilidade urgente não exige novo SVG nesta etapa porque não altera a hierarquia estrutural da superfície.

No mesmo contrato, o bloco de atenção deverá poder apresentar:

> **Nenhuma responsabilidade exige ação imediata neste momento.**

Nesse estado:

- nenhuma urgência será fabricada;
- contagens não serão convertidas em prioridade;
- o responsável poderá continuar navegando por áreas autorizadas;
- nenhuma perda, punição ou redução de reputação decorrerá da ausência de ação.

A materialização de estados P0B adicionais continua separada conforme UXA-059.

## 9. Autoridade insuficiente

A validação da referência principal não materializa o estado P0B de autoridade insuficiente.

O contrato aprovado exige, porém, que quando a representação não for válida ou o escopo não autorizar a ação:

- operações protegidas não sejam executáveis;
- o motivo seja explicável;
- a pessoa possa consultar permissões;
- exista caminho de retorno, ajuda ou contestação aplicável;
- nenhuma autoridade seja inferida apenas por vínculo, apoio institucional ou posição histórica.

Esse estado poderá receber wireframe separado quando autorizado, conforme UXA-059.

## 10. Dados, privacidade e proteção

A superfície é aprovada porque preserva minimização e finalidade:

- solicitações são exibidas por estado e contagem;
- detalhes pessoais não aparecem na visão geral;
- o evento protegido é indicado sem relato ou evidência sensível;
- a jornada pessoal dos participantes permanece inacessível por padrão;
- apoio institucional não concede dados adicionais;
- lista nominal pública não é presumida;
- nenhuma inferência de dedicação, engajamento ou valor pessoal é produzida.

## 11. Continuidade e `GKR-TRN-112`

A UXA-087 valida a **origem** de `GKR-TRN-112`, não a transição ponta a ponta.

Após esta validação:

```text
GKR-SURF-COL-002 — materializada e validada
→ GKR-TRN-112 — parcial; origem validada
→ GKR-SURF-COL-003 — ainda ausente como operação do responsável
```

Portanto:

- a ação `Revisar solicitações` é funcionalmente válida como intenção de saída;
- o destino ainda não possui fila operacional própria;
- não é possível validar carregamento, retorno, decisão, pedido de informação, aprovação, recusa ou expiração na perspectiva do responsável;
- `GKR-TRN-112` permanece `parcial` e não deve ser promovida para `localmente validada` ou equivalente.

## 12. Fechamento da lacuna de `GKR-SURF-COL-002`

O gate específico da superfície pode ser encerrado porque agora existem:

- autoridade contratual;
- materialização necessária;
- entrada protegida identificada;
- decisão principal compreensível;
- dados e conteúdos delimitados;
- saída documental identificada;
- alternativa e contestação;
- retorno explícito;
- proteção de dados;
- tratamento contratual de ausência de urgência e autoridade insuficiente;
- validação funcional correspondente.

O fechamento de `GKR-SURF-COL-002` **não fecha a continuidade para `GKR-SURF-COL-003`** e não torna a jornada do Coletivo completa.

## 13. Veredito

**Aprovada após reformulação controlada no escopo da superfície.**

`GKR-SURF-COL-002 — Visão Geral do Responsável` pode passar de `materializado; validação pendente` para `validado` como referência funcional de baixa fidelidade.

O veredito não aprova:

- `GKR-SURF-COL-003`;
- `GKR-TRN-112` ponta a ponta;
- gestão de participantes;
- comunicação especializada;
- moderação completa;
- relação bilateral Organização–Coletivo;
- responsividade móvel;
- estados P0B ainda não materializados;
- jornada integrada do Coletivo como completa.

## 14. Efeito quantitativo

Após integração da UXA-087:

| Indicador | Antes | Depois |
|---|---:|---:|
| SVGs existentes | 98 | 98 |
| associações individuais | 98 | 98 |
| perfis de rastreabilidade | 24 | 24 |
| validações funcionais registradas | 87 | 88 |
| pendentes de validação específica | 11 | 10 |
| IDs com referência visual | 26 de 40 | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 | 13 |
| superfícies registradas | 40 | 40 |
| transições registradas | 37 | 37 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

## 15. Limites

A UXA-087 não:

- adiciona novo SVG;
- cria novo ID de superfície ou transição;
- materializa a gestão completa de solicitações;
- valida decisão sobre solicitação na perspectiva do responsável;
- materializa Meus Coletivos, Central de Atualizações ou Início do Participante;
- promove a jornada do Coletivo;
- cria protótipo navegável;
- executa teste com pessoas;
- define design visual final ou componente técnico;
- altera Modelo Econômico ou Resultados Empresariais;
- inicia Engenharia de Produto.

## 16. Próxima transição possível

Após integração e autorização separada, a próxima frente recomendada é:

> **UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo (`GKR-SURF-COL-003`).**

A UXA-088 não é iniciada por esta validação.
