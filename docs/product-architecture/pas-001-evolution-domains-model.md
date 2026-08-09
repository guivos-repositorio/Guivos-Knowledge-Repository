---
id: PAS-001-DOMAIN-MODEL-001
title: Modelo Canônico dos Domínios de Evolução do Guivos Journey
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
parent: PAS-001
normative: true
related:
  - GPA-001
  - PAS-001
  - PAS-001-CV-STATE-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - PAS-001-EXP-CONTRACT-001
  - PAS-001-EC-FOUNDATION-001
  - PAS-001-EC-CONTRACT-001
  - GIA-000
---

# PAS-001-DOMAIN-MODEL-001 — Modelo Canônico dos Domínios de Evolução do Guivos Journey

> **Decisão canônica:** o Guivos Journey passa a possuir um eixo explícito de **Domínios de Evolução** para responder **sobre quais áreas da vida, da atuação coletiva ou da trajetória institucional a jornada está tratando**.
>
> Os Domínios de Evolução são ortogonais às capacidades do Journey e às dimensões estruturais do Contexto Vivo. Eles não são scores, diagnósticos, níveis de mérito, etapas obrigatórias ou categorias permanentes do participante.

## 1. Finalidade

Esta autoridade resolve a lacuna semântica entre:

- **como** o Journey compreende, direciona, acompanha e reconhece mudanças; e
- **sobre o que** uma jornada concreta está tratando.

O `PAS-001` já governa as capacidades funcionais do Journey. O `PAS-001-CV-STATE-001` já governa dimensões estruturais do Contexto Vivo. A Capacidade de Evolução Contínua já governa reconhecimento de trajetórias. Faltava uma taxonomia canônica que permitisse dizer, por exemplo, que um Objetivo, Próximo Passo, Oportunidade, Experiência ou Trajetória de Evolução se relaciona a **Saúde e Bem-estar**, **Vida Financeira**, **Espiritualidade, Propósito e Valores** ou a mais de um domínio simultaneamente.

Esta autoridade estabelece essa taxonomia.

## 2. Origem do baseline

O baseline inicial deriva das áreas utilizadas na pesquisa B2C da Guivos para a pergunta:

> **Qual área da sua vida você mais gostaria de cuidar, fortalecer ou transformar?**

As opções utilizadas na pesquisa foram consolidadas arquiteturalmente em nove domínios canônicos. A opção “Ainda não sei ou escolheria outra área” foi decomposta em dois conceitos distintos:

- **Ainda estou descobrindo** — estado legítimo de exploração, não um domínio;
- **Outra área** — mecanismo de extensibilidade e captura de uma necessidade ainda não mapeada.

A promoção desse baseline para autoridade arquitetural não transforma a pesquisa em evidência de eficácia da Guivos. Ela fornece vocabulário inicial de organização da experiência.

## 3. Distinção entre os dois eixos do Journey

### 3.1 Eixo funcional — como a jornada opera

```text
Captura de Contexto
→ Contexto Vivo
→ Objetivos
→ Eventos de Vida
→ Próximos Passos
→ Oportunidades Ativas
→ Intervenções Contextuais
→ Experiências
→ Evolução Contínua
```

### 3.2 Eixo de domínio — sobre o que a jornada trata

```text
Domínio de Evolução
→ subárea
→ contexto específico
→ objetivos, eventos, movimentos, oportunidades, experiências e evidências relacionados
```

Os dois eixos se cruzam.

Exemplo:

```text
Pessoa
→ Domínio: Saúde e Bem-estar
→ Subárea: atividade física
→ Momento Atual
→ Objetivo
→ Próximo Passo
→ Oportunidade
→ Experiência
→ Evidência
→ Trajetória de Evolução
```

## 4. Domínio de Evolução não é dimensão do Contexto Vivo

Os oito elementos do Contexto Vivo — Identidade, Momento, Direção, Capacidades, Restrições, Preferências, Relacionamentos e Evolução — descrevem **como o contexto é representado**.

Os Domínios de Evolução descrevem **qual área está em foco**.

Portanto:

```text
Saúde e Bem-estar ≠ Momento
Vida Financeira ≠ Direção
Espiritualidade ≠ Identidade
Relacionamentos e Vida Social ≠ dimensão estrutural Relacionamentos
```

Uma mesma área pode possuir, simultaneamente:

- um Momento atual;
- uma Direção declarada;
- Capacidades relevantes;
- Restrições;
- Preferências;
- Relacionamentos;
- evidências de Evolução.

## 5. Definição canônica

