---
id: UXA-010
title: Validação Funcional e Reformulação da Tela Hoje
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-002
  - UXA-005
  - UXA-006
  - UXA-009
related:
  - UXA-003
  - UXA-004
  - UXA-020
  - PAS-001-CV-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
normative: true
---

# Validação Funcional e Reformulação da Tela Hoje (identificador UXA-010)

## 1. Finalidade

Este documento registra a primeira validação humana funcional da **Tela Hoje**, governa a reformulação do respectivo wireframe de baixa fidelidade e preserva a decisão posterior de que a **Página Inicial da Guivos e Início da Jornada** deverá antecedê-la na primeira entrada pessoal.

A decisão permanece restrita à arquitetura da experiência. Ela não aprova design visual, componentes técnicos, protótipo navegável, testes de usabilidade ou desenvolvimento.

## 2. Decisões humanas registradas

### 2.1 Reformulação funcional original

O Fundador aprovou o prosseguimento com a reformulação funcional apresentada após a revisão do wireframe inicial.

A decisão aceitou os seguintes ajustes:

1. manter a síntese do momento, mas torná-la condicional;
2. preservar somente um item principal de atenção;
3. apresentar oportunidades em cartões de largura integral e empilhados;
4. explicitar o contexto de atuação com a expressão `Agindo como`;
5. mostrar Coletivos e atividades somente quando houver utilidade temporal.

### 2.2 Precedência da HOME

Em 26/07/2026, o Fundador determinou que a experiência pessoal deverá possuir uma **HOME anterior à Tela Hoje**, na qual a pessoa:

- conhece a Guivos e o ecossistema;
- é convidada a iniciar sua jornada;
- conta seu Momento Atual por texto, voz, arquivos ou outras formas autorizadas;
- revisa o que a Guivos compreendeu;
- corrige, limita e confirma a compreensão;
- somente então recebe indicações contextuais na Tela Hoje.

Essa decisão não invalida a hierarquia funcional já aprovada para a Tela Hoje. Ela altera sua posição na jornada: de primeira entrada pessoal para **entrada recorrente após a compreensão inicial confirmada**.

## 3. Sequência de entrada preservada

A sequência pessoal passa a ser:

```text
Página Inicial da Guivos
→ início voluntário da jornada
→ relato do Momento Atual
→ compreensão inicial revisável
→ confirmação e autorização
→ Tela Hoje
```

A Tela Hoje não deverá:

- substituir a apresentação institucional da HOME;
- coletar o primeiro relato completo sem contexto;
- apresentar personalização antes do gate de compreensão;
- utilizar popularidade, publicidade ou perfil genérico para simular relevância.

## 4. Estrutura recorrente preservada

Dentro da Tela Hoje, a ordem funcional permanece:

```text
contexto de atuação
→ síntese condicional
→ atenção principal
→ movimento atual
→ oportunidades para considerar
→ Coletivos e atividades, quando materialmente relevantes
→ navegação global
```

O Próximo Passo permanece antes das oportunidades para preservar continuidade da jornada e evitar que o conteúdo comercial ocupe prioridade superior ao movimento declarado pela pessoa.

## 5. Síntese do momento

A síntese permanece válida, mas não será um bloco obrigatório.

### 5.1 Quando aparece

A síntese deverá aparecer quando existirem pelo menos dois acontecimentos materiais que possam ser compreendidos melhor em conjunto, por exemplo:

- um Próximo Passo pronto;
- uma confirmação pendente;
- uma oportunidade com prazo real;
- uma atividade próxima;
- uma alteração material em processo iniciado.

A síntese deverá possuir base em compreensão confirmada, atualização posterior ou fonte autorizada.

### 5.2 Quando não aparece

A síntese deverá ser omitida quando:

- houver somente um item relevante, evitando repetição;
- não houver informação material;
- a agregação aumentar exposição de informação sensível;
- a fonte estiver incompleta ou com sincronização incerta;
- a compreensão inicial ainda não possuir segurança suficiente.

A ausência da síntese não deverá deixar espaço vazio artificial.

## 6. Atenção principal e múltiplos itens críticos

A Tela Hoje continuará destacando no máximo um item principal de atenção.

Quando existirem múltiplos itens críticos:

1. o item de maior prioridade material ocupará o destaque principal;
2. a tela informará quantos outros itens precisam de revisão;
3. o acesso conduzirá à Central de Intervenções;
4. os itens não competirão simultaneamente por destaque;
5. publicidade, patrocínio ou popularidade não influenciarão a prioridade.

A priorização seguirá segurança e direitos, prazo ou risco material, confirmação solicitada, processo iniciado, dependência real e prioridade declarada.

## 7. Contexto de atuação

O seletor deverá apresentar explicitamente:

> Agindo como: Minha jornada

As alternativas poderão incluir Organização representada ou Coletivo administrado ou integrado.

A interface deverá impedir que uma ação institucional seja executada como ação pessoal ou vice-versa. Mudanças de contexto deverão ser conscientes, visíveis e reversíveis.

## 8. Oportunidades para considerar

Os cartões lado a lado deixam de ser a solução preferencial para a tela móvel de referência.

A apresentação reformulada deverá:

- utilizar a largura integral disponível;
- empilhar até dois cartões;
- preservar título, preço ou gratuidade, prazo, modalidade ou localização e razão de relevância;
- oferecer explicação de por que a oportunidade aparece;
- manter acesso ao conjunto completo em Explorar ou Minhas Oportunidades;
- evitar repetição de categorias ou fontes;
- permitir que somente uma oportunidade seja exibida quando apenas uma possuir utilidade temporal suficiente;
- utilizar somente contexto autorizado e corrigível para justificar relevância pessoal.

A quantidade máxima de dois cartões não constitui meta de preenchimento. Nenhuma oportunidade deverá ser apresentada apenas para completar a tela.

Antes do gate da compreensão inicial, itens gerais poderão existir em Explorar ou na HOME, mas não serão descritos como indicação pessoal.

## 9. Coletivos e atividades

O bloco de Coletivos permanece na Tela Hoje somente quando houver utilidade temporal, como:

- atividade próxima;
- convite ou solicitação pendente;
- mudança material de horário, local ou regra;
- ação de causa ou voluntariado;
- decisão necessária de líder, moderador ou participante;
- recurso com prazo de uso.

Publicações sociais, atualizações genéricas ou ausência recente não justificam o bloco.

## 10. Navegação preservada

A navegação pessoal permanece:

- Hoje;
- Jornada;
- Explorar;
- Mapa;
- Eu.

`Jornada` é o termo consolidado para contexto, objetivos, Próximos Passos, experiências e evolução. O incremento não altera essa nomenclatura.

A HOME continuará acessível por marca, menu institucional ou opção de acesso ao Ecossistema Guivos, sem necessariamente ocupar a navegação principal recorrente.

## 11. Resultado da reformulação

A nova versão do Wireframe de Baixa Fidelidade da Tela Hoje deverá demonstrar:

- posição recorrente após a HOME e a compreensão inicial;
- contexto de atuação mais explícito;
- síntese condicional;
- um único item principal;
- continuidade da jornada antes da descoberta comercial;
- oportunidades legíveis em largura integral;
- ausência legítima de blocos sem utilidade temporal;
- acesso claro a itens adicionais sem sobrecarregar a superfície;
- personalização sustentada por contexto confirmado e corrigível.

## 12. Estados ainda não resolvidos

Permanecem pendentes de wireframes separados:

- primeira Tela Hoje após a confirmação da compreensão inicial;
- estado totalmente vazio;
- múltiplos itens críticos;
- informação sensível em modo discreto;
- falha de fonte externa;
- baixa conectividade;
- contexto de Organização;
- contexto de Coletivo;
- alteração de preço em processo iniciado;
- acessibilidade com texto ampliado.

## 13. Limites

Esta decisão não autoriza:

- design visual definitivo;
- definição de cores, tipografia ou iconografia;
- protótipo navegável;
- testes de usabilidade;
- implementação;
- criação automática dos estados alternativos;
- início da Engenharia de Produto.

## 14. Próximo ponto de decisão

Após a integração desta reformulação, os próximos atos dependerão de autorização separada e poderão:

1. validar funcionalmente a HOME da Guivos;
2. detalhar a captura multimodal do Momento Atual;
3. validar a revisão da compreensão inicial;
4. criar a primeira variação da Tela Hoje após a transição da HOME;
5. selecionar outro estado alternativo da Tela Hoje para wireframe.

O protótipo navegável continuará dependendo de autorização explícita posterior.