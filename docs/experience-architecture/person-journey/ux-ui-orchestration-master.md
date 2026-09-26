---
id: GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001
title: Jornada da Pessoa — Documento Mestre de Orquestração UX/UI
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: true
maturity: ux_orchestration_authority
depends_on:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-JOURNEY-PERSON-FUNCTIONAL-COMPLETENESS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-PLANS-PERSON-001
related:
  - GKR-UX-PER008-MASTER-001
  - GKR-UX-PER201-MASTER-001
  - GKR-UX-PER202-MASTER-001
  - GKR-UX-PER203-MASTER-001
  - GKR-UX-PER301-MASTER-001
---

# Jornada da Pessoa — Documento Mestre de Orquestração UX/UI

## 1. Finalidade

Este documento governa a **conexão e o comportamento ponta a ponta da Jornada da Pessoa** para orientar designer humana, IA de apoio, Produto, UX, prototipação e futura implementação.

Os Documentos Mestres por superfície definem responsabilidades locais. Este documento define **como essas responsabilidades devem funcionar em conjunto**: o que a Pessoa encontra em cada momento, como o sistema responde às suas ações, como contexto e estado atravessam a Journey, como o plano vigente afeta capacidades e como possibilidades de upgrade podem ser apresentadas sem distorcer a experiência.

Ele não substitui os Masters, o Surface Registry, o Transition Registry ou a autoridade comercial de Planos. Em conflito, prevalece a autoridade específica aplicável.

```text
MASTER DE SUPERFÍCIE
→ governa responsabilidade local

ESTE DOCUMENTO
→ governa orquestração entre responsabilidades
→ continuidade
→ comportamento
→ plano e entitlement visível
→ descoberta progressiva
→ comunicação de upgrade
→ estados transversais

PROTÓTIPO UX/UI
→ materializa essas regras
→ não cria regra nova
```

## 2. Princípio de experiência

A Jornada deve parecer **um sistema contínuo**, não uma coleção de telas independentes.

A Pessoa deve perceber, ao longo do uso:

1. onde está;
2. o que o sistema compreendeu;
3. o que está disponível agora;
4. o que depende de uma ação sua;
5. o que depende de autorização;
6. o que pertence ao seu plano;
7. o que existe em outro plano;
8. o que mudou após sua ação;
9. como voltar, revisar, corrigir, interromper ou continuar.

A experiência deve preservar contexto legítimo entre superfícies sem transformar navegação em consentimento, decisão, contratação ou confirmação.

## 3. Modelo mental do sistema

O comportamento deve seguir o ciclo:

```text
CONTEXTO VIGENTE
→ ESTADO REAL
→ POSSIBILIDADES LEGÍTIMAS
→ ESCOLHA DA PESSOA
→ PROCESSAMENTO VISÍVEL QUANDO NECESSÁRIO
→ RESULTADO CONFIRMADO
→ CONTINUIDADE COERENTE
```

Nunca:

```text
EXIBIÇÃO
≠ ACEITE

CLIQUE
≠ AUTORIZAÇÃO AMPLA

NAVEGAÇÃO
≠ CONSENTIMENTO

INTENÇÃO
≠ PROCESSAMENTO

PROCESSAMENTO
≠ SUCESSO

PLANO COMERCIAL
≠ ENTITLEMENT IMPLEMENTADO

UPGRADE DISPONÍVEL
≠ PRESSÃO PARA UPGRADE
```

## 4. Espinha dorsal da primeira experiência

A entrada principal deve respeitar a sequência governada:

```text
PER-001 — HOME PÚBLICA
→ PER-002 — ENTRADA PROTEGIDA
→ PER-003 — ESCOLHA DE MODALIDADE
→ expressão por Texto/Voz, Arquivo ou Perguntas Opcionais
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
→ PER-006 — PROCESSAMENTO VISÍVEL
→ PER-007 — COMPREENSÃO INICIAL REVISÁVEL
→ PER-008 — HOJE
```

A primeira experiência deve priorizar compreensão e confiança. Plano pago não deve interromper artificialmente a construção inicial da Journey.

