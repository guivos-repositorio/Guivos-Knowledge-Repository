---
id: PAS-001-PP-VIEW-001
title: Comportamentos Funcionais da Visualização e do Controle dos Próximos Passos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-PP-FOUNDATION-001
  - PAS-001-PP-LIFECYCLE-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-PP-VIEW-001 — Comportamentos Funcionais da Visualização e do Controle dos Próximos Passos

## 1. Autoridade e vínculo

Este documento é a **terceira extensão normativa da Capacidade 05 — Próximos Passos** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 0 a 1672 consolidadas pelo `PAS-001 0.5.0`, pelas extensões normativas de Contexto Vivo, Objetivos, Eventos de Vida e pelos documentos `PAS-001-PP-FOUNDATION-001 1.0.0` e `PAS-001-PP-LIFECYCLE-001 1.0.0`.

Esta extensão mantém a Capacidade 05 no estado `In progress` e eleva seu progresso editorial de referência de `40%` para `60%`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade da especificação-base ou das capacidades concluídas.

# 1673. Visualização e controle dos Próximos Passos

A visualização deverá permitir que o participante compreenda, organize e controle seus movimentos possíveis sem transformar sua jornada em uma lista infinita de tarefas.

A superfície funcional principal será denominada:

> **Meus Próximos Passos**

Seu fluxo geral deverá permitir compreender:

```text
o que poderá ser feito
→ por que poderá fazer sentido
→ qual é o estado atual
→ o que depende de quê
→ o que impede a continuidade
→ quem possui responsabilidade
→ quando poderá ser realizado
→ quais alternativas existem
→ qual resultado foi observado
```

# 1674. Objetivos funcionais da visão

A visão deverá permitir ao participante:

1. compreender quais movimentos estão disponíveis;
2. distinguir propostas de decisões confirmadas;
3. identificar o que está pronto, agendado, em andamento, bloqueado ou pausado;
4. visualizar prioridades sem receber julgamento de produtividade;
5. compreender dependências e bloqueios;
6. comparar alternativas;
7. acompanhar passos recorrentes;
8. controlar responsabilidades;
9. revisar passos compartilhados;
10. iniciar, pausar, concluir, cancelar ou substituir movimentos;
11. registrar resultados;
12. corrigir ou contestar informações;
13. controlar compartilhamentos;
14. proteger passos sensíveis;
15. compreender recomendações e sugestões da Guivos;
16. reduzir sobrecarga e fadiga;
17. preservar períodos legítimos sem passos ativos.

# 1675. Princípios da visualização

## 1675.1 Clareza antes de quantidade

A interface deverá priorizar compreensão, não volume de itens apresentados.

## 1675.2 Movimento, não tarefa

A visualização deverá preservar Próximo Passo como movimento contextual, mesmo quando tarefas operacionais existirem.

## 1675.3 Autonomia

O participante deverá poder rejeitar, modificar, adiar, pausar, cancelar ou substituir passos pessoais.

## 1675.4 Estado real

A interface não deverá apresentar proposta, sugestão, agendamento ou atividade observada como execução ou conclusão confirmada.

## 1675.5 Prioridade explicável

Toda prioridade sugerida deverá possuir justificativa compreensível.

## 1675.6 Privacidade por padrão

Passos sensíveis deverão permanecer minimizados até ação consciente do participante.

## 1675.7 Detalhamento progressivo

A visão deverá apresentar primeiro o necessário para decisão e controle.

## 1675.8 Ausência de cobrança

A interface não deverá utilizar culpa, vergonha, medo, competição ou pressão artificial.

## 1675.9 Neutralidade comercial

Produtos, serviços, patrocínios e comissões não deverão alterar prioridade ou destaque funcional.

## 1675.10 Ação no mundo real

A experiência deverá apoiar realização concreta, não maximizar tempo de tela.

# 1676. Escopo da superfície

`Meus Próximos Passos` deverá governar a visualização e o controle dos movimentos da jornada.

Ela não deverá substituir:

- `Meus Objetivos`;
- `Meu Contexto Hoje`;
- Eventos de Vida;
- agenda ou calendário completo;
- gerenciador de projetos;
- lista genérica de tarefas;
- Oportunidades Ativas;
- Intervenções Contextuais;
- Experiências;
- avaliação de evolução;
- serviços profissionais especializados.

# 1677. Estrutura funcional principal

A superfície poderá possuir:

1. visão geral;
2. portfólio ativo;
3. propostas e alternativas;
4. próximos movimentos;
5. agenda e janelas;
6. dependências e bloqueios;
7. passos em andamento;
8. recorrências;
9. passos compartilhados;
10. resultados recentes;
11. histórico e arquivados;
12. configurações de privacidade e notificações.

A arquitetura visual definitiva pertence ao design posterior.

# 1678. Visão geral

A visão geral deverá sintetizar:

- passo principal, quando existir;
- passos ativos;
- passos prontos;
- passos agendados;
- passos em andamento;
- passos bloqueados;
- passos pausados;
- propostas pendentes;
- decisões necessárias;
- dependências próximas de resolução;
- resultados aguardando revisão;
- sincronizações pendentes.

Ela não deverá apresentar uma pontuação geral de produtividade.

# 1679. Resumo linguístico

A Guivos poderá apresentar resumo como:

> Você possui dois movimentos em andamento, um passo pronto para começar e uma proposta aguardando sua decisão.

A linguagem deverá:

- ser descritiva;
- evitar culpa;
- evitar urgência artificial;
- distinguir sugestão e decisão;
- informar incerteza;
- permitir acesso aos detalhes;
- respeitar preferências linguísticas.

# 1680. Ausência de Próximos Passos

Quando não houver passos ativos, a visão poderá apresentar:

> Nenhum Próximo Passo precisa da sua atenção agora.

A ausência não deverá ser tratada como:

- inatividade inadequada;
- falta de objetivo;
- baixa evolução;
- desengajamento;
- falha;
- necessidade de criar novas ações.

# 1681. Portfólio ativo

O portfólio ativo deverá reunir somente movimentos com relevância operacional atual.

Ele poderá apresentar:

- principal;
- prioritários;
- prontos;
- agendados;
- em andamento;
- bloqueados;
- pausados;
- aguardando condição;
- alternativos;
- compartilhados.

Passos futuros e propostas não confirmadas deverão permanecer separados.

# 1682. Limite visual do portfólio

A interface deverá evitar apresentar todos os passos simultaneamente.

Poderá utilizar:

- recortes;
- agrupamentos;
- filtros;
- expansão progressiva;
- foco por objetivo;
- foco por período;
- foco por contexto;
- foco por responsabilidade.

Itens adicionais deverão permanecer acessíveis sem competir visualmente com os movimentos atuais.

# 1683. Organização do portfólio

O participante poderá organizar a visão por:

- prioridade;
- estado;
- objetivo;
- área da vida;
- responsabilidade;
- período;
- prontidão;
- esforço;
- bloqueio;
- sensibilidade;
- passo compartilhado;
- origem;
- tipo funcional.

A organização escolhida não deverá alterar o estado dos registros.

# 1684. Formas de visualização

A superfície poderá oferecer:

- lista;
- cartões;
- linha temporal;
- agenda;
- sequência;
- dependências;
- agrupamento por objetivo;
- agrupamento por contexto;
- quadro de estados;
- visão resumida.

Nenhuma forma visual deverá redefinir a semântica funcional.

# 1685. Filtros

Os filtros poderão incluir:

- estado;
- prioridade;
- horizonte;
- tipo;
- titular;
- responsável;
- executor;
- objetivo relacionado;
- Evento de Vida relacionado;
- prontidão;
- bloqueio;
- recorrência;
- sensibilidade;
- origem;
- compartilhamento;
- atualidade.

Filtros deverão ser reversíveis e compreensíveis.

# 1686. Busca

A busca deverá considerar:

- formulação;
- expressão original;
- objetivo;
- resultado esperado;
- responsável;
- dependência;
- bloqueio;
- alternativa;
- evento relacionado.

Passos sensíveis deverão respeitar limitações de indexação e acesso.

# 1687. Cartão de Próximo Passo

Cada Próximo Passo poderá ser representado por um cartão funcional.

O cartão deverá apresentar somente as informações necessárias para:

- identificação;
- compreensão do estado;
- decisão;
- próxima ação possível;
- reconhecimento de atenção necessária.

# 1688. Conteúdo mínimo do cartão

O cartão poderá apresentar:

- formulação resumida;
- estado funcional;
- prioridade, quando relevante;
- objetivo ou contexto relacionado;
- janela temporal;
- responsável;
- prontidão;
- bloqueio principal;
- indicação de compartilhamento;
- marcador de sensibilidade;
- ação principal disponível.

# 1689. Informações não obrigatórias no cartão

Não deverão ser expostos automaticamente:

- narrativa completa;
- dados clínicos;
- valores financeiros;
- nomes de terceiros;
- justificativas sensíveis;
- evidências;
- histórico detalhado;
- permissões completas;
- documentos;
- dados de localização;
- significado emocional.

# 1690. Títulos funcionais

O título deverá descrever o movimento de forma:

- clara;
- neutra;
- acionável;
- não julgadora;
- proporcional;
- compreensível.

Exemplo adequado:

> Conversar com a instituição sobre as opções disponíveis.

Exemplo inadequado:

> Resolver sua falta de comprometimento com a formação.

# 1691. Títulos neutros para passos sensíveis

Um passo sensível poderá aparecer como:

> Revisar assunto pessoal.

em vez de revelar:

> Agendar avaliação para condição clínica específica.

O participante deverá poder controlar a apresentação.

# 1692. Estado visual

O estado deverá ser apresentado por:

- texto;
- ícone acessível;
- explicação;
- indicação visual complementar.

A interface não deverá depender exclusivamente de cor.

# 1693. Estado funcional e estado da informação

A visão deverá apresentá-los separadamente quando necessário.

```text
Estado funcional:
Em andamento

Estado da informação:
Atualização pendente
```

Outro exemplo:

```text
Estado funcional:
Concluído

Estado da informação:
Contestado
```

# 1694. Prioridade no cartão

Quando apresentada, a prioridade deverá indicar:

- nível;
- escopo;
- origem;
- fatores considerados;
- possibilidade de alteração.

Ela não deverá ser confundida com urgência, obrigação ou valor pessoal.

# 1695. Prontidão no cartão

A prontidão poderá ser apresentada como:

- pronto;
- parcialmente pronto;
- dependência pendente;
- bloqueado;
- revisão necessária;
- informação insuficiente.

O cartão deverá permitir compreender o motivo.

# 1696. Ação principal do cartão

A ação principal deverá variar conforme o estado.

Exemplos:

| Estado | Ação principal possível |
|---|---|
| Proposto | Avaliar |
| Confirmado | Preparar |
| Pronto | Iniciar |
| Agendado | Consultar agenda |
| Em andamento | Atualizar |
| Bloqueado | Ver impedimento |
| Pausado | Revisar retomada |
| Concluído | Registrar resultado |
| Contestado | Resolver contestação |
| Expirado | Reavaliar |
| Arquivado | Consultar histórico |

A ação não deverá ocultar alternativas relevantes.

# 1697. Detalhamento do Próximo Passo

A visão detalhada deverá permitir consultar:

1. formulação;
2. expressão original;
3. titular;
4. proponente;
5. decisor;
6. responsável;
7. executor;
8. estado funcional;
9. estado da informação;
10. tipo;
11. origem;
12. autoridade;
13. finalidade;
14. objetivo relacionado;
15. Evento de Vida relacionado;
16. resultado imediato esperado;
17. prioridade;
18. prontidão;
19. temporalidade;
20. dependências;
21. bloqueios;
22. esforço;
23. risco;
24. alternativas;
25. recorrência;
26. compartilhamentos;
27. permissões;
28. evidências;
29. histórico;
30. ações disponíveis.

