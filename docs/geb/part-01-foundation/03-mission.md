---
id: GEB-P01-F03
title: Missão Operacional
status: approved-draft
version: 0.3.0
owner: Guivos
last_updated: 2026-08-27
dependencies:
  - 01-essence.md
  - 02-purpose.md
related_adrs:
  - ADR-002
related:
  - GKR-STATE-001
  - RP-002
---

# Missão Operacional

## 1. Missão

> **Ajudar cada participante a compreender seu Momento, reconhecer Próximos Passos e acessar condições, conexões, Possibilidades e experiências que possam contribuir para sua evolução.**

A missão traduz o propósito em critério de atuação diária sem transformar a Guivos em agente que decide, diagnostica de forma absoluta ou conduz obrigatoriamente uma pessoa a uma oferta.

## 2. Relação entre propósito e missão

```text
PROPÓSITO
→ por que a Guivos existe

MISSÃO OPERACIONAL
→ como a Guivos atua para servir ao propósito

PRODUTOS / TECNOLOGIAS / CANAIS
→ como capacidades específicas podem materializar partes dessa missão
```

A missão deve sobreviver à substituição de qualquer tecnologia, canal ou Produto Especializado.

## 3. Critério operacional principal

Toda funcionalidade, Produto Especializado, algoritmo, interface, campanha, parceria, processo, regra econômica ou nova tecnologia deve conseguir responder:

> **Esta decisão amplia uma condição legítima para que um participante compreenda seu Momento, reconheça um Próximo Passo, acesse uma Possibilidade ou viva uma experiência coerente com sua jornada?**

Uma resposta positiva precisa ser explicável. Não basta afirmar genericamente que algo “gera evolução”.

## 4. Modelo operacional da missão

```text
ENTENDER O CONTEXTO
↓
SEPARAR FATO / DECLARAÇÃO / INFERÊNCIA / INCERTEZA
↓
COMPREENDER O MOMENTO
↓
RECONHECER OBJETIVO / NECESSIDADE, quando houver
↓
APOIAR UM PRÓXIMO PASSO
↓
EXPLICAR POSSIBILIDADES, quando agregarem valor
↓
CONECTAR A MECANISMOS E OPORTUNIDADES REAIS, quando pertinente
↓
PRESERVAR ESCOLHA
↓
APOIAR EXPERIÊNCIA E CONTINUIDADE
↓
REGISTRAR APRENDIZADO / CONTRIBUIÇÃO SEM EXAGERAR CAUSALIDADE
```

A missão não exige que todas as etapas ocorram em toda interação.

## 5. Modos legítimos de contribuição

A Guivos pode cumprir a missão por diferentes formas de apoio:

| Modo | Exemplo | Cuidado |
|---|---|---|
| **Compreensão** | organizar um Momento confuso | não transformar inferência em fato |
| **Clareza** | mostrar opções e implicações | não decidir pelo participante |
| **Organização** | estruturar objetivo ou Próximo Passo | não converter tudo em produtividade |
| **Conexão** | aproximar participantes legítimos | não transferir autoridade |
| **Possibilidade** | apresentar caminhos potenciais | não tratar possibilidade como obrigação |
| **Oportunidade** | apresentar oferta concreta pertinente | pagamento não compra relevância |
| **Experiência** | apoiar continuidade antes/durante/depois | realização não prova impacto |
| **Aprendizado** | transformar evidências em compreensão | correlação não vira causalidade |
| **Proteção** | evidenciar risco, limite, contestação ou saída | segurança não pode ser escondida pela simplicidade |

## 6. Critérios de reavaliação

Uma decisão deve ser reavaliada quando:

- não existe participante ou necessidade claramente beneficiada;
- a justificativa depende apenas de receita, engajamento ou volume;
- a relevância não pode ser explicada pelo contexto;
- a recomendação reduz autonomia;
- uma inferência é apresentada como verdade;
- uma Possibilidade é convertida automaticamente em Oportunidade;
- uma Oportunidade comercial recebe prioridade por pagamento;
- uma experiência é tratada como prova automática de evolução;
- a tecnologia passa a determinar o conceito institucional;
- o desenho exige complexidade desnecessária do participante;
- o uso de dados excede finalidade ou autoridade.