### 4.1 Antes de existir contexto suficiente

O sistema não deve antecipar:

- oportunidade personalizada;
- urgência;
- objetivo;
- Próximo Passo;
- evolução;
- recomendação de plano baseada em inferência não confirmada;
- promessa de resultado.

### 4.2 Quando o plano pode aparecer

O plano pode ser visível de forma contextual antes de PER-301 quando houver razão funcional clara, por exemplo:

- identificação discreta do plano vigente;
- capacidade indisponível naquele plano;
- cota legítima atingida;
- comparação de uma capacidade que a Pessoa tentou usar;
- acesso voluntário a Planos por Conta/Configurações.

O plano **não deve dominar** a entrada protegida, a autorização de dados, o processamento inicial ou a revisão da compreensão.

A superfície especializada para compreender e comparar planos continua sendo `PER-301`.

## 5. Hoje como centro de continuidade

`PER-008 — Hoje` deve funcionar como síntese dinâmica do estado vigente, não como feed infinito ou catálogo.

Pode reunir, quando houver base real:

- contexto atual;
- atenção material;
- Próximo Passo existente;
- oportunidade legitimamente aplicável;
- atividade próxima;
- atualização pertinente;
- portas para Objetivos, Próximos Passos e Evolução.

A quantidade de conteúdo deve responder ao estado real. Ausência é válida.

O plano pode afetar **profundidade e capacidade**, mas não deve transformar Hoje em vitrine permanente de upsell.

## 6. Oportunidades — arquitetura de acesso

O sistema deve distinguir pelo menos três naturezas de acesso:

### 6.1 Catálogo e descoberta pública

Free, Plus e Pro preservam acesso ao catálogo público compatível com Explorar, Mapa, Lista, busca manual e informações públicas essenciais.

```text
PLANO FREE
≠ CATÁLOGO ARTIFICIALMENTE REDUZIDO

UPGRADE
≠ DESBLOQUEAR O QUE JÁ É INFORMAÇÃO PÚBLICA ESSENCIAL
```

Uma oportunidade pública não deve ser ocultada apenas para fabricar valor de upgrade.

### 6.2 Correspondência personalizada

A correspondência personalizada utiliza contexto autorizado para demonstrar relação entre a Pessoa e uma oportunidade.

Baseline comercial corrente:

- Free: 2 correspondências personalizadas completas por semana;
- Plus: correspondências personalizadas ampliadas, sujeitas a uso justo;
- Pro: correspondências ampliadas com maior profundidade analítica.

A cota Free é consumida somente conforme a autoridade comercial vigente: quando a Pessoa abre a correspondência completa.

### 6.3 Profundidade analítica

Plus e Pro podem ampliar explicação e análise somente nos limites funcionalmente contratados.

Onde entitlement, profundidade, uso justo ou capacidade técnica ainda não estiverem contratados de modo executável, o protótipo deve representar a diferença como **capacidade comercial declarada**, sem inventar número, algoritmo, limite ou comportamento técnico.

## 7. Regra mestre para oportunidades ofuscadas

O ofuscamento é permitido somente para comunicar uma **camada premium real** que a Pessoa ainda não possui ou cuja cota legítima foi atingida.

Não é permitido usar ofuscamento para esconder:

- existência de oportunidade pública que já deveria estar acessível;
- título ou informação pública essencial apenas para pressionar pagamento;
- condição material necessária para decisão segura;
- patrocínio ou relação comercial;
- informação de segurança, direito ou obrigação;
- dado que a própria Pessoa forneceu;
- estado de processo já iniciado.

### 7.1 Como uma correspondência ofuscada deve se comportar

Quando houver base legítima para indicar que existe uma correspondência personalizada além da capacidade vigente, a UI pode apresentar uma prévia limitada que:

1. deixa claro que existe conteúdo adicional;
2. identifica que o limite decorre do plano/cota, não de erro;
3. preserva somente contexto suficiente para compreensão;
4. não revela análise premium por transparência visual acidental;
5. oferece comparação contextual com o plano que habilita maior capacidade;
6. mantém alternativa gratuita de explorar a oportunidade pelo catálogo público, quando ela for pública;
7. não cria urgência, medo de perda ou falsa escassez.