# 1698. Formulação e expressão original

A visão deverá distinguir:

## Formulação funcional

Representação estruturada do movimento.

## Expressão original

Forma como o participante ou fonte descreveu a intenção.

A reformulação não deverá apagar a expressão original.

# 1699. Relação contextual

O detalhamento deverá explicar por que o passo existe.

Ele poderá estar relacionado a:

- objetivo;
- necessidade;
- responsabilidade;
- Evento de Vida;
- mudança de contexto;
- bloqueio;
- oportunidade;
- obrigação;
- resultado anterior;
- preparação;
- proteção;
- exploração.

# 1700. Explicação da proposta

Quando o passo tiver sido proposto, a visão deverá informar:

- quem propôs;
- por que foi proposto;
- quais informações foram consideradas;
- quais alternativas existem;
- quais limitações existem;
- se houve uso de Guivos Intelligence;
- se existe interesse comercial relacionado;
- quais efeitos ocorrerão após confirmação.

# 1701. Propostas pendentes

As propostas deverão permanecer em área separada dos passos confirmados.

Elas poderão ser organizadas por:

- relevância contextual;
- objetivo;
- origem;
- prazo de oportunidade;
- tipo;
- sensibilidade;
- necessidade de decisão.

A interface não deverá criar pressão para aceitar propostas.

# 1702. Avaliação de proposta

A visão deverá permitir:

- confirmar;
- rejeitar;
- reformular;
- comparar alternativas;
- solicitar explicação;
- adiar decisão;
- limitar finalidade;
- ocultar;
- arquivar.

A rejeição não deverá exigir justificativa obrigatória.

# 1703. Comparação de alternativas

Alternativas poderão ser comparadas por:

- resultado imediato;
- esforço;
- temporalidade;
- risco;
- reversibilidade;
- dependências;
- custo;
- disponibilidade;
- adequação contextual;
- necessidade de apoio;
- sensibilidade;
- impacto sobre outros passos.

A comparação não deverá produzir vencedor automático sem regra autorizada.

# 1704. Alternativa recomendada

Quando a Guivos destacar uma alternativa, deverá explicar:

- critérios considerados;
- informações utilizadas;
- limitações;
- incerteza;
- alternativas não destacadas;
- existência de patrocínio ou relação comercial.

Interesse comercial não deverá determinar a recomendação funcional.

# 1705. Confirmação visual

Antes de confirmar um Próximo Passo, a visão deverá apresentar:

- formulação;
- titular;
- responsável;
- resultado esperado;
- condições;
- nível de compromisso;
- prazo ou janela, quando existente;
- compartilhamentos;
- riscos;
- efeitos da confirmação.

# 1706. Confirmação não implica outras ações

A interface deverá informar que confirmar não significa automaticamente:

- iniciar;
- agendar;
- compartilhar;
- contratar serviço;
- reservar recurso;
- aceitar oportunidade;
- assumir prazo;
- alterar objetivo;
- concluir decisão externa.

# 1707. Confirmação condicionada

Passos condicionados deverão apresentar claramente:

- condição;
- estado da condição;
- fonte;
- forma de verificação;
- consequência do atendimento;
- consequência da não ocorrência;
- momento de revisão.

# 1708. Confirmação parcial

Em passo composto ou compartilhado, o participante deverá poder confirmar:

- apenas sua responsabilidade;
- parte do movimento;
- determinado período;
- um subpasso;
- uma condição;
- determinado compartilhamento.

# 1709. Rejeição visual

Ao rejeitar uma proposta, a interface deverá:

- informar que nenhum compromisso será criado;
- permitir arquivamento;
- oferecer alternativa opcional;
- preservar motivo somente quando declarado;
- impedir penalização;
- evitar nova apresentação repetitiva.

# 1710. Portfólio de possibilidades

Possibilidades ainda não confirmadas poderão permanecer em área como:

> Para considerar depois

Essa área deverá:

- não competir com passos ativos;
- permitir revisão futura;
- permitir exclusão;
- indicar origem;
- evitar notificações frequentes;
- não ser tratada como backlog obrigatório.

# 1711. Visualização da prioridade

A prioridade deverá ser apresentada separadamente de:

- urgência;
- prazo;
- estado;
- prontidão;
- esforço;
- risco;
- importância do objetivo;
- valor humano.

# 1712. Explicação da prioridade

A visão deverá conseguir responder:

- por que este passo recebeu prioridade;
- quem definiu;
- quais fatores foram considerados;
- qual escopo da prioridade;
- quando foi revisada;
- como alterá-la;
- quais passos poderão ser afetados.

# 1713. Alteração de prioridade

O participante deverá poder:

- aumentar;
- reduzir;
- remover;
- definir como principal;
- retirar condição de principal;
- mover para futuro;
- manter sem prioridade;
- aplicar prioridade dentro de um objetivo específico.

# 1714. Reordenação manual

A interface poderá permitir reordenação manual.

A reordenação deverá:

- registrar decisão;
- preservar dependências;
- alertar sobre conflitos objetivos;
- não alterar estados;
- não modificar prioridades institucionais fora da autoridade;
- permitir desfazimento.

# 1715. Prioridade institucional

Passos institucionais deverão indicar:

- autoridade;
- origem;
- prazo;
- natureza obrigatória ou opcional;
- possibilidade de contestação;
- separação da prioridade pessoal.

A interface não deverá transformar prioridade institucional em prioridade global da vida.

# 1716. Prontidão

A visão deverá demonstrar quais condições já foram atendidas e quais permanecem pendentes.

Exemplo:

```text
Prontidão:
Parcialmente pronto

Condições atendidas:
- decisão confirmada
- documento disponível

Condição pendente:
- autorização da instituição
```

# 1717. Checklist de prontidão

O checklist poderá incluir:

- informação;
- decisão;
- recurso;
- documento;
- autorização;
- competência;
- disponibilidade;
- responsável;
- segurança;
- dependência.

Ele não deverá ser transformado automaticamente em lista de tarefas obrigatórias.

# 1718. Início do passo

Quando o passo estiver pronto, a visão poderá oferecer:

- iniciar agora;
- agendar;
- manter pronto;
- revisar prioridade;
- adicionar preparação;
- pausar;
- cancelar;
- escolher alternativa.

A interface não deverá pressionar o início imediato.

# 1719. Agenda dos Próximos Passos

A agenda deverá apresentar somente passos com:

- data;
- janela;
- compromisso;
- recorrência;
- gatilho temporal;
- revisão prevista.

Ela não deverá substituir o calendário geral do participante.

# 1720. Tipos de temporalidade visual

A interface deverá distinguir:

- data confirmada;
- data sugerida;
- prazo;
- janela;
- período aproximado;
- condição futura;
- recorrência;
- revisão;
- temporalidade desconhecida.

Datas sugeridas não deverão parecer compromissos confirmados.

# 1721. Passos sem prazo

Passos sem prazo deverão permanecer válidos.

A interface poderá utilizar expressões como:

- quando houver disponibilidade;
- após a condição ser atendida;
- em momento oportuno;
- sem data definida;
- para revisão futura.

# 1722. Prazo vencido

A visão deverá apresentar o prazo vencido sem linguagem de culpa.

Ações possíveis:

- manter;
- reagendar;
- remover prazo;
- pausar;
- revisar;
- substituir;
- cancelar;
- registrar conclusão retroativa.

# 1723. Adiamento

Ao adiar, a interface deverá permitir:

- nova data;
- nova janela;
- condição;
- motivo opcional;
- revisão de dependências;
- atualização de participantes;
- ajuste de notificações.

Adiamentos repetidos deverão gerar oferta de revisão, não julgamento.

# 1724. Dependências

As dependências deverão ser apresentadas de forma visível e compreensível.

Cada dependência poderá apresentar:

- descrição;
- tipo;
- estado;
- responsável;
- criticidade;
- temporalidade;
- ação possível;
- evidência;
- relação com outros passos.

# 1725. Mapa de dependências

Quando útil, a interface poderá apresentar:

```text
Passo A
→ depende de Documento X
→ depende da decisão de Pessoa B
→ desbloqueia Passo C
```

O mapa deverá possuir alternativa textual acessível.

# 1726. Dependências externas

Dependências externas deverão indicar:

- pessoa ou organização;
- autoridade;
- informação compartilhada;
- resposta esperada;
- prazo, quando existente;
- alternativa;
- limite de controle do participante.

A interface não deverá responsabilizar o participante por condições externas.

# 1727. Dependência atendida

Ao atender uma dependência, a visão deverá informar possíveis efeitos:

- passo torna-se pronto;
- bloqueio é removido;
- prioridade poderá mudar;
- agendamento torna-se possível;
- outro passo é desbloqueado;
- nova confirmação poderá ser necessária.

# 1728. Bloqueios

A interface deverá distinguir bloqueio de:

- dificuldade;
- baixa prioridade;
- pausa;
- ausência de prazo;
- esforço elevado;
- incerteza;
- atraso.

# 1729. Cartão de bloqueio

O bloqueio deverá apresentar:

- descrição;
- origem;
- criticidade;
- temporalidade;
- condição de resolução;
- responsável possível;
- alternativas;
- próxima revisão;
- sensibilidade.

# 1730. Ações sobre bloqueios

O participante poderá:

- corrigir;
- contestar;
- resolver;
- dispensar, quando autorizado;
- escolher alternativa;
- solicitar apoio;
- pausar o passo;
- reformular;
- cancelar;
- definir revisão posterior.

# 1731. Bloqueios sensíveis

Bloqueios relacionados a:

- saúde;
- finanças;
- família;
- trabalho;
- questões jurídicas;
- violência;
- deficiência;
- religião;
- sexualidade;
- localização;

deverão possuir visualização minimizada e acesso restrito.

# 1732. Passos em andamento

A visão deverá apresentar:

- formulação atual;
- início;
- responsável;
- execução realizada;
- próximos elementos;
- dependências;
- bloqueios;
- resultado parcial;
- prazo;
- risco;
- última atualização;
- ações disponíveis.

# 1733. Atualização de execução

O participante poderá registrar:

- ação realizada;
- resultado parcial;
- bloqueio;
- mudança de escopo;
- alteração de prazo;
- esforço real;
- apoio necessário;
- evidência;
- decisão de pausa;
- conclusão.

O registro não deverá exigir acompanhamento excessivo.

# 1734. Nível de acompanhamento

A interface poderá oferecer níveis como:

- somente estado final;
- atualizações essenciais;
- acompanhamento periódico;
- acompanhamento detalhado;
- acompanhamento institucional obrigatório.

O participante deverá controlar o nível em passos pessoais.

# 1735. Subpassos e tarefas

Subpassos e tarefas deverão aparecer como detalhamento opcional.

A interface deverá permitir:

- adicionar;
- concluir;
- reordenar;
- delegar;
- remover;
- ocultar.

A conclusão de todas as tarefas não deverá concluir automaticamente um passo qualitativo quando o resultado ainda exigir confirmação.

# 1736. Resultado imediato

A visão deverá apresentar o resultado separadamente do estado de execução.

```text
Execução:
Concluída

Resultado:
Diferente do esperado
```

Outro exemplo:

```text
Execução:
Concluída

Resultado:
Ainda desconhecido
```

# 1737. Registro de resultado