## 7. Consequência arquitetural

A missão orienta diretamente:

- o modelo de Journey;
- o conceito de Momento;
- o conceito de Próximo Passo;
- a arquitetura de Possibilidades;
- o modelo de Oportunidades;
- a relação com Organizações e Coletivos;
- Guivos Intelligence;
- IA e modelos de inferência;
- desenho da experiência;
- governança de dados e privacidade;
- modelos econômicos;
- comunicação e GTM;
- governança do ecossistema.

Nenhum desses elementos adquire autoridade superior à missão por ser tecnicamente sofisticado ou comercialmente relevante.

## 8. Invariantes vigentes

| ID | Invariante |
|---|---|
| INV-F03-01 | A execução diária deve permanecer orientada à evolução e às condições que podem sustentá-la. |
| INV-F03-02 | Toda decisão relevante deve demonstrar contribuição legítima para compreensão, Próximo Passo, Possibilidade, experiência ou proteção. |
| INV-F03-03 | Decisões sem aderência à jornada devem ser reavaliadas. |
| INV-F03-04 | IA, algoritmos e experiência do usuário devem permanecer subordinados à missão. |
| INV-F03-05 | A governança do ecossistema deve operar segundo propósito, jornada e autoridade dos participantes. |
| INV-F03-06 | Oportunidade não é etapa obrigatória de todo Próximo Passo. |
| INV-F03-07 | Simplicidade para o participante não pode eliminar controles, evidência ou rastreabilidade necessários nos bastidores. |

## 9. Responsabilidades institucionais

| ID | Responsabilidade |
|---|---|
| RESP-F03-01 | Traduzir o propósito em critérios verificáveis de execução. |
| RESP-F03-02 | Avaliar decisões pela contribuição legítima ao Momento e ao Próximo Passo. |
| RESP-F03-03 | Reavaliar funcionalidades, Produtos, algoritmos, interfaces, campanhas e parcerias sem aderência. |
| RESP-F03-04 | Orientar Journey, Possibilidades e Oportunidades pela missão. |
| RESP-F03-05 | Orientar IA e Experience Architecture pela missão. |
| RESP-F03-06 | Governar o ecossistema sem substituir a autoridade dos participantes. |
| RESP-F03-07 | Manter explicável por que uma recomendação, Possibilidade ou Oportunidade aparece. |
| RESP-F03-08 | Separar atividade, experiência, contribuição, resultado e impacto conforme evidência. |
| RESP-F03-09 | Preservar privacidade, minimização e finalidade em qualquer apoio contextual. |

## 10. Exemplos de aplicação

### Funcionalidade

```text
IDEIA
→ feed infinito de ofertas para aumentar tempo de sessão

TESTE DA MISSÃO
→ não parte do Momento
→ não demonstra Próximo Passo
→ incentiva volume, não pertinência

RESULTADO
→ REAVALIAR
```

### Recomendação contextual

```text
MOMENTO
→ pessoa declara busca por recolocação

PRÓXIMO PASSO
→ compreender alternativas de posicionamento profissional

POSSIBILIDADES
→ revisar narrativa profissional
→ ampliar rede
→ buscar capacitação específica

OPORTUNIDADE
→ só entra quando uma oferta concreta e pertinente existir
```

### Coletivo

```text
MOMENTO
→ aumento de conflitos internos

PRÓXIMO PASSO
→ revisar governança e forma de decisão

POSSIBILIDADE
→ facilitar uma revisão coletiva

OPORTUNIDADE EXTERNA
→ pode existir ou não
```

## 11. Evidência e limites

A missão possui alta convergência com Fundação, Experience Architecture e Research posterior.

Ela não autoriza afirmar:

- que a Guivos conhece perfeitamente o Momento;
- que todo Próximo Passo é correto;
- que toda recomendação é relevante;
- que evolução é causada pela plataforma;
- que IA está implementada;
- que o modelo de recomendação já possui performance comprovada;
- que PMF foi validado.