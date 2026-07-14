---
id: PAS-001-PP-INTEGRATION-001
title: Integrações Funcionais da Capacidade de Próximos Passos
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
  - PAS-001-PP-VIEW-001
  - PAS-001-PP-EVENT-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-PP-INTEGRATION-001 — Integrações Funcionais da Capacidade de Próximos Passos

## 1. Autoridade e vínculo

Este documento é a **quinta extensão normativa da Capacidade 05 — Próximos Passos** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 1448 a 1530, 1531 a 1672, 1673 a 1796 e 1797 a 1909, consolidadas respectivamente por `PAS-001-PP-FOUNDATION-001 1.0.0`, `PAS-001-PP-LIFECYCLE-001 1.0.0`, `PAS-001-PP-VIEW-001 1.0.0` e `PAS-001-PP-EVENT-001 1.0.0`, além da autoridade do `PAS-001 0.5.0` e das extensões concluídas de Contexto Vivo, Objetivos e Eventos de Vida.

Esta extensão mantém a Capacidade 05 no estado `In progress` e eleva seu progresso editorial de referência de `80%` para `90%`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade da especificação-base ou das capacidades concluídas.

# 1910. Integrações funcionais dos Próximos Passos

As integrações deverão permitir que a capacidade receba, produza e compartilhe informações necessárias à compreensão e à execução de movimentos, sem transferir titularidade ou decisão para sistemas externos.

O fluxo geral será:

```text
fonte ou capacidade produtora
→ validação de identidade e autoridade
→ validação de finalidade
→ minimização
→ transformação controlada
→ admissão como sinal, proposta, comando ou fato
→ decisão da Capacidade de Próximos Passos
→ evento funcional
→ produção de recorte
→ processamento pelo consumidor autorizado
```

# 1911. Objetivos

As integrações deverão:

1. preservar a singularidade da capacidade;
2. manter a autoridade limitada da fonte;
3. impedir decisões automáticas indevidas;
4. aplicar finalidade explícita;
5. minimizar dados;
6. preservar proveniência;
7. distinguir fatos, interpretações e recomendações;
8. suportar sincronização segura;
9. permitir pausa e revogação;
10. operar com degradação controlada;
11. evitar ciclos e duplicidades;
12. preservar explicabilidade;
13. proteger informações sensíveis;
14. manter o participante no controle.

# 1912. Princípios obrigatórios

- titularidade preservada;
- autoridade limitada;
- finalidade antes do acesso;
- minimização antes do compartilhamento;
- confirmação proporcional ao impacto;
- independência funcional das capacidades;
- proveniência reconstruível;
- temporalidade explícita;
- revogabilidade;
- neutralidade comercial;
- falha segura;
- não vigilância;
- não fabricação de precisão;
- não transferência silenciosa de responsabilidade.

# 1913. Integração não representa decisão

A integração poderá:

- fornecer informação;
- apresentar evidência;
- sugerir um Próximo Passo;
- informar dependência;
- confirmar um fato dentro da autoridade da fonte;
- solicitar reavaliação;
- executar operação previamente autorizada.

Ela não poderá, isoladamente:

- criar compromisso pessoal;
- definir prioridade pessoal;
- atribuir responsabilidade;
- confirmar execução humana;
- concluir um Próximo Passo;
- concluir um objetivo;
- criar Evento de Vida;
- compartilhar conteúdo sensível;
- substituir decisão do participante.

# 1914. Tipos de integração

- interna entre capacidades;
- interna entre camadas;
- especializada entre produtos;
- organizacional;
- profissional;
- pessoal;
- temporária;
- externa automatizada;
- externa assistida;
- baseada em importação;
- baseada em eventos;
- baseada em consulta;
- baseada em sincronização;
- baseada em autorização pontual.

# 1915. Modos funcionais

- leitura;
- escrita;
- proposição;
- confirmação;
- execução;
- sincronização;
- notificação;
- consulta;
- exportação;
- compartilhamento;
- revogação;
- auditoria.