O participante poderá registrar:

- alcançado;
- parcialmente alcançado;
- não alcançado;
- diferente do esperado;
- desconhecido;
- contestado;
- não aplicável.

A interface deverá permitir descrição adicional opcional.

# 1738. Conclusão

Antes de concluir, a visão deverá apresentar:

- formulação;
- resultado imediato;
- partes concluídas;
- partes pendentes;
- dependências liberadas;
- passos desbloqueados;
- evidências;
- capacidades que poderão receber recortes.

# 1739. Conclusão sem resultado esperado

A interface deverá permitir concluir o passo mesmo quando o resultado desejado não ocorrer.

Ela deverá preservar:

- execução realizada;
- resultado observado;
- aprendizado;
- necessidade de nova decisão;
- relação com o objetivo.

# 1740. Conclusão parcial

Passos compostos deverão permitir:

- registrar partes concluídas;
- manter partes pendentes;
- desdobrar o restante;
- concluir o ciclo atual;
- criar novo passo;
- cancelar parte não necessária.

# 1741. Conclusão automática

Quando a conclusão for automática, a interface deverá informar:

- fonte;
- fato reconhecido;
- momento;
- autoridade;
- possibilidade de contestação;
- efeitos produzidos.

# 1742. Cancelamento

Ao cancelar, a visão deverá apresentar:

- compromissos existentes;
- participantes afetados;
- recursos reservados;
- dependências;
- passos relacionados;
- compartilhamentos;
- resultados já produzidos.

O cancelamento não deverá ser apresentado como fracasso.

# 1743. Substituição

A interface deverá permitir:

- escolher passo substituto;
- criar novo passo;
- transferir dependências;
- revisar responsabilidades;
- preservar histórico;
- cancelar notificações anteriores;
- manter resultados produzidos.

# 1744. Expiração

Passos expirados deverão indicar:

- motivo;
- regra;
- fonte;
- data;
- oportunidade relacionada;
- alternativas;
- possibilidade de reabertura;
- possibilidade de contestação.

# 1745. Contestação

O participante deverá poder contestar:

- formulação;
- titularidade;
- responsabilidade;
- prioridade;
- estado;
- prazo;
- bloqueio;
- conclusão;
- cancelamento;
- expiração;
- resultado;
- evidência;
- compartilhamento.

# 1746. Visão de contestação

A interface deverá apresentar:

- item contestado;
- informação atual;
- origem;
- efeitos temporariamente limitados;
- status da revisão;
- próximos passos;
- histórico;
- possibilidade de adicionar evidência.

# 1747. Correção

A correção deverá permitir:

- alterar informação incorreta;
- preservar versão anterior;
- explicar efeitos;
- recompor recortes;
- notificar participantes necessários;
- revisar automações;
- desfazer quando aplicável.

# 1748. Reabertura

Ao reabrir, a visão deverá indicar:

- ciclo anterior;
- motivo;
- contexto atual;
- nova temporalidade;
- dependências;
- prioridade;
- necessidade de nova confirmação;
- relação com resultados anteriores.

# 1749. Arquivamento

O arquivamento deverá retirar o passo da operação cotidiana.

A interface deverá informar que:

- o histórico permanece;
- resultados permanecem;
- relações permanecem;
- impactos legítimos permanecem;
- o passo poderá ser consultado;
- reabertura poderá ser possível.

# 1750. Recorrência

A visão de recorrência deverá demonstrar:

- frequência;
- período;
- próxima ocorrência;
- ocorrências anteriores;
- ocorrências pendentes;
- condição de pausa;
- condição de encerramento;
- forma de conclusão.

# 1751. Ocorrências recorrentes

Cada ocorrência poderá apresentar:

- data;
- estado;
- executor;
- resultado;
- evidência;
- motivo de não realização;
- contestação;
- correção.

# 1752. Ocorrência não realizada

A interface deverá permitir classificar como:

- adiada;
- dispensada;
- cancelada;
- bloqueada;
- não aplicável;
- perdida;
- desconhecida.

Não deverá utilizar linguagem de punição, sequência quebrada ou fracasso.

# 1753. Indicadores de recorrência

A interface não deverá apresentar automaticamente:

- disciplina;
- aderência pessoal;
- força de vontade;
- evolução;
- mérito;
- ranking;
- comparação social.

Estatísticas operacionais poderão existir quando úteis e autorizadas.

# 1754. Pausa da recorrência

A pausa deverá permitir:

- definir início;
- definir revisão;
- informar motivo opcional;
- suspender notificações;
- preservar ocorrências anteriores;
- impedir geração retroativa automática;
- manter opção de encerramento.

# 1755. Passos compartilhados

A visão deverá separar:

- parte comum;
- responsabilidades individuais;
- decisões pendentes;
- confirmações;
- conteúdos privados;
- dependências coletivas;
- temporalidade;
- participantes.

# 1756. Confirmações compartilhadas

A interface deverá indicar:

- quem confirmou;
- quem ainda não confirmou;
- quem rejeitou;
- quem não possui responsabilidade;
- quais partes estão confirmadas;
- quais decisões permanecem pendentes.

# 1757. Responsabilidades compartilhadas

Cada responsabilidade deverá apresentar:

- titular;
- responsável;
- executor;
- escopo;
- autoridade;
- prazo;
- dependências;
- estado;
- possibilidade de delegação.

# 1758. Delegação

A interface deverá permitir ao executor:

- aceitar;
- rejeitar;
- solicitar esclarecimento;
- negociar prazo;
- limitar escopo;
- informar bloqueio;
- propor alternativa.

Responsabilidade não deverá surgir por silêncio.

# 1759. Saída de participante

Quando aplicável, a visão deverá permitir:

- retirar responsabilidade futura;
- preservar ações anteriores;
- revisar dependências;
- informar participantes necessários;
- proteger conteúdo privado;
- recompor o passo compartilhado.

# 1760. Compartilhamentos

A visão deverá indicar:

- quem possui acesso;
- qual recorte recebe;
- finalidade;
- período;
- possibilidade de redistribuição;
- última utilização relevante;
- condição de revogação.

# 1761. Revogação

Ao revogar, a interface deverá:

- interromper novos usos;
- indicar propagação pendente;
- informar consumidores;
- explicar obrigações legítimas;
- mostrar efeitos que não podem ser revertidos;
- confirmar conclusão somente após processamento efetivo.

# 1762. Privacidade visual

A visão deverá permitir:

- títulos neutros;
- ocultação de detalhes;
- modo discreto;
- autenticação reforçada;
- notificações minimizadas;
- ocultação em dispositivos compartilhados;
- limitação de capturas automáticas;
- restrição de busca;
- separação entre passo pessoal e institucional.

# 1763. Notificações

As notificações deverão:

- utilizar conteúdo mínimo;
- evitar culpa;
- respeitar frequência;
- respeitar silêncio;
- evitar exposição sensível;
- distinguir sugestão de compromisso;
- permitir desativação;
- não repetir avisos dispensados;
- não utilizar urgência comercial.

# 1764. Fila de atenção

A fila poderá reunir:

- propostas aguardando decisão;
- passos com bloqueio crítico;
- dependências próximas;
- prazos relevantes;
- responsabilidades compartilhadas pendentes;
- contestações;
- sincronizações incompletas;
- resultados aguardando revisão;
- revogações pendentes.

A fila não deverá tratar todos os itens como urgentes.

# 1765. Priorização da atenção

A atenção poderá considerar:

- risco;
- irreversibilidade;
- prazo real;
- responsabilidade sobre terceiros;
- segurança;
- dependência crítica;
- decisão necessária;
- sensibilidade;
- preferência do participante.

Interesse comercial não deverá influenciar.

# 1766. Prevenção de fadiga

A interface deverá:

- agrupar revisões relacionadas;
- evitar perguntas repetidas;
- limitar notificações;
- permitir adiamento;
- oferecer revisão em lote quando seguro;
- não fragmentar movimentos artificialmente;
- ocultar possibilidades futuras da visão principal;
- respeitar silêncio funcional.

# 1767. Revisão do portfólio

A revisão deverá permitir:

- confirmar atualidade;
- retirar passos irrelevantes;
- revisar prioridades;
- identificar excesso;
- revisar bloqueios;
- ajustar temporalidade;
- arquivar;
- substituir;
- reconhecer ausência legítima de movimentos.

# 1768. Revisão em lote

A revisão em lote poderá ser utilizada para:

- arquivar itens antigos;
- mover passos para futuro;
- remover prioridades;
- pausar notificações;
- confirmar atualidade.

Ações materiais como conclusão, cancelamento, responsabilidade ou compartilhamento deverão exigir revisão individual quando necessário.

# 1769. Explicabilidade

A visão deverá permitir explicações sobre:

- criação;
- proposição;
- prioridade;
- prontidão;
- bloqueio;
- alternativa;
- agendamento;
- conclusão;
- expiração;
- recomendação;
- compartilhamento;
- automação;
- falha;
- sincronização.

# 1770. Explicação da criação

A Guivos deverá responder:

- por que o passo existe;
- qual foi a origem;
- quem o propôs;
- qual necessidade atende;
- se foi confirmado;
- quais informações foram utilizadas.

# 1771. Explicação da recomendação

Uma recomendação deverá informar:

- objetivo ou necessidade considerada;
- contexto utilizado;
- fatores favoráveis;
- limitações;
- riscos;
- alternativas;
- relação comercial, quando existir;
- papel da Guivos Intelligence.

# 1772. Explicação da prontidão

A visão deverá mostrar:

- condições atendidas;
- condições pendentes;
- bloqueios;
- fontes;
- atualidade da avaliação;
- possibilidade de contestação;
- ação necessária, quando existente.

# 1773. Explicação do bloqueio

A explicação deverá indicar:

- impedimento;
- origem;
- por que impede a continuidade;
- como poderá ser resolvido;
- alternativas;
- limite de controle do participante;
- data de revisão.

# 1774. Explicação da conclusão

A visão deverá indicar:

- quem reconheceu;
- qual fato sustentou;
- resultado registrado;
- evidência;
- efeitos produzidos;
- possibilidade de correção;
- relação com objetivos.

# 1775. Histórico

O histórico deverá apresentar:

- criação;
- formulações;
- propostas;
- confirmações;
- prioridades;
- prontidão;
- agendamentos;
- dependências;
- bloqueios;
- pausas;
- retomadas;
- execução;
- resultados;
- conclusões;
- cancelamentos;
- substituições;
- expirações;
- contestações;
- correções;
- compartilhamentos;
- revogações;
- falhas.

# 1776. Histórico compreensível

A visão padrão deverá utilizar linguagem compreensível.

Exemplo:

> O prazo foi alterado de 10 para 20 de agosto por decisão do participante.

Logs técnicos detalhados deverão permanecer em camada separada.

# 1777. Consistência entre canais

Aplicativo, web, conversa, notificações, calendário e integrações autorizadas deverão refletir:

- mesma versão;
- mesmo estado;
- mesma prioridade;
- mesmas permissões;
- mesmas contestações;
- mesmos bloqueios;
- mesma temporalidade;
- mesma responsabilidade.

# 1778. Canais conversacionais

Em conversa, a Guivos poderá:

- apresentar propostas;
- comparar alternativas;
- solicitar confirmação;
- registrar início;
- atualizar estado;
- registrar bloqueio;
- registrar resultado;
- concluir;
- cancelar;
- contestar;
- explicar.

As alterações deverão utilizar os mesmos contratos da visão principal.

# 1779. Integração com calendário

A visão poderá permitir:

- adicionar passo;
- criar janela;
- criar compromisso;
- atualizar data;
- remover compromisso;
- sincronizar estado de reserva.

O calendário não deverá confirmar execução ou conclusão automaticamente.

# 1780. Integração com oportunidades

A visualização poderá apresentar oportunidades relacionadas ao passo.

Ela deverá indicar:

- compatibilidade;
- elegibilidade;
- custo;
- origem;
- patrocínio;
- alternativas;
- limitações.

A oportunidade não deverá ocupar visualmente posição superior ao próprio movimento.

# 1781. Conteúdo comercial

Conteúdo comercial deverá permanecer:

- identificado;
- separado da prioridade funcional;
- explicável;
- opcional;
- compatível com a finalidade;
- não baseado em vulnerabilidade sensível.

# 1782. Acessibilidade

A visão deverá considerar:

- leitores de tela;
- navegação por teclado;
- contraste;
- escala de texto;
- linguagem simples;
- descrições de diagramas;
- alternativas a arrastar e soltar;
- datas compreensíveis;
- não dependência de cor;
- comandos acessíveis;
- carga cognitiva reduzida.

# 1783. Acessibilidade cognitiva

A interface deverá:

- reduzir quantidade simultânea de informações;
- utilizar linguagem consistente;
- evitar múltiplas decisões em uma única etapa;
- permitir salvar e continuar depois;
- oferecer exemplos;
- explicar termos;
- preservar previsibilidade;
- permitir visão simplificada.

# 1784. Falhas

Em caso de falha, a visão deverá informar:

- ação solicitada;
- estado anterior;
- parte concluída;
- parte pendente;
- possibilidade de repetição;
- risco de duplicidade;
- caminho de recuperação;
- necessidade de ação do participante.

# 1785. Sincronização pendente

A interface poderá apresentar:

> A alteração foi registrada, mas alguns serviços ainda estão processando a atualização.

Ela não deverá afirmar sucesso integral antes da confirmação necessária.

# 1786. Conflito de versões

Quando houver conflito, a visão deverá apresentar:

- versões;
- autores;
- temporalidades;
- diferenças;
- efeitos;
- possibilidade de escolha;
- necessidade de revisão.

Nenhuma versão deverá ser sobrescrita silenciosamente.

# 1787. Estado desatualizado

Quando a informação estiver desatualizada, a visão deverá:

- indicar a última atualização;
- reduzir automação;
- evitar conclusão;
- solicitar revisão proporcional;
- preservar o último estado válido;
- não interpretar ausência de atualização como abandono.

# 1788. Ações do participante

A superfície deverá permitir, conforme autoridade:

- criar;
- confirmar;
- rejeitar;
- reformular;
- dividir;
- unificar;
- priorizar;
- reordenar;
- ativar;
- preparar;
- agendar;
- adiar;
- iniciar;
- atualizar;
- bloquear;
- desbloquear;
- pausar;
- retomar;
- registrar resultado;
- concluir;
- cancelar;
- substituir;
- contestar;
- corrigir;
- reabrir;
- arquivar;
- delegar;
- compartilhar;
- revogar;
- ocultar;
- solicitar explicação.

# 1789. Confirmações de ações críticas

Deverão exigir confirmação proporcional:

- atribuir responsabilidade a terceiro;
- criar compromisso externo;
- compartilhar conteúdo sensível;
- concluir passo institucional;
- cancelar passo com dependências;
- substituir passo em andamento;
- alterar estado contestado;
- revogar compartilhamento;
- reabrir passo arquivado;
- aplicar ação em lote.

# 1790. Desfazimento

A interface deverá permitir desfazer ações reversíveis, como:

- prioridade;
- reordenação;
- arquivamento;
- ocultação;
- pausa;
- adiamento;
- alteração de filtro;
- mudança de visualização.

Ações historicamente materiais deverão utilizar correção ou compensação.

# 1791. Eventos funcionais da visão

A visão poderá produzir:

- `VisaoDeProximosPassosAcessada`;
- `PortfolioDeProximosPassosConsultado`;
- `FiltroDeProximosPassosAplicado`;
- `DetalheDeProximoPassoAcessado`;
- `PropostaDeProximoPassoRevisada`;
- `AlternativasDeProximoPassoComparadas`;
- `ProximoPassoConfirmadoPelaVisao`;
- `ProximoPassoRejeitadoPelaVisao`;
- `ProximoPassoReformuladoPelaVisao`;
- `PrioridadeDeProximoPassoAlteradaPelaVisao`;
- `ProntidaoDeProximoPassoConsultada`;
- `AgendamentoDeProximoPassoAlteradoPelaVisao`;
- `BloqueioDeProximoPassoRevisado`;
- `ProximoPassoIniciadoPelaVisao`;
- `ResultadoDeProximoPassoRegistradoPelaVisao`;
- `ProximoPassoConcluidoPelaVisao`;
- `ProximoPassoCanceladoPelaVisao`;
- `ProximoPassoSubstituidoPelaVisao`;
- `ProximoPassoContestadoPelaVisao`;
- `ProximoPassoCorrigidoPelaVisao`;
- `ProximoPassoArquivadoPelaVisao`;
- `ProximoPassoReabertoPelaVisao`;
- `ResponsabilidadeDeProximoPassoDelegadaPelaVisao`;
- `CompartilhamentoDeProximoPassoAlterado`;
- `PrivacidadeVisualDeProximoPassoAlterada`;
- `HistoricoDeProximoPassoConsultado`;
- `ExplicacaoDeProximoPassoSolicitada`;
- `ConflitoDeSincronizacaoDeProximoPassoExibido`.

# 1792. Métricas iniciais da visão

A visão poderá acompanhar:

- propostas consultadas;
- propostas rejeitadas;
- explicações solicitadas;
- prioridades alteradas;
- passos iniciados;
- passos adiados;
- bloqueios revisados;
- conclusões contestadas;
- ações desfeitas;
- notificações dispensadas;
- passos ocultados;
- falhas de sincronização;
- uso de modo privado;
- esforço de confirmação;
- abandono de fluxos críticos.

As métricas deverão avaliar a experiência e o sistema, não o valor do participante.

# 1793. Comportamentos visualmente proibidos

A visão não deverá:

- apresentar proposta como obrigação;
- transformar prioridade sugerida em ordem;
- utilizar contagem de passos como pontuação;
- exibir sequência de produtividade;
- penalizar atraso;
- celebrar quantidade sem contexto;
- classificar bloqueio como incapacidade;
- classificar pausa ou cancelamento como fracasso;
- utilizar vermelho como julgamento pessoal;
- destacar patrocinador como melhor movimento;
- revelar conteúdo sensível em notificações;
- atribuir responsabilidade por silêncio;
- apresentar data sugerida como compromisso;
- concluir passo por clique ou visualização;
- ocultar alternativas não comerciais;
- usar vulnerabilidade para induzir compra;
- criar ações artificiais para manter engajamento.

# 1794. Critérios funcionais de aceite

A visualização será considerada adequadamente definida quando:

1. possuir superfície principal clara;
2. apresentar visão geral sem pontuação de produtividade;
3. distinguir portfólio ativo, propostas e possibilidades futuras;
4. representar cartões minimizados;
5. oferecer detalhamento progressivo;
6. separar estado funcional e estado da informação;
7. distinguir prioridade, urgência, prontidão, prazo, esforço e risco;
8. explicar propostas e recomendações;
9. permitir comparação de alternativas;
10. apresentar confirmação proporcional;
11. preservar passos sem prazo;
12. representar agenda sem substituir calendário;
13. apresentar dependências e bloqueios;
14. permitir início sem pressão;
15. acompanhar execução proporcionalmente;
16. separar execução, resultado, progresso e conclusão;
17. permitir conclusão sem resultado esperado;
18. tratar cancelamento, substituição e expiração sem julgamento;
19. permitir contestação, correção e reabertura;
20. representar recorrência sem gamificação coercitiva;
21. suportar passos compartilhados e delegação;
22. apresentar responsabilidades individualizadas;
23. governar compartilhamentos e revogação;
24. proteger passos sensíveis;
25. oferecer acessibilidade;
26. prevenir fadiga;
27. preservar consistência entre canais;
28. explicar falhas e sincronização;
29. permitir controle amplo do participante;
30. manter neutralidade comercial.

# 1795. Regras fundamentais da visualização

1. `Meus Próximos Passos` é superfície de clareza e controle.
2. A visão não é lista infinita de tarefas.
3. Propostas não deverão parecer decisões assumidas.
4. Passos futuros não deverão competir com o portfólio ativo.
5. Prioridade não representa valor pessoal.
6. Urgência não equivale a prioridade.
7. Prontidão não equivale a início.
8. Agendamento não equivale a execução.
9. Execução não equivale ao resultado esperado.
10. Resultado não equivale a progresso.
11. Conclusão do passo não conclui o objetivo.
12. Bloqueio não representa incapacidade.
13. Pausa não representa fracasso.
14. Cancelamento não representa necessariamente desistência.
15. Prazo vencido não representa falha pessoal.
16. Ausência de atualização não representa abandono.
17. Passos sem prazo são legítimos.
18. Ausência de Próximo Passo é legítima.
19. A rejeição de proposta não gera penalidade.
20. Alternativas deverão permanecer visíveis.
21. Tarefas são detalhamento opcional.
22. Recorrência não comprova hábito.
23. Ocorrência não realizada não mede disciplina.
24. Confirmação compartilhada é individual.
25. Responsabilidade não surge por silêncio.
26. Delegação não transfere titularidade.
27. Conteúdo sensível deverá ser minimizado.
28. Notificações deverão ser discretas.
29. Compartilhamento exige finalidade.
30. Revogação interrompe novos usos.
31. Histórico deverá permanecer compreensível.
32. Conflitos não deverão ser sobrescritos.
33. Falhas não deverão gerar sucesso falso.
34. Oportunidade não deverá ocupar o lugar do movimento.
35. Patrocínio não deverá alterar prioridade.
36. Vulnerabilidade não deverá ser explorada.
37. A interface deverá apoiar ação no mundo real.
38. O participante permanece no controle.

# 1796. Continuidade normativa

`PAS-001-PP-VIEW-001 1.0.0` deverá ser registrado como a **terceira extensão normativa da Capacidade 05 — Próximos Passos**.

Ele deverá:

- consolidar a visualização e o controle funcional da capacidade;
- preservar a autoridade de `PAS-001-PP-FOUNDATION-001 1.0.0`;
- preservar a autoridade de `PAS-001-PP-LIFECYCLE-001 1.0.0`;
- manter a Capacidade 05 no estado `In progress`;
- elevar o progresso editorial de referência para `60%`;
- preservar as Capacidades 02, 03 e 04 como `Functionally complete`;
- manter prioridade, prontidão, execução, resultado e progresso como dimensões distintas.

Com isso, ficam definidos os **comportamentos funcionais da visualização e do controle dos Próximos Passos**, incluindo visão geral, portfólio, cartões, propostas, alternativas, prioridade, agenda, dependências, bloqueios, execução, resultados, recorrência, passos compartilhados, privacidade, acessibilidade, explicabilidade, histórico e ações do participante.

O próximo bloco deverá consolidar:

> **os contratos dos eventos funcionais da Capacidade de Próximos Passos, incluindo comandos, propostas, fatos reconhecidos, criação, confirmação, ativação, prontidão, prioridade, dependências, bloqueios, execução, resultados, conclusão, cancelamento, substituição, expiração, contestação, correção, recorrência, compartilhamento, propagação, idempotência, ordenação, versionamento, auditoria e falha segura.**