O efeito visual pode usar blur, máscara, redução de detalhe, skeleton estático ou outra solução de Design. O significado deve ser sempre comunicável também por texto e tecnologia assistiva.

```text
OFUSCADO
→ CAPACIDADE PREMIUM NÃO DISPONÍVEL NO ESTADO VIGENTE
→ MOTIVO EXPLICÁVEL
→ CAMINHO DE UPGRADE OPCIONAL
→ ALTERNATIVA FREE PRESERVADA QUANDO A INFORMAÇÃO É PÚBLICA
```

### 7.2 O que não pode ser inferido

O protótipo não pode inventar:

- quantidade de previews ofuscados;
- frequência de exposição;
- percentual de blur;
- regra de ordenação premium;
- ranking de oportunidades;
- probabilidade de sucesso;
- score humano;
- “melhor oportunidade” universal;
- limite Plus/Pro não governado.

## 8. Plano vigente e consciência de upgrade

A Pessoa deve conseguir perceber seu plano atual quando isso for útil, sem precisar memorizar a taxonomia.

A comunicação pode seguir três níveis:

1. **silencioso/contextual** — badge, rótulo ou informação de estado quando não interfere na tarefa;
2. **explicativo** — ao tentar capacidade não incluída ou atingir limite legítimo;
3. **comparativo** — em PER-301, com Free, Plus e Pro e suas diferenças.

A interface deve demonstrar que existem capacidades superiores sem declarar que a Pessoa “precisa” delas.

## 9. Upgrade contextual

Um convite de upgrade é legítimo quando nasce de uma ação ou necessidade observável no contexto atual, por exemplo:

- cota Free de correspondência personalizada atingida;
- tentativa de usar capacidade comercialmente definida como Plus/Pro;
- consulta voluntária a Planos;
- necessidade de profundidade que a própria Pessoa pediu e que pertença a plano superior.

O convite deve explicar:

```text
VOCÊ ESTÁ EM
→ plano vigente

ESTA CAPACIDADE
→ não está disponível / atingiu limite vigente

COM PLUS OU PRO
→ diferença comercial aplicável

VOCÊ AINDA PODE
→ continuar com alternativas válidas do plano atual

SE QUISER ALTERAR
→ abrir PER-301
```

Não usar:

- contagem regressiva artificial;
- “você está perdendo”;
- bloqueio surpresa de capacidade Free;
- comparação depreciativa;
- plano pré-selecionado como decisão;
- upgrade automático;
- dark patterns;
- esconder saída/continuidade gratuita.

## 10. Comparação Free, Plus e Pro no fluxo

A comparação completa pertence a `PER-301`.

Fora de PER-301, mostrar apenas a diferença necessária ao contexto. Exemplo: se a Pessoa atingiu a cota de correspondência personalizada Free, a experiência pode explicar a ampliação no Plus sem despejar toda a tabela comercial.

Quando a Pessoa pedir comparação ou abrir Planos, PER-301 deve apresentar:

- plano vigente, quando conhecido;
- Free, Plus e Pro;
- preços correntes;
- capacidades correntes;
- limites relevantes;
- diferenças compreensíveis;
- opção de permanecer no plano atual;
- continuidade para contratação somente por ação afirmativa.

Nenhum plano deve ser rotulado como “melhor para você” sem autoridade específica. Pode-se explicar **o que muda** em cada opção.

## 11. Comportamento por plano

### Free

Deve parecer uma experiência real e completa em seu escopo, não uma demonstração quebrada.

Preserva:

- entrada e compreensão;
- jornada essencial;
- catálogo público;
- Explorar, Mapa e busca manual;
- 2 correspondências personalizadas completas por semana;
- histórico essencial;
- controles de dados e direitos;
- oportunidades conforme condições do publicador.

Quando atingir limite, a Pessoa continua navegando pelas capacidades Free.

### Plus