Cada modo deverá possuir permissões próprias.

# 1916. Contrato comum

Toda integração deverá identificar:

- `integration_id`;
- produtor;
- consumidor;
- participante;
- categoria do participante;
- finalidade;
- escopo;
- campos autorizados;
- autoridade;
- origem;
- proveniência;
- temporalidade;
- qualidade;
- confiança;
- sensibilidade;
- transformação aplicada;
- frequência;
- prazo de validade;
- possibilidade de pausa;
- possibilidade de revogação;
- retenção;
- estado de sincronização;
- último processamento;
- falhas pendentes.

# 1917. Admissão

Uma informação somente deverá ser admitida quando:

- houver participante identificável;
- a associação for suficientemente confiável;
- a finalidade for legítima;
- a fonte possuir autoridade compatível;
- o conteúdo for necessário;
- a temporalidade for compreensível;
- a sensibilidade estiver classificada;
- a integração estiver autorizada;
- o significado não tiver sido ampliado;
- houver tratamento seguro para falhas.

# 1918. Identidade e associação

Disponibilidade técnica de um identificador não deverá ser suficiente para associar um dado à jornada.

Associações incertas deverão permanecer:

- pendentes;
- contestáveis;
- limitadas;
- sem efeitos críticos;
- sem propagação ampla.

# 1919. Autoridade da fonte

A autoridade deverá ser limitada ao fato que a fonte pode legitimamente confirmar.

Exemplos:

- calendário confirma compromisso registrado, não intenção humana;
- banco confirma transação, não significado pessoal;
- plataforma esportiva confirma atividade registrada, não evolução;
- organização confirma obrigação institucional, não prioridade pessoal;
- marketplace confirma compra, não execução do Próximo Passo;
- profissional confirma atendimento dentro do escopo autorizado, não toda a jornada.

# 1920. Proveniência

Deverão ser preservados:

- sistema original;
- registro original;
- ator original;
- momento de origem;
- transformações;
- correções;
- versão;
- autoridade;
- limitações;
- cadeia de processamento.

# 1921. Qualidade e confiança

Qualidade técnica, confiança funcional e autoridade deverão permanecer separadas.

Um dado poderá ser:

- tecnicamente íntegro;
- associado corretamente;
- recente;
- mas insuficiente para confirmar execução ou conclusão.

# 1922. Temporalidade

A integração deverá distinguir:

- tempo do fato;
- tempo do registro externo;
- tempo da sincronização;
- tempo do conhecimento;
- tempo do processamento;
- tempo da aplicação;
- tempo da correção.

# 1923. Transformações permitidas

Poderão ocorrer:

- normalização;
- conversão de unidade;
- classificação funcional;
- agregação autorizada;
- extração de recorte;
- pseudonimização;
- anonimização;
- tradução;
- enriquecimento com fonte identificada;
- cálculo explicável.

# 1924. Transformações proibidas

Não poderão ser fabricados:

- prazo;
- prioridade;
- intenção;
- responsabilidade;
- compromisso;
- significado emocional;
- causalidade;
- diagnóstico;
- evolução;
- conclusão;
- precisão inexistente.

# 1925. Sincronização

A sincronização deverá controlar:

- versão;
- idempotência;
- duplicidade;
- ordenação;
- estado pendente;
- conflito;
- reconciliação;
- latência;
- atualização parcial;
- fonte indisponível;
- reprocessamento.

# 1926. Prevenção de ciclos

Deverão ser impedidos ciclos como:

```text
Próximos Passos sugere oportunidade
→ oportunidade retorna como novo passo
→ novo passo gera nova oportunidade equivalente
→ processo se repete
```

Toda reentrada deverá possuir correlação, finalidade e limite.

# 1927. Minimização

O consumidor deverá receber somente o necessário.

Exemplo:

```text
necessidade de serviço jurídico
```

não deverá exigir o compartilhamento integral de:

- histórico pessoal;
- objetivos;
- Eventos de Vida;
- informações familiares;
- situação financeira;
- outros passos ativos.