**Domínio de Evolução** é uma categoria semântica governada que organiza uma área relevante da jornada de uma Pessoa, Coletivo ou Organização e permite relacionar contexto, objetivos, mudanças, próximos passos, oportunidades, experiências e evidências sem reduzir o participante a essa categoria.

Um Domínio de Evolução:

- pode ser declarado pelo participante;
- pode ser sugerido como candidato pela Guivos Intelligence;
- pode coexistir com outros domínios;
- pode tornar-se temporariamente prioritário;
- pode perder relevância;
- pode ser contestado;
- pode permanecer desconhecido;
- não define identidade;
- não define valor;
- não define mérito;
- não comprova evolução.

## 6. Taxonomia canônica inicial

| ID | Domínio canônico | Formulação pública |
|---|---|---|
| `JED-001` | Saúde e Bem-estar | Saúde e bem-estar |
| `JED-002` | Trabalho, Carreira e Estudos | Trabalho, carreira e estudos |
| `JED-003` | Vida Financeira | Vida financeira |
| `JED-004` | Empreendedorismo e Projetos | Empreendedorismo e projetos |
| `JED-005` | Relacionamentos e Vida Social | Relacionamentos e vida social |
| `JED-006` | Espiritualidade, Propósito e Valores | Espiritualidade, propósito e valores |
| `JED-007` | Viagens, Lazer, Cultura e Novas Experiências | Viagens, lazer, cultura e novas experiências |
| `JED-008` | Causas, Voluntariado e Contribuição | Causas, voluntariado e contribuição |
| `JED-009` | Organização e Equilíbrio da Vida | Organização e equilíbrio da vida |

O conjunto é um baseline canônico inicial, não uma taxonomia eternamente fechada.

## 7. JED-001 — Saúde e Bem-estar

### 7.1 Definição

Organiza jornadas relacionadas ao cuidado, manutenção ou fortalecimento do bem-estar físico, hábitos de saúde, autocuidado e condições que influenciem qualidade de vida, sempre respeitando limites de competência profissional e proteção de dados sensíveis.

### 7.2 Subáreas iniciais

- saúde física;
- atividade física e movimento;
- sono e descanso;
- alimentação e hábitos relacionados;
- prevenção e autocuidado;
- bem-estar emocional declarado;
- qualidade de vida;
- rotina de cuidado;
- acessibilidade e condições funcionais quando relevantes à finalidade.

### 7.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- iniciar ou manter atividade física;
- organizar uma rotina de sono;
- encontrar atividades compatíveis com seu momento e restrições;
- desenvolver hábitos de autocuidado;
- localizar profissionais ou serviços quando apropriado;
- encontrar conteúdos, grupos, experiências ou oportunidades de bem-estar;
- acompanhar uma mudança de rotina declarada;
- compreender como uma condição funcional afeta objetivos e próximos passos.

### 7.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- organizar atividades de bem-estar para participantes;
- promover caminhada, esporte, prevenção ou autocuidado comunitário;
- tornar experiências mais acessíveis e seguras;
- conectar o coletivo a profissionais, organizações ou recursos adequados;
- acompanhar resultados agregados legitimamente definidos.

### 7.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- estruturar iniciativas de saúde, segurança e qualidade de vida;
- oferecer oportunidades voluntárias de bem-estar;
- organizar campanhas e programas com autoridades adequadas;
- acompanhar indicadores institucionais permitidos;
- conectar pessoas a recursos sem inferir diagnóstico ou condição individual.

### 7.6 Guardrails específicos

A Guivos não deverá:

- diagnosticar automaticamente;
- prescrever tratamento;
- substituir profissional competente;
- inferir que frequência de atividade representa melhora de saúde;
- utilizar dado sensível de saúde para publicidade comportamental;
- permitir que Coletivo ou Organização declare evolução pessoal integral de terceiros.

## 8. JED-002 — Trabalho, Carreira e Estudos

### 8.1 Definição

Organiza jornadas de aprendizagem, educação, empregabilidade, carreira, desenvolvimento profissional, competências e realização ligada a estudo ou trabalho.

### 8.2 Subáreas iniciais

- emprego e recolocação;
- carreira e transição profissional;
- educação formal;
- cursos e formação;
- competências;
- certificações;
- liderança;
- desenvolvimento profissional;
- produtividade funcional sem score humano;
- preparação para oportunidades;
- aprendizagem contínua.

### 8.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- buscar emprego ou recolocação;
- planejar uma mudança de carreira;
- melhorar currículo e preparação profissional;
- desenvolver uma competência;
- escolher ou concluir um curso;
- preparar-se para certificação;
- desenvolver liderança;
- organizar estudos;
- encontrar mentores, especialistas, conteúdos, coletivos ou oportunidades profissionais.