Deve comunicar expansão de conveniência, personalização e continuidade.

Pode representar comercialmente:

- correspondências ampliadas sujeitas a uso justo;
- explicação completa da relação;
- filtros avançados;
- alertas personalizados;
- histórico ampliado;
- planos salvos, lembretes e acompanhamento ampliado;
- exportação padrão;
- processamento/Intelligence ampliados;
- integrações limitadas autorizadas;
- suporte ampliado.

Onde o contrato funcional transversal ainda não existir, protótipo não deve simular operação como se estivesse implementada.

### Pro

Deve comunicar maior profundidade, não superioridade humana.

Pode representar comercialmente:

- análises aprofundadas e comparativas;
- organização autorizada entre áreas;
- maior capacidade de processamento/Intelligence;
- relatórios pessoais ampliados;
- exportações avançadas;
- integrações autorizadas ampliadas;
- suporte prioritário;
- acesso antecipado quando aplicável e aprovado.

Pro não autoriza fabricar precisão, certeza, diagnóstico, garantia ou recomendação absoluta.

## 12. Descoberta progressiva

A Journey deve revelar complexidade conforme ela se torna útil.

```text
PRIMEIRO
→ tarefa e contexto

DEPOIS
→ capacidade relacionada

SE HOUVER LIMITE REAL
→ explicar limite

SE HOUVER ALTERNATIVA
→ preservar alternativa

SE A PESSOA QUISER SABER MAIS
→ aprofundar comparação

SE DECIDIR MUDAR
→ revisão consciente
→ processamento
→ resultado confirmado
```

O sistema não deve apresentar todas as capacidades, planos e controles em todas as superfícies.

## 13. Persistência e continuidade de contexto

Ao atravessar superfícies, preservar somente contexto necessário e autorizado.

Retornos devem reconsultar estado canônico quando aplicável.

Exemplos:

- Mapa ↔ Lista preserva consulta territorial;
- Detalhe → retorno preserva contexto válido de descoberta;
- Hoje ↔ Objetivos/Próximos Passos/Evolução preserva continuidade sem efeitos silenciosos;
- Conta ↔ Planos preserva navegação sem selecionar plano;
- revisão de contratação preserva plano alvo sem afirmar contratação;
- falha financeira preserva estado anterior até confirmação real.

## 14. Ação, processamento e feedback

Toda ação material deve ter estados distinguíveis quando aplicável:

```text
DISPONÍVEL
→ AÇÃO DA PESSOA
→ PROCESSANDO
→ SUCESSO CONFIRMADO
   ou
→ FALHA RECUPERÁVEL
   ou
→ ESTADO INDETERMINADO
```

A interface não deve antecipar sucesso.

Repetição após incerteza deve evitar efeitos duplicados.

## 15. Estados vazios, indisponibilidade e recuperação

O sistema deve tratar legitimamente:

- ausência de histórico;
- ausência de objetivo;
- ausência de Próximo Passo;
- zero oportunidades na consulta;
- localização desativada;
- oportunidade encerrada;
- dado desatualizado;
- falha de processamento;
- capacidade indisponível;
- limite de plano atingido;
- conexão insuficiente.

Estado vazio não é espaço obrigatório para publicidade ou upsell.

Upgrade só aparece no vazio quando resolver uma limitação real do plano; nunca como substituto de conteúdo inexistente.

## 16. Salvar e comparar oportunidades

Salvar e Comparar permanecem controles de `PER-203`.

Salvar:

```text
NÃO SALVO
→ SALVAR
→ PROCESSAR
→ SALVO CONFIRMADO
→ CONSULTAR DEPOIS QUANDO LEGÍTIMO
→ REMOVER CONSCIENTEMENTE
```

Comparar:

```text
DETALHE
→ SELECIONAR COMPARAÇÃO
→ ADICIONAR OPORTUNIDADE COMPATÍVEL
→ COMPARAR DIMENSÕES COMPREENSÍVEIS
→ REMOVER / RETORNAR
```

Comparação não deve produzir vencedor universal nem ranking pessoal.