# 1928. Finalidade e permissões

Permissões deverão ser específicas por:

- finalidade;
- consumidor;
- campo;
- período;
- modo de uso;
- possibilidade de redistribuição;
- sensibilidade;
- retenção.

# 1929. Pausa e revogação

O participante deverá poder:

- pausar coleta;
- pausar sincronização;
- limitar campos;
- limitar finalidade;
- revogar consumidor;
- desconectar fonte;
- impedir novos usos;
- solicitar recomposição de recortes.

# 1930. Revogação e fatos históricos

A revogação deverá interromper novos acessos e usos autorizáveis.

Ela não deverá apagar automaticamente:

- fato legítimo já ocorrido;
- operação concluída;
- obrigação legal;
- auditoria mínima;
- evento funcional historicamente reconhecido.

# 1931. Falha e degradação controlada

Em falha, o sistema deverá:

- preservar o último estado válido;
- marcar sincronização pendente;
- reduzir automações;
- evitar falsa confirmação;
- evitar falsa conclusão;
- limitar propagação;
- permitir recuperação;
- informar o participante quando necessário.

## Integrações internas do Journey

# 1932. Captura de Contexto

Poderá fornecer:

- declaração;
- solicitação;
- necessidade;
- restrição;
- preferência;
- disponibilidade;
- intenção;
- contestação.

Não deverá converter intenção diretamente em passo confirmado.

# 1933. Contexto Vivo

Poderá fornecer recortes sobre:

- estado atual;
- capacidades;
- restrições;
- preferências;
- relacionamentos;
- disponibilidade;
- condições relevantes.

Próximos Passos deverá governar individualmente a decisão sobre movimentos.

# 1934. Objetivos

Objetivos poderá informar:

- direção;
- prioridade estratégica;
- critérios;
- conflitos;
- progresso;
- estado;
- revisão necessária.

A conclusão de um Próximo Passo não deverá concluir automaticamente o objetivo.

# 1935. Eventos de Vida

Eventos de Vida poderá solicitar reavaliação de:

- atualidade;
- prioridade;
- prontidão;
- dependências;
- riscos;
- responsabilidade;
- agenda;
- adequação.

A mudança não deverá cancelar ou alterar todos os passos indiscriminadamente.

# 1936. Oportunidades Ativas

Próximos Passos poderá solicitar meios compatíveis.

Oportunidades Ativas poderá devolver:

- alternativas;
- disponibilidade;
- requisitos;
- custos;
- localização;
- elegibilidade;
- vínculos comerciais.

A oportunidade não deverá criar compromisso nem determinar prioridade.

# 1937. Intervenções Contextuais

Próximos Passos poderá informar:

- decisão pendente;
- bloqueio;
- prazo real;
- dependência;
- risco;
- revisão necessária;
- sincronização pendente.

Intervenções Contextuais deverá decidir entre:

- agir;
- perguntar;
- lembrar;
- observar;
- esperar;
- silenciar.

# 1938. Experiências

Um Próximo Passo poderá originar uma experiência.

Participação, presença ou consumo não deverão confirmar automaticamente:

- resultado;
- progresso;
- transformação;
- Evento de Vida;
- conclusão de objetivo.

# 1939. Evolução Contínua

Poderá receber:

- resultados;
- evidências;
- mudanças de capacidade;
- adaptações;
- aprendizados;
- transições.

Quantidade de passos concluídos não deverá medir evolução humana.

## Camadas e produtos

# 1940. Guivos Intelligence

Poderá:

- identificar possibilidades;
- sugerir formulações;
- comparar alternativas;
- detectar dependências;
- identificar bloqueios;
- apoiar prioridade;
- estimar esforço;
- resumir estado;
- explicar recomendações.

Não poderá:

- confirmar decisão pessoal;
- atribuir responsabilidade;
- ativar compromisso;
- concluir execução;
- impor prioridade;
- utilizar vulnerabilidade comercialmente.