### 8.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- capacitar membros ou voluntários;
- criar trilhas de aprendizagem;
- distribuir conhecimento;
- organizar papéis e competências necessárias;
- conectar participantes a formação e oportunidades.

### 8.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- desenvolver capacidades organizacionais;
- estruturar programas de capacitação;
- conectar pessoas a oportunidades de aprendizagem;
- fortalecer liderança e competências;
- acompanhar resultados institucionais sem converter desempenho em valor humano.

## 9. JED-003 — Vida Financeira

### 9.1 Definição

Organiza jornadas relacionadas à compreensão, organização e sustentabilidade financeira no escopo adequado ao tipo de participante.

### 9.2 Subáreas iniciais

- organização financeira;
- orçamento;
- reserva e segurança financeira;
- dívidas e compromissos;
- renda;
- planejamento de objetivos financeiros;
- educação financeira;
- sustentabilidade financeira de Coletivo;
- sustentabilidade econômico-institucional de Organização.

### 9.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- organizar orçamento;
- compreender prioridades financeiras;
- estruturar um objetivo de reserva;
- buscar educação financeira;
- reorganizar dívidas;
- planejar uma compra, viagem ou projeto;
- explorar caminhos legítimos para aumento de renda;
- encontrar apoio especializado quando necessário.

### 9.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- planejar sustentabilidade de uma iniciativa;
- organizar necessidades de recursos;
- estruturar captação ou apoio permitido;
- acompanhar orçamento de ações;
- conectar-se a parceiros e organizações apoiadoras.

### 9.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- relacionar sustentabilidade econômica a objetivos institucionais;
- organizar iniciativas e recursos;
- acompanhar resultados econômico-institucionais no escopo permitido;
- conectar investimentos sociais ou programas a evidências de execução.

### 9.6 Guardrails específicos

Vida Financeira não deverá ser utilizada como proxy de:

- sucesso humano;
- prosperidade moral;
- mérito;
- valor pessoal;
- capacidade integral da pessoa.

## 10. JED-004 — Empreendedorismo e Projetos

### 10.1 Definição

Organiza jornadas de criação, validação, estruturação e desenvolvimento de iniciativas, negócios, projetos pessoais, coletivos ou institucionais.

### 10.2 Subáreas iniciais

- ideia e descoberta;
- projeto pessoal;
- validação;
- empreendedorismo;
- modelo de negócio;
- execução de projeto;
- inovação;
- parcerias;
- desenvolvimento de iniciativa;
- recursos e capacidades do projeto.

### 10.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- transformar uma ideia em projeto;
- estruturar próximos passos;
- validar uma iniciativa;
- desenvolver competências empreendedoras;
- encontrar parceiros, conteúdos, ferramentas e especialistas;
- organizar metas e evidências de execução;
- desenvolver um projeto paralelo ou negócio.

### 10.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- criar e organizar iniciativas comunitárias;
- estruturar campanhas e projetos;
- encontrar parceiros e recursos;
- dividir responsabilidades;
- acompanhar entregas e aprendizados.

### 10.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- estruturar iniciativas e programas;
- promover inovação;
- organizar portfólios de projetos;
- conectar equipes, parceiros e recursos;
- acompanhar evidências de execução e resultados institucionais.

## 11. JED-005 — Relacionamentos e Vida Social

### 11.1 Definição

Organiza jornadas relacionadas a vínculos, convivência, pertencimento, redes de apoio, relações familiares, amizades, participação social e relações relevantes ao tipo de participante.

### 11.2 Subáreas iniciais

- família;
- amizades;
- vínculos afetivos declarados;
- vida social;
- pertencimento;
- convivência;
- comunicação;
- redes de apoio;
- relações comunitárias;
- relações institucionais.

### 11.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- fortalecer vínculos familiares ou sociais;
- ampliar círculo social;
- encontrar atividades compartilhadas;
- participar de grupos ou coletivos;
- desenvolver comunicação e convivência;
- retomar conexões relevantes;
- encontrar espaços de pertencimento compatíveis com seus interesses e limites.

### 11.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- fortalecer pertencimento;
- organizar participação;
- melhorar comunicação;
- facilitar colaboração;
- estruturar redes de apoio;
- criar experiências que fortaleçam vínculos sem exigir exposição indevida.

### 11.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- fortalecer colaboração e cultura;
- organizar comunidades internas ou externas;
- melhorar relações entre atores institucionais;
- criar oportunidades de conexão;
- acompanhar sinais agregados de participação e relacionamento sem criar scores pessoais de sociabilidade.

## 12. JED-006 — Espiritualidade, Propósito e Valores

### 12.1 Definição