## 17. Coletivos no fluxo

A família de Coletivos deve preservar a sequência governada de exploração, perfil, revisão, solicitação, pendência, vínculo e participação.

Estados de vínculo devem permanecer distinguíveis de plano comercial.

```text
PLANO PESSOA
≠ VÍNCULO COM COLETIVO

SAIR DO COLETIVO
≠ SAIR DA GUIVOS
≠ CANCELAR PLANO
```

## 18. Conta, dados e direitos

PER-009 concentra responsabilidades administrativas transversais já governadas sem virar catálogo universal de configurações.

A experiência deve distinguir:

- correção de compreensão;
- correção de dado;
- exclusão de compreensão;
- exclusão de dado;
- exclusão/saída de conta;
- exportação;
- permissões;
- plano;
- vínculo com Coletivo.

Não fundir essas ações por conveniência visual.

## 19. Sistema dinâmico

“Dinâmico” significa responder a estado real, não mudar arbitrariamente.

A UI pode adaptar:

- presença ou ausência de módulos;
- profundidade de informação;
- chamadas contextuais;
- estado de oportunidade;
- capacidades do plano;
- continuidade após ações;
- conteúdo autorizado e vigente.

A adaptação deve ser explicável quando material e nunca transformar inferência em fato.

## 20. Prioridade de conteúdo

Quando múltiplos elementos disputarem atenção, priorizar:

1. segurança, direito ou obrigação material;
2. processo iniciado que exija ação;
3. prazo real;
4. estado solicitado pela Pessoa;
5. continuidade da tarefa atual;
6. oportunidade contextual legítima;
7. descoberta adicional;
8. comunicação comercial contextual.

Patrocínio ou possibilidade de upgrade não ultrapassam prioridade humana apenas por valor comercial.

## 21. Patrocínio, plano e relevância

Manter separadas três dimensões:

```text
RELEVÂNCIA PARA A PESSOA
≠ PATROCÍNIO
≠ ENTITLEMENT DO PLANO
```

Patrocínio deve ser identificado.

Plano determina acesso a capacidades governadas, não relevância humana automática.

Nenhum plano pago deve fazer oportunidade patrocinada parecer organicamente mais relevante.

## 22. Prototipação UX/UI — estados mínimos a demonstrar

Uma prototipação ponta a ponta deve conseguir demonstrar, sem afirmar implementação:

- primeira entrada;
- autenticação/reentrada;
- escolha de modalidade;
- Texto/Voz;
- Arquivo;
- Perguntas Opcionais;
- inventário e autorização;
- processamento;
- revisão da compreensão;
- primeira entrada em Hoje;
- Hoje recorrente;
- Objetivos;
- Próximos Passos;
- Evolução;
- descoberta por Mapa e Lista;
- Detalhe;
- Salvar;
- Comparar;
- saída externa consciente;
- fluxo de Coletivos;
- Conta/controles;
- Free em uso normal;
- Free próximo/ao atingir cota legítima;
- correspondência personalizada ofuscada legítima;
- continuidade Free após limite;
- upgrade contextual;
- comparação Free/Plus/Pro;
- revisão de contratação;
- resultado confirmado;
- falha/recuperação;
- downgrade/cancelamento;
- estados vazios e indisponíveis;
- retorno e persistência coerente de contexto.

Isso não exige um frame por item. Estados podem pertencer à mesma superfície.

## 23. Matriz de comportamento para prototipação

| Situação | Deve aparecer | Não deve acontecer |
|---|---|---|
| primeira entrada | orientação e contexto necessário | upsell dominante |
| Hoje sem histórico | estado legítimo e continuidades possíveis | histórico fabricado |
| oportunidade pública | informação pública essencial | bloqueio artificial por plano |
| correspondência Free disponível | relação personalizada dentro da cota | cobrança implícita |
| cota Free atingida | explicação do limite + alternativa Free + upgrade opcional | bloquear catálogo |
| capacidade premium | valor e diferença aplicável | pressão ou urgência falsa |
| conteúdo ofuscado | motivo do bloqueio e caminho opcional | esconder disclosure material |
| Plus/Pro | capacidades adicionais governadas | inventar entitlement técnico |
| falha | estado real + recuperação | declarar sucesso |
| downgrade/cancelamento | consequências e data quando governadas | retenção coerciva |

