---
id: UXA-010
title: Validação Funcional e Reformulação da Tela Hoje
status: draft
version: 0.1.0
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
  - PAS-001-CV-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-OA-VIEW-001
  - PAS-001-IC-VIEW-001
normative: true
---

# Validação Funcional e Reformulação da Tela Hoje (identificador UXA-010)

## 1. Finalidade

Este documento registra a primeira validação humana funcional da **Tela Hoje** e governa a reformulação do respectivo wireframe de baixa fidelidade.

A decisão permanece restrita à arquitetura da experiência. Ela não aprova design visual, componentes técnicos, protótipo navegável, testes de usabilidade ou desenvolvimento.

## 2. Decisão humana registrada

O Fundador aprovou o prosseguimento com a reformulação funcional apresentada após a revisão do wireframe inicial.

A decisão aceita os seguintes ajustes:

1. manter a síntese do momento, mas torná-la condicional;
2. preservar somente um item principal de atenção;
3. apresentar oportunidades em cartões de largura integral e empilhados;
4. explicitar o contexto de atuação com a expressão `Agindo como`;
5. mostrar Coletivos e atividades somente quando houver utilidade temporal.

## 3. Estrutura preservada

A ordem funcional permanece:

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

## 4. Síntese do momento

A síntese permanece válida, mas não será um bloco obrigatório.

### 4.1 Quando aparece

A síntese deverá aparecer quando existirem pelo menos dois acontecimentos materiais que possam ser compreendidos melhor em conjunto, por exemplo:

- um Próximo Passo pronto;
- uma confirmação pendente;
- uma oportunidade com prazo real;
- uma atividade próxima;
- uma alteração material em processo iniciado.

### 4.2 Quando não aparece

A síntese deverá ser omitida quando:

- houver somente um item relevante, evitando repetição;
- não houver informação material;
- a agregação aumentar exposição de informação sensível;
- a fonte estiver incompleta ou com sincronização incerta.

A ausência da síntese não deverá deixar espaço vazio artificial.

## 5. Atenção principal e múltiplos itens críticos

A Tela Hoje continuará destacando no máximo um item principal de atenção.

Quando existirem múltiplos itens críticos:

1. o item de maior prioridade material ocupará o destaque principal;
2. a tela informará quantos outros itens precisam de revisão;
3. o acesso conduzirá à Central de Intervenções;
4. os itens não competirão simultaneamente por destaque;
5. publicidade, patrocínio ou popularidade não influenciarão a prioridade.

A priorização seguirá segurança e direitos, prazo ou risco material, confirmação solicitada, processo iniciado, dependência real e prioridade declarada.

## 6. Contexto de atuação

O seletor deverá apresentar explicitamente:

> Agindo como: Minha jornada

As alternativas poderão incluir Organização representada ou Coletivo administrado ou integrado.

A interface deverá impedir que uma ação institucional seja executada como ação pessoal ou vice-versa. Mudanças de contexto deverão ser conscientes, visíveis e reversíveis.

## 7. Oportunidades para considerar

Os cartões lado a lado deixam de ser a solução preferencial para a tela móvel de referência.

A apresentação reformulada deverá:

- utilizar a largura integral disponível;
- empilhar até dois cartões;
- preservar título, preço ou gratuidade, prazo, modalidade ou localização e razão de relevância;
- oferecer explicação de por que a oportunidade aparece;
- manter acesso ao conjunto completo em Explorar ou Minhas Oportunidades;
- evitar repetição de categorias ou fontes;
- permitir que somente uma oportunidade seja exibida quando apenas uma possuir utilidade temporal suficiente.

A quantidade máxima de dois cartões não constitui meta de preenchimento. Nenhuma oportunidade deverá ser apresentada apenas para completar a tela.

## 8. Coletivos e atividades

O bloco de Coletivos permanece na Tela Hoje somente quando houver utilidade temporal, como:

- atividade próxima;
- convite ou solicitação pendente;
- mudança material de horário, local ou regra;
- ação de causa ou voluntariado;
- decisão necessária de líder, moderador ou participante;
- recurso com prazo de uso.

Publicações sociais, atualizações genéricas ou ausência recente não justificam o bloco.

## 9. Navegação preservada

A navegação pessoal permanece:

- Hoje;
- Jornada;
- Explorar;
- Mapa;
- Eu.

`Jornada` é o termo consolidado para contexto, objetivos, Próximos Passos, experiências e evolução. O incremento não altera essa nomenclatura.

## 10. Resultado da reformulação

A nova versão do Wireframe de Baixa Fidelidade da Tela Hoje deverá demonstrar:

- contexto de atuação mais explícito;
- síntese condicional;
- um único item principal;
- continuidade da jornada antes da descoberta comercial;
- oportunidades legíveis em largura integral;
- ausência legítima de blocos sem utilidade temporal;
- acesso claro a itens adicionais sem sobrecarregar a superfície.

## 11. Estados ainda não resolvidos

Permanecem pendentes de wireframes separados:

- estado totalmente vazio;
- múltiplos itens críticos;
- informação sensível em modo discreto;
- falha de fonte externa;
- baixa conectividade;
- contexto de Organização;
- contexto de Coletivo;
- alteração de preço em processo iniciado;
- acessibilidade com texto ampliado.

## 12. Limites

Esta decisão não autoriza:

- design visual definitivo;
- definição de cores, tipografia ou iconografia;
- protótipo navegável;
- testes de usabilidade;
- implementação;
- criação automática dos estados alternativos;
- retomada da decisão sobre Capacidade de reinvestimento responsável;
- início da Engenharia de Produto.

## 13. Próximo ponto de decisão

Após a integração desta reformulação, a próxima decisão deverá escolher separadamente entre:

1. validar funcionalmente o Detalhe de Oportunidade;
2. validar funcionalmente o Cadastro de Oportunidade pela Organização;
3. selecionar um estado alternativo da Tela Hoje para novo wireframe.

O protótipo navegável continuará dependendo de autorização explícita posterior.