Organiza jornadas voluntariamente relacionadas a fé, espiritualidade, sentido, propósito, valores e coerência entre aquilo que o participante declara importante e suas escolhas ou práticas.

### 12.2 Subáreas iniciais

- fé declarada;
- espiritualidade;
- práticas espirituais ou religiosas;
- comunidades de fé;
- propósito;
- sentido;
- valores;
- reflexão;
- gratidão como prática voluntária;
- serviço e contribuição relacionados a valores.

### 12.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- aprofundar uma prática espiritual escolhida;
- encontrar comunidade religiosa ou espiritual compatível;
- participar de encontros, estudos, retiros ou ações;
- refletir sobre propósito;
- aproximar decisões de valores declarados;
- encontrar conteúdos e experiências relacionadas;
- organizar práticas voluntárias de reflexão, gratidão ou serviço.

### 12.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- organizar comunidade de fé ou reflexão;
- promover encontros e ações coerentes com valores declarados;
- estruturar serviço comunitário;
- preservar diversidade e limites de participação;
- conectar pessoas interessadas sem presumir crença.

### 12.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- explicitar propósito e valores institucionais;
- acompanhar coerência entre compromissos declarados e práticas institucionais;
- organizar iniciativas de ética, propósito e contribuição;
- respeitar crenças individuais e não transformar a Organização em autoridade espiritual sobre pessoas.

### 12.6 Guardrails específicos

A Guivos não deverá:

- medir fé;
- medir proximidade de Deus;
- diagnosticar condição espiritual;
- classificar crenças como superiores ou inferiores;
- presumir religião;
- converter prática religiosa em mérito;
- usar espiritualidade para manipulação comercial;
- impor propósito de vida;
- permitir que Organização ou Coletivo atribua estado espiritual a terceiros.

## 13. JED-007 — Viagens, Lazer, Cultura e Novas Experiências

### 13.1 Definição

Organiza jornadas de descoberta, lazer, cultura, hobbies, viagens e experiências novas ou desejadas que contribuam para repertório, bem-estar, conexão ou objetivos voluntariamente escolhidos.

### 13.2 Subáreas iniciais

- viagens;
- turismo;
- lazer;
- cultura;
- hobbies;
- gastronomia;
- experiências locais;
- descoberta de lugares;
- eventos;
- aprendizado experiencial.

### 13.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- conhecer novos lugares;
- planejar viagens;
- descobrir experiências compatíveis com orçamento, localização e preferências;
- participar de eventos culturais;
- desenvolver hobbies;
- experimentar novas atividades;
- conhecer pessoas, culturas e contextos;
- organizar momentos de lazer e experiências desejadas.

### 13.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- organizar experiências compartilhadas;
- promover atividades culturais ou de lazer;
- planejar encontros e deslocamentos;
- criar experiências de pertencimento e descoberta;
- conectar parceiros e recursos.

### 13.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- organizar programas e experiências institucionais;
- estruturar iniciativas culturais ou de integração;
- oferecer experiências voluntárias a públicos elegíveis;
- conectar programas ao Guivos Travel, Media, Mall ou parceiros quando o handoff for legítimo.

## 14. JED-008 — Causas, Voluntariado e Contribuição

### 14.1 Definição

Organiza jornadas de participação cívica, voluntariado, causas, contribuição social, mobilização e impacto coletivo ou institucional.

### 14.2 Subáreas iniciais

- voluntariado;
- causas sociais;
- ação comunitária;
- cidadania;
- doação e apoio quando aplicável;
- mobilização;
- contribuição por competências;
- projetos de impacto;
- responsabilidade social;
- participação em coletivos e movimentos legítimos.

### 14.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- encontrar uma causa;
- participar de voluntariado;
- contribuir com competências;
- apoiar projetos sociais;
- participar de movimentos e ações;
- conectar-se a Coletivos e Organizações;
- reconhecer experiências e resultados sem transformar contribuição em ranking moral.

### 14.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- criar e organizar ação social;
- mobilizar participantes;
- divulgar oportunidades legítimas;
- receber apoio de pessoas e organizações;
- organizar recursos, responsabilidades e evidências;
- acompanhar impacto coletivo conforme critérios adequados.

### 14.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- apoiar causas;
- oferecer recursos, conhecimento ou infraestrutura;
- criar programas de voluntariado;
- patrocinar ações sem adquirir autoridade sobre o valor humano dos participantes;
- acompanhar resultados institucionais e sociais;
- conectar investimento social a iniciativas legítimas.

### 14.6 Exemplo ecossistêmico

```text
Pessoa quer contribuir
→ Coletivo organiza uma ação
→ Organização disponibiliza recurso ou apoio
→ Journey conecta os atores conforme relevância e autorização
→ experiência acontece
→ evidências e resultados são registrados no escopo correto
→ evolução individual, coletiva e institucional permanece separada
```

## 15. JED-009 — Organização e Equilíbrio da Vida

### 15.1 Definição

Organiza jornadas de priorização, rotina, coordenação, gestão de responsabilidades e equilíbrio entre frentes relevantes, respeitando que “equilíbrio” é contextual e não um padrão imposto pela Guivos.

### 15.2 Subáreas iniciais

- rotina;
- prioridades;
- gestão de tempo;
- organização pessoal;
- hábitos;
- responsabilidades;
- transições de rotina;
- coordenação coletiva;
- governança operacional de Coletivo;
- priorização e coordenação institucional.

### 15.3 Exemplos — Pessoa

A Guivos pode apoiar a pessoa a:

- organizar rotina;
- definir prioridades;
- estruturar objetivos;
- melhorar gestão do tempo;
- equilibrar responsabilidades;
- reorganizar a vida após Evento de Vida;
- reduzir sobrecarga por meio de escolhas e próximos passos legítimos;
- criar ou revisar hábitos;
- compreender qual área merece atenção primeiro.

### 15.4 Exemplos — Coletivo

A Guivos pode apoiar o Coletivo a:

- organizar agenda, responsabilidades e papéis;
- priorizar iniciativas;
- coordenar participação;
- distribuir atividades;
- revisar capacidade e restrições;
- manter continuidade sem centralização indevida.

### 15.5 Exemplos — Organização

A Guivos pode apoiar a Organização a:

- organizar prioridades e iniciativas;
- coordenar programas e responsabilidades;
- relacionar capacidade a compromissos;
- identificar sobreposição de frentes;
- apoiar equilíbrio operacional sem transformar produtividade em score humano.

## 16. Estado transversal — Ainda estou descobrindo

`Ainda estou descobrindo` é um estado legítimo de jornada para o participante que:

- ainda não sabe o que deseja transformar;
- percebe desconforto ou necessidade sem conseguir nomear a área;
- deseja explorar possibilidades antes de assumir um Objetivo;
- possui múltiplos temas sem prioridade clara;
- prefere não classificar sua situação naquele momento.

Esse estado:

- não é falha;
- não é abandono;
- não é um décimo domínio;
- não exige classificação automática;
- não autoriza coleta excessiva;
- não autoriza a Guivos a inventar propósito ou prioridade.

A Guivos pode apoiar por meio de:

- perguntas abertas;
- revisão do Momento Atual;
- exploração de possibilidades;
- apresentação explicável de domínios candidatos;
- reconhecimento de Eventos de Vida;
- identificação de interesses e restrições;
- possibilidade explícita de permanecer sem escolha.

## 17. Mecanismo — Outra área

`Outra área` representa uma necessidade ou contexto ainda não adequadamente coberto pela taxonomia canônica.

Quando utilizado, o Journey deverá preservar:

- expressão original do participante;
- eventual aproximação semântica sugerida;
- decisão de mapear ou não para um domínio existente;
- possibilidade de criar candidatura de novo subdomínio ou domínio;
- proibição de reclassificação silenciosa.

Novos domínios canônicos exigem governança documental. Frequência de uso não cria domínio automaticamente.

## 18. Aplicabilidade por participante

Os nove domínios pertencem ao vocabulário comum do Journey, mas **não possuem interpretação idêntica** para os três participantes.

| Domínio | Pessoa | Coletivo | Organização |
|---|---|---|---|
| Saúde e Bem-estar | cuidado, hábitos e qualidade de vida | bem-estar e proteção de participantes | programas, condições e saúde/segurança institucionalmente promovidas |
| Trabalho, Carreira e Estudos | carreira, emprego e aprendizagem | capacitação e aprendizagem coletiva | desenvolvimento de pessoas e capacidades organizacionais |
| Vida Financeira | organização e segurança financeira pessoal | sustentabilidade e recursos do coletivo | sustentabilidade econômico-institucional |
| Empreendedorismo e Projetos | negócio ou projeto pessoal | iniciativas e projetos coletivos | inovação e projetos institucionais |
| Relacionamentos e Vida Social | família, amizades, vínculos e pertencimento | convivência, participação e redes | cultura, colaboração e relações institucionais |
| Espiritualidade, Propósito e Valores | fé, sentido, propósito e valores declarados | identidade e valores compartilhados, quando voluntários | propósito, ética e valores institucionais, sem autoridade espiritual individual |
| Viagens, Lazer, Cultura e Novas Experiências | viagens, lazer, cultura e hobbies | experiências compartilhadas | programas e experiências promovidas |
| Causas, Voluntariado e Contribuição | participação e contribuição | mobilização e ação | apoio, responsabilidade social e impacto institucional |
| Organização e Equilíbrio da Vida | rotina, prioridades e responsabilidades | coordenação e governança | priorização e equilíbrio operacional |