# 1941. Platform Layer

Deverá sustentar:

- identidade;
- autenticação;
- autorização;
- eventos;
- APIs;
- filas;
- grafo;
- armazenamento;
- busca;
- notificações;
- auditoria;
- retenção;
- criptografia;
- observabilidade;
- idempotência;
- reconstrução.

Não deverá redefinir a semântica funcional.

# 1942. Guivos Business

Poderá integrar:

- responsabilidades institucionais;
- processos;
- aprovações;
- compromissos organizacionais;
- capacitações;
- resultados operacionais.

A Organização não deverá receber a jornada pessoal integral do participante.

# 1943. Guivos Mall

Compra, pagamento, entrega ou contratação poderão representar fatos comerciais.

Não deverão confirmar automaticamente:

- intenção pessoal;
- execução do passo;
- resultado esperado;
- progresso;
- conclusão.

# 1944. Guivos Travel

Reservas, deslocamentos e experiências poderão apoiar passos relacionados a viagens.

Reserva não representa viagem realizada e viagem realizada não representa transformação humana.

# 1945. Guivos Media

Conteúdo poderá apoiar compreensão, preparação ou aprendizado.

Visualização, leitura ou conclusão de conteúdo não deverão equivaler automaticamente a execução ou progresso.

# 1946. Guivos Ads

Guivos Ads não deverá:

- acessar passos sensíveis;
- utilizar vulnerabilidades;
- alterar prioridade;
- inserir publicidade como recomendação funcional neutra;
- transformar patrocínio em relevância;
- inferir intenção comercial a partir de passos protegidos.

## Fontes e serviços externos

# 1947. Serviços profissionais

Profissionais poderão:

- propor;
- orientar;
- confirmar atendimento;
- registrar resultado dentro do escopo;
- informar dependência;
- solicitar revisão.

Eles não deverão controlar toda a jornada do participante.

# 1948. Educação

Matrícula, presença, avaliação ou certificação poderão produzir fatos educacionais.

Nenhum deles deverá confirmar automaticamente aprendizado, capacidade ou evolução.

# 1949. Saúde

Integrações de saúde exigirão proteção reforçada, finalidade específica, autoridade profissional e minimização.

Não poderão produzir diagnóstico ou orientação clínica pela Capacidade de Próximos Passos.

# 1950. Serviços financeiros

Poderão informar:

- pagamento;
- saldo autorizado;
- obrigação;
- orçamento;
- vencimento;
- transação.

Não deverão inferir intenção, prioridade pessoal ou condição emocional.

# 1951. Calendários

Calendários poderão informar:

- compromissos;
- janelas;
- indisponibilidades;
- recorrências;
- conflitos.

Evento no calendário não deverá representar execução.

# 1952. Localização

Localização somente deverá ser utilizada com:

- finalidade explícita;
- precisão necessária;
- período limitado;
- controle do participante.

Presença em local não confirma ação ou resultado.

# 1953. Esportes e atividades

Atividades registradas poderão informar execução objetiva quando o contrato do passo permitir.

Não deverão confirmar:

- saúde;
- aderência;
- hábito;
- identidade;
- disciplina;
- evolução humana.

# 1954. Organizações sociais e voluntariado

Poderão confirmar:

- inscrição;
- participação;
- horas;
- função;
- atividade realizada.

Pontos, recompensas ou reconhecimento não deverão substituir o significado da ação social.

# 1955. Comunidades religiosas

Integrações deverão preservar liberdade religiosa, privacidade espiritual e ausência de julgamento.

Participação não deverá medir fé, proximidade com Deus ou valor moral.

# 1956. Serviços jurídicos

Poderão confirmar processos, documentos, prazos e atendimentos dentro do escopo autorizado.

Não deverão expor conteúdo jurídico sensível para capacidades ou produtos sem necessidade.

# 1957. Fontes públicas

Informação pública não representa autorização irrestrita de uso.

Deverão ser avaliados:

- identidade;
- legitimidade;
- finalidade;
- atualidade;
- sensibilidade;
- impacto;
- necessidade.

## Operação, controle e governança

# 1958. Integrações temporárias

Deverão possuir:

- finalidade delimitada;
- início;
- expiração;
- escopo;
- consumidor;
- retenção;
- encerramento automático;
- possibilidade de revogação antecipada.

# 1959. Integrações pessoais

O participante poderá conectar fontes próprias, mantendo controle sobre:

- campos;
- finalidade;
- frequência;
- período;
- consumidores;
- notificações;
- desconexão.

# 1960. Informações de terceiros

Deverão ser minimizadas, protegidas e removidas quando deixarem de ser necessárias.

Não deverão formar perfis independentes de terceiros.

# 1961. Passos compartilhados

A integração deverá preservar:

- estado global;
- estado individual;
- responsabilidade individual;
- confirmação individual;
- permissões;
- possibilidade de saída;
- contestação.

# 1962. Conflitos entre fontes

A divergência deverá gerar:

- conflito explícito;
- comparação de autoridade;
- análise temporal;
- manutenção das versões;
- limitação de efeitos;
- eventual solicitação ao participante.

Não haverá hierarquia universal de fontes.

# 1963. Eventos retroativos

Informações recebidas posteriormente deverão preservar:

- momento real do fato;
- momento do registro;
- momento do conhecimento;
- momento da aplicação;
- limitações da reconstrução.

# 1964. Canais conversacionais

Conversas poderão iniciar integrações, autorizações e comandos.

Linguagem ambígua deverá exigir esclarecimento proporcional ao impacto.

# 1965. Notificações

Notificações deverão ser:

- necessárias;
- discretas;
- minimizadas;
- controláveis;
- compatíveis com sensibilidade;
- sem linguagem de culpa;
- sem urgência fabricada.

# 1966. Busca

Busca e indexação deverão respeitar:

- finalidade;
- sensibilidade;
- titularidade;
- permissões;
- títulos neutros;
- exclusão de conteúdo protegido.

# 1967. Saídas permitidas

As integrações poderão produzir:

- sinais;
- propostas;
- evidências;
- confirmações autorizadas;
- dependências;
- bloqueios;
- resultados objetivos;
- solicitações de revisão;
- recortes;
- notificações;
- eventos de falha;
- confirmações de processamento.

# 1968. Ações proibidas

Nenhuma integração deverá:

- criar passo pessoal confirmado por inferência;
- atribuir responsabilidade por silêncio;
- definir prioridade por receita;
- confirmar execução por localização;
- confirmar conclusão por compra;
- concluir objetivo por atividade;
- criar Evento de Vida automaticamente;
- utilizar passo sensível para publicidade;
- compartilhar jornada integral;
- fabricar precisão;
- ocultar fonte;
- ignorar revogação;
- apresentar falha parcial como sucesso.

# 1969. Eventos funcionais das integrações

Deverão ser previstos, entre outros:

- `IntegracaoDeProximosPassosAutorizada`;
- `IntegracaoDeProximosPassosPausada`;
- `IntegracaoDeProximosPassosRetomada`;
- `IntegracaoDeProximosPassosRevogada`;
- `RecorteDeProximoPassoRecebido`;
- `RecorteDeProximoPassoRejeitado`;
- `RecorteDeProximoPassoPropagado`;
- `ConflitoDeIntegracaoDeProximoPassoIdentificado`;
- `SincronizacaoDeProximoPassoPendente`;
- `SincronizacaoDeProximoPassoConcluida`;
- `ProcessamentoDeIntegracaoDeProximoPassoFalhou`;
- `ReconciliacaoDeIntegracaoDeProximoPassoConcluida`.

# 1970. Métricas funcionais

As métricas poderão avaliar:

- integrações ativas;
- integrações temporárias;
- autorizações;
- revogações;
- revogações pendentes;
- falhas;
- duplicidades;
- conflitos;
- latência;
- recortes excessivos;
- finalidade incompatível;
- usos após revogação;
- associações incorretas;
- eventos fora de ordem;
- sincronizações divergentes;
- recuperações;
- exposições sensíveis.

