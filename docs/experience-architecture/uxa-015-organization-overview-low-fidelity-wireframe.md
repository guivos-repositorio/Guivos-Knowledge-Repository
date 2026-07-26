---
id: UXA-015
title: Wireframe de Baixa Fidelidade da Visão Geral da Organização
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-005
depends_on:
  - UXA-003
  - UXA-004
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-013
  - UXA-014
related:
  - UXA-016
  - UXA-017
normative: false
---

# Wireframe de Baixa Fidelidade da Visão Geral da Organização

## 1. Pergunta da superfície

> **Em nome de qual Organização estou atuando, qual é o momento institucional, qual responsabilidade exige decisão e como a Organização está cumprindo seus compromissos com jornadas humanas?**

A Visão Geral da Organização é a superfície inicial do contexto institucional. Ela organiza autoridade, momento, compromissos, capacidade, responsabilidades, movimentos operacionais, evidências, relações e decisões.

Ela não deverá funcionar como painel de vendas, página publicitária, catálogo de oportunidades, relatório financeiro isolado ou painel genérico de indicadores.

## 2. Wireframe reformulado

![Wireframe para computador da Visão Geral da Organização](../assets/wireframes/uxa-015-organization-overview-desktop.svg)

[Visualizar o arquivo gráfico vetorial escalável](../assets/wireframes/uxa-015-organization-overview-desktop.svg)

O wireframe permanece estrutural e monocromático. Ele não define identidade visual final, componentes técnicos ou comportamento implementado.

## 3. Hierarquia funcional

| Ordem | Bloco | Responsabilidade |
|---:|---|---|
| 1 | autoridade representada e contexto | mostrar Organização, unidade, papel, escopo de autoridade e verificação |
| 2 | momento institucional | explicar mudanças, compromissos afetados, fontes e incertezas |
| 3 | responsabilidade principal agora | apresentar uma responsabilidade material, motivo, consequência, responsável e alternativas |
| 4 | jornadas apoiadas e compromissos ativos | mostrar finalidade humana, compromisso assumido, limites e evidências sem expor perfis individuais |
| 5 | capacidade e condições para cumprir | relacionar recursos, disponibilidade, acessibilidade, suporte e limitações aos compromissos |
| 6 | movimentos institucionais | apresentar oportunidades e programas por estado, responsabilidade e decisão necessária |
| 7 | avanço institucional e evidências | reconhecer mudança relevante relacionada a compromissos, com evidência e limitações |
| 8 | relações, dependências e transparência | apresentar Coletivos, Organizações, recursos, dados, patrocínio e autonomia |
| 9 | decisões e Próximos Passos | justificar decisões e preservar alternativas legítimas |
| 10 | navegação institucional | permitir acesso às demais áreas da Organização |

## 4. Autoridade representada e contexto

O cabeçalho deverá permanecer visível e apresentar:

- nome da Organização;
- unidade ou filial;
- papel da pessoa autenticada;
- escopo de autoridade;
- estado de verificação;
- contexto selecionado;
- acesso a permissões, ajuda e contestação.

Exemplo:

> **Instituto Horizonte · Unidade Central**
>
> Você está atuando como Administrador institucional. Pode revisar informações, atribuir responsabilidades e pausar oportunidades desta unidade.

Ações fora do escopo deverão ser bloqueadas com explicação e caminho para solicitar autoridade legítima.

## 5. Como compreendemos este momento

A síntese deverá começar por mudanças e compromissos materiais, não por contagens.

Exemplo:

> A formação de Inglês profissional se aproxima da capacidade declarada. A condição de acessibilidade do próximo encontro ainda não foi confirmada e afeta o compromisso de participação sem barreiras. Duas oportunidades continuam em avaliação, sem decisão necessária hoje.

A superfície deverá distinguir:

- informação confirmada pela Organização;
- observação operacional;
- fonte externa autorizada;
- inferência da Guivos;
- informação desconhecida;
- informação contestada.

Controles:

- `Ver informações, fontes e incertezas`;
- `Corrigir o contexto institucional`;
- `Informar uma mudança`;
- `Contestar esta leitura`.

## 6. Responsabilidade principal agora

Somente uma responsabilidade material deverá receber prioridade principal.

Exemplo:

> **Confirmar a condição de acessibilidade do próximo encontro.**
>
> Esse compromisso afeta a decisão e a participação das pessoas. A informação precisa ser confirmada antes da abertura de novas inscrições. Ainda não existe responsável atribuído.

O bloco deverá mostrar:

- compromisso relacionado;
- motivo;
- prazo, risco ou consequência real;
- responsável ou ausência de responsável;
- ação principal;
- alternativas;
- possibilidade de contestação.

Ações possíveis:

- revisar agora;
- atribuir responsável;
- solicitar apoio especializado;
- limitar disponibilidade;
- pausar a atividade;
- definir prazo legítimo;
- contestar a prioridade.

## 7. Jornadas apoiadas e compromissos ativos

O bloco deverá apresentar:

- jornada ou necessidade geral apoiada;
- compromisso institucional;
- forma de contribuição;
- grupo geral autorizado;
- limites de atuação;
- evidências disponíveis;
- informações ainda não confirmadas.

Exemplo:

> **Transição profissional**
>
> Compromisso ativo: oferecer formação, mentoria e acesso a oportunidades com custos, condições e acessibilidade informados de forma compreensível.
>
> A adequação individual permanece com a Guivos e o participante.

A Organização não receberá contexto pessoal individual sem autoridade, finalidade, necessidade e consentimento legítimos.

## 8. Capacidade e condições para cumprir

A capacidade deverá ser relacionada ao compromisso, evitando percentuais isolados.

Deverá apresentar:

- capacidade declarada;
- capacidade confirmada;
- utilização conhecida;
- recursos disponíveis;
- suporte;
- acessibilidade;
- qualidade e validade da informação;
- limitações;
- responsável;
- decisão necessária.

Exemplo:

> A turma possui capacidade declarada para 50 participantes e 42 inscrições confirmadas. A ampliação não está confirmada. A Organização precisa decidir entre manter oito vagas, criar lista de espera ou encerrar inscrições.

## 9. Movimentos institucionais

Oportunidades e programas permanecerão visíveis, mas subordinados aos compromissos e responsabilidades.

Cada item deverá mostrar:

- título e natureza;
- jornada ou compromisso relacionado;
- estado;
- capacidade ou condição material;
- responsável institucional;
- alteração recente;
- decisão necessária;
- relação comercial, quando aplicável.

Estados resumidos:

- ativa;
- em avaliação;
- ajustes solicitados;
- próxima do limite de capacidade;
- pausada;
- expirando;
- informação contestada;
- encerrada.

Volume, vendas, conversão e publicidade não definirão a prioridade funcional.

## 10. Avanço institucional e evidências

Avanço somente aparecerá quando houver evidência suficiente de mudança relevante relacionada a um compromisso.

Exemplo:

> **Avanço institucional reconhecido:** todas as oportunidades ativas passaram a informar custo total, cancelamento e recursos de acessibilidade. A mudança melhorou a clareza das condições para participantes e reduziu correções solicitadas durante a avaliação.

A interface deverá mostrar:

- mudança observada;
- compromisso relacionado;
- evidência utilizada;
- período;
- contribuição demonstrável;
- limitações e incertezas;
- fonte ou confirmação;
- possibilidade de correção.

Quando não houver evidência suficiente:

> **Nenhum avanço institucional foi confirmado neste período.**

Aumento de vendas, visualizações, anúncios, seguidores ou quantidade de oportunidades não será apresentado isoladamente como evolução institucional.

## 11. Relações, dependências e transparência

Cada relação deverá mostrar:

- participante relacionado;
- finalidade;
- natureza do vínculo;
- autonomia e autoridade;
- responsabilidades;
- recursos ou apoio envolvidos;
- dados compartilhados;
- relação comercial ou patrocínio;
- dependências materiais;
- estado, revisão e encerramento.

Exemplo:

> O Coletivo Rede de Mentores conduz encontros mensais com autonomia de governança. A Organização fornece espaço e suporte administrativo. Nenhum dado pessoal é compartilhado fora das finalidades informadas.

## 12. Decisões e Próximos Passos

A superfície deverá distinguir decisão institucional de tarefa operacional.

A explicação seguirá:

```text
momento institucional compreendido
→ compromisso ou responsabilidade afetada
→ evidência e incertezas
→ decisão necessária
→ alternativas legítimas
→ contribuição esperada
→ responsável e prazo material
```

Exemplo:

> **Decidir a capacidade final da turma.**
>
> Faz sentido decidir agora porque as inscrições se aproximam do limite confirmado. As alternativas são manter oito vagas, criar lista de espera, confirmar ampliação responsável ou encerrar inscrições. Nenhuma alternativa será selecionada automaticamente.

## 13. Navegação institucional

A navegação inicial deverá incluir:

- Visão Geral;
- Oportunidades;
- Programas e Jornadas Apoiadas;
- Coletivos e Relações;
- Resultados e Evidências;
- Equipe, Papéis e Autoridades;
- Organização e Unidades;
- Privacidade, Proteção e Conformidade.

Os nomes poderão ser refinados posteriormente, mas deverão comunicar responsabilidades completas.

## 14. Estados alternativos preservados

Exigirão detalhamento separado:

- operação regular sem responsabilidade urgente;
- Organização não verificada;
- autoridade insuficiente;
- unidade sem responsável;
- contexto incompleto;
- informação contestada ou conflitante;
- nenhuma oportunidade ou programa ativo;
- capacidade limitada ou esgotada;
- obrigação material vencida;
- risco elevado;
- nenhuma evidência de avanço confirmada;
- relação institucional suspensa;
- falha de integração;
- baixa conectividade;
- operação em vários países, idiomas e moedas.

## 15. Critérios de aceite

A superfície foi considerada funcionalmente válida porque:

1. autoridade e contexto antecedem ação;
2. o momento institucional é compreensível, verificável e corrigível;
3. uma responsabilidade material recebe prioridade;
4. jornadas e compromissos antecedem volume operacional;
5. capacidade é relacionada ao compromisso que precisa ser cumprido;
6. oportunidades e programas permanecem subordinados;
7. avanço utiliza evidência de mudança relevante;
8. relações e dependências são transparentes;
9. decisões possuem justificativa e alternativas;
10. a superfície não parece painel comercial genérico;
11. o comportamento permanece alinhado à Fundação da Guivos.

## 16. Situação

A Visão Geral da Organização está **validada funcionalmente e reformulada em baixa fidelidade**.

Ela continua sendo hipótese estrutural e ainda não constitui protótipo navegável, design visual ou implementação.

## 17. Limites

Esta versão não cria protótipo navegável, design visual final, testes de usabilidade, componentes técnicos, indicadores empresariais finais, preços, planos comerciais, validação jurídica ou desenvolvimento.

## 18. Próxima etapa da ordem autorizada

Após a integração deste incremento, a próxima etapa será a validação funcional do **Início do Coletivo**, em incremento separado.