### 18.1 Regra de separação

```text
trajetória da Pessoa
≠ trajetória do Coletivo
≠ trajetória da Organização
≠ indicador agregado
≠ impacto social amplo
```

A Organização não poderá declarar que uma Pessoa evoluiu apenas porque um programa institucional melhorou seus indicadores.

O Coletivo não poderá declarar transformação integral de seus membros apenas porque uma ação foi concluída.

## 19. Multidomínio e relações entre áreas

Uma jornada pode envolver `1..n` domínios simultaneamente.

A Guivos não deverá forçar o participante a escolher apenas um domínio fora de contextos de pesquisa ou interfaces que explicitamente solicitem priorização temporária.

### 19.1 Exemplo — finanças, viagem e carreira

Declaração:

> “Quero melhorar minha situação financeira porque estou planejando uma viagem e também pensando em mudar de carreira.”

Representação:

```text
JED-003 Vida Financeira
        ↕
JED-007 Viagens, Lazer, Cultura e Novas Experiências
        ↕
JED-002 Trabalho, Carreira e Estudos
```

Nenhum domínio precisa ser reduzido ao outro.

### 19.2 Exemplo — espiritualidade, pertencimento e mudança de cidade

Declaração:

> “Quero voltar a frequentar minha igreja porque depois que me mudei estou me sentindo sozinho.”

Representação possível, sujeita à confirmação:

```text
JED-006 Espiritualidade, Propósito e Valores
+
JED-005 Relacionamentos e Vida Social
+
Evento de Vida: mudança de cidade
```

A Guivos não deverá inferir religião, solidão clínica, estado emocional ou significado espiritual além do que foi declarado ou legitimamente confirmado.

## 20. Relação com as capacidades do Journey

### 20.1 Captura de Contexto

Pode receber sinais ou declarações de domínio, preservando expressão original e finalidade.

### 20.2 Contexto Vivo

Pode representar quais domínios estão atualmente relevantes sem convertê-los em identidade permanente.

### 20.3 Objetivos

Um Objetivo pode referenciar um ou vários domínios.

Exemplo:

```text
Objetivo: “Correr minha primeira prova de 5 km”
→ JED-001 Saúde e Bem-estar
```

### 20.4 Eventos de Vida

Um Evento de Vida pode afetar múltiplos domínios.

Exemplo:

```text
Mudança de cidade
→ Relacionamentos e Vida Social
→ Trabalho, Carreira e Estudos
→ Vida Financeira
→ Organização e Equilíbrio da Vida
```

O impacto deve ser avaliado, não presumido.

### 20.5 Próximos Passos

Um Próximo Passo pode ser relacionado a um domínio sem transformar a atividade em prova de evolução.

### 20.6 Oportunidades Ativas

O domínio pode compor relevância contextual, mas:

```text
domínio compatível ≠ oportunidade relevante
```

Relevância também depende de Momento, Objetivos, Restrições, Preferências, autoridade, localização, temporalidade e outros critérios.

### 20.7 Intervenções Contextuais

O domínio pode ajudar a explicar contexto da manifestação, mas não amplia legitimidade para interromper o participante.

### 20.8 Experiências

Uma Experiência pode produzir evidências relacionadas a um ou vários domínios, sem provar evolução automaticamente.

### 20.9 Evolução Contínua

Uma Trajetória de Evolução pode referenciar um domínio e uma ou mais subáreas, mantendo separadas:

- observação;
- evidência;
- interpretação;
- direção;
- baseline;
- confiança;
- incerteza;
- significado atribuído pelo participante.

## 21. Relação com Guivos Intelligence

A Guivos Intelligence poderá:

- classificar texto ou eventos em domínios candidatos;
- sugerir relações multidomínio;
- detectar que uma necessidade ainda está sem domínio;
- explicar por que sugeriu determinado domínio;
- apoiar busca de oportunidades e conteúdos compatíveis;
- detectar possíveis conflitos de classificação;
- preservar confiança e incerteza.

Ela não poderá:

- transformar candidato em domínio confirmado sem autoridade;
- inferir saúde, religião, condição emocional ou situação financeira sensível sem base e finalidade adequadas;
- inventar prioridade;
- definir propósito de vida;
- transformar domínio em perfil publicitário;
- criar score humano global ou por domínio;
- concluir evolução apenas porque um indicador aumentou.