As métricas deverão avaliar o sistema, não o participante.

# 1971. Explicabilidade

O participante deverá compreender:

- quais fontes estão conectadas;
- quais dados são acessados;
- por qual finalidade;
- quais transformações ocorrem;
- quais decisões permanecem com a Guivos;
- quais consumidores recebem recortes;
- como pausar;
- como revogar;
- o que ocorre em falhas.

# 1972. Auditoria

A auditoria deverá reconstruir:

```text
autorização
→ fonte
→ coleta
→ validação
→ transformação
→ admissão
→ decisão funcional
→ evento
→ recorte
→ consumidor
→ processamento
→ correção, falha ou revogação
```

# 1973. Critérios de aceite

A extensão será considerada consolidada quando:

1. definir contrato comum;
2. preservar titularidade;
3. limitar autoridade das fontes;
4. aplicar finalidade e minimização;
5. distinguir fato, interpretação e proposta;
6. preservar proveniência;
7. controlar temporalidade;
8. impedir fabricação de significado;
9. governar sincronização;
10. prevenir ciclos;
11. governar pausa e revogação;
12. preservar fatos históricos legítimos;
13. tratar falhas com degradação controlada;
14. integrar todas as capacidades do Journey;
15. integrar Intelligence e Platform Layer;
16. governar produtos especializados;
17. governar organizações e serviços externos;
18. proteger informações de terceiros;
19. preservar neutralidade comercial;
20. manter o participante no controle.

# 1974. Regras fundamentais

1. Integração não representa decisão.
2. Disponibilidade técnica não representa autorização.
3. Fonte somente confirma fatos dentro de sua autoridade.
4. Finalidade precede acesso.
5. Minimização precede compartilhamento.
6. Titularidade não é transferida.
7. Consumidor governa sua própria decisão.
8. Informação externa não cria compromisso pessoal.
9. Calendário não confirma execução.
10. Compra não confirma conclusão.
11. Localização não confirma ação.
12. Atividade não confirma progresso.
13. Participação não confirma transformação.
14. Organização não recebe a jornada pessoal integral.
15. Receita não altera prioridade.
16. Patrocínio não altera recomendação funcional.
17. Conteúdo sensível não alimenta publicidade.
18. Transformações não fabricam precisão ou causalidade.
19. Sincronização não pode duplicar efeitos.
20. Mensagens fora de ordem não podem criar estados impossíveis.
21. Revogação interrompe novos usos.
22. Revogação exige propagação efetiva.
23. Falha reduz automação.
24. Falha parcial não representa sucesso integral.
25. Ausência de dado não representa ausência de necessidade.
26. Informação pública não representa uso irrestrito.
27. Integrações temporárias devem expirar.
28. Terceiros não devem formar perfis independentes.
29. Métricas avaliam o sistema.
30. O participante permanece no controle.

# 1975. Continuidade normativa

`PAS-001-PP-INTEGRATION-001 1.0.0` deverá ser registrado como a **quinta extensão normativa da Capacidade 05 — Próximos Passos**.

A extensão deverá:

- preservar as quatro extensões anteriores;
- manter a capacidade `In progress`;
- elevar o progresso editorial para `90%`;
- preservar as Capacidades 02, 03 e 04 como `Functionally complete`;
- consolidar os limites de todas as integrações internas e externas;
- definir o contrato final como próxima etapa.

Com isso, ficam definidas as **integrações funcionais da Capacidade de Próximos Passos**, incluindo contratos comuns, finalidade, minimização, identidade, autoridade, proveniência, temporalidade, sincronização, revogação, integrações internas do Journey, camadas, produtos, serviços, fontes externas, falha segura, explicabilidade e auditoria.

O bloco seguinte será:

> **KPIs, guardrails, baseline, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão e contrato final da Capacidade de Próximos Passos.**