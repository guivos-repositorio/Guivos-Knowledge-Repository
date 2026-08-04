---
id: UXA-060
title: Wireframes Móveis de Explorar Coletivos e Resultados de Busca
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-03
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-024
  - UXA-028
  - UXA-030
  - UXA-038
  - UXA-042
  - UXA-043
  - UXA-055
related:
  - UXA-061
  - UXA-062
  - M7.63
normative: false
---

# Wireframes Móveis de Explorar Coletivos e Resultados de Busca

## 1. Finalidade

Este documento governa a primeira família móvel de descoberta de Coletivos no programa UXA-059.

A versão 0.2.0 incorpora a validação e as reformulações registradas na UXA-061.

A família contém referências para:

1. Explorar Coletivos;
2. resultados de busca;
3. filtros;
4. busca concluída sem resultados;
5. explicação da origem patrocinada.

Os artefatos representam baixa fidelidade. Eles não representam design final, dados reais, algoritmo, protótipo, teste ou implementação.

## 2. Posição no programa

A UXA-059 organiza a materialização em P0A, P0B, P1 e P2.

Esta família cobre o início da P0A e apenas os estados P0B indispensáveis à busca:

```text
Explorar Coletivos
→ buscar ou escolher tema
→ comparar resultados
→ revisar filtros
→ compreender origem
→ abrir futuro Perfil Público
```

O Perfil Público, a participação, `Meus Coletivos`, a Central de Atualizações e a gestão permanecem fora deste conjunto.

## 3. Cenário canônico

- tema: ciclismo;
- área: Belo Horizonte e Coletivos on-line;
- localização precisa: não utilizada;
- personalização: desativada na exploração;
- resultado orgânico principal: `Pedal Horizonte`;
- resultado orgânico seguinte: `Ciclistas da Serra`;
- conteúdo patrocinado ilustrativo: `Pedal Urbano Aberto`;
- anunciante: `Associação Movimento Livre`;
- destino futuro: Perfil Público do Coletivo.

Os dados são fictícios e existem somente para validação estrutural.

## 4. Artefatos

### 4.1 Explorar Coletivos

![Explorar Coletivos](../assets/wireframes/uxa-060-collective-explore-mobile.svg)

`docs/assets/wireframes/uxa-060-collective-explore-mobile.svg`

### 4.2 Resultados de busca

![Resultados de busca de Coletivos](../assets/wireframes/uxa-060-collective-search-results-mobile.svg)

`docs/assets/wireframes/uxa-060-collective-search-results-mobile.svg`

### 4.3 Filtros

![Filtros da busca de Coletivos](../assets/wireframes/uxa-060-collective-search-filters-mobile.svg)

`docs/assets/wireframes/uxa-060-collective-search-filters-mobile.svg`

### 4.4 Sem resultados

![Busca de Coletivos sem resultados](../assets/wireframes/uxa-060-collective-search-no-results-mobile.svg)

`docs/assets/wireframes/uxa-060-collective-search-no-results-mobile.svg`

### 4.5 Explicação patrocinada

![Explicação da origem patrocinada](../assets/wireframes/uxa-060-collective-discovery-origin-mobile.svg)

`docs/assets/wireframes/uxa-060-collective-discovery-origin-mobile.svg`

## 5. Canal e dimensão

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- navegação: `Hoje | Jornada | Explorar | Mapa | Eu`;
- item ativo: `Explorar`.

Uma referência para computador somente será criada se houver mudança material de hierarquia ou responsabilidade.

## 6. Explorar Coletivos

A hierarquia validada é:

```text
título e personalização
→ busca direta
→ área editável
→ categorias
→ Coletivos com entrada disponível
→ origem em cada cartão
→ explicação das origens
→ privacidade territorial
→ navegação recorrente
```

A superfície funciona sem conteúdo da Jornada e sem localização precisa.

`Com entrada disponível` poderá reunir entrada aberta ou mediante aprovação, desde que o modelo real permaneça explícito.

Coletivos privados, protegidos e não listados não aparecem na exploração geral.

## 7. Busca e resultados

A lista validada apresenta:

- busca preservada;
- área manual e ausência de localização precisa;
- filtros ativos;
- total correspondente;
- ordenação explicável;
- primeiro resultado orgânico;
- publicidade identificada;
- resultados orgânicos posteriores;
- origem em cada cartão;
- continuidade para o Perfil Público.

A ação `Limpar só filtros` não apaga busca ou área.

## 8. Cartões

Cada cartão poderá apresentar, quando permitido:

- origem;
- nome;
- propósito ou categoria;
- território e modalidade;
- modelo de entrada;
- funcionamento;
- acessibilidade;
- contagem governada;
- proteção da lista nominal;
- relação comercial;
- explicação;
- continuidade ao Perfil Público.

Informação ausente não será preenchida por inferência.

## 9. Ordenação

A ordenação orgânica poderá considerar:

- correspondência com busca;
- filtros;
- território;
- modalidade;
- entrada disponível;
- atualidade;
- acessibilidade;
- confiabilidade.

Não poderão dominar:

- quantidade de participantes;
- volume de mensagens;
- popularidade;
- tempo na plataforma;
- plano contratado;
- publicidade;
- avaliação isolada.

Sem personalização autorizada, não será usada linguagem como `melhor para você`.

## 10. Contagem de participantes

A formulação ilustrada é:

> **Participantes: cerca de 80 · lista nominal protegida**

A contagem:

- é aproximada;
- não mistura seguidores, participantes, presença ou moderadores;
- não cria ranking;
- não prova qualidade ou impacto;
- não torna a lista nominal pública.

## 11. Publicidade

O item patrocinado apresenta, antes do conteúdo:

> **PATROCINADO · PUBLICIDADE**

Também apresenta:

- anunciante;
- critérios;
- distinção de recomendação;
- ordem orgânica preservada;
- explicação `Por que este anúncio?`;
- continuidade `Ver perfil público`.

A possibilidade de abrir o Perfil Público não elimina a natureza comercial da distribuição.

Publicidade não preenche artificialmente a busca vazia.

## 12. Origem

As origens permanecem distintas:

- resultado de busca;
- exploração por tema;
- território;
- sugestão da Guivos;
- recomendação pessoal;
- convite;
- link compartilhado;
- publicidade.

Uma origem não poderá ser apresentada como outra.

A materialização detalhada de sugestão, recomendação e convite permanece para pacotes próprios.

## 13. Explicação patrocinada

A explicação validada apresenta:

- natureza comercial;
- anunciante;
- posição após o primeiro resultado orgânico;
- critérios objetivos;
- ausência de ampliação silenciosa;
- dados não utilizados;
- identidade do visualizador não entregue;
- controles separados;
- retorno aos resultados com contexto preservado.

Ao voltar, permanecem busca, área, filtros e posição do item.

## 14. Controles publicitários

- ocultar este anúncio;
- reduzir semelhantes;
- desativar publicidade;
- denunciar anúncio.

Os efeitos são diferentes. Preferência publicitária não é filtro orgânico.

## 15. Filtros

O painel validado preserva busca e área.

As dimensões ilustradas são:

- tema;
- forma de entrada;
- modalidade;
- território;
- acessibilidade;
- idioma.

Os filtros selecionados utilizam texto e marca, sem depender apenas de cor.

`Cancelar` não aplica mudanças.

`Limpar somente filtros` não altera:

- busca;
- área;
- preferência publicitária;
- autorização territorial.

Nenhuma mudança é aplicada antes da confirmação.

## 16. Estado sem resultados

O estado somente aparece quando:

- a consulta foi concluída;
- busca, região e filtros são conhecidos;
- a cobertura aplicável foi verificada;
- não existe falha material;
- o total real é zero.

A região é apresentada separadamente:

> **Belo Horizonte · região manual · sem localização precisa**

A mensagem principal é:

> **0 resultados correspondem a esta consulta**

> **Sua consulta permanece intacta.**

## 17. Recuperação do zero

A pessoa poderá:

- editar busca;
- revisar filtros;
- ampliar região;
- alterar modalidade;
- explorar sem alterar a consulta.

Cada mudança deverá ser revisada antes da aplicação e preservar as dimensões não alteradas.

Publicidade não será usada para esconder o estado vazio.

## 18. Distinção de estados

| Condição | Tratamento |
|---|---|
| zero confirmado | preservar consulta e permitir revisão consciente |
| falha de fonte | declarar que nem todas as fontes foram verificadas |
| carregamento | manter estrutura e informar atualização |
| baixa conectividade | declarar possível desatualização |
| cobertura parcial | limitar a conclusão às fontes disponíveis |
| indisponibilidade | permitir nova tentativa sem declarar zero |

Esta família materializa apenas o zero confirmado.

## 19. Território e privacidade

Permanecem diferentes:

- região manual;
- localização aproximada autorizada;
- localização precisa temporária;
- modalidade on-line;
- ausência de território.

A exploração e a busca não exigem localização precisa.

Visualizar resultados não autoriza rastreamento, histórico de deslocamento ou uso publicitário de posição precisa.

## 20. Continuidade para Perfil Público

`Ver perfil público` será a continuidade dos resultados orgânicos e patrocinados autorizados.

O Perfil Público deverá receber, quando permitido:

- origem;
- consulta;
- área;
- filtros;
- posição;
- relação comercial;
- estado de personalização.

Ao retornar, o contexto deverá ser recuperado.

O Perfil Público não é criado nesta família.

## 21. Acessibilidade funcional

Os artefatos utilizam:

- `title` e `desc`;
- rótulos textuais;
- seleção identificada por texto e marca;
- total zero escrito;
- ações nomeadas;
- origem e publicidade textuais;
- hierarquia linear;
- ausência de dependência exclusiva de cor.

Conformidade técnica permanece pendente.

## 22. Privacidade e proteção

- exploração sem personalização;
- área manual;
- localização precisa opcional;
- lista nominal protegida;
- ausência de vínculo após visualização;
- ausência de contato automático;
- conteúdo protegido fora da publicidade;
- identidade do visualizador não entregue;
- Coletivos protegidos fora da busca geral;
- origem e relação comercial explicáveis.

## 23. Resultado da validação

A UXA-061 considera a família **funcionalmente válida após reformulação**.

| Artefato | Resultado |
|---|---|
| Explorar Coletivos | válido sem alteração |
| Resultados | válido após reformulação |
| Filtros | válido após reformulação |
| Sem resultados | válido após reformulação |
| Explicação patrocinada | válido após reformulação |

## 24. Cobertura

### Descoberta de Coletivos

- cinco materializados;
- cinco validados;
- zero pendente nesta família.

### Opportunity Boost

Permanece separado:

- 46 materializados;
- 36 validados por pacote;
- dez pendentes.

## 25. Limites

Esta família não:

- define algoritmo;
- cria publicidade real;
- cria Perfil Público;
- cria participação;
- cria dados reais;
- cria protótipo;
- executa testes;
- inicia design final;
- inicia Engenharia de Produto.

## 26. Próximo ato governado

Após integração e nova autorização, o próximo pacote recomendado será a UXA-062 — Wireframes Móveis do Perfil Público do Coletivo.

Nenhum ato posterior é iniciado automaticamente.