## 24. Liberdade de Design

Este documento governa comportamento, hierarquia semântica e continuidade, não estética.

Design pode decidir:

- arquitetura visual;
- composição;
- componentes;
- navegação visual;
- tipografia conforme autoridade de marca;
- cores;
- imagens;
- iconografia;
- densidade;
- motion;
- microinterações;
- forma visual do ofuscamento;
- responsividade;
- quantidade de frames;
- apresentação comparativa.

A liberdade visual não pode alterar responsabilidade, plano, preço, benefício, transição, autorização, estado ou significado governado.

## 25. Regras para IA

Uma IA que construa ou auxilie a prototipação deve consumir este documento junto dos Masters específicos necessários.

A IA não pode:

- inventar PER/TRN;
- criar benefício ou preço;
- remover benefício;
- inventar entitlement;
- inventar algoritmo;
- inventar oportunidade real;
- preencher dado ausente;
- criar ranking humano;
- declarar plano “melhor para você”;
- transformar upgrade em obrigação;
- ocultar alternativa Free legítima;
- promover candidato a implementado;
- interpretar protótipo como Product Engineering liberado.

Quando houver lacuna, deve sinalizá-la em vez de completá-la por conveniência.

## 26. Critérios executivos de aceite

Uma prototipação orientada por este documento é semanticamente aceitável quando:

1. parece uma Journey contínua;
2. respeita as responsabilidades e transições governadas;
3. preserva estado e contexto legítimos;
4. diferencia ação, processamento e resultado;
5. Free funciona de verdade em seu escopo;
6. catálogo público não é artificialmente bloqueado;
7. correspondências personalizadas respeitam a baseline comercial;
8. ofuscamento só representa capacidade premium legítima;
9. upgrade é contextual, opcional e explicável;
10. plano vigente é compreensível quando material;
11. Plus e Pro demonstram valor sem prometer resultado;
12. diferenças não contratadas tecnicamente não são inventadas;
13. estados vazios e falhas são tratados;
14. acessibilidade não depende de blur/cor/motion;
15. patrocínio, relevância e plano permanecem distintos;
16. direitos e privacidade permanecem preservados;
17. IA não assume autoridade;
18. Design mantém liberdade criativa;
19. protótipo não é confundido com implementação;
20. Product Engineering não é liberado por este documento.

## 27. Ordem recomendada de consumo para construção

Para construir uma prototipação integrada:

1. Leia Primeiro;
2. este Documento Mestre de Orquestração UX/UI;
3. Fluxo Completo de Superfícies;
4. Planos — Pessoa;
5. Surface Registry e detalhamento da Pessoa;
6. Transition Registry;
7. Master da superfície em construção;
8. autoridades específicas citadas pelo Master.

A prototipação deve validar continuidade entre superfícies, e não apenas fidelidade isolada de cada frame.

## 28. Estado

```text
PERSON JOURNEY UX/UI ORCHESTRATION
→ ACTIVE

ROLE
→ EXECUTIVE / MASTER ORIENTATION
→ END-TO-END BEHAVIOR
→ PROTOTYPING CONSUMPTION AUTHORITY

CURRENT PERSON RESPONSIBILITIES
→ 29

ORIGINAL MASTER COLLECTION
→ 26 / 26 COMPLETE

POST-AUDIT EXTENSIONS
→ PER-013 / PER-014

PLANS
→ FREE / PLUS / PRO
→ COMMERCIAL BASELINE PRESERVED

OPPORTUNITY BLUR / LOCK
→ ALLOWED ONLY FOR LEGITIMATE PREMIUM CAPABILITY
→ PUBLIC ESSENTIAL ACCESS PRESERVED

NEW PER / TRN IDS
→ NONE

VISUAL BASELINE
→ NONE

PROTOTYPE
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```