## 22. Modelo mínimo de associação de domínio

```yaml
domain_link:
  domain_id: JED-001..JED-009 | other_unmapped | null
  subdomain: string_or_null
  participant_type: person | collective | organization
  relation_type: primary | secondary | contextual | candidate
  authority: participant_declared | authorized_source | guivos_candidate | professional | institutional
  confirmation_state: candidate | declared | confirmed | contested | withdrawn | unknown
  confidence: low | moderate | high | unknown
  sensitive: true | false | context_dependent
  purpose: string
  source_ref: string_or_null
  valid_from: datetime_or_null
  valid_until: datetime_or_null
  notes: string_or_null
```

Esse contrato é semântico. Ele não autoriza implementação, banco de dados, API ou esquema técnico definitivo.

## 23. Regras de classificação

1. A declaração direta do participante deverá prevalecer sobre inferência incompatível.
2. Um domínio candidato deverá permanecer candidato até autoridade suficiente.
3. Ausência de domínio não representa ausência de necessidade.
4. Um item poderá possuir mais de um domínio.
5. O sistema deverá preservar a expressão original quando houver ambiguidade.
6. A classificação poderá ser contestada e retirada.
7. Mudança de domínio não deverá apagar histórico legítimo.
8. Domínio não deverá ser usado como identidade definitiva.
9. “Outra área” não deverá ser silenciosamente encaixada em taxonomia existente.
10. “Ainda estou descobrindo” deverá permanecer opção legítima.

## 24. Sensibilidade e proteção

A sensibilidade é contextual. Alguns domínios contêm subáreas que podem envolver dados pessoais sensíveis ou de alto risco.

Exigem proteção reforçada, conforme aplicável:

- saúde;
- deficiência;
- condição emocional;
- religião e espiritualidade;
- finanças;
- emprego;
- família;
- sexualidade quando emergir em relacionamento ou contexto;
- violência, trauma ou luto;
- localização protegida;
- crianças e adolescentes;
- vulnerabilidade.

Domínio sensível ou elemento sensível não deverá ser utilizado para:

- publicidade comportamental;
- manipulação de preço;
- ranking humano;
- discriminação;
- exclusão indevida;
- exposição a terceiros sem base apropriada;
- inferência de mérito, fé, saúde, solvência ou valor pessoal.

## 25. Domínios não são scores

O Journey não deverá criar, por padrão, uma “roda da vida” obrigatória com notas para cada domínio.

Portanto:

```text
Domínio Saúde ≠ score de saúde
Domínio Financeiro ≠ score de sucesso
Domínio Espiritualidade ≠ score de fé
Domínio Relacionamentos ≠ score de sociabilidade
Domínio Organização ≠ score de produtividade
```

Uma visualização poderá apresentar estados, prioridades, evidências ou trajetórias se houver finalidade legítima, explicabilidade e autoridade, mas não deverá induzir uma nota global de valor ou evolução humana.

## 26. O que significa evoluir em um domínio

Evolução não exige transformação radical.

Dependendo do contexto, uma trajetória legítima pode representar:

- descobrir;
- compreender;
- iniciar;
- aprender;
- desenvolver;
- fortalecer;
- organizar;
- adaptar;
- recuperar;
- manter;
- consolidar;
- experimentar;
- concluir;
- reorientar;
- pausar;
- abandonar legitimamente;
- reduzir impacto de uma restrição;
- reconhecer ausência de mudança;
- permanecer inconclusiva.

A direção e o significado devem respeitar o participante e a autoridade aplicável.

## 27. Handoffs com produtos e ecossistema

Os domínios podem orientar descoberta e handoffs, mas não determinam produto automaticamente.

Exemplos:

- Saúde e Bem-estar pode levar a conteúdo, profissional, experiência, Coletivo, Mall ou outro meio legítimo;
- Trabalho, Carreira e Estudos pode levar a conteúdo, especialista, Organização, Coletivo ou oportunidade;
- Viagens e Experiências pode produzir handoff ao Guivos Travel;
- Causas e Voluntariado pode conectar Pessoa, Coletivo e Organização;
- um conteúdo do Guivos Media pode apoiar vários domínios;
- Guivos Ads não adquire autoridade sobre relevância por comprar mídia.

```text
domínio → contexto de relevância
≠ domínio → produto obrigatório
```

## 28. Exemplos end-to-end

### 28.1 Pessoa — Saúde e Bem-estar

```text
Pessoa declara: “Quero voltar a me exercitar duas vezes por semana.”
→ JED-001 Saúde e Bem-estar
→ Objetivo confirmado pela Pessoa
→ restrições e preferências revisadas
→ Próximo Passo possível: escolher atividade compatível
→ Oportunidades avaliadas
→ Experiência vivida
→ evidências autorizadas
→ Evolução Contínua avalia trajetória
```

Cumprir duas atividades não significa automaticamente “a pessoa ficou saudável”.

### 28.2 Pessoa — Descoberta

```text
Pessoa declara: “Sinto que preciso mudar alguma coisa, mas ainda não sei o quê.”
→ estado: Ainda estou descobrindo
→ Contexto Vivo pode ser revisado
→ domínios candidatos podem ser apresentados com explicação
→ Pessoa pode escolher, rejeitar ou permanecer sem domínio
```

### 28.3 Coletivo — Causa social

```text
Coletivo deseja reduzir barreiras de acesso a uma atividade comunitária
→ JED-008 Causas, Voluntariado e Contribuição
+ JED-001 Saúde e Bem-estar, se a atividade envolver bem-estar e houver finalidade legítima
→ estrutura ação
→ mobiliza participantes
→ recebe apoio autorizado de Organização
→ acompanha evidências coletivas
```

Nenhum resultado agregado declara evolução individual automática.

### 28.4 Organização — Desenvolvimento e contribuição

```text
Organização cria programa voluntário de capacitação de jovens
→ JED-002 Trabalho, Carreira e Estudos
+ JED-008 Causas, Voluntariado e Contribuição
→ define público e critérios
→ conecta-se a Coletivos e Pessoas elegíveis
→ registra execução e resultados institucionais
→ participantes preservam sua própria autoridade sobre experiência e evolução
```

## 29. Governança e extensibilidade

### 29.1 Subáreas

Subáreas podem evoluir com menor custo de governança quando:

- não alteram o significado do domínio;
- não criam nova autoridade;
- não reduzem proteção;
- possuem uso e finalidade claros;
- preservam compatibilidade com a taxonomia.

### 29.2 Novo domínio

A criação de um décimo ou novo domínio canônico deverá exigir:

1. evidência de necessidade semântica não coberta;
2. análise de sobreposição com os nove domínios;
3. definição de fronteira;
4. exemplos Pessoa × Coletivo × Organização;
5. análise de sensibilidade;
6. relação com capacidades do Journey;
7. impacto em Intelligence, experiência e grafo;
8. decisão documental explícita.

### 29.3 Renomeação

Renomear domínio exige análise de compatibilidade porque nomes podem aparecer em:

- pesquisas;
- jornadas;
- conteúdos;
- oportunidades;
- analytics;
- taxonomias;
- grafo;
- integrações;
- materiais públicos.

## 30. Critérios de qualidade

O modelo estará semanticamente saudável quando:

- cada domínio possuir fronteira compreensível;
- exemplos não forem tratados como lista fechada;
- os três participantes tiverem interpretação adequada;
- domínios puderem coexistir;
- “Ainda estou descobrindo” permanecer legítimo;
- dados sensíveis receberem proteção proporcional;
- o modelo não produzir score humano;
- Intelligence preservar candidatura, explicação e incerteza;
- evolução permanecer dependente de evidência e contrato;
- produtos especializados não adquirirem autoridade sobre o Journey;
- a taxonomia puder evoluir sem perder histórico.

## 31. Invariantes finais

```text
Domínio ≠ identidade
Domínio ≠ Objetivo
Domínio ≠ Momento
Domínio ≠ Evento de Vida
Domínio ≠ Próximo Passo
Domínio ≠ Oportunidade
Domínio ≠ Experiência
Domínio ≠ Evidência
Domínio ≠ Evolução
Domínio ≠ Score
Domínio ≠ diagnóstico
Domínio ≠ produto
Domínio ≠ autoridade comercial
```

E:

```text
Saúde ≠ diagnóstico
Espiritualidade ≠ medir fé
Finanças ≠ medir sucesso humano
Relacionamentos ≠ medir valor social
Voluntariado ≠ ranking moral
Organização ≠ produtividade como valor humano
```

## 32. Estado arquitetural resultante

Com esta autoridade, o Guivos Journey passa a possuir dois eixos semânticos complementares:

```text
EIXO FUNCIONAL
como a jornada opera

+

EIXO DE DOMÍNIO
sobre qual área a jornada trata
```

O modelo está autorizado documentalmente como baseline canônico de produto.

Ele não comprova:

- implementação técnica;
- disponibilidade em produção;
- eficácia de recomendações;
- integração de IA;
- integração com grafo;
- existência de dados reais por domínio;
- consentimentos operacionais;
- resultados de evolução